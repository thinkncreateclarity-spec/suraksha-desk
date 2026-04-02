from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class IncidentType(str, Enum):
    whatsapp_job_scam = "whatsapp_job_scam"
    password_theft = "password_theft"
    email_job_scam = "email_job_scam"


class IncidentStatus(str, Enum):
    draft = "draft"
    in_progress = "in_progress"
    completed = "completed"


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class ReportRoute(str, Enum):
    chakshu_sanchar_saathi = "chakshu_sanchar_saathi"
    ncrp = "ncrp"
    helpline_1930 = "helpline_1930"
    bank_support = "bank_support"
    platform_support = "platform_support"


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


class ClassificationResult(BaseModel):
    incident_id: int
    incident_type: IncidentType
    risk_level: RiskLevel
    recommended_primary_route: ReportRoute
    recommended_secondary_routes: List[ReportRoute] = []
    immediate_actions: List[str] = []
    reasoning: str
