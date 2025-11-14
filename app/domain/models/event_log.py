import datetime
from uuid import UUID

from value_objects.event_type import EventType


class EventLog:
    id: UUID
    event_type: EventType
    payload: str
    created_at: datetime