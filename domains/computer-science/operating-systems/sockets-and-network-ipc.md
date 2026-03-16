---
id: sockets-and-network-ipc
title: Sockets and Network Inter-Process Communication
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication-mechanisms
  type: hard
tags:
- ipc
- sockets
- networking
stage: formal-systems
status: draft
---

# Sockets and Network Inter-Process Communication

## Core Idea
Sockets are the primary mechanism for network communication and can also be used for local IPC via Unix domain sockets. TCP sockets provide reliable, connection-oriented communication; UDP sockets provide connectionless, datagram-based communication. Unix domain sockets enable efficient local inter-process communication without network stack overhead.

## Explainer

You have already studied IPC mechanisms like pipes and shared memory, which let processes on the same machine exchange data. Sockets extend this idea across a network — they let processes communicate whether they are on the same machine, across a room, or across the world. A **socket** is an endpoint for communication, identified by an address and a port number. When two processes each create a socket and connect them, they get a bidirectional communication channel that works through the standard read/write file descriptor interface you already know from Unix I/O.

The two main socket types correspond to two fundamentally different communication models. **TCP sockets** (SOCK_STREAM) provide a reliable, ordered byte stream — the OS guarantees that data arrives in order, without duplication, and retransmits anything lost in transit. The tradeoff is setup cost: TCP requires a three-way handshake to establish a connection before any data flows. This is the right choice for web servers, databases, SSH sessions, and anything where correctness matters more than latency. **UDP sockets** (SOCK_DGRAM) provide a connectionless, best-effort datagram service — each send is an independent message with no delivery guarantee. UDP is faster (no handshake, no retransmission overhead) and suits applications like video streaming, DNS lookups, and online games where occasional packet loss is acceptable and low latency is critical.

The typical TCP workflow follows a client-server pattern. The server calls **socket()** to create a socket, **bind()** to attach it to an address and port, **listen()** to mark it as accepting connections, and **accept()** to wait for a client. The client calls socket() and then **connect()** to reach the server. After the connection is established, both sides use read() and write() (or send() and recv()) to exchange data, just as they would with a file descriptor. This uniformity — treating network connections like files — is one of Unix's most powerful abstractions.

For processes on the same machine, **Unix domain sockets** offer the best of both worlds: the socket API's flexibility with the performance of local IPC. Instead of an IP address and port, Unix domain sockets use a filesystem path as their address (e.g., /var/run/app.sock). Data never touches the network stack, so communication is significantly faster than TCP loopback. Many production systems use Unix domain sockets for communication between co-located services — for example, a web server talking to a database on the same host, or a container communicating with its orchestrator. Understanding when to use TCP, UDP, or Unix domain sockets is a practical skill that comes up in nearly every systems programming context.
