from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException, status

from .schemas import (
    ClassificationResult,
    Incident,
    IncidentCreate,
    IncidentStatus,
)
from .services_classification import classify_incident

router = APIRouter(prefix="/incidents", tags=["incidents"])

_incidents: list[Incident] = []
_next_id = 1


@router.post("/", response_model=Incident, status_code=status.HTTP_201_CREATED)
def create_incident(payload: IncidentCreate) -> Incident:
    global _next_id
    now = datetime.utcnow()
    incident = Incident(
        id=_next_id,
        status=IncidentStatus.draft,
        created_at=now,
        updated_at=now,
        **payload.dict(),
    )
    _incidents.append(incident)
    _next_id += 1
    return incident


@router.get("/", response_model=List[Incident])
def list_incidents() -> list[Incident]:
    return _incidents


@router.get("/{incident_id}", response_model=Incident)
def get_incident(incident_id: int) -> Incident:
    for incident in _incidents:
        if incident.id == incident_id:
            return incident
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Incident not found"
    )


@router.post("/{incident_id}/classify", response_model=ClassificationResult)
def classify_existing_incident(incident_id: int) -> ClassificationResult:
    for incident in _incidents:
        if incident.id == incident_id:
            return classify_incident(incident)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Incident not found"
    )
