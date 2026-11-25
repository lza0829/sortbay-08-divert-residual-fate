from __future__ import annotations

from fastapi import APIRouter

from app.db import db
from app.services.ledger import overview_snapshot

router = APIRouter(tags=["总览"])


@router.get("/总览")
@router.get("/overview")
@router.get("/dashboard")
def overview():
    with db() as conn:
        return overview_snapshot(conn)
