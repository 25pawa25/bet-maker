import enum
import uuid
from decimal import Decimal

from sqlalchemy import DECIMAL, CheckConstraint, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.orm import Mapped

from db.postgres.models.base_model import BaseModel, Column
from db.postgres.models.mixins import IdMixin, TsMixinCreated, TsMixinUpdated


@enum.unique
class BetStatus(enum.Enum):
    PENDING = "pending"
    WIN = "win"
    FAILED = "failed"


class Bet(BaseModel, IdMixin, TsMixinCreated, TsMixinUpdated):
    """Data model for bet db table."""

    __tablename__ = "bet"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="bet_pkey"),
        CheckConstraint("amount > 0", name="check_amount_positive"),
    )
    event_id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True),
        nullable=False,
    )
    amount: Mapped[Decimal] = Column(DECIMAL(precision=15, scale=2), nullable=False)
    status: Mapped[str] = Column(
        ENUM(BetStatus, name="bet_status"), nullable=False, default=BetStatus.PENDING
    )
    # Можно добавить поле "Цель ставки" (на победу кого ставим)

    def __repr__(self):
        return (
            f"Bet(id={self.id}, event_id={self.event_id}, amount={self.amount}, "
            f"status={self.status}, created_at={self.created_at}, updated_at={self.updated_at})"
        )
