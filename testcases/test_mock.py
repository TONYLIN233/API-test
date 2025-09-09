from datetime import datetime

import pytest

from apis.mock.apis import (
    GetUserAPI, 
    GetUsersAPI,
    CreateUserAPI,
    GetProductsAPI,
    GetProductAPI,
    CreateOrderAPI,
    UpdateOrderStatusAPI,
    GetUserDetailAPI,
    GetCommentsAPI,
    GetSystemStatusAPI,
    AddProductCommentAPI,
    DeleteCommentAPI,
    UploadAvatarAPI,
)



@pytest.mark.mock_api
def test_get_users():
    """测试获取用户列表API"""
    query_params = GetUsersAPI.QueryParams(limit=2)
    res = GetUsersAPI(query_params=query_params).send()

    assert res.response_model.ret_code == 0
    assert len(res.response_model.data) <= 2
    assert res.response_model.total >= 0


@pytest.mark.mock_api
def test_get_user():
    """测试获取单个用户API"""
    path_params = GetUserAPI.PathParams(user_id=1)

    res = GetUserAPI(path_params=path_params).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.id == 1
    assert res.response_model.data.username is not None


@pytest.mark.mock_api
def test_create_user():
    """测试创建用户API"""
    request_body = CreateUserAPI.RequestBodyModel(
        id=4,
        username="赵六",
        email="zhaoliu@example.com",
        created_at=datetime.now()
    )

    res = CreateUserAPI(request_body=request_body).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.id == 4
    assert res.response_model.data.username == "赵六"


@pytest.mark.mock_api
def test_get_products():
    """测试获取产品列表API"""
    query_params = GetProductsAPI.QueryParams(
        category="电子产品"
    )

    res = GetProductsAPI(query_params=query_params).send()

    assert res.response_model.ret_code == 0
    assert len(res.response_model.data) > 0
    for product in res.response_model.data:
        assert product.category == "电子产品"


@pytest.mark.mock_api
def test_get_product():
    """测试获取单个产品API"""
    path_params = GetProductAPI.PathParams(product_id=1)

    res = GetProductAPI(path_params=path_params).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.id == 1
    assert res.response_model.data.name is not None


@pytest.mark.mock_api
def test_create_order():
    """测试创建订单API"""
    request_body = CreateOrderAPI.RequestBodyModel(
        id=3,
        user_id=3,
        products=[{"product_id": 3, "quantity": 2}],
        total_price=1998.0,
        status="待付款",
        created_at=datetime.now()
    )

    res = CreateOrderAPI(request_body=request_body).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.id == 3
    assert res.response_model.data.status == "待付款"


@pytest.mark.mock_api
def test_update_order_status():
    """测试更新订单状态API"""
    path_params = UpdateOrderStatusAPI.PathParams(order_id=1)
    request_body = UpdateOrderStatusAPI.RequestBodyModel(status="已发货")

    res = UpdateOrderStatusAPI(
        path_params=path_params,
        request_body=request_body
    ).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.message == "订单状态更新成功"


@pytest.mark.mock_api
def test_get_user_detail():
    """测试获取用户详细信息API"""
    path_params = GetUserDetailAPI.PathParams(user_id=1)

    res = GetUserDetailAPI(path_params=path_params).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.user_id == 1
    assert res.response_model.data.address is not None
    assert res.response_model.data.phone is not None


@pytest.mark.mock_api
def test_get_comments():
    """测试获取评论列表API"""
    query_params = GetCommentsAPI.QueryParams(
        product_id=1,
        min_rating=4
    )

    res = GetCommentsAPI(query_params=query_params).send()

    assert res.response_model.ret_code == 0
    assert len(res.response_model.data) > 0
    for comment in res.response_model.data:
        assert comment.product_id == 1
        assert comment.rating >= 4


@pytest.mark.mock_api
def test_get_system_status():
    """测试获取系统状态API"""
    res = GetSystemStatusAPI().send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.status == "running"
    assert res.response_model.data.version is not None


@pytest.mark.mock_api
def test_add_product_comment():
    """测试添加产品评论API"""
    path_params = AddProductCommentAPI.PathParams(product_id=1)
    request_body = AddProductCommentAPI.RequestBodyModel(
        id=5,
        product_id=1,
        user_id=2,
        content="非常满意的购物体验",
        rating=5,
        created_at=datetime.now()
    )

    res = AddProductCommentAPI(
        path_params=path_params,
        request_body=request_body
    ).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.id == 5
    assert res.response_model.data.content == "非常满意的购物体验"


@pytest.mark.mock_api
def test_delete_comment():
    """测试删除评论API"""
    # 先添加一个评论
    add_comment_path_params = AddProductCommentAPI.PathParams(product_id=1)
    add_comment_request_body = AddProductCommentAPI.RequestBodyModel(
        id=6,
        product_id=1,
        user_id=3,
        content="测试删除评论",
        rating=4,
        created_at=datetime.now()
    )

    AddProductCommentAPI(
        path_params=add_comment_path_params,
        request_body=add_comment_request_body
    ).send()

    # 然后删除这个评论
    path_params = DeleteCommentAPI.PathParams(comment_id=6)

    res = DeleteCommentAPI(path_params=path_params).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.message == "评论删除成功"


@pytest.mark.mock_api
def test_upload_avatar():
    """测试上传头像API"""
    path_params = UploadAvatarAPI.PathParams(user_id=1)
    request_body = UploadAvatarAPI.RequestBodyModel(
        file_name="avatar.png",
        file_size=2048,
        file_type="image/png"
    )

    res = UploadAvatarAPI(
        path_params=path_params,
        request_body=request_body
    ).send()

    assert res.response_model.ret_code == 0
    assert res.response_model.data.file_name == "avatar.png"
    assert res.response_model.data.download_url is not None
    