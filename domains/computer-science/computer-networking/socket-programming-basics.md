---
id: socket-programming-basics
title: Socket Programming and Network APIs
domain: computer-science
course: computer-networking
prerequisites:
- id: port-addressing-sockets
  type: hard
- id: system-calls
  type: hard
tags:
- socket-api
- programming
- tcp-client
- udp-client
- bind-listen-accept
stage: advanced
status: validated
---

# Socket Programming and Network APIs

## Core Idea
Sockets are the primary API for network programming. TCP servers use socket(), bind(), listen(), and accept() to receive connections; clients use socket() and connect(). UDP uses sendto() and recvfrom(). Understanding socket semantics is essential for building networked applications.

## Questions

```yaml
- question: "A TCP server calls socket(), bind(), listen(), and then accept(). A client connects and the server receives a new file descriptor from accept(). The server finishes handling that client, closes the client socket, and calls accept() again. What is happening on the second call to accept()?"
  type: multiple-choice
  options:
    - "The server is rebinding to a new port to accept a second connection"
    - "The server is waiting on the original listening socket for a second client to connect"
    - "The server is closing the listening socket and terminating"
    - "The server is reconnecting to the first client on a new descriptor"
  answer: 1
  explanation: "This reveals the critical distinction between the listening socket and the connected socket. The first accept() call returned a new, dedicated file descriptor for client A's conversation — that is now closed. But the original listening socket (bound to the port via bind() and listen()) is still open and still watching for new connections. The second accept() call blocks on that same listening socket, waiting for a second client. The listening socket persists for the server's lifetime; connected sockets come and go per client."

- question: "A UDP server is being designed to receive datagrams from multiple clients. Which of the following correctly describes the socket API sequence it should use?"
  type: multiple-choice
  options:
    - "socket() → bind() → listen() → accept() → recvfrom(), identical to a TCP server"
    - "socket() → bind() → recvfrom() / sendto(), skipping listen() and accept() because UDP is connectionless"
    - "socket() → connect() → recv(), since UDP requires a connection before receiving"
    - "socket() → listen() → sendto(), since UDP servers only send, never receive"
  answer: 1
  explanation: "UDP is connectionless: there is no handshake, no established connection state, and therefore no need for listen() (which marks a socket as willing to accept connection requests) or accept() (which completes a TCP handshake and returns a connected socket). A UDP server simply binds to a port and uses recvfrom() to receive datagrams — each call returns the sender's address so the server can respond with sendto(). The simplicity comes at the cost of reliability: UDP provides no guaranteed delivery, ordering, or duplicate elimination."

- question: "When a TCP server calls accept(), it gets back a new socket file descriptor that is distinct from the original listening socket — one specifically for communicating with the newly connected client."
  type: true-false
  answer: true
  explanation: "This distinction is one of the most important concepts in socket programming. The listening socket (created by socket(), bound via bind(), marked passive via listen()) remains open to receive future connection requests. accept() returns a separate, connected socket representing exactly one client conversation. Data is read from and written to this connected socket; the listening socket is not used for data transfer. When the conversation ends, you close the connected socket — not the listening socket, which continues accepting new clients."

- question: "A UDP server must call listen() before calling recvfrom(), just as a TCP server calls listen() before accept()."
  type: true-false
  answer: false
  explanation: "listen() is specific to connection-oriented (TCP) sockets. It marks a socket as passive, meaning it will accept incoming connection requests via accept(). UDP is connectionless — there are no connection requests to accept. A UDP server simply calls socket(), bind() to a port, and then recvfrom() to receive incoming datagrams directly. Calling listen() on a UDP socket would either fail or have no meaningful effect depending on the OS. The API asymmetry between TCP and UDP reflects their fundamentally different transport models."

- question: "Why does a simple TCP server that loops — calling accept(), handling one client completely, then looping back to accept() — fail to serve multiple simultaneous clients well, and what are the standard strategies to fix this?"
  type: short-answer
  answer: "Because sockets block by default, a server stuck inside recv() (or any other blocking call) waiting for client A to send data cannot simultaneously call accept() to receive client B's connection. Client B's connection sits in the listen backlog queue and is not served until client A's entire session finishes. Standard strategies include: (1) fork/thread per connection — spawn a new process or thread for each accepted client so blocking in one doesn't affect others; (2) non-blocking I/O with select(), poll(), or epoll() — monitor multiple socket file descriptors simultaneously and only read/write when data is available; (3) async I/O frameworks — event loops (like libuv or asyncio) that multiplex many connections in a single thread."
  explanation: "The blocking nature of the default socket API is a feature for simple cases but a fundamental limitation for production servers. The choice of concurrency strategy involves tradeoffs: threads have lower latency but higher memory cost per connection; select()/poll() scale to many connections but require more complex code; async frameworks hide the complexity but add abstraction. Understanding the raw blocking behavior is what makes these tradeoffs legible — and it explains why high-performance servers like nginx use event-loop architectures rather than one-thread-per-connection models."
```

## Explainer

You already know that port numbers identify specific processes on a host and that system calls are how user programs request services from the operating system kernel. A **socket** is the meeting point of these two ideas: it is an OS-managed endpoint for network communication, created and manipulated through a small set of system calls. When you create a socket, the kernel allocates internal buffers and state to track a network connection, and gives your program a file descriptor — an integer handle you use for all subsequent operations, just like reading or writing a file.

The TCP server workflow follows a predictable sequence. First, `socket()` creates an endpoint and specifies the protocol (TCP or UDP). Then `bind()` attaches it to a specific IP address and port number — this is where your knowledge of port addressing comes in, because bind tells the OS "I want to receive traffic arriving on port 8080." Next, `listen()` marks the socket as passive, meaning it will accept incoming connections rather than initiate them, and sets a backlog queue size for pending connections. Finally, `accept()` blocks until a client connects, then returns a *new* socket dedicated to that specific client conversation. The original listening socket stays open to accept more clients. This distinction — the listening socket versus the connected socket — is one of the most important concepts in socket programming.

The client side is simpler: `socket()` to create the endpoint, then `connect()` to initiate a TCP handshake with the server's IP and port. Once connected, both sides use `send()` and `recv()` (or `read()` and `write()`) to exchange data over the established connection. UDP skips the connection setup entirely — since it is connectionless, you use `sendto()` and `recvfrom()`, specifying the destination address with every message. There is no handshake, no connection state, and no guaranteed delivery, which matches UDP's lightweight design.

A common stumbling point is that sockets are **blocking by default**: `accept()` waits until a client connects, `recv()` waits until data arrives. For a server handling multiple clients, this means you need a concurrency strategy — spawning threads or processes per connection, or using non-blocking I/O with `select()` or `poll()` to monitor multiple sockets simultaneously. The socket API is deliberately low-level, giving you direct control over how your program interacts with the transport layer. Higher-level abstractions like HTTP libraries are built on top of sockets, but understanding the raw API lets you reason about what those abstractions are actually doing underneath.
