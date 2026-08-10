import json

from fastapi import APIRouter
from fastapi import Form
from sqlalchemy.orm import Session

from app.approval_constants import ApprovalStatus, RequestType
from app.approval_service import get
from app.crud import create_product as create_product_db
from app.database import SessionLocal
from app.schemas import ProductCreate
from app.slack_service import update_approval_message, update_approval_message_user
from app.config import get_slack_user_channel_id

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

        if approve:
            if approval.request_type == RequestType.CREATE_PRODUCT:
                product_payload = ProductCreate.model_validate(approval.payload)
                create_product_db(product_payload, db)

        db.commit()
        db.refresh(approval)

        update_approval_message(
            approval.slack_channel,
            approval.slack_ts,
            approve,
            approver,
        )

        update_approval_message_user(
            get_slack_user_channel_id(),
            approval.status,
            approval_id,
            approver
        )

        return ""

    finally:
        db.close()