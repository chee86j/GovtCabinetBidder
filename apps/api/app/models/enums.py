from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SqlAlchemyEnum


class StrEnum(str, Enum):
    """String-valued enum base for API and ORM interoperability."""


def build_enum(enum_type: type[StrEnum], name: str) -> SqlAlchemyEnum:
    """Builds a SQLAlchemy enum that persists business-facing string values."""

    return SqlAlchemyEnum(
        enum_type,
        name=name,
        native_enum=False,
        values_callable=lambda members: [member.value for member in members],
        validate_strings=True,
    )


class BidType(StrEnum):
    MATERIAL_ONLY = "material_only"
    LABOR_ONLY = "labor_only"
    SUPPLY_AND_INSTALL = "supply_and_install"
    FULL_REHAB_UNIT_TURNOVER = "full_rehab_unit_turnover"
    COMMERCIAL_CASEWORK_MILLWORK = "commercial_casework_millwork"
    UNKNOWN = "unknown"


class BidStatus(StrEnum):
    NEW = "new"
    REVIEWING = "reviewing"
    NEED_PARTNER = "need_partner"
    PRICING = "pricing"
    SUBMITTED = "submitted"
    WON = "won"
    LOST = "lost"
    SKIPPED = "skipped"


class PartnerStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    REJECTED = "rejected"


class SupplierType(StrEnum):
    LOCAL_CABINET_WHOLESALER = "local_cabinet_wholesaler"
    RTA_SUPPLIER = "rta_supplier"
    IMPORTED_MANUFACTURER = "imported_manufacturer"
    COUNTERTOP_FABRICATOR = "countertop_fabricator"
    VANITY_SUPPLIER = "vanity_supplier"
    HARDWARE_SUPPLIER = "hardware_supplier"
    PLUMBING_APPLIANCE_SUPPLIER = "plumbing_appliance_supplier"
    OTHER = "other"
