# Technical Specification

---

## API Contracts

### POST /trend.fetch
Request
{
  "region": "string",
  "limit": number
}

Response
{
  "topics": ["string"]
}

---

### POST /content.generate
Request
{
  "persona_id": "string",
  "topic": "string"
}

Response
{
  "text": "string",
  "media_urls": ["string"]
}

---

## Agent Skill Interfaces

### skill_fetch_trends
Input:
{ region, limit }

Output:
{ topics[] }

### skill_generate_content
Input:
{ persona_id, topic }

Output:
{ text, media_urls }

---

## Database Schema

Agent
- id
- persona_file

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
