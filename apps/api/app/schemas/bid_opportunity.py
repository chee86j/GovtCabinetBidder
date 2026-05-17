from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import AnyUrl, BaseModel, ConfigDict, Field

from app.models.enums import BidStatus, BidType


class BidOpportunityBase(BaseModel):
    bid_name: str = Field(min_length=1)
    agency: str = Field(min_length=1)
    location: str = Field(min_length=1)
    due_date: datetime | None = None
    bid_link: AnyUrl | None = None
    bid_type: BidType | None = None
    scope_summary: str | None = None
    material_required: bool | None = None
    labor_required: bool | None = None
    license_required: bool | None = None
    bond_required: bool | None = None
    insurance_required: bool | None = None
    workers_comp_required: bool | None = None
    prevailing_wage: bool | None = None
    site_visit_required: bool | None = None
    estimated_contract_size: str | None = None
    estimated_kitchens_units: int | None = None
    suggested_bid_range: str | None = None
    opportunity_score: int | None = Field(default=None, ge=0, le=100)
    status: BidStatus | None = None


class BidOpportunityCreate(BidOpportunityBase):
    pass


class BidOpportunityUpdate(BaseModel):
    bid_name: str | None = Field(default=None, min_length=1)
    agency: str | None = Field(default=None, min_length=1)
    location: str | None = Field(default=None, min_length=1)
    due_date: datetime | None = None
    bid_link: AnyUrl | None = None
    bid_type: BidType | None = None
    scope_summary: str | None = None
    material_required: bool | None = None
    labor_required: bool | None = None
    license_required: bool | None = None
    bond_required: bool | None = None
    insurance_required: bool | None = None
    workers_comp_required: bool | None = None
    prevailing_wage: bool | None = None
    site_visit_required: bool | None = None
    estimated_contract_size: str | None = None
    estimated_kitchens_units: int | None = None
    suggested_bid_range: str | None = None
    opportunity_score: int | None = Field(default=None, ge=0, le=100)
    status: BidStatus | None = None


class BidOpportunityRead(BidOpportunityBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: BidStatus
    created_at: datetime
    updated_at: datetime
