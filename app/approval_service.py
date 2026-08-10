from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import approval_crud
from app.approval_schemas import ApprovalCreate


def create(
    db: Session,
    request: ApprovalCreate,
):
    return approval_crud.create_approval(
        db,
        request,
    )


def get(
    db: Session,
    approval_id: str,
):
    approval = approval_crud.get_approval(
        db,
        approval_id,
    )

    if approval is None:
        raise HTTPException(
            status_code=404,
            detail="Approval not found",
        )

    return approval


def list_pending(
    db: Session,
):
    return approval_crud.get_pending_approvals(
        db,
    )


def approve(
    db: Session,
    approval_id: str,
    comments: str | None,
):
    approval = get(
        db,
        approval_id,
    )

    return approval_crud.approve(
        db,
        approval,
        comments,
    )


def reject(
    db: Session,
    approval_id: str,
    comments: str | None,
):
    approval = get(
        db,
        approval_id,
    )

    return approval_crud.reject(
        db,
        approval,
        comments,
    )