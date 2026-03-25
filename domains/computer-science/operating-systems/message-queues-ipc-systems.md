---
id: message-queues-ipc-systems
title: Message Queues and Message Passing IPC
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication
  type: hard
- id: semaphores
  type: soft
tags:
- ipc
- message-queues
- asynchronous
stage: formal-systems
status: validated
---

# Message Queues and Message Passing IPC

## Core Idea
Message queues enable asynchronous communication where processes send discrete messages that queue in the kernel until the receiver retrieves them. The kernel manages the queue, decoupling sender and receiver in time and making the system more resilient to transient overload. Message queues can enforce FIFO ordering, priority-based delivery, or type-based message selection.

## Questions

```yaml
- question: "A web server receives unpredictable bursts of image-processing requests that take 200ms each to handle. The processing is done by a separate worker process. Should the server use a pipe or a message queue to send jobs to the worker, and why?"
  type: multiple-choice
  options:
    - "A pipe — it is faster and lower overhead than a message queue"
    - "A message queue — the server can enqueue bursts immediately without blocking, and the worker processes jobs at its own pace"
    - "A pipe — it supports priority ordering, so urgent requests can jump the queue"
    - "A message queue — it uses shared memory internally so it is faster for large image data"
  answer: 1
  explanation: "The key advantage of message queues is temporal decoupling: the sender (web server) deposits a message and continues executing immediately, without waiting for the receiver (worker) to consume it. During a burst, messages accumulate in the queue rather than blocking the server. A pipe would block the server once the pipe buffer fills, degrading responsiveness. Message queues also support typed/priority messages (pipes carry only undifferentiated byte streams). The lower throughput compared to shared memory is acceptable here since image jobs are discrete, moderate-frequency events."

- question: "What distinguishes message queues from pipes as IPC mechanisms?"
  type: multiple-choice
  options:
    - "Pipes support multiple senders and receivers; message queues support only one of each"
    - "Message queues carry typed, discrete messages that can be selectively retrieved; pipes carry an undifferentiated byte stream that must be read in strict FIFO order"
    - "Message queues require both processes to run simultaneously; pipes do not"
    - "Pipes are managed by the kernel; message queues are managed by user-space libraries"
  answer: 1
  explanation: "Pipes stream raw bytes — the receiver must process data in exactly the order it was sent, with no structure beyond byte position. Message queues carry discrete messages with type fields, allowing the receiver to selectively retrieve messages by type (e.g., process priority messages before routine ones). This makes message queues suitable for multi-channel communication within a single queue. The opposite is true for synchronization: pipes block the writer when full and the reader when empty; message queues asynchronously decouple sender and receiver."

- question: "When a process sends a message to a message queue, it blocks until the receiving process retrieves the message."
  type: true-false
  answer: false
  explanation: "Temporal decoupling is the defining feature of message queues. The sender deposits the message into the kernel-managed queue and returns immediately — the receiver does not need to be running or even to exist at the moment of sending. The sender only blocks if the queue is full (at its configured capacity limit), at which point it waits for the receiver to drain some messages. This asynchronous behavior is exactly what makes message queues useful for handling rate mismatches between producers and consumers."

- question: "Message queue resources in the POSIX/System V kernel persist until they are explicitly removed, even if all processes that used the queue have terminated."
  type: true-false
  answer: true
  explanation: "This is a deliberate design difference from pipes. Pipes are reference-counted: when both the read and write ends are closed, the kernel cleans up automatically. Message queues have kernel persistence — they survive process termination and remain available (with any unread messages) until a process explicitly deletes them (via mq_unlink or msgctl IPC_RMID). This allows a new process to start, find the existing queue by name or key, and read messages left by a process that has since exited. The tradeoff is that abandoned queues accumulate kernel resources if not cleaned up."

- question: "Explain temporal decoupling in message queues — what it means and why it matters for system design."
  type: short-answer
  answer: "Temporal decoupling means the sender and receiver do not need to be running simultaneously or processing at the same rate. The sender deposits a message into the kernel queue and continues executing; the receiver retrieves messages at its own pace. This matters because it absorbs rate mismatches: if the receiver is temporarily overloaded, messages buffer in the queue rather than blocking or crashing the sender. It also simplifies restart logic — if the receiver crashes and restarts, unprocessed messages remain in the queue. This pattern is foundational to resilient system design and is the precursor to distributed message brokers like RabbitMQ and Kafka."
  explanation: "Without temporal decoupling (as with synchronous IPC like pipes or direct function calls), sender and receiver must be synchronized — the sender waits for the receiver, creating tight coupling. Temporal decoupling trades a small amount of latency and memory (the queue buffer) for resilience and flexibility. It enables the sender to continue serving requests during receiver downtime, and allows horizontal scaling by adding multiple consumers reading from the same queue."
```

## Explainer

From your study of IPC mechanisms, you know that processes can communicate through pipes and shared memory. Pipes work well for streaming byte data between a producer and consumer, but they have limitations: they carry unstructured byte streams, they are typically unidirectional, and the producer blocks when the buffer fills. **Message queues** address these limitations by providing structured, asynchronous, and potentially prioritized communication between processes.

Think of a message queue as a mailbox managed by the kernel. A sending process drops a discrete **message** — a self-contained unit with a type tag and a body — into the queue, and continues executing immediately without waiting for the receiver to pick it up. The receiver retrieves messages at its own pace, potentially selecting by type. This **temporal decoupling** is the key advantage: the sender and receiver do not need to be running at the same time or processing at the same rate. If the receiver is temporarily slow or busy, messages accumulate in the queue rather than blocking the sender (up to a configurable limit).

In the POSIX and System V IPC APIs, message queues live in the kernel and are identified by a key or name. Each message has a **type field** (a long integer) that the receiver can use to selectively retrieve messages — for example, a server process might use different type values for different client requests, allowing it to process urgent requests before routine ones. This is fundamentally different from pipes, where data is an undifferentiated byte stream and you must read bytes in strict FIFO order. The type-based selection makes message queues suitable for patterns where multiple logical channels share a single queue.

The tradeoff is overhead and complexity. Every send and receive involves a system call and data copying through the kernel, making message queues slower than shared memory for high-throughput scenarios. Queue size limits mean the sender eventually blocks or gets an error if the receiver falls too far behind. And the kernel resources consumed by the queue persist until explicitly removed, unlike pipes which clean up automatically when both ends close. For these reasons, message queues are best suited to scenarios with moderate message rates where the structured, asynchronous, priority-capable communication model justifies the overhead — such as task dispatching, event notification, or request-response protocols between loosely coupled services.
