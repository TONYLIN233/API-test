from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Dict
from attrs import define, field

__ALL__ = [
    "User",
    "UserListResponse",
    "UserResponse",
    "Address",
    "UserDetail",
    "UserDetailResponse",
    "FileUploadResponse",
    "FileUploadDataResponse",
]


@define(kw_only=True)
class User:
    id: int = field()
    username: str = field()
    email: str = field()
    created_at: datetime = field()
    is_active: Optional[bool] = field(default=True)


@define(kw_only=True)
class UserListResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[List[User]] = field(default=None)
    total: Optional[int] = field(default=0)


@define(kw_only=True)
class UserResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[User] = field(default=None)


@define(kw_only=True)
class Address:
    street: str = field()
    city: str = field()
    province: str = field()
    postal_code: str = field()
    country: Optional[str] = field(default="中国")


@define(kw_only=True)
class UserDetail:
    user_id: int = field()
    address: Address = field()
    phone: str = field()
    birth_date: Optional[datetime] = field(default=None)
    tags: Optional[List[str]] = field(default=None)
    preferences: Optional[Dict] = field(factory=dict)


@define(kw_only=True)
class UserDetailResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[UserDetail] = field(default=None)


@define(kw_only=True)
class FileUploadResponse:
    file_id: str = field()
    file_name: str = field()
    file_size: int = field()
    file_type: str = field()
    upload_time: datetime = field()
    download_url: str = field()


@define(kw_only=True)
class FileUploadDataResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[FileUploadResponse] = field(default=None)
