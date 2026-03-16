---
id: reverse-proxy-caching-architecture
title: Reverse Proxy and Caching Architecture
domain: computer-science
course: computer-networking
prerequisites:
- id: http-hypertext-transfer-protocol
  type: hard
- id: load-balancing-server-selection
  type: hard
builds-toward:
- content-delivery-networks
- network-management-and-monitoring
tags:
- application-layer
- caching
- proxy
- performance
stage: advanced
status: draft
---

# Reverse Proxy and Caching Architecture

## Core Idea
A reverse proxy sits between clients and origin servers, intercepting requests and serving cached responses when available. It improves performance by reducing origin server load, reduces bandwidth by compressing responses, and provides security by hiding server details. Caching strategies (LRU, TTL-based) determine which responses are cached and for how long.

## How It's Best Learned
Deploy Nginx or Apache with mod_proxy as a reverse proxy. Configure cache headers (Cache-Control, ETag) on origin servers. Observe cache hits/misses using Nginx cache logs. Test cache invalidation strategies and purge mechanisms.

## Common Misconceptions
Reverse proxies do not cache all responses; only cacheable ones (GET, 200 OK, etc.). Cache coherence requires careful coordination between proxy and origin; stale caches can serve incorrect data. A reverse proxy must not cache authenticated or personalized content.

## Explainer

You already understand HTTP request-response cycles and how load balancers distribute traffic across servers. A **reverse proxy** sits in front of your origin servers and intercepts every incoming client request before it reaches the backend. From the client's perspective, the reverse proxy *is* the server — the client has no idea that its request might be forwarded to one of many backend machines. This is the "reverse" in the name: a forward proxy acts on behalf of clients (hiding client identity from servers), while a reverse proxy acts on behalf of servers (hiding server identity and architecture from clients).

The most powerful capability a reverse proxy adds is **caching**. When the reverse proxy forwards a request to an origin server and receives a response, it can store that response locally. The next time any client requests the same resource, the proxy serves the cached copy directly without contacting the origin server at all. For a popular webpage that gets 10,000 requests per minute, this means the origin server might handle just one request per cache lifetime instead of 10,000. The performance improvement is dramatic: responses come from a server that is often geographically and topologically closer to the client, and the origin server's CPU and database connections are freed for requests that genuinely need fresh computation.

Not everything should be cached, and the rules for what gets cached are controlled through **HTTP cache headers** that you know from studying HTTP. The `Cache-Control` header tells the proxy how long a response can be reused (`max-age=3600` means one hour). The `ETag` header provides a fingerprint of the content, allowing the proxy to ask the origin "has this changed?" with a lightweight conditional request instead of fetching the full response again. Responses to POST requests, authenticated sessions, and pages with `Set-Cookie` headers are typically excluded from caching because they are either non-idempotent or personalized. Getting these rules wrong leads to serious bugs — serving one user's account page to another, for instance.

When a cache entry expires or is explicitly invalidated, the proxy must decide what to do. **TTL-based expiration** (time-to-live) is the simplest: after a set duration, the cached response is considered stale and the next request triggers a fresh fetch. **LRU eviction** (least recently used) manages limited cache storage by discarding entries that haven't been requested recently. More sophisticated setups use **cache purge mechanisms** — API endpoints that let the application explicitly tell the proxy "this content has changed, discard your copy." Modern reverse proxies like Nginx, Varnish, and HAProxy combine these strategies, and configuring them well is the difference between a site that handles traffic spikes gracefully and one that collapses under load.

Beyond caching, reverse proxies provide several other benefits that complement load balancing. They can terminate TLS connections (handling encryption overhead so backend servers don't have to), compress responses to reduce bandwidth, add or modify HTTP headers for security (hiding server version information, adding CORS headers), and serve as a single point for rate limiting and access control. This layered architecture — clients talk to the reverse proxy, which talks to backend servers — is the standard pattern for production web applications and forms the foundation for content delivery networks, which extend this caching concept to servers distributed worldwide.
