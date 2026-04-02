from .schemas import (
    ClassificationResult,
    Incident,
    IncidentType,
    ReportRoute,
    RiskLevel,
)


def classify_incident(incident: Incident) -> ClassificationResult:
    if incident.incident_type == IncidentType.whatsapp_job_scam:
        return ClassificationResult(
            incident_id=incident.id,
            incident_type=incident.incident_type,
            risk_level=RiskLevel.medium,
            recommended_primary_route=ReportRoute.chakshu_sanchar_saathi,
            recommended_secondary_routes=[ReportRoute.ncrp],
            immediate_actions=[
                "Stop replying to the sender.",
                "Do not send money, OTPs, or identity documents.",
                "Capture screenshots, number, links, and payment requests.",
            ],
            reasoning=(
                "Suspicious recruitment message delivered over WhatsApp; "
                "fraudulent communication reporting is primary, with cybercrime "
                "reporting as secondary if harm occurred."
            ),
        )

    if incident.incident_type == IncidentType.password_theft:
        return ClassificationResult(
            incident_id=incident.id,
            incident_type=incident.incident_type,
            risk_level=RiskLevel.high,
            recommended_primary_route=ReportRoute.ncrp,
            recommended_secondary_routes=[
                ReportRoute.platform_support,
                ReportRoute.bank_support,
            ],
            immediate_actions=[
                "Change the password immediately.",
                "Log out of other sessions and enable MFA.",
                "Preserve phishing links, login alerts, and suspicious activity evidence.",
            ],
            reasoning=(
                "Possible account compromise requires urgent account securing and "
                "cybercrime reporting, with provider and bank follow-up when relevant."
            ),
        )

    return ClassificationResult(
        incident_id=incident.id,
        incident_type=incident.incident_type,
        risk_level=RiskLevel.medium,
        recommended_primary_route=ReportRoute.ncrp,
        recommended_secondary_routes=[],
        immediate_actions=[
            "Do not share money or sensitive documents.",
            "Preserve the full email, sender details, attachments, and any fake offer.",
        ],
        reasoning=(
            "Email-based job scam or phishing should be preserved carefully and "
            "routed to cybercrime reporting."
        ),
    )
