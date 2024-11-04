from sqlalchemy import UniqueConstraint

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

from .mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (
        UniqueConstraint("foo", "bar"),
    )

