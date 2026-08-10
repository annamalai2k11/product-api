from sqlalchemy.orm import Session

from app.approval_constants import ApprovalStatus
from app.approval_models import Approval
from app.approval_schemas import ApprovalCreate


def create_approval(
    db: Session,
    request: ApprovalCreate,
):
    approval = Approval(
        request_type=request.request_type,
        requested_by=request.requested_by,
        payload=request.payload,
    )

    db.add(approval)
    db.commit()
    db.refresh(approval)

    return approval


def get_approval(
    db: Session,
    approval_id: str,
):
    return (
        db.query(Approval)
        .filter(
            Approval.approval_id == approval_id
        )
        .first()
    )


def get_pending_approvals(
    db: Session,
):
    return (
        db.query(Approval)
        .filter(
            Approval.status == ApprovalStatus.PENDING
        )
        .all()
    )


def approve(
    db: Session,
    approval: Approval,
    comments: str | None,
):
    approval.status = ApprovalStatus.APPROVED
    approval.comments = comments

    db.commit()
    db.refresh(approval)

    return approval


def reject(
    db: Session,
    approval: Approval,
    comments: str | None,
):
    approval.status = ApprovalStatus.REJECTED
    approval.comments = comments

    db.commit()
    db.refresh(approval)

    return approval