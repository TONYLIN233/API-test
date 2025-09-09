from __future__ import annotations

from datetime import datetime
from typing import Optional, List
from attrs import define, field

__ALL__ = ["Comment", "CommentListResponse", "CommentResponse", "GenericResponse"]


@define(kw_only=True)
class Comment:
    id: int = field()
    product_id: int = field()
    user_id: int = field()
    content: str = field()
    rating: int = field()
    created_at: datetime = field()


@define(kw_only=True)
class CommentListResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[List[Comment]] = field(default=None)
    total: Optional[int] = field(default=0)


@define(kw_only=True)
class CommentResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[Comment] = field(default=None)


@define(kw_only=True)
class GenericResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
