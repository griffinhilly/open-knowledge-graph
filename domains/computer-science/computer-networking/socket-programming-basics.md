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
status: draft
---

# Socket Programming and Network APIs

## Core Idea
Sockets are the primary API for network programming. TCP servers use socket(), bind(), listen(), and accept() to receive connections; clients use socket() and connect(). UDP uses sendto() and recvfrom(). Understanding socket semantics is essential for building networked applications.

## Explainer

You already know that port numbers identify specific processes on a host and that system calls are how user programs request services from the operating system kernel. A **socket** is the meeting point of these two ideas: it is an OS-managed endpoint for network communication, created and manipulated through a small set of system calls. When you create a socket, the kernel allocates internal buffers and state to track a network connection, and gives your program a file descriptor — an integer handle you use for all subsequent operations, just like reading or writing a file.

The TCP server workflow follows a predictable sequence. First, `socket()` creates an endpoint and specifies the protocol (TCP or UDP). Then `bind()` attaches it to a specific IP address and port number — this is where your knowledge of port addressing comes in, because bind tells the OS "I want to receive traffic arriving on port 8080." Next, `listen()` marks the socket as passive, meaning it will accept incoming connections rather than initiate them, and sets a backlog queue size for pending connections. Finally, `accept()` blocks until a client connects, then returns a *new* socket dedicated to that specific client conversation. The original listening socket stays open to accept more clients. This distinction — the listening socket versus the connected socket — is one of the most important concepts in socket programming.

The client side is simpler: `socket()` to create the endpoint, then `connect()` to initiate a TCP handshake with the server's IP and port. Once connected, both sides use `send()` and `recv()` (or `read()` and `write()`) to exchange data over the established connection. UDP skips the connection setup entirely — since it is connectionless, you use `sendto()` and `recvfrom()`, specifying the destination address with every message. There is no handshake, no connection state, and no guaranteed delivery, which matches UDP's lightweight design.

A common stumbling point is that sockets are **blocking by default**: `accept()` waits until a client connects, `recv()` waits until data arrives. For a server handling multiple clients, this means you need a concurrency strategy — spawning threads or processes per connection, or using non-blocking I/O with `select()` or `poll()` to monitor multiple sockets simultaneously. The socket API is deliberately low-level, giving you direct control over how your program interacts with the transport layer. Higher-level abstractions like HTTP libraries are built on top of sockets, but understanding the raw API lets you reason about what those abstractions are actually doing underneath.
