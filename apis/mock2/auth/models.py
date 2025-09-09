from __future__ import annotations

from typing import Optional
from attrs import define, field

__ALL__ = ["TokenResponse", "TokenResponseData"]


@define(kw_only=True)
class TokenResponse:
    access_token: str = field()
    token_type: str = field()
    expires_in: int = field()


@define(kw_only=True)
class TokenResponseData:
    ret_code: Optional[int] = field(default=0)
    message: Optional[str] = field(default="success")
    data: Optional[TokenResponse] = field(default=None)
