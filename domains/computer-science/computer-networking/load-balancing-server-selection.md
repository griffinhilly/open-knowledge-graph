---
id: load-balancing-server-selection
title: Load Balancing and Server Selection
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
- id: http-hypertext-transfer-protocol
  type: hard
tags:
- load-balancing
- server-selection
- distribution
- failover
stage: advanced
status: validated
---

# Load Balancing and Server Selection

## Core Idea
Load balancers distribute incoming requests across multiple servers to balance load, improve throughput, and provide fault tolerance. They may operate at layer 4 (transport) for simple round-robin distribution or layer 7 (application) for sophisticated decisions based on request content. Load balancing is essential for scaling services and maintaining availability.

## Questions

```yaml
- question: "An e-commerce site wants to route all requests with URLs containing '/checkout/' to a high-security server pool and all image requests to a CDN-optimized pool. Which type of load balancer can achieve this?"
  type: multiple-choice
  options:
    - "A Layer 4 load balancer, using port-based routing rules"
    - "A Layer 7 load balancer, which inspects the HTTP request URL and can route based on path"
    - "Either — both Layer 4 and Layer 7 load balancers can inspect HTTP URL paths"
    - "Neither — this routing requires DNS-level configuration, not a load balancer"
  answer: 1
  explanation: "A Layer 4 (transport) load balancer only sees TCP/IP header information — source/destination IP addresses and port numbers. It has no visibility into the HTTP request itself and cannot inspect URL paths. A Layer 7 (application) load balancer operates at the HTTP layer and can inspect the full request including URL path, headers, cookies, and even the request body. Content-based routing (by path, by header value, by client type) requires Layer 7. This is why Layer 7 balancers are more expensive — the additional inspection capability comes with computational cost."

- question: "A load balancer uses round-robin to distribute requests. Server A processes each request in 50ms; Server B is currently handling a 5-second video encoding job. After the next few requests, Server B is becoming overloaded. Which algorithm would handle this situation better?"
  type: multiple-choice
  options:
    - "Weighted round-robin with higher weight assigned to Server B"
    - "IP hash, to keep sessions pinned to consistent servers"
    - "Least-connections, which always sends the next request to whichever server currently has the fewest active connections"
    - "Random selection — it statistically evens out over time regardless of request duration"
  answer: 2
  explanation: "Round-robin assumes all requests are equivalent in duration, so it distributes them evenly by count — but if one server is tied up on a long job, it accumulates a queue. Least-connections tracks active connection counts per server and routes new requests to the least-loaded server. In this scenario, Server A finishes its requests quickly and accumulates few active connections; Server B's encoding job keeps its count high. Least-connections naturally directs traffic away from Server B until it finishes its long job, dynamically adapting to uneven request durations. IP hash would make things worse by locking certain clients to the overloaded server."

- question: "A Layer 7 load balancer can route traffic to different backend pools based on HTTP headers, such as directing mobile clients (identified by the User-Agent header) to a mobile-optimized server pool."
  type: true-false
  answer: true
  explanation: "Layer 7 load balancers operate at the HTTP application layer and can inspect any part of the HTTP request, including all headers. The User-Agent header identifies the client browser and device type, enabling the balancer to distinguish mobile from desktop clients. Other header-based routing examples include routing based on Accept-Language for localization, Authorization headers for authenticated vs. anonymous users, or custom headers set by API gateways. This flexibility is the core value proposition of Layer 7 over Layer 4."

- question: "When a backend server fails, it must be manually removed from the load balancer's pool by an administrator — and manually re-added after recovery — to prevent traffic from reaching it."
  type: true-false
  answer: false
  explanation: "Load balancers implement automatic health checking: they periodically send probe requests (TCP connection attempts, HTTP requests, or custom health check endpoints) to each backend server. If a server fails to respond within the configured threshold, the load balancer automatically removes it from the pool and stops sending traffic to it. When the server recovers and passes health checks, it is automatically restored to the pool. This automation is what makes load balancing a genuine high-availability solution, not just a performance tool — servers can crash or undergo maintenance without human intervention and without client-visible downtime."

- question: "Why is a Layer 4 load balancer faster than a Layer 7 load balancer, and what does that speed advantage cost in terms of capability?"
  type: short-answer
  answer: "A Layer 4 load balancer makes routing decisions using only TCP/IP header information — source and destination IP addresses and port numbers — without inspecting the actual content of the request. This is computationally inexpensive: the balancer looks at a small, fixed-size header and makes a routing decision. A Layer 7 balancer must parse the full HTTP request — URL path, headers, possibly cookies and body — before routing. This parsing is more expensive, introducing latency and consuming more CPU. The cost of Layer 4's speed is content-blindness: it cannot route based on what the request is asking for, only where it appears to be going."
  explanation: "The choice between Layer 4 and Layer 7 is an engineering tradeoff. For very high-volume, uniform traffic (e.g., a DNS server or a simple file server), Layer 4 may be preferable. For web applications with heterogeneous request types (APIs, static assets, authentication flows), Layer 7's routing intelligence is usually worth the overhead. Many modern load balancers (like AWS ALB/NLB or NGINX) support both modes."
```

## Explainer

From your knowledge of IP routing and HTTP, you understand that a client sends a request to an IP address, the network routes it to the destination, and a server processes it and returns a response. But what happens when a single server cannot handle the volume of incoming requests? You cannot simply make one server infinitely powerful — hardware has limits, and a single machine is a single point of failure. The solution is to place multiple servers behind a **load balancer**, a device or software component that accepts all incoming connections and distributes them across a pool of backend servers, called a **server farm** or **backend pool**.

The simplest distribution strategy is **round-robin**: the load balancer sends the first request to server 1, the second to server 2, the third to server 3, and so on, cycling through the list. This works when all servers are identical and all requests take roughly the same effort. But real workloads are uneven — some requests are quick lookups, others trigger heavy computation. **Weighted round-robin** assigns more traffic to more powerful servers. **Least-connections** sends each new request to whichever server currently has the fewest active connections, naturally adapting to varying request durations. **IP hash** routes all requests from the same client IP to the same server, providing session affinity — important when the server maintains state about the client between requests.

Load balancers operate at two fundamentally different layers. A **Layer 4 (transport) load balancer** makes routing decisions based only on the TCP/IP header — source and destination IP addresses and port numbers. It is fast because it does not need to inspect the request content, but it cannot make content-aware decisions. A **Layer 7 (application) load balancer** inspects the actual HTTP request — the URL path, headers, cookies, even the request body. This enables powerful routing: send all `/api/` requests to one server pool and all `/static/` requests to another; route authenticated users to servers with their session data; direct mobile clients to optimized backends. Layer 7 balancing is more computationally expensive but enables fine-grained traffic management that layer 4 cannot achieve.

Beyond distributing load, load balancers provide **health checking** and **fault tolerance**. The load balancer periodically probes each backend server — sending a TCP connection attempt, an HTTP request, or a custom health check — and removes unresponsive servers from the pool automatically. When a server recovers, it is added back. This means a server can crash or be taken offline for maintenance without any client-visible downtime, as long as the remaining servers can absorb the load. Combined with redundant load balancers (an active-passive or active-active pair), this architecture eliminates single points of failure and provides the high availability that modern internet services require.
