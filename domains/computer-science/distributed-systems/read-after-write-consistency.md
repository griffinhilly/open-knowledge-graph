---
id: read-after-write-consistency
title: Read-After-Write Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- strong-eventual-consistency
tags:
- consistency
- session-consistency
- guarantees
stage: advanced
status: draft
---

# Read-After-Write Consistency

## Core Idea
Read-after-write (RaW) consistency, also called session consistency, guarantees that if a client writes data, all its subsequent reads will reflect that write. This is weaker than linearizability but captures a natural expectation: 'I just wrote my profile, I should see it when I reload.' It is often sufficient for user-facing applications.
