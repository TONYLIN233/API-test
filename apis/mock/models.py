from typing import Any, Dict, List, Optional
from datetime import datetime
from attrs import define, field

@define(kw_only=True)
class GenericResponse:
    ret_code: int = field(default=0)
    message: str = field(default="success")


@define(kw_only=True)
class GenericDataResponse(GenericResponse):
    data: Any = field(default=None)


@define(kw_only=True)
class GenericListResponse(GenericResponse):
    data: List[Any] = field(factory=list)
    total: int = field(default=0)


@define(kw_only=True)
class User:
    id: int = field()
    username: str = field()
    email: str = field()
    created_at: datetime = field()
    is_active: bool = field(default=True)


@define(kw_only=True)
class Product:
    id: int = field()
    name: str = field()
    price: float = field()
    description: Optional[str] = field(default=None)
    stock: int = field()
    category: str = field()


@define(kw_only=True)
class Order:
    id: int = field()
    user_id: int = field()
    products: List[Dict[str, Any]] = field()
    total_price: float = field()
    status: str = field()
    created_at: datetime = field()


@define(kw_only=True)
class Address:
    street: str = field()
    city: str = field()
    province: str = field()
    postal_code: str = field()
    country: str = field(default="中国")


@define(kw_only=True)
class UserDetail:
    user_id: int = field()
    address: Address = field()
    phone: str = field()
    birth_date: Optional[datetime] = field(default=None)
    tags: List[str] = field(factory=list)
    preferences: Dict[str, Any] = field(factory=dict)


@define(kw_only=True)
class Comment:
    id: int = field()
    product_id: int = field()
    user_id: int = field()
    content: str = field()
    rating: int = field()
    created_at: datetime = field()


@define(kw_only=True)
class ProductDetail:
    basic_info: Product = field()
    sales_count: int = field(default=0)
    comments: List[Comment] = field(factory=list)
    related_products: List[int] = field(factory=list)
    specifications: Dict[str, Any] = field(factory=dict)


@define(kw_only=True)
class FileUploadResponse:
    file_id: str = field()
    file_name: str = field()
    file_size: int = field()
    file_type: str = field()
    upload_time: datetime = field()
    download_url: str = field()


@define(kw_only=True)
class SystemStatus:
    status: str = field()
    version: str = field()
    uptime: str = field()
    cpu_usage: float = field()
    memory_usage: float = field()
    user_count: int = field()
    product_count: int = field()
    order_count: int = field()

@define(kw_only=True)
class UserResponse(GenericResponse):
    data: Optional[User] = field(default=None)

@define(kw_only=True)
class UserListResponse(GenericResponse):
    data: List[User] = field(factory=list)
    total: int = field(default=0)

@define(kw_only=True)
class UserDetailResponse(GenericResponse):
    data: Optional[UserDetail] = field(default=None)

# 产品相关响应模型
@define(kw_only=True)
class ProductResponse(GenericResponse):
    data: Optional[Product] = field(default=None)

@define(kw_only=True)
class ProductListResponse(GenericResponse):
    data: List[Product] = field(factory=list)
    total: int = field(default=0)

@define(kw_only=True)
class ProductDetailResponse(GenericResponse):
    data: Optional[ProductDetail] = field(default=None)

@define(kw_only=True)
class OrderResponse(GenericResponse):
    data: Optional[Order] = field(default=None)

@define(kw_only=True)
class OrderListResponse(GenericResponse):
    data: List[Order] = field(factory=list)
    total: int = field(default=0)

@define(kw_only=True)
class CommentResponse(GenericResponse):
    data: Optional[Comment] = field(default=None)

@define(kw_only=True)
class CommentListResponse(GenericResponse):
    data: List[Comment] = field(factory=list)
    total: int = field(default=0)

@define(kw_only=True)
class FileUploadDataResponse(GenericResponse):
    data: Optional[FileUploadResponse] = field(default=None)

@define(kw_only=True)
class SystemStatusResponse(GenericResponse):
    data: Optional[SystemStatus] = field(default=None)

@define(kw_only=True)
class TokenResponse:
    access_token: str = field()
    token_type: str = field()
    expires_in: int = field()

@define(kw_only=True)
class TokenResponseData(GenericDataResponse):
    data: Optional[TokenResponse] = field(default=None)   
    