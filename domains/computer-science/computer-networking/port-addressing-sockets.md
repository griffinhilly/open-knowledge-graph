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

## Explainer

You already know that TCP and UDP deliver data between hosts, but a host typically runs dozens of networked applications simultaneously — a web browser, a mail client, a chat program, a file sync service. When a packet arrives at a machine, the transport layer needs to know which application should receive it. This is the problem that **port numbers** solve. A port is a 16-bit number (ranging from 0 to 65535) included in every TCP segment and UDP datagram header. It acts like an apartment number in a building: the IP address gets the packet to the right building (host), and the port number delivers it to the right apartment (application). This process of directing incoming data to the correct application is called **demultiplexing**.

Ports are divided into three ranges by convention. **Well-known ports** (0–1023) are reserved for standard services: port 80 for HTTP, port 443 for HTTPS, port 22 for SSH, port 53 for DNS. These assignments are managed by IANA and are consistent across virtually all systems, which is why your browser knows to connect to port 443 when you type an HTTPS URL. **Registered ports** (1024–49151) are assigned to specific applications by request but are less strictly controlled. **Ephemeral ports** (49152–65535) are temporary ports that the operating system assigns dynamically to client-side connections — when your browser opens a connection to a web server, it picks an ephemeral port as its source port so the server's replies can find their way back to that specific browser tab's connection.

A **socket** is the abstraction that ties all of this together. Formally, a socket is an endpoint defined by a combination of IP address, transport protocol, and port number. A TCP connection is uniquely identified by a pair of sockets: (source IP, source port) and (destination IP, destination port). This four-tuple means a single server port — say, port 443 on a web server — can handle thousands of simultaneous connections, because each connection has a unique combination of client IP and client ephemeral port. When the server's operating system receives a packet, it matches the four-tuple to the correct socket and delivers the data to the right application thread.

Understanding ports and sockets clarifies many practical networking situations. When you see "address already in use" errors, it means a socket with that port is still bound (often in TIME_WAIT state from a recently closed TCP connection). When a firewall blocks a port, it is filtering based on these numbers in the transport header. And when you write networked code, you will explicitly create sockets, bind them to ports, and use them to send and receive data — making these abstractions the bridge between protocol theory and real programming.
