from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Base
from app.schemas import EventSchema
from app.ingestion import ingest_events
from app.metrics import get_metrics
from app.funnel import get_funnel
from app.anomalies import get_anomalies
from app.health import health_status

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Store Intelligence API")


@app.get("/")
def home():
    return {"message": "Store Intelligence API Running"}


@app.get("/health")
def health():
    return health_status()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/events/ingest")
def ingest(
    events: list[EventSchema],
    db: Session = Depends(get_db)
):
    return ingest_events(db, events)


@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str, db: Session = Depends(get_db)):
    return get_metrics(db, store_id)


@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str, db: Session = Depends(get_db)):
    return get_funnel(db, store_id)


@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str, db: Session = Depends(get_db)):
    return get_anomalies(db, store_id)