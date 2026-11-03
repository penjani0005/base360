from pydantic import BaseModel
from datetime import datetime

class Booking(BaseModel):
    booking_id: str
    property_id: str
    guest_name: str
    checkin: datetime
    checkout: datetime
    guest_message: str = ""
    status: str = "confirmed"

class GuestMessage(BaseModel):
    property_id: str
    guest_name: str
    message: str

class PricingRequest(BaseModel):
    property_id: str
    base_price: float
    occupancy_next_7_days: float
