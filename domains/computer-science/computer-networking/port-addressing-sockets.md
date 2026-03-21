---
id: port-addressing-sockets
title: Port Addressing and Sockets
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: udp-user-datagram-protocol
  type: hard
builds-toward:
- socket-programming-basics
- dns-domain-name-system
- http-hypertext-transfer-protocol
tags:
- port
- socket
- demultiplexing
- well-known-ports
- ephemeral-ports
stage: advanced
status: draft
---

# Port Addressing and Sockets

## Core Idea
Ports are 16-bit identifiers that allow multiple applications to use the same transport protocol on a single host. A socket is an endpoint of a network connection, identified by a tuple (IP, protocol, port). Well-known ports (0–1023) are assigned to standard services; ephemeral ports (49152–65535) are assigned dynamically to clients.

## Questions

```yaml
- question: "A web server is listening on port 443. Simultaneously, 500 clients from different locations are each connected to it. How is this possible given that port 443 is a single 16-bit number?"
  type: multiple-choice
  options:
    - "The server opens a new, unique port number for each client after the initial handshake"
    - "Each TCP connection is uniquely identified by the four-tuple (source IP, source port, destination IP, destination port), so many connections can share the same server port"
    - "UDP is used instead of TCP so the server does not need to track individual connections"
    - "The operating system assigns a distinct IP address to each simultaneous connection"
  answer: 1
  explanation: "The server port (443) is the same for all connections, but each connection is uniquely identified by the full four-tuple. Client 1 from IP 10.0.0.1:52300 and Client 2 from IP 10.0.0.2:48721 both connect to 443, but the OS matches each incoming packet to the right socket using all four fields. This four-tuple uniqueness is what allows a single server port to handle thousands of simultaneous connections — a fundamental insight that distinguishes socket-level understanding from simple port-numbering knowledge."

- question: "A developer tries to start a server on port 8080 and receives an 'address already in use' error. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Port 8080 is a well-known port reserved for standard services and cannot be bound by user applications"
    - "The operating system has exhausted its ephemeral port range and can no longer accept new connections"
    - "A socket bound to port 8080 still exists — likely a recently closed TCP connection still in the TIME_WAIT state"
    - "The developer's firewall is blocking port 8080 from being bound locally"
  answer: 2
  explanation: "When a TCP connection closes, the OS keeps the socket in TIME_WAIT state for a period (typically 2× the Maximum Segment Lifetime, ~60–120 seconds) to ensure all packets from the previous connection have been delivered before the port is reused. During this window, the port is still 'in use' even though no application is actively using it. This is the most common cause of the error during development. Solutions include waiting, using SO_REUSEADDR socket option, or restarting with a different port."

- question: "A server process listening on port 80 can handle at most one TCP connection at a time, because a port is a single number and two connections cannot simultaneously share the same port."
  type: true-false
  answer: false
  explanation: "This is the key misconception about ports. A single server port can handle thousands of simultaneous connections because connections are identified by the four-tuple (src IP, src port, dst IP, dst port), not by server port alone. Each client contributes a unique (client IP, client ephemeral port) pair, making every connection's four-tuple globally unique. The OS demultiplexes incoming packets using all four fields and routes each to the correct socket. The server port 80 appears in every connection's four-tuple, but that doesn't conflict — it's the remaining two fields that distinguish them."

- question: "Ephemeral ports are temporary port numbers assigned by the operating system to the client side of a connection, ensuring that the server's reply packets are routed to the correct application process on the client."
  type: true-false
  answer: true
  explanation: "When a client opens a connection, its OS assigns an unused ephemeral port (typically in the range 49152–65535) as the source port. The server's replies are addressed to (client IP, client ephemeral port), which the OS uses to route the data to the correct socket — and thereby the correct application or browser tab. Without ephemeral ports, if every connection from a machine used the same source port, the OS could not distinguish which application should receive a reply, and simultaneous connections from the same host would be impossible to demultiplex."

- question: "A web server listens on port 443. When a client connects, the OS assigns an ephemeral port as the connection's source port. Why is this ephemeral port necessary, and what would go wrong if all client connections used the same source port?"
  type: short-answer
  answer: "The ephemeral port is the client's contribution to the four-tuple (src IP, src port, dst IP, dst port) that uniquely identifies each TCP connection. If every connection from the same client machine used the same source port — say, 12345 — then all reply packets from the server would arrive with the same four-tuple, and the OS could not tell which socket (which browser tab, which application) should receive each packet. Two simultaneous connections to the same server would be indistinguishable. By assigning a different ephemeral port to each new connection, the OS ensures that every active connection has a unique four-tuple and can be correctly demultiplexed."
  explanation: "This is also why a browser can open many parallel connections to the same website: each tab or each resource request gets its own ephemeral port, making each connection uniquely identifiable even though the destination IP and port are identical. The source port is what creates uniqueness on the client side."
```

## Explainer

You already know that TCP and UDP deliver data between hosts, but a host typically runs dozens of networked applications simultaneously — a web browser, a mail client, a chat program, a file sync service. When a packet arrives at a machine, the transport layer needs to know which application should receive it. This is the problem that **port numbers** solve. A port is a 16-bit number (ranging from 0 to 65535) included in every TCP segment and UDP datagram header. It acts like an apartment number in a building: the IP address gets the packet to the right building (host), and the port number delivers it to the right apartment (application). This process of directing incoming data to the correct application is called **demultiplexing**.

Ports are divided into three ranges by convention. **Well-known ports** (0–1023) are reserved for standard services: port 80 for HTTP, port 443 for HTTPS, port 22 for SSH, port 53 for DNS. These assignments are managed by IANA and are consistent across virtually all systems, which is why your browser knows to connect to port 443 when you type an HTTPS URL. **Registered ports** (1024–49151) are assigned to specific applications by request but are less strictly controlled. **Ephemeral ports** (49152–65535) are temporary ports that the operating system assigns dynamically to client-side connections — when your browser opens a connection to a web server, it picks an ephemeral port as its source port so the server's replies can find their way back to that specific browser tab's connection.

A **socket** is the abstraction that ties all of this together. Formally, a socket is an endpoint defined by a combination of IP address, transport protocol, and port number. A TCP connection is uniquely identified by a pair of sockets: (source IP, source port) and (destination IP, destination port). This four-tuple means a single server port — say, port 443 on a web server — can handle thousands of simultaneous connections, because each connection has a unique combination of client IP and client ephemeral port. When the server's operating system receives a packet, it matches the four-tuple to the correct socket and delivers the data to the right application thread.

Understanding ports and sockets clarifies many practical networking situations. When you see "address already in use" errors, it means a socket with that port is still bound (often in TIME_WAIT state from a recently closed TCP connection). When a firewall blocks a port, it is filtering based on these numbers in the transport header. And when you write networked code, you will explicitly create sockets, bind them to ports, and use them to send and receive data — making these abstractions the bridge between protocol theory and real programming.
