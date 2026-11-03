from fastapi import FastAPI, BackgroundTasks
from datetime import timedelta
from .models import Booking, GuestMessage, PricingRequest
from .supabase_client import supabase

app = FastAPI(title="Base360 Airbnb Automation - Penjani")

@app.post("/webhooks/airbnb")
async def airbnb_webhook(booking: Booking, background_tasks: BackgroundTasks):
    supabase.table("reservations").upsert({
        "id": booking.booking_id,
        "property_id": booking.property_id,
        "guest_name": booking.guest_name,
        "checkin": booking.checkin.isoformat(),
        "checkout": booking.checkout.isoformat(),
        "status": booking.status
    }).execute()
    cleaning_time = booking.checkout + timedelta(hours=2)
    supabase.table("cleaning_tasks").insert({
        "property_id": booking.property_id,
        "booking_id": booking.booking_id,
        "scheduled_at": cleaning_time.isoformat(),
        "status": "pending"
    }).execute()
    background_tasks.add_task(lambda: print(f"SMS Cleaning {booking.property_id}"))
    return {"status": "ok", "cleaning_scheduled_at": cleaning_time.isoformat()}

@app.post("/guest/message")
async def guest_ai(msg: GuestMessage):
    return {"reply": f"Hi {msg.guest_name}! Check-in: Code 1234, 2nd floor. WiFi: Flex_Guest"}

@app.post("/pricing/adjust")
async def adjust_pricing(req: PricingRequest):
    new_price = req.base_price * 0.85 if req.occupancy_next_7_days < 0.5 else req.base_price
    return {"new_price": round(new_price,2)}

@app.get("/")
async def root():
    return {"message": "Base360 prep by Penjani - Ready"}
