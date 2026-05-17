from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import model modules so their tables are registered on Base.metadata.
from app.models.bid_opportunity import BidOpportunity  # noqa: E402,F401
from app.models.labor_partner import LaborPartner  # noqa: E402,F401
