from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class EventSchema(BaseModel):
    event_id: str
    store_id: str
    camera_id: str
    visitor_id: str
    event_type: str
    timestamp: datetime
    zone_id: Optional[str]
    dwell_ms: int
    is_staff: bool
    confidence: float
    metadata: Dict