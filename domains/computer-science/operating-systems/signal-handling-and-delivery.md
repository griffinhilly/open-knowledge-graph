---
id: signal-handling-and-delivery
title: Signal Handling and Delivery
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
- id: interrupt-exception-handling
  type: soft
tags:
- signals
- asynchronous
- events
stage: formal-systems
status: draft
---

# Signal Handling and Delivery

## Core Idea
Signals are asynchronous notifications delivered to processes, interrupting their normal execution flow. A process can install signal handlers to respond to specific signals (SIGTERM, SIGUSR1, etc.) or use default behavior (termination, ignoring, core dump). Signal delivery is not guaranteed to be immediate, and blocking signals during critical sections prevents race conditions and data corruption.
