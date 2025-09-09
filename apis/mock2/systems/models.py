from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict
from attrs import define, field

__ALL__ = ["SystemStatusResponse", "FileUploadResponse", "FileUploadDataResponse"]


@define(kw_only=True)
class SystemStatusResponse:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[Dict] = field(factory=dict)


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
