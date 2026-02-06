A - POST /trend.fetch

Request:
{
  "region": "ET",
  "limit": 10
}

Response:
{
  "topics": ["AI agents", "automation"]
}

B — Database schema

Video
- id
- title
- script
- status
- created_at

Trend
- id
- topic
- score

C — Agent Interfaces

Define skill IO.
