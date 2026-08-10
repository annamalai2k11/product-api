from app.approval_models import Approval
from app.slack_service import send_approval_request


def send_approval_notification(
    approval: Approval,
):
    return send_approval_request(
        approval
    )