---
id: sockets-and-network-ipc
title: Sockets and Network Inter-Process Communication
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication
  type: hard
tags:
- ipc
- sockets
- networking
stage: formal-systems
status: validated
---

# Sockets and Network Inter-Process Communication

## Core Idea
Sockets are the primary mechanism for network communication and can also be used for local IPC via Unix domain sockets. TCP sockets provide reliable, connection-oriented communication; UDP sockets provide connectionless, datagram-based communication. Unix domain sockets enable efficient local inter-process communication without network stack overhead.

## Questions

```yaml
- question: "A DNS server needs to respond to thousands of short queries per second from many clients. Occasional packet loss is acceptable because clients retry automatically. Which socket type is most appropriate?"
  type: multiple-choice
  options:
    - "TCP (SOCK_STREAM), because reliability is important for DNS correctness"
    - "UDP (SOCK_DGRAM), because low latency and connectionless operation suit short, retry-tolerant queries"
    - "Unix domain sockets, because DNS servers and clients run on the same machine"
    - "TCP with SO_LINGER set to zero, to avoid the three-way handshake overhead"
  answer: 1
  explanation: "DNS is the canonical real-world example of UDP's strengths. Each query is a single small datagram with a self-contained response — no state needs to persist between exchanges. UDP eliminates TCP's three-way handshake, which would double the round-trip time for a protocol where sub-millisecond response is normal. Clients already implement their own retry logic, so OS-level reliability is unnecessary overhead. TCP is appropriate when data ordering, reliability, and multi-message sessions matter (HTTP, SSH, databases). Unix domain sockets are for local IPC only."

- question: "A web application server and its database run on the same physical machine. The developer is choosing between TCP loopback (127.0.0.1) and a Unix domain socket for their connection. What is the primary advantage of the Unix domain socket?"
  type: multiple-choice
  options:
    - "Unix domain sockets support both TCP and UDP semantics simultaneously"
    - "Unix domain sockets bypass the network stack entirely, reducing overhead and latency"
    - "Unix domain sockets are more secure because they cannot be accessed over a network"
    - "Unix domain sockets allow multiple processes to share a single file descriptor"
  answer: 1
  explanation: "The decisive advantage is performance. TCP loopback, despite being local, still processes the full network stack — IP header construction, checksum calculation, routing decisions, and TCP segment handling — even though the data never leaves the machine. Unix domain sockets use a filesystem path as their address and transfer data entirely within kernel memory, bypassing all of that. The result is measurably lower latency and higher throughput. While the security benefit (option C) is real, it is a secondary consideration; the primary motivation in production systems like Nginx-to-PostgreSQL connections is reduced overhead."

- question: "Unix domain sockets use IP addresses and port numbers to identify communication endpoints."
  type: true-false
  answer: false
  explanation: "Unix domain sockets use filesystem paths as their addresses (e.g., /var/run/postgres/.s.PGSQL.5432 or /tmp/app.sock). Instead of binding to an IP address and port, the server calls bind() with a filesystem path, and the client connects to that path. This is why Unix domain sockets are purely local — they have no concept of a network address. The tradeoff is that both processes must be on the same machine and have access to the same filesystem. This path-based addressing is also why Unix domain sockets leave a socket file on the filesystem that must be cleaned up when the server exits."

- question: "A TCP server must call listen() and accept() before a client can connect, establishing a connection through a three-way handshake."
  type: true-false
  answer: true
  explanation: "This is the TCP connection lifecycle. listen() marks the socket as passive (willing to accept incoming connections) and creates a backlog queue for pending connection requests. accept() blocks until a client connects, then returns a new socket dedicated to that client session. The three-way handshake (SYN → SYN-ACK → ACK) happens automatically between client's connect() and server's accept() returning. This setup cost is the price of TCP's reliability guarantees. UDP, by contrast, has no connection phase — the server simply calls recvfrom() and messages arrive without prior setup."

- question: "Why might a production system prefer Unix domain sockets over TCP loopback for communication between two processes running on the same machine?"
  type: short-answer
  answer: "Unix domain sockets bypass the network stack entirely. TCP loopback still processes IP and TCP headers, performs checksums, and goes through the full kernel networking subsystem even though no data ever crosses a network interface. Unix domain sockets transfer data directly between kernel buffers using a filesystem path as the address, eliminating that overhead. The result is lower latency and higher throughput for local IPC — which matters at scale when a web server makes hundreds of database calls per request."
  explanation: "The network stack isn't free even on loopback. Profiling studies consistently show that Unix domain socket connections have 30-50% lower latency than TCP loopback for typical database query workloads. Production systems like PostgreSQL, Redis, and Nginx all support Unix domain sockets specifically for co-located deployments. The tradeoff is that you lose the ability to move either process to a separate host without a configuration change — but that's usually acceptable when performance is the priority."
```

## Explainer

You have already studied IPC mechanisms like pipes and shared memory, which let processes on the same machine exchange data. Sockets extend this idea across a network — they let processes communicate whether they are on the same machine, across a room, or across the world. A **socket** is an endpoint for communication, identified by an address and a port number. When two processes each create a socket and connect them, they get a bidirectional communication channel that works through the standard read/write file descriptor interface you already know from Unix I/O.

The two main socket types correspond to two fundamentally different communication models. **TCP sockets** (SOCK_STREAM) provide a reliable, ordered byte stream — the OS guarantees that data arrives in order, without duplication, and retransmits anything lost in transit. The tradeoff is setup cost: TCP requires a three-way handshake to establish a connection before any data flows. This is the right choice for web servers, databases, SSH sessions, and anything where correctness matters more than latency. **UDP sockets** (SOCK_DGRAM) provide a connectionless, best-effort datagram service — each send is an independent message with no delivery guarantee. UDP is faster (no handshake, no retransmission overhead) and suits applications like video streaming, DNS lookups, and online games where occasional packet loss is acceptable and low latency is critical.

The typical TCP workflow follows a client-server pattern. The server calls **socket()** to create a socket, **bind()** to attach it to an address and port, **listen()** to mark it as accepting connections, and **accept()** to wait for a client. The client calls socket() and then **connect()** to reach the server. After the connection is established, both sides use read() and write() (or send() and recv()) to exchange data, just as they would with a file descriptor. This uniformity — treating network connections like files — is one of Unix's most powerful abstractions.

For processes on the same machine, **Unix domain sockets** offer the best of both worlds: the socket API's flexibility with the performance of local IPC. Instead of an IP address and port, Unix domain sockets use a filesystem path as their address (e.g., /var/run/app.sock). Data never touches the network stack, so communication is significantly faster than TCP loopback. Many production systems use Unix domain sockets for communication between co-located services — for example, a web server talking to a database on the same host, or a container communicating with its orchestrator. Understanding when to use TCP, UDP, or Unix domain sockets is a practical skill that comes up in nearly every systems programming context.
