# OpenClaw Integration

## Capability Advertisement
POST /agent/status
{ agent_id, capabilities, availability }

## Heartbeat
POST /agent/heartbeat
{ agent_id, state }

## Task Receive
POST /task/receive
{ task_id, payload }
