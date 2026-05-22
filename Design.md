# DESIGN DOCUMENT

# 1. Introduction

The Store Intelligence Platform is an AI-powered retail analytics system designed to convert raw CCTV footage into actionable business intelligence.

The platform processes store activity in real time and generates insights related to:

- customer movement
- zone engagement
- billing congestion
- dwell behavior
- conversion analytics
- operational anomalies

The system combines:

- Computer Vision
- Event-Driven Architecture
- Backend APIs
- Real-Time Analytics
- Dashboard Visualization

to create a scalable retail intelligence platform.

---

# 2. Design Goals

The architecture was designed with the following goals:

| Goal | Description |
|---|---|
| Scalability | Support multiple stores and cameras |
| Real-Time Analytics | Provide live business insights |
| Modularity | Independent reusable components |
| Maintainability | Easy debugging and extension |
| Production Readiness | Enterprise-style architecture |
| Extensibility | Future AI and cloud integration |
| Fault Isolation | Failure in one component should not crash entire system |

---

# 3. High-Level Architecture

```text
CCTV Videos
      ↓
Detection Pipeline
      ↓
Event Generation
      ↓
FastAPI Backend
      ↓
PostgreSQL Database
      ↓
Analytics Engine
      ↓
Streamlit Dashboard
```

---

# 4. Architecture Components

# 4.1 Detection Pipeline

## File

```text
pipeline/detect.py
```

## Purpose

Processes CCTV videos and detects customers.

## Responsibilities

- video frame processing
- person detection
- tracking
- zone mapping
- dwell measurement
- event generation

## Output

Structured JSON events.

---

# 4.2 Event Layer

## Purpose

Converts raw visual information into standardized events.

## Example Event

```json
{
  "event_type": "ZONE_DWELL",
  "visitor_id": "VIS_001",
  "zone_id": "SKINCARE",
  "dwell_ms": 42000
}
```

## Benefits

- decoupled architecture
- easier debugging
- replayability
- scalable streaming

---

# 4.3 FastAPI Backend

## File

```text
app/main.py
```

## Responsibilities

- event ingestion
- validation
- metrics APIs
- funnel APIs
- anomaly APIs

## Why FastAPI

- asynchronous support
- automatic documentation
- high performance
- clean API structure

---

# 4.4 Database Layer

## Technology

PostgreSQL

## Responsibilities

Stores:

- visitor events
- timestamps
- dwell analytics
- queue metrics
- conversion data

## Why PostgreSQL

- transactional consistency
- SQL analytics support
- scalability
- reliability

---

# 4.5 Analytics Layer

## Files

```text
app/metrics.py
app/funnel.py
app/anomalies.py
```

## Responsibilities

Calculates:

- conversion rate
- average dwell
- funnel metrics
- congestion analytics
- anomalies

---

# 4.6 Dashboard Layer

## File

```text
dashboard/streamlit_app.py
```

## Responsibilities

Displays:

- real-time metrics
- conversion funnel
- anomalies
- visitor analytics

## Why Streamlit

- fast dashboard development
- Python-native
- easy integration

---

# 5. Data Flow Design

# Step 1 — Video Input

Videos are configured inside:

```text
config/store_layout.json
```

This file defines:

- camera IDs
- video paths
- store layout
- zones

---

# Step 2 — Detection

YOLO processes frames and identifies people.

---

# Step 3 — Tracking

Visitors are tracked across frames.

---

# Step 4 — Event Generation

Behavior is converted into JSON events.

---

# Step 5 — Event Ingestion

Events are sent to FastAPI APIs.

---

# Step 6 — Database Storage

Events are stored in PostgreSQL.

---

# Step 7 — Analytics Processing

Metrics and anomalies are computed.

---

# Step 8 — Dashboard Visualization

Business users monitor live KPIs.

---

# 6. Why Event-Driven Architecture Was Used

Instead of directly connecting video processing with analytics, events were introduced as an intermediate layer.

## Benefits

| Benefit | Explanation |
|---|---|
| Scalability | Easier multi-store expansion |
| Replayability | Historical event replay |
| Debugging | Easier issue tracing |
| Streaming Support | Future Kafka compatibility |
| Loose Coupling | Independent services |

---

# 7. Detection Design

# Model Selected

YOLOv8n

## Why

- lightweight
- fast inference
- production ready
- sufficient retail accuracy

## Business Advantage

Enables real-time retail analytics.

---

# 8. Database Design

# Core Table

## Events Table

Stores:

- visitor_id
- event_type
- timestamp
- zone_id
- dwell_ms
- confidence

## Design Philosophy

Immutable event storage.

Advantages:

- replay support
- auditing
- historical analysis

---

# 9. API Design

# APIs

| Endpoint | Purpose |
|---|---|
| /events/ingest | ingest events |
| /stores/{id}/metrics | KPIs |
| /stores/{id}/funnel | conversion funnel |
| /stores/{id}/anomalies | anomaly alerts |
| /health | service health |

---

# 10. Scalability Considerations

The design considers future scaling.

## Future Improvements

- Kafka streaming
- Redis caching
- Kubernetes deployment
- cloud inference
- distributed workers

---

# 11. Reliability Considerations

System designed considering:

- camera failures
- API downtime
- queue spikes
- dropped frames

## Techniques

- retries
- health checks
- modular services

---

# 12. Security Considerations

Production improvements may include:

- JWT authentication
- HTTPS encryption
- RBAC
- encrypted credentials
- audit logging
- API rate limiting

---

# 13. Performance Considerations

The system prioritizes low latency.

## Optimizations

- async APIs
- lightweight models
- efficient event schema
- modular processing

---

# 14. Maintainability Considerations

The project uses:

- modular folders
- separated concerns
- reusable services
- configuration-driven setup

Benefits:

- easier debugging
- easier onboarding
- easier upgrades

---

# 15. Future Enhancements

Potential future upgrades:

- facial recognition
- AI heatmaps
- customer segmentation
- predictive staffing
- cloud analytics
- recommendation systems

---

# 16. Conclusion

The Store Intelligence Platform was designed as a scalable, modular, and production-oriented retail analytics system.

The architecture transforms CCTV footage into actionable business intelligence using:

- AI
- APIs
- databases
- analytics
- dashboards

The event-driven design ensures scalability and future extensibility for enterprise retail deployments.