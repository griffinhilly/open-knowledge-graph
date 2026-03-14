---
id: cache-line-and-offset
title: Cache Line Organization and Byte Offset
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-memory-design
  type: hard
- id: memory-hierarchy-overview
  type: hard
tags:
- cache
- memory-organization
stage: formal-systems
status: draft
---

# Cache Line Organization and Byte Offset

## Core Idea
Cache lines (typically 32–128 bytes) are the unit of cache allocation. Addresses split into tag (identifies line), index (line location within set), and offset (byte within line), exploiting spatial locality.
