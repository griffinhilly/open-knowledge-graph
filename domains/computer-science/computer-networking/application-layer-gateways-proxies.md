---
id: application-layer-gateways-proxies
title: Application-Layer Gateways and Proxies
domain: computer-science
course: computer-networking
prerequisites:
- id: http-hypertext-transfer-protocol
  type: hard
- id: tcp-transmission-control-protocol
  type: hard
tags:
- proxy
- gateway
- application-layer
- filtering
stage: advanced
status: draft
---

# Application-Layer Gateways and Proxies

## Core Idea
Application-layer gateways (proxies) terminate client connections, parse application protocol messages, and make forwarding decisions based on application content rather than just network headers. Proxies can filter malicious content, cache responses, rewrite URLs, and enforce policies on application-specific protocols. They provide stronger security than network-layer firewalls but require protocol-specific logic.

## Explainer

From your knowledge of HTTP and TCP, you understand that application data is carried inside TCP connections and structured according to application-layer protocols. A network-layer firewall can filter traffic based on IP addresses and port numbers, but it cannot inspect or understand the actual content of an HTTP request — it sees only packet headers. An **application-layer gateway**, commonly called a **proxy**, bridges this gap by operating at Layer 7. It fully terminates the client's TCP connection, reads and parses the application-layer messages (HTTP requests, FTP commands, DNS queries), makes decisions based on their content, and then opens a separate connection to the destination server to forward the request.

The most familiar example is an **HTTP proxy**. When a web browser is configured to use a proxy, it sends its HTTP requests to the proxy server instead of directly to the destination website. The proxy examines the full request — URL, headers, cookies, even the request body — and decides whether to allow it, block it, or modify it. It might deny access to certain domains, strip tracking cookies, scan downloads for malware, or add authentication headers. Because the proxy understands HTTP, it can also **cache** frequently requested content: if ten users request the same web page, the proxy can serve it from its local cache instead of fetching it from the origin server ten times, saving bandwidth and reducing latency.

A critical architectural distinction is between **forward proxies** and **reverse proxies**. A forward proxy sits in front of clients and acts on their behalf — the client knows it is using a proxy and directs traffic to it. Corporate networks use forward proxies to enforce acceptable-use policies and log employee web activity. A **reverse proxy** sits in front of servers and acts on the server's behalf — clients typically do not know it exists. Reverse proxies handle load balancing across multiple backend servers, SSL/TLS termination (offloading encryption from application servers), and protection against attacks like DDoS. Content delivery networks (CDNs) are essentially globally distributed reverse proxy caches.

The tradeoff compared to simpler firewalls is performance and complexity. Because a proxy must fully parse application-layer protocols, it introduces more latency than a packet filter that only examines headers. It must also be updated whenever the application protocol changes — a proxy built for HTTP/1.1 needs modification to handle HTTP/2's binary framing or HTTP/3's QUIC transport. Each protocol the proxy supports requires its own parsing and decision logic. Despite these costs, proxies remain essential for security architectures because the most dangerous threats — SQL injection, cross-site scripting, data exfiltration — are invisible at the network layer and can only be detected by inspecting application content.
