from datetime import datetime
from typing import Optional, List, Dict
from attrs import define, field
from .models import (
    UserListResponse,
    UserResponse,
    UserDetailResponse,
    Address,
    FileUploadDataResponse,
)
from aomaker.core.api_object import BaseAPIObject as BaseAPI
from aomaker.core.router import router

__ALL__ = [
    "GetUsersApiUsersGetAPI",
    "CreateUserApiUsersPostAPI",
    "GetUserApiUsersUserIdGetAPI",
    "GetUserDetailApiUserDetailsUserIdGetAPI",
    "UpdateUserDetailApiUserDetailsUserIdPutAPI",
    "UploadAvatarApiUsersUserIdAvatarPatchAPI",
]


@define(kw_only=True)
@router.get("/api/users")
class GetUsersApiUsersGetAPI(BaseAPI[UserListResponse]):
    """获取系统中的用户列表，支持分页和按用户名模糊搜索"""

    @define
    class QueryParams:
        offset: Optional[int] = field(default=0, metadata={"description": "偏移量，用于分页"})
        limit: Optional[int] = field(default=10, metadata={"description": "限制数量，用于分页"})
        username: Optional[str] = field(
            default=None, metadata={"description": "用户名，支持模糊搜索"}
        )

    query_params: QueryParams = field(factory=QueryParams)
    response: Optional[UserListResponse] = field(default=UserListResponse)
    endpoint_id: Optional[str] = field(default="get_users_api_users_get")


@define(kw_only=True)
@router.post("/api/users")
class CreateUserApiUsersPostAPI(BaseAPI[UserResponse]):
    """创建一个新的用户"""

    @define
    class RequestBodyModel:
        id: int = field()
        username: str = field()
        email: str = field()
        created_at: datetime = field()
        is_active: Optional[bool] = field(default=True)

    request_body: RequestBodyModel

    response: Optional[UserResponse] = field(default=UserResponse)
    endpoint_id: Optional[str] = field(default="create_user_api_users_post")


@define(kw_only=True)
@router.get("/api/users/{user_id}")
class GetUserApiUsersUserIdGetAPI(BaseAPI[UserResponse]):
    """根据用户ID获取单个用户的详细信息"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    path_params: PathParams
    response: Optional[UserResponse] = field(default=UserResponse)
    endpoint_id: Optional[str] = field(default="get_user_api_users__user_id__get")


@define(kw_only=True)
@router.get("/api/user_details/{user_id}")
class GetUserDetailApiUserDetailsUserIdGetAPI(BaseAPI[UserDetailResponse]):
    """根据用户ID获取用户的详细信息，包括地址、联系方式等"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    path_params: PathParams
    response: Optional[UserDetailResponse] = field(default=UserDetailResponse)
    endpoint_id: Optional[str] = field(
        default="get_user_detail_api_user_details__user_id__get"
    )


@define(kw_only=True)
@router.put("/api/user_details/{user_id}")
class UpdateUserDetailApiUserDetailsUserIdPutAPI(BaseAPI[UserDetailResponse]):
    """根据用户ID更新用户的详细信息"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    @define
    class RequestBodyModel:
        user_id: int = field()
        address: Address = field()
        phone: str = field()
        birth_date: Optional[datetime] = field(default=None)
        tags: Optional[List[str]] = field(default=None)
        preferences: Optional[Dict] = field(factory=dict)

    request_body: RequestBodyModel

    path_params: PathParams
    response: Optional[UserDetailResponse] = field(default=UserDetailResponse)
    endpoint_id: Optional[str] = field(
        default="update_user_detail_api_user_details__user_id__put"
    )


@define(kw_only=True)
@router.patch("/api/users/{user_id}/avatar")
class UploadAvatarApiUsersUserIdAvatarPatchAPI(BaseAPI[FileUploadDataResponse]):
    """为指定用户上传头像文件"""

    @define
    class PathParams:
        user_id: int = field(metadata={"description": "用户ID"})

    path_params: PathParams
    response: Optional[FileUploadDataResponse] = field(default=FileUploadDataResponse)
    endpoint_id: Optional[str] = field(
        default="upload_avatar_api_users__user_id__avatar_patch"
    )
