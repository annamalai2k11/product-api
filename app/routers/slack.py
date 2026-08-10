import json

from fastapi import APIRouter
from fastapi import Form
from sqlalchemy.orm import Session

from app.approval_constants import ApprovalStatus
from app.approval_service import get
from app.database import SessionLocal
from app.slack_service import update_approval_message

router = APIRouter(
    prefix="/slack",
    tags=["Slack"],
)


@router.post("/actions")
async def slack_actions(
    payload: str = Form(...),
):
    body = json.loads(payload)

    action = body["actions"][0]
    value = json.loads(action["value"])

    approval_id = value["approval_id"]
    approve = value["action"] == "APPROVE"
    approver = body["user"]["username"]

    db: Session = SessionLocal()

    try:
        approval = get(
            db,
            approval_id,
        )

        approval.status = (
            ApprovalStatus.APPROVED
            if approve
            else ApprovalStatus.REJECTED
        )

        db.commit()
        db.refresh(approval)

        update_approval_message(
            approval.slack_channel,
            approval.slack_ts,
            approve,
            approver,
        )

        return ""

    finally:
        db.close()