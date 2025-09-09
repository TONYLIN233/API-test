from typing import Optional, Dict, List, Any
from datetime import datetime

from attrs import define, field
from aomaker.core.router import router
from aomaker.core.api_object import BaseAPIObject

from .models import (
    UserListResponse,
    GenericResponse,
    UserDetailResponse,
    ProductResponse,
    ProductDetailResponse,
    Comment,
    Address,
    Product,
    UserResponse,
    OrderResponse, 
    CommentListResponse, 
    SystemStatusResponse, 
    CommentResponse, 
    ProductListResponse,
    FileUploadDataResponse,
    TokenResponseData

)

@define(kw_only=True)
@router.post("/api/login/token")
class LoginAPI(BaseAPIObject[TokenResponseData]):
    """登录"""

    @define
    class RequestBodyModel:
        username: str = field()
        password: str = field()

    request_body: RequestBodyModel
    response: Optional[TokenResponseData] = field(default=TokenResponseData)


@define(kw_only=True)
@router.get("/api/users")
class GetUsersAPI(BaseAPIObject[UserListResponse]):
    """获取用户列表"""

    @define
    class QueryParams:
        offset: int = field(default=0, metadata={"description": "偏移量"})
        limit: int = field(default=10, metadata={"description": "限制数量"})
        username: Optional[str] = field(
            default=None, metadata={"description": "用户名，模糊搜索"}
        )

    query_params: QueryParams = field(factory=QueryParams)
    response: Optional[UserListResponse] = field(default=UserListResponse)
    endpoint_id: Optional[str] = field(default="get_users_api_users_get")


@define(kw_only=True)
@router.get("/api/users/{user_id}")
class GetUserAPI(BaseAPIObject[UserResponse]):
    """获取单个用户信息"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    path_params: PathParams
    response: Optional[UserResponse] = field(default=UserResponse)
    endpoint_id: Optional[str] = field(default="get_user_api_users__user_id__get")


@define(kw_only=True)
@router.post("/api/users")
class CreateUserAPI(BaseAPIObject[UserResponse]):
    """创建新用户"""

    @define
    class RequestBodyModel:
        id: int = field()
        username: str = field()
        email: str = field()
        created_at: datetime = field()
        is_active: bool = field(default=True)

    request_body: RequestBodyModel
    response: Optional[UserResponse] = field(default=UserResponse)
    endpoint_id: Optional[str] = field(default="create_user_api_users_post")


@define(kw_only=True)
@router.get("/api/products")
class GetProductsAPI(BaseAPIObject[ProductListResponse]):
    """获取产品列表"""

    @define
    class QueryParams:
        offset: int = field(default=0, metadata={"description": "偏移量"})
        limit: int = field(default=10, metadata={"description": "限制数量"})
        category: Optional[str] = field(
            default=None, metadata={"description": "产品类别"}
        )

    query_params: QueryParams = field(factory=QueryParams)
    response: Optional[ProductListResponse] = field(default=ProductListResponse)
    endpoint_id: Optional[str] = field(default="get_products_api_products_get")


@define(kw_only=True)
@router.get("/api/products/{product_id}")
class GetProductAPI(BaseAPIObject[ProductResponse]):
    """获取单个产品信息"""

    @define
    class PathParams:
        product_id: int = field(metadata={"description": "产品ID"})

    path_params: PathParams
    response: Optional[ProductResponse] = field(default=ProductResponse)
    endpoint_id: Optional[str] = field(default="get_product_api_products__product_id__get")


@define(kw_only=True)
@router.post("/api/orders")
class CreateOrderAPI(BaseAPIObject[OrderResponse]):
    """创建新订单"""

    @define
    class RequestBodyModel:
        id: int = field()
        user_id: int = field()
        products: List[Dict[str, Any]] = field()
        total_price: float = field()
        status: str = field()
        created_at: datetime = field()

    request_body: RequestBodyModel
    response: Optional[OrderResponse] = field(default=OrderResponse)
    endpoint_id: Optional[str] = field(default="create_order_api_orders_post")


@define(kw_only=True)
@router.put("/api/orders/{order_id}/status")
class UpdateOrderStatusAPI(BaseAPIObject[GenericResponse]):
    """更新订单状态"""

    @define
    class PathParams:
        order_id: int = field(metadata={"description": "订单ID"})

    @define
    class RequestBodyModel:
        status: str = field(metadata={"description": "新状态"})

    path_params: PathParams
    request_body: RequestBodyModel
    response: Optional[GenericResponse] = field(default=GenericResponse)
    endpoint_id: Optional[str] = field(default="update_order_status_api_orders__order_id__status_put")


# 1. GET请求，带路径参数
@define(kw_only=True)
@router.get("/api/user_details/{user_id}")
class GetUserDetailAPI(BaseAPIObject[UserDetailResponse]):
    """获取用户详细信息"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    path_params: PathParams
    response: Optional[UserDetailResponse] = field(default=UserDetailResponse)
    endpoint_id: Optional[str] = field(default="get_user_detail_api_user_details__user_id__get")


# 2. GET请求，带查询参数
@define(kw_only=True)
@router.get("/api/comments")
class GetCommentsAPI(BaseAPIObject[CommentListResponse]):
    """获取评论列表"""

    @define
    class QueryParams:
        product_id: Optional[int] = field(default=None, metadata={"description": "产品ID"})
        user_id: Optional[int] = field(default=None, metadata={"description": "用户ID"})
        min_rating: Optional[int] = field(default=None, metadata={"description": "最低评分"})
        offset: int = field(default=0, metadata={"description": "偏移量"})
        limit: int = field(default=10, metadata={"description": "限制数量"})

    query_params: QueryParams = field(factory=QueryParams)
    response: Optional[CommentListResponse] = field(default=CommentListResponse)
    endpoint_id: Optional[str] = field(default="get_comments_api_comments_get")


# 3. GET请求，无路径参数和查询参数
@define(kw_only=True)
@router.get("/api/system/status")
class GetSystemStatusAPI(BaseAPIObject[SystemStatusResponse]):
    """获取系统状态"""

    response: Optional[SystemStatusResponse] = field(default=SystemStatusResponse)
    endpoint_id: Optional[str] = field(default="get_system_status_api_system_status_get")


# 4. POST请求，带路径参数和请求体
@define(kw_only=True)
@router.post("/api/products/{product_id}/comments")
class AddProductCommentAPI(BaseAPIObject[CommentResponse]):
    """添加产品评论"""

    @define
    class PathParams:
        product_id: int = field(metadata={"description": "产品ID"})

    @define
    class RequestBodyModel:
        id: int = field()
        product_id: int = field()
        user_id: int = field()
        content: str = field()
        rating: int = field()
        created_at: datetime = field()

    path_params: PathParams
    request_body: RequestBodyModel
    response: Optional[CommentResponse] = field(default=CommentResponse)
    endpoint_id: Optional[str] = field(default="add_product_comment_api_products__product_id__comments_post")


# 5. DELETE请求
@define(kw_only=True)
@router.delete("/api/comments/{comment_id}")
class DeleteCommentAPI(BaseAPIObject[GenericResponse]):
    """删除评论"""

    @define
    class PathParams:
        comment_id: int = field(metadata={"description": "评论ID"})

    path_params: PathParams
    response: Optional[GenericResponse] = field(default=GenericResponse)
    endpoint_id: Optional[str] = field(default="delete_comment_api_comments__comment_id__delete")


# 6. PATCH请求，模拟文件上传
@define(kw_only=True)
@router.patch("/api/users/{user_id}/avatar")
class UploadAvatarAPI(BaseAPIObject[FileUploadDataResponse]):
    """上传用户头像"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    @define
    class RequestBodyModel:
        file_name: str = field()
        file_size: int = field()
        file_type: str = field()

    path_params: PathParams
    request_body: RequestBodyModel
    response: Optional[FileUploadDataResponse] = field(default=FileUploadDataResponse)
    endpoint_id: Optional[str] = field(default="upload_avatar_api_users__user_id__avatar_patch")


# 7. PUT请求，更新用户详情
@define(kw_only=True)
@router.put("/api/user_details/{user_id}")
class UpdateUserDetailAPI(BaseAPIObject[UserDetailResponse]):
    """更新用户详细信息"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    @define
    class RequestBodyModel:
        user_id: int = field()
        address: Address = field()
        phone: str = field()
        birth_date: Optional[datetime] = field(default=None)
        tags: List[str] = field(factory=list)
        preferences: Dict[str, Any] = field(factory=dict)

    path_params: PathParams
    request_body: RequestBodyModel
    response: Optional[UserDetailResponse] = field(default=UserDetailResponse)
    endpoint_id: Optional[str] = field(default="update_user_detail_api_user_details__user_id__put")


# 8. 带嵌套模型的GET请求
@define(kw_only=True)
@router.get("/api/product_details/{product_id}")
class GetProductDetailAPI(BaseAPIObject[ProductDetailResponse]):
    """获取产品详细信息"""

    @define
    class PathParams:
        product_id: int = field(metadata={"description": "产品ID"})

    path_params: PathParams
    response: Optional[ProductDetailResponse] = field(default=ProductDetailResponse)
    endpoint_id: Optional[str] = field(default="get_product_detail_api_product_details__product_id__get")


# 9. 带嵌套模型的POST请求
@define(kw_only=True)
@router.post("/api/product_details")
class CreateProductDetailAPI(BaseAPIObject[ProductDetailResponse]):
    """创建产品详细信息"""

    @define
    class RequestBodyModel:
        basic_info: Product = field()
        sales_count: int = field(default=0)
        comments: List[Comment] = field(factory=list)
        related_products: List[int] = field(factory=list)
        specifications: Dict[str, Any] = field(factory=dict)

    request_body: RequestBodyModel
    response: Optional[ProductDetailResponse] = field(default=ProductDetailResponse)
    endpoint_id: Optional[str] = field(default="create_product_detail_api_product_details_post")
  
    