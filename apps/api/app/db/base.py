from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import model modules so their tables are registered on Base.metadata.
from app.models.bid_opportunity import BidOpportunity  # noqa: E402,F401
from app.models.labor_partner import LaborPartner  # noqa: E402,F401
from app.models.labor_material_match import LaborMaterialMatch  # noqa: E402,F401
from app.models.material_supplier import MaterialSupplier  # noqa: E402,F401
from app.models.pricing_benchmark import PricingBenchmark  # noqa: E402,F401
