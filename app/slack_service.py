import json

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from app.approval_models import Approval
from app.config import get_slack_bot_token, get_slack_manager_channel_id


client = WebClient(
    token=get_slack_bot_token()
)


def send_approval_request(
    approval: Approval,
):
    try:
        print("Sending Slack message...")
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Product Approval Request"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Approval Id*\n{approval.approval_id}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Requested By*\n{approval.requested_by}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Request Type*\n{approval.request_type.value}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Status*\n{approval.status.value}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```{json.dumps(approval.payload, indent=2)}```"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "✅ Approve"
                        },
                        "style": "primary",
                        "action_id": "approve_product",
                        "value": json.dumps({
                            "approval_id": approval.approval_id,
                            "action": "APPROVE"
                        })
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "❌ Reject"
                        },
                        "style": "danger",
                        "action_id": "reject_product",
                        "value": json.dumps({
                            "approval_id": approval.approval_id,
                            "action": "REJECT"
                        })
                    }
                ]
            }
        ]

        response = client.chat_postMessage(
            channel=get_slack_manager_channel_id(),
            text="Approval Request",
            blocks=blocks
        )
        return response


    except SlackApiError as ex:
        raise Exception(ex.response["error"])

def update_approval_message(
    channel: str,
    ts: str,
    approved: bool,
    approver: str,
):
    text = (
        f"✅ Approved by {approver}"
        if approved
        else f"❌ Rejected by {approver}"
    )

    try:
        response = client.chat_update(
            channel=channel,
            ts=ts,
            text=text,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text,
                    },
                }
            ],
        )

        return response

    except SlackApiError as ex:
        print(ex.response.data)
        raise Exception(ex.response["error"])