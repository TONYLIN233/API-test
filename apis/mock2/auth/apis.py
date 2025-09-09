from typing import Optional
from attrs import define, field
from .models import TokenResponseData
from aomaker.core.api_object import BaseAPIObject as BaseAPI
from aomaker.core.router import router

__ALL__ = ["LoginForAccessTokenApiLoginTokenPostAPI"]


@define(kw_only=True)
@router.post("/api/login/token")
class LoginForAccessTokenApiLoginTokenPostAPI(BaseAPI[TokenResponseData]):
    """用户提供用户名和密码进行登录，成功后返回JWT令牌"""

    @define
    class RequestBodyModel:
        username: str = field()
        password: str = field()

    request_body: RequestBodyModel

    response: Optional[TokenResponseData] = field(default=TokenResponseData)
    endpoint_id: Optional[str] = field(
        default="login_for_access_token_api_login_token_post"
    )
