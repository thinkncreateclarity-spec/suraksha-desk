from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class IncidentType(str, Enum):
    whatsapp_job_scam = "whatsapp_job_scam"
    password_theft = "password_theft"
    email_job_scam = "email_job_scam"


class IncidentStatus(str, Enum):
    draft = "draft"
    in_progress = "in_progress"
    completed = "completed"


class IncidentBase(BaseModel):
    incident_type: IncidentType = Field(..., description="High-level incident category")
    title: str = Field(..., min_length=3, max_length=200)
    description: str = Field(..., min_length=3, max_length=4000)
    happened_at: Optional[datetime] = None


class IncidentCreate(IncidentBase):
    pass


class Incident(IncidentBase):
    id: int
    status: IncidentStatus = IncidentStatus.draft
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
