---
id: message-passing-ipc-semantics
title: 'Message Passing IPC: Semantics and Guarantees'
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication
  type: hard
- id: monitor-pattern-definition
  type: soft
builds-toward:
- shared-memory-ipc-mechanisms
tags:
- ipc
- message-passing
- semantics
stage: formal-systems
status: draft
---

# Message Passing IPC: Semantics and Guarantees

## Core Idea
Message passing provides asynchronous, indirect IPC: senders and receivers need not know each other. Semantics vary: blocking vs. non-blocking send/receive, FIFO vs. priority ordering, and reliability guarantees (at-most-once, at-least-once, exactly-once).
