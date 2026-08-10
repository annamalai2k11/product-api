from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.approval_schemas import ApprovalCreate
from app.approval_schemas import ApprovalResponse
from app.approval_schemas import ApprovalStatusResponse
from app.approval_schemas import ApprovalStatusUpdate
from app.approval_service import approve
from app.approval_service import create
from app.approval_service import get
from app.approval_service import list_pending
from app.approval_service import reject
from app.database import get_db
from app.notification_service import (
    send_approval_notification,
)

router = APIRouter(
    prefix="/approvals",
    tags=["Approvals"],
)


@router.post(
    "",
    response_model=ApprovalResponse,
)
def create_approval(
    request: ApprovalCreate,
    db: Session = Depends(get_db),
):
    approval = create(
        db,
        request,
    )

    try:
        response = send_approval_notification(
            approval,
        )

        approval.slack_channel = response["channel"]
        approval.slack_ts = response["ts"]

        db.commit()
        db.refresh(approval)

        return approval

    except Exception:
        db.rollback()
        raise


@router.get(
    "",
    response_model=list[ApprovalResponse],
)
def get_pending(
    db: Session = Depends(get_db),
):
    return list_pending(db)


@router.get(
    "/{approval_id}",
    response_model=ApprovalResponse,
)
def get_approval(
    approval_id: str,
    db: Session = Depends(get_db),
):
    return get(
        db,
        approval_id,
    )


@router.post(
    "/{approval_id}/approve",
    response_model=ApprovalStatusResponse,
)
def approve_request(
    approval_id: str,
    request: ApprovalStatusUpdate,
    db: Session = Depends(get_db),
):
    return approve(
        db,
        approval_id,
        request.comments,
    )


@router.post(
    "/{approval_id}/reject",
    response_model=ApprovalStatusResponse,
)
def reject_request(
    approval_id: str,
    request: ApprovalStatusUpdate,
    db: Session = Depends(get_db),
):
    return reject(
        db,
        approval_id,
        request.comments,
    )