from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Dict
from attrs import define, field

__ALL__ = ["Order", "OrderResponse", "GenericResponse"]


@define(kw_only=True)
class Order:
    id: int = field()
    user_id: int = field()
    products: List[Dict] = field()
    total_price: float = field()
    status: str = field()
    created_at: datetime = field()


@define(kw_only=True)
class OrderResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[Order] = field(default=None)


@define(kw_only=True)
class GenericResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
