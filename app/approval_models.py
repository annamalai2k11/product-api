from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, Enum, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.approval_constants import ApprovalStatus, RequestType
from .database import Base


class Approval(Base):
    __tablename__ = "approvals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    approval_id: Mapped[str] = mapped_column(
        String,
        unique=True,
        default=lambda: str(uuid4()),
        nullable=False,
    )
    request_type: Mapped[RequestType] = mapped_column(Enum(RequestType), nullable=False)
    requested_by: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[ApprovalStatus] = mapped_column(
        Enum(ApprovalStatus),
        default=ApprovalStatus.PENDING,
        nullable=False,
    )
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    comments: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    slack_channel: Mapped[str | None] = mapped_column(nullable=True)
    slack_ts: Mapped[str | None] = mapped_column(nullable=True)



