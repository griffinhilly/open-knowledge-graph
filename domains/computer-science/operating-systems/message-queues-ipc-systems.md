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

## Explainer

From your study of IPC mechanisms, you know that processes can communicate through pipes and shared memory. Pipes work well for streaming byte data between a producer and consumer, but they have limitations: they carry unstructured byte streams, they are typically unidirectional, and the producer blocks when the buffer fills. **Message queues** address these limitations by providing structured, asynchronous, and potentially prioritized communication between processes.

Think of a message queue as a mailbox managed by the kernel. A sending process drops a discrete **message** — a self-contained unit with a type tag and a body — into the queue, and continues executing immediately without waiting for the receiver to pick it up. The receiver retrieves messages at its own pace, potentially selecting by type. This **temporal decoupling** is the key advantage: the sender and receiver do not need to be running at the same time or processing at the same rate. If the receiver is temporarily slow or busy, messages accumulate in the queue rather than blocking the sender (up to a configurable limit).

In the POSIX and System V IPC APIs, message queues live in the kernel and are identified by a key or name. Each message has a **type field** (a long integer) that the receiver can use to selectively retrieve messages — for example, a server process might use different type values for different client requests, allowing it to process urgent requests before routine ones. This is fundamentally different from pipes, where data is an undifferentiated byte stream and you must read bytes in strict FIFO order. The type-based selection makes message queues suitable for patterns where multiple logical channels share a single queue.

The tradeoff is overhead and complexity. Every send and receive involves a system call and data copying through the kernel, making message queues slower than shared memory for high-throughput scenarios. Queue size limits mean the sender eventually blocks or gets an error if the receiver falls too far behind. And the kernel resources consumed by the queue persist until explicitly removed, unlike pipes which clean up automatically when both ends close. For these reasons, message queues are best suited to scenarios with moderate message rates where the structured, asynchronous, priority-capable communication model justifies the overhead — such as task dispatching, event notification, or request-response protocols between loosely coupled services.
