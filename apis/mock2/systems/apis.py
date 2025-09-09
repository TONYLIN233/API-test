from typing import Optional, List, Dict, Tuple, Union, Any
from attrs import define, field
from .models import SystemStatusResponse, FileUploadDataResponse
from aomaker.core.api_object import BaseAPIObject as BaseAPI
from aomaker.core.router import router

__ALL__ = [
    "GetSystemStatusApiSystemStatusGetAPI",
    "UploadFileApiFilesUploadPostAPI",
    "BatchUploadFilesApiFilesBatchUploadPostAPI",
]


@define(kw_only=True)
@router.get("/api/system/status")
class GetSystemStatusApiSystemStatusGetAPI(BaseAPI[SystemStatusResponse]):
    """获取当前系统的运行状态，包括版本、运行时间、资源使用情况等"""

    response: Optional[SystemStatusResponse] = field(default=SystemStatusResponse)
    endpoint_id: Optional[str] = field(
        default="get_system_status_api_system_status_get"
    )


@define(kw_only=True)
@router.post("/api/files/upload")
class UploadFileApiFilesUploadPostAPI(BaseAPI[FileUploadDataResponse]):
    """真实的文件上传接口，支持multipart/form-data格式，可以上传实际文件"""

    @define
    class RequestBodyModel:
        description: Optional[str] = field(
            default=None, metadata={"description": "文件描述"}
        )
        category: Optional[str] = field(
            default="general", metadata={"description": "文件分类"}
        )

    request_body: RequestBodyModel

    files: Union[Dict[str, Any], List[Tuple[str, Any]]] = field(
        metadata={"description": "file: 要上传的文件"}
    )
    response: Optional[FileUploadDataResponse] = field(default=FileUploadDataResponse)
    endpoint_id: Optional[str] = field(default="upload_file_api_files_upload_post")


@define(kw_only=True)
@router.post("/api/files/batch-upload")
class BatchUploadFilesApiFilesBatchUploadPostAPI(BaseAPI):
    """批量上传多个文件，支持multipart/form-data格式"""

    @define
    class RequestBodyModel:
        project: str = field(metadata={"description": "项目名称"})
        version: Optional[str] = field(default="1.0.0", metadata={"description": "版本号"})

    request_body: RequestBodyModel

    files: Union[Dict[str, Any], List[Tuple[str, Any]]] = field(
        metadata={"description": "files: 要上传的文件列表"}
    )
    endpoint_id: Optional[str] = field(
        default="batch_upload_files_api_files_batch_upload_post"
    )
