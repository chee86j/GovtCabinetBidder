from __future__ import annotations

from datetime import datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from app.models import BidStatus, BidType
from app.schemas import BidOpportunityCreate, BidOpportunityRead, BidOpportunityUpdate


def test_bid_opportunity_create_requires_core_fields() -> None:
    with pytest.raises(ValidationError) as exc_info:
        BidOpportunityCreate()

    message = str(exc_info.value)
    assert "bid_name" in message
    assert "agency" in message
    assert "location" in message


def test_bid_opportunity_create_rejects_invalid_opportunity_score() -> None:
    with pytest.raises(ValidationError, match="less than or equal to 100"):
        BidOpportunityCreate(
            bid_name="Kitchen Renovation",
            agency="Housing Authority",
            location="Albany, NY",
            opportunity_score=101,
        )


def test_bid_opportunity_create_rejects_invalid_bid_link() -> None:
    with pytest.raises(ValidationError, match="valid URL"):
        BidOpportunityCreate(
            bid_name="Kitchen Renovation",
            agency="Housing Authority",
            location="Albany, NY",
            bid_link="not-a-url",
        )


def test_bid_opportunity_create_accepts_valid_optional_fields() -> None:
    schema = BidOpportunityCreate(
        bid_name="Kitchen Renovation",
        agency="Housing Authority",
        location="Albany, NY",
        due_date="2026-06-01T15:30:00Z",
        bid_link="https://example.gov/bids/123",
        opportunity_score=85,
        bid_type=BidType.MATERIAL_ONLY,
    )

    assert schema.due_date == datetime(2026, 6, 1, 15, 30, 0, tzinfo=schema.due_date.tzinfo)
    assert str(schema.bid_link) == "https://example.gov/bids/123"
    assert schema.opportunity_score == 85


def test_bid_opportunity_update_allows_partial_updates() -> None:
    schema = BidOpportunityUpdate(opportunity_score=0)

    assert schema.opportunity_score == 0
    assert schema.bid_name is None


def test_bid_opportunity_read_exposes_response_fields() -> None:
    schema = BidOpportunityRead(
        id=uuid4(),
        bid_name="Kitchen Renovation",
        agency="Housing Authority",
        location="Albany, NY",
        due_date=None,
        bid_link=None,
        bid_type=BidType.UNKNOWN,
        scope_summary=None,
        material_required=None,
        labor_required=None,
        license_required=None,
        bond_required=None,
        insurance_required=None,
        workers_comp_required=None,
        prevailing_wage=None,
        site_visit_required=None,
        estimated_contract_size=None,
        estimated_kitchens_units=None,
        suggested_bid_range=None,
        opportunity_score=75,
        status=BidStatus.NEW,
        created_at=datetime(2026, 5, 17, 12, 0, 0),
        updated_at=datetime(2026, 5, 17, 12, 0, 0),
    )

    assert schema.status is BidStatus.NEW
