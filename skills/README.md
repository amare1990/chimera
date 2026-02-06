# Chimera Agent Skills

Definition:
A Skill is a deterministic capability package that performs internal logic
and may call MCP tools for external actions.

Skills MUST:
- be stateless
- have explicit input/output contracts
- be independently testable
- never directly call external SDKs

---

## skill_fetch_trends

Purpose:
Retrieve trending topics using configured MCP resource.

Input:
{
  "region": "string",
  "limit": number
}

Output:
{
  "topics": ["string"]
}

Uses:
- trend-resource MCP

---

## skill_generate_content

Purpose:
Generate persona-aligned content.

Input:
{
  "persona_id": "string",
  "topic": "string"
}

Output:
{
  "text": "string",
  "media_urls": ["string"]
}

Uses:
- LLM tool MCP

---

## skill_publish_post

Purpose:
Publish content to social platform.

Input:
{
  "platform": "string",
  "text": "string",
  "media_urls": ["string"]
}

Output:
{
  "post_id": "string"
}

Uses:
- social-post MCP
