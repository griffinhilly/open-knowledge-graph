---
id: message-queues-ipc-systems
title: Message Queues and Message Passing IPC
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication-mechanisms
  type: hard
- id: semaphores
  type: soft
tags:
- ipc
- message-queues
- asynchronous
stage: formal-systems
status: draft
---

# Message Queues and Message Passing IPC

## Core Idea
Message queues enable asynchronous communication where processes send discrete messages that queue in the kernel until the receiver retrieves them. The kernel manages the queue, decoupling sender and receiver in time and making the system more resilient to transient overload. Message queues can enforce FIFO ordering, priority-based delivery, or type-based message selection.
