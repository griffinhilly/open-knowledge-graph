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
status: draft
---

# Load Balancing and Server Selection

## Core Idea
Load balancers distribute incoming requests across multiple servers to balance load, improve throughput, and provide fault tolerance. They may operate at layer 4 (transport) for simple round-robin distribution or layer 7 (application) for sophisticated decisions based on request content. Load balancing is essential for scaling services and maintaining availability.

## Explainer

From your knowledge of IP routing and HTTP, you understand that a client sends a request to an IP address, the network routes it to the destination, and a server processes it and returns a response. But what happens when a single server cannot handle the volume of incoming requests? You cannot simply make one server infinitely powerful — hardware has limits, and a single machine is a single point of failure. The solution is to place multiple servers behind a **load balancer**, a device or software component that accepts all incoming connections and distributes them across a pool of backend servers, called a **server farm** or **backend pool**.

The simplest distribution strategy is **round-robin**: the load balancer sends the first request to server 1, the second to server 2, the third to server 3, and so on, cycling through the list. This works when all servers are identical and all requests take roughly the same effort. But real workloads are uneven — some requests are quick lookups, others trigger heavy computation. **Weighted round-robin** assigns more traffic to more powerful servers. **Least-connections** sends each new request to whichever server currently has the fewest active connections, naturally adapting to varying request durations. **IP hash** routes all requests from the same client IP to the same server, providing session affinity — important when the server maintains state about the client between requests.

Load balancers operate at two fundamentally different layers. A **Layer 4 (transport) load balancer** makes routing decisions based only on the TCP/IP header — source and destination IP addresses and port numbers. It is fast because it does not need to inspect the request content, but it cannot make content-aware decisions. A **Layer 7 (application) load balancer** inspects the actual HTTP request — the URL path, headers, cookies, even the request body. This enables powerful routing: send all `/api/` requests to one server pool and all `/static/` requests to another; route authenticated users to servers with their session data; direct mobile clients to optimized backends. Layer 7 balancing is more computationally expensive but enables fine-grained traffic management that layer 4 cannot achieve.

Beyond distributing load, load balancers provide **health checking** and **fault tolerance**. The load balancer periodically probes each backend server — sending a TCP connection attempt, an HTTP request, or a custom health check — and removes unresponsive servers from the pool automatically. When a server recovers, it is added back. This means a server can crash or be taken offline for maintenance without any client-visible downtime, as long as the remaining servers can absorb the load. Combined with redundant load balancers (an active-passive or active-active pair), this architecture eliminates single points of failure and provides the high availability that modern internet services require.
