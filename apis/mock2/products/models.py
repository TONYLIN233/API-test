from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Dict
from attrs import define, field

__ALL__ = [
    "Product",
    "ProductListResponse",
    "ProductResponse",
    "Comment",
    "ProductDetail",
    "ProductDetailResponse",
]


@define(kw_only=True)
class Product:
    id: int = field()
    name: str = field()
    price: float = field()
    stock: int = field()
    category: str = field()
    description: Optional[str] = field(default=None)


@define(kw_only=True)
class ProductListResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[List[Product]] = field(default=None)
    total: Optional[int] = field(default=0)


@define(kw_only=True)
class ProductResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[Product] = field(default=None)


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
    sales_count: Optional[int] = field(default=0)
    comments: Optional[List[Comment]] = field(default=None)
    related_products: Optional[List[int]] = field(default=None)
    specifications: Optional[Dict] = field(factory=dict)


@define(kw_only=True)
class ProductDetailResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[ProductDetail] = field(default=None)
