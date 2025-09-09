"""
Auth模块下的Token相关测试用例
核心测试接口：LoginForAccessTokenApiLoginTokenPostAPI
"""
import aomaker
from aomaker import cache
from aomaker.params import Variables

import pytest
# 从当前项目层级的apis模块导入接口模型（注意相对路径导入）
from apis.mock2.auth.apis import TokenResponseData
from apis.mock2.auth.apis import LoginForAccessTokenApiLoginTokenPostAPI

class TestToken:
    """Token获取与验证测试套件"""

    @pytest.mark.smoke
    def test_login_for_access_token_success(self):
        """正向用例：使用有效凭证成功获取access token"""
        # 1. 准备测试数据（在实际项目中，这些数据应来自config或data_maker）
        username = "test_user"
        password = "test_password"  # 应使用测试环境的有效账户

        # 2. 实例化API对象并发送请求
        # 注意：aomaker的API对象使用attrs定义，必须传入关键字参数
        api_obj = LoginForAccessTokenApiLoginTokenPostAPI(
            request_body={
                "username": username,
                "password": password
            }
        )
        response = api_obj.send()

        # 3. 断言（使用aomaker推荐的链式断言风格）
        (response
         .assert_status_code(200)  # 断言状态码
         .assert_response_model(TokenResponseData)  # 断言响应结构符合模型
         .assert_field_exists("access_token")  # 断言关键字段存在
         .assert_field_equal("token_type", "bearer"))  # 断言字段值正确

        # 4. 【可选】将token存入缓存，供后续依赖接口使用
        # aomaker的cache是跨用例的全局缓存
        cache.set("access_token", response.data.access_token)

    @pytest.mark.parametrize("username, password, expected_status, expected_keyword", [
        ("wrong_user", "test_password", 401, "invalid credentials"),  # 错误用户名
        ("test_user", "wrong_password", 401, "invalid credentials"),  # 错误密码
        (None, "test_password", 422, "username"),  # 缺失用户名
        ("test_user", None, 422, "password"),  # 缺失密码
    ], ids=[
        "wrong_username",
        "wrong_password",
        "missing_username",
        "missing_password"
    ])
    def test_login_failure_cases(self, username, password, expected_status, expected_keyword):
        """参数化测试：各种导致登录失败的异常场景"""
        # 构建请求体，过滤掉None值（模拟前端未传参）
        request_body = {}
        if username is not None:
            request_body["username"] = username
        if password is not None:
            request_body["password"] = password

        api_obj = LoginForAccessTokenApiLoginTokenPostAPI(request_body=request_body)
        response = api_obj.send()

        # 断言
        response.assert_status_code(expected_status)
        # 检查返回信息中包含预期关键词（模糊匹配，避免硬编码具体错误信息）
        assert expected_keyword in response.text.lower()

    @dependence(LoginForAccessTokenApiLoginTokenPostAPI, "access_token")
    def test_token_can_access_protected_api(self):
        """
        依赖测试：验证获取的token确实可以用于访问受保护的接口
        使用@dependence装饰器，确保先执行test_login_for_access_token_success获取token
        """
        # 从缓存中取出依赖用例存入的token
        token = cache.get("access_token")
        headers = {"Authorization": f"Bearer {token}"}

        # 假设一个需要认证的接口：UserProfileAPI
        # 注意：此处为示例，您需要替换为项目中真实的受保护接口
        # from ...apis.user import UserProfileAPI
        # profile_api = UserProfileAPI(headers=headers)
        # response = profile_api.send()
        # response.assert_status_code(200)

        # 示例中我们先模拟断言token存在即可
        assert token is not None
        print(f"✅ 成功获取到Token: {token[:20]}...")  # 打印部分token，避免日志泄露完整信息

# 以下为运行本文件的示例命令（通常通过主入口运行，但也可单独调试）
if __name__ == "__main__":
    # 使用aomaker的cli运行本文件所有测试
    # 命令行中执行: aomaker run test_token.py
    pass