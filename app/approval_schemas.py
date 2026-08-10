from datetime import datetime

from pydantic import BaseModel,ConfigDict

from app.approval_constants import ApprovalStatus
from app.approval_constants import RequestType


class ApprovalCreate(BaseModel):
    request_type: RequestType
    requested_by: str
    payload: dict


class ApprovalResponse(BaseModel):
    approval_id: str
    request_type: RequestType
    requested_by: str
    status: ApprovalStatus
    payload: dict
    comments: str | None
    model_config = ConfigDict(from_attributes=True)


class ApprovalStatusUpdate(BaseModel):
    comments: str | None = None


class ApprovalStatusResponse(BaseModel):
    approval_id: str
    status: ApprovalStatus
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)