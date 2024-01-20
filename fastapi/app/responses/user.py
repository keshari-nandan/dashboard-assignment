

import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict


class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class UserResponse(BaseResponse):
    id: int
    first_name: str
    last_name: str
    email: str
    is_active: bool
    created_at: Union[str, None, datetime.datetime] = None

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: Union[str, None] = None
    expires_in: int
    token_type: str = "Bearer"