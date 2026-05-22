# CHOICES DOCUMENT

# 1. Introduction

This document explains the major technical and architectural decisions made during the development of the Store Intelligence Platform.

Each choice was evaluated considering:

- scalability
- simplicity
- production readiness
- development speed
- maintainability
- business value

---

# 2. Programming Language Choice

# Selected

Python

## Alternatives Considered

- Java
- Node.js
- C++

## Why Python Was Selected

| Reason | Explanation |
|---|---|
| AI ecosystem | Excellent CV and ML libraries |
| Faster development | Reduced implementation time |
| Strong backend support | FastAPI integration |
| Community support | Large ecosystem |

## Business Benefit

Reduced development cost and faster prototyping.

---

# 3. Backend Framework Choice

# Selected

FastAPI

## Alternatives Considered

- Flask
- Django
- Express.js

## Why FastAPI Was Selected

| Advantage | Explanation |
|---|---|
| High performance | Async architecture |
| Validation | Pydantic integration |
| Documentation | Automatic Swagger docs |
| Scalability | Production-ready APIs |

## Business Benefit

Supports scalable real-time analytics APIs.

---

# 4. Database Choice

# Selected

PostgreSQL

## Alternatives Considered

- SQLite
- MongoDB
- MySQL

## Why PostgreSQL Was Selected

| Advantage | Explanation |
|---|---|
| Reliability | Production-grade database |
| SQL support | Strong analytics capability |
| Scalability | Multi-store support |
| Transactions | Data consistency |

## Business Benefit

Supports enterprise-level analytics storage.

---

# 5. ORM Choice

# Selected

SQLAlchemy

## Alternatives Considered

- Raw SQL
- Django ORM
- Peewee

## Why SQLAlchemy Was Selected

| Advantage | Explanation |
|---|---|
| Maintainability | Cleaner code |
| Flexibility | Advanced query support |
| Portability | Easier DB migration |

## Business Benefit

Reduces long-term maintenance complexity.

---

# 6. Detection Model Choice

# Selected

YOLOv8n

## Alternatives Considered

- FasterRCNN
- SSD
- RT-DETR

## Why YOLOv8 Was Selected

| Advantage | Explanation |
|---|---|
| Fast inference | Real-time performance |
| Lightweight | Lower hardware cost |
| Accuracy | Strong retail detection |
| Simplicity | Easier deployment |

## Business Benefit

Enables live customer analytics.

---

# 7. Video Processing Library Choice

# Selected

OpenCV

## Alternatives Considered

- PIL
- FFmpeg-only pipelines

## Why OpenCV Was Selected

| Advantage | Explanation |
|---|---|
| Industry standard | Widely adopted |
| Video support | Real-time frame handling |
| Performance | Efficient processing |

## Business Benefit

Reliable retail video analytics.

---

# 8. Dashboard Framework Choice

# Selected

Streamlit

## Alternatives Considered

- React
- Tableau
- Power BI

## Why Streamlit Was Selected

| Advantage | Explanation |
|---|---|
| Fast development | Minimal frontend effort |
| Python-native | Easy integration |
| Interactive | Real-time analytics |

## Business Benefit

Rapid dashboard delivery.

---

# 9. Event Schema Choice

# Selected

JSON Events

## Alternatives Considered

- Relational-only schema
- Binary protobuf schema

## Why JSON Was Selected

| Advantage | Explanation |
|---|---|
| Human-readable | Easier debugging |
| Flexible | Extensible metadata |
| Streaming-friendly | Kafka compatibility |

## Business Benefit

Supports scalable event architecture.

---

# 10. Architecture Style Choice

# Selected

Event-Driven Architecture

## Alternatives Considered

- tightly coupled processing
- monolithic analytics pipeline

## Why Event-Driven Was Selected

| Advantage | Explanation |
|---|---|
| Scalability | Multi-service support |
| Replayability | Historical processing |
| Fault isolation | Better resilience |
| Extensibility | Future integrations |

## Business Benefit

Enterprise scalability.

---

# 11. Deployment Choice

# Selected

Docker

## Alternatives Considered

- manual installation
- VM deployment

## Why Docker Was Selected

| Advantage | Explanation |
|---|---|
| Environment consistency | Same behavior everywhere |
| Easy deployment | One-command startup |
| Isolation | Cleaner infrastructure |

## Business Benefit

Simplifies deployment and evaluation.

---

# 12. API Server Choice

# Selected

Uvicorn

## Alternatives Considered

- Gunicorn
- Waitress

## Why Uvicorn Was Selected

| Advantage | Explanation |
|---|---|
| Async support | FastAPI compatibility |
| Lightweight | Efficient runtime |
| Performance | High throughput |

## Business Benefit

Supports high event ingestion rates.

---

# 13. Why PostgreSQL Was Preferred Over SQLite

SQLite was useful for local testing but PostgreSQL was selected for production realism.

## PostgreSQL Advantages

- concurrent users
- better scaling
- enterprise reliability
- stronger analytics support

## Business Benefit

Suitable for large retail deployments.

---

# 14. Why Streamlit Was Chosen Over React

React provides better frontend flexibility but increases development complexity.

Streamlit was selected because:

- faster implementation
- Python-only stack
- rapid prototyping
- sufficient for analytics dashboards

## Business Benefit

Reduced development effort and faster delivery.

---

# 15. Why Lightweight Tracking Was Used

Deep ReID systems were not implemented because:

- higher complexity
- GPU requirements
- longer development time

Instead, lightweight tracking heuristics were used.

## Business Benefit

Faster implementation while maintaining acceptable analytics quality.

---

# 16. Why Modular Folder Structure Was Used

The project separates:

- APIs
- pipelines
- dashboards
- configs
- tests

Benefits:

- maintainability
- scalability
- easier collaboration

---

# 17. Tradeoffs Considered

| Decision | Tradeoff |
|---|---|
| YOLOv8n | Slightly lower accuracy for faster inference |
| Streamlit | Less frontend flexibility for faster development |
| JSON events | Larger payload size for better readability |
| Lightweight tracking | Reduced identity persistence for simplicity |

---

# 18. Future Enterprise Improvements

Potential upgrades include:

- Kafka
- Redis
- Kubernetes
- GPU inference clusters
- cloud deployment
- Spark analytics

---

# 19. Conclusion

The technology choices prioritized:

- production readiness
- scalability
- rapid development
- maintainability
- business value

The final architecture balances engineering practicality with enterprise scalability while demonstrating strong AI and backend engineering capabilities.