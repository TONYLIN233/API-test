from datetime import datetime
from typing import Optional
from attrs import define, field
from .models import CommentListResponse, CommentResponse, GenericResponse
from aomaker.core.api_object import BaseAPIObject as BaseAPI
from aomaker.core.router import router

__ALL__ = [
    "GetCommentsApiCommentsGetAPI",
    "AddProductCommentApiProductsProductIdCommentsPostAPI",
    "DeleteCommentApiCommentsCommentIdDeleteAPI",
]


@define(kw_only=True)
@router.get("/api/comments")
class GetCommentsApiCommentsGetAPI(BaseAPI[CommentListResponse]):
    """获取系统中的评论列表，支持按产品ID、用户ID和最低评分筛选"""

    @define
    class QueryParams:
        product_id: Optional[int] = field(
            default=None, metadata={"description": "产品ID"}
        )
        user_id: Optional[int] = field(default=None, metadata={"description": "用户ID"})
        min_rating: Optional[int] = field(
            default=None, metadata={"description": "最低评分，1-5"}
        )
        offset: Optional[int] = field(default=0, metadata={"description": "偏移量，用于分页"})
        limit: Optional[int] = field(default=10, metadata={"description": "限制数量，用于分页"})

    query_params: QueryParams = field(factory=QueryParams)
    response: Optional[CommentListResponse] = field(default=CommentListResponse)
    endpoint_id: Optional[str] = field(default="get_comments_api_comments_get")


@define(kw_only=True)
@router.post("/api/products/{product_id}/comments")
class AddProductCommentApiProductsProductIdCommentsPostAPI(BaseAPI[CommentResponse]):
    """为指定产品添加一条评论"""

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

    request_body: RequestBodyModel

    path_params: PathParams
    response: Optional[CommentResponse] = field(default=CommentResponse)
    endpoint_id: Optional[str] = field(
        default="add_product_comment_api_products__product_id__comments_post"
    )


@define(kw_only=True)
@router.delete("/api/comments/{comment_id}")
class DeleteCommentApiCommentsCommentIdDeleteAPI(BaseAPI[GenericResponse]):
    """根据评论ID删除一条评论"""

    @define
    class PathParams:
        comment_id: int = field(metadata={"description": "评论ID"})

    path_params: PathParams
    response: Optional[GenericResponse] = field(default=GenericResponse)
    endpoint_id: Optional[str] = field(
        default="delete_comment_api_comments__comment_id__delete"
    )
