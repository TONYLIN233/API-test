from datetime import datetime
from typing import List, Dict, Optional
from attrs import define, field
from .models import OrderResponse, GenericResponse
from aomaker.core.api_object import BaseAPIObject as BaseAPI
from aomaker.core.router import router

__ALL__ = [
    "CreateOrderApiOrdersPostAPI",
    "UpdateOrderStatusApiOrdersOrderIdStatusPutAPI",
]


@define(kw_only=True)
@router.post("/api/orders")
class CreateOrderApiOrdersPostAPI(BaseAPI[OrderResponse]):
    """创建一个新的订单"""

    @define
    class RequestBodyModel:
        id: int = field()
        user_id: int = field()
        products: List[Dict] = field()
        total_price: float = field()
        status: str = field()
        created_at: datetime = field()

    request_body: RequestBodyModel

    response: Optional[OrderResponse] = field(default=OrderResponse)
    endpoint_id: Optional[str] = field(default="create_order_api_orders_post")


@define(kw_only=True)
@router.put("/api/orders/{order_id}/status")
class UpdateOrderStatusApiOrdersOrderIdStatusPutAPI(BaseAPI[GenericResponse]):
    """根据订单ID更新订单的状态"""

    @define
    class PathParams:
        order_id: int = field(metadata={"description": "订单ID"})

    @define
    class RequestBodyModel:
        status: str = field(metadata={"description": "新的订单状态"})

    request_body: RequestBodyModel

    path_params: PathParams
    response: Optional[GenericResponse] = field(default=GenericResponse)
    endpoint_id: Optional[str] = field(
        default="update_order_status_api_orders__order_id__status_put"
    )
