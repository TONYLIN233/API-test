from typing import Optional, List, Dict
from attrs import define, field
from .models import (
    ProductListResponse,
    ProductResponse,
    ProductDetailResponse,
    Product,
    Comment,
)
from aomaker.core.api_object import BaseAPIObject as BaseAPI
from aomaker.core.router import router

__ALL__ = [
    "GetProductsApiProductsGetAPI",
    "GetProductApiProductsProductIdGetAPI",
    "GetProductDetailApiProductDetailsProductIdGetAPI",
    "CreateProductDetailApiProductDetailsPostAPI",
]


@define(kw_only=True)
@router.get("/api/products")
class GetProductsApiProductsGetAPI(BaseAPI[ProductListResponse]):
    """获取系统中的产品列表，支持分页和按类别筛选"""

    @define
    class QueryParams:
        offset: Optional[int] = field(default=0, metadata={"description": "偏移量，用于分页"})
        limit: Optional[int] = field(default=10, metadata={"description": "限制数量，用于分页"})
        category: Optional[str] = field(
            default=None, metadata={"description": "产品类别，精确匹配"}
        )

    query_params: QueryParams = field(factory=QueryParams)
    response: Optional[ProductListResponse] = field(default=ProductListResponse)
    endpoint_id: Optional[str] = field(default="get_products_api_products_get")


@define(kw_only=True)
@router.get("/api/products/{product_id}")
class GetProductApiProductsProductIdGetAPI(BaseAPI[ProductResponse]):
    """根据产品ID获取单个产品的详细信息"""

    @define
    class PathParams:
        product_id: int = field(metadata={"description": "产品ID"})

    path_params: PathParams
    response: Optional[ProductResponse] = field(default=ProductResponse)
    endpoint_id: Optional[str] = field(
        default="get_product_api_products__product_id__get"
    )

@define(kw_only=True)
@router.get("/api/products/{product_id}")
class GetProductApiProductsProductIdGetAPI(BaseAPI[ProductResponse]):
    """根据产品ID获取单个产品的详细信息"""

    @define
    class PathParams:
        product_id: int = field(metadata={"description": "产品ID"})

    path_params: PathParams
    response: Optional[ProductResponse] = field(default=ProductResponse)
    endpoint_id: Optional[str] = field(
        default="get_product_api_products__product_id__get"
    )



@define(kw_only=True)
@router.get("/api/product_details/{product_id}")
class GetProductDetailApiProductDetailsProductIdGetAPI(BaseAPI[ProductDetailResponse]):
    """根据产品ID获取产品的详细信息，包括销售数据、评论等"""

    @define
    class PathParams:
        product_id: int = field(metadata={"description": "产品ID"})

    path_params: PathParams
    response: Optional[ProductDetailResponse] = field(default=ProductDetailResponse)
    endpoint_id: Optional[str] = field(
        default="get_product_detail_api_product_details__product_id__get"
    )


@define(kw_only=True)
@router.post("/api/product_details")
class CreateProductDetailApiProductDetailsPostAPI(BaseAPI[ProductDetailResponse]):
    """创建一个新的产品详细信息"""

    @define
    class RequestBodyModel:
        basic_info: Product = field()
        sales_count: Optional[int] = field(default=0)
        comments: Optional[List[Comment]] = field(default=None)
        related_products: Optional[List[int]] = field(default=None)
        specifications: Optional[Dict] = field(factory=dict)

    request_body: RequestBodyModel

    response: Optional[ProductDetailResponse] = field(default=ProductDetailResponse)
    endpoint_id: Optional[str] = field(
        default="create_product_detail_api_product_details_post"
    )
