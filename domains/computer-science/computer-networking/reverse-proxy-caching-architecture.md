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
status: validated
---

# Reverse Proxy and Caching Architecture

## Core Idea
A reverse proxy sits between clients and origin servers, intercepting requests and serving cached responses when available. It improves performance by reducing origin server load, reduces bandwidth by compressing responses, and provides security by hiding server details. Caching strategies (LRU, TTL-based) determine which responses are cached and for how long.

## How It's Best Learned
Deploy Nginx or Apache with mod_proxy as a reverse proxy. Configure cache headers (Cache-Control, ETag) on origin servers. Observe cache hits/misses using Nginx cache logs. Test cache invalidation strategies and purge mechanisms.

## Common Misconceptions
Reverse proxies do not cache all responses; only cacheable ones (GET, 200 OK, etc.). Cache coherence requires careful coordination between proxy and origin; stale caches can serve incorrect data. A reverse proxy must not cache authenticated or personalized content.

## Questions

```yaml
- question: "A developer configures their reverse proxy to cache all HTTP 200 responses with Cache-Control: max-age=3600. The site has a 'My Account' page that displays each user's personal order history and payment methods. What serious problem will this configuration cause?"
  type: multiple-choice
  options:
    - "The cache will fill up quickly because account pages are large, degrading performance for other resources"
    - "The first user's account page will be cached and served to subsequent users requesting that URL, exposing private data"
    - "The origin server will stop receiving requests and become unavailable when its idle timeout expires"
    - "Cache-Control: max-age only works for static assets; it is silently ignored for dynamic pages"
  answer: 1
  explanation: "Caching personalized content is a critical misconfiguration. When user A requests '/my-account', the proxy caches the response. When user B requests the same URL, the proxy serves the cached version — user A's account page — to user B. This exposes private data and is a serious security vulnerability. Authenticated and personalized responses must be excluded from caching, typically by ensuring responses include headers like `Cache-Control: private, no-store` or `Set-Cookie`, which tell the proxy not to cache them."

- question: "What distinguishes a reverse proxy from a forward proxy?"
  type: multiple-choice
  options:
    - "A reverse proxy uses HTTPS while a forward proxy uses HTTP"
    - "A reverse proxy operates at layer 4 while a forward proxy operates at layer 7"
    - "A forward proxy acts on behalf of clients (hiding their identity from servers); a reverse proxy acts on behalf of servers (hiding server details from clients)"
    - "A reverse proxy can only cache static files; a forward proxy caches all request types"
  answer: 2
  explanation: "The 'reverse' in reverse proxy refers to whose side it represents. A forward proxy sits in front of clients: clients configure it explicitly and use it to make requests on their behalf — the server sees the proxy's IP, not the client's. A reverse proxy sits in front of servers: clients connect to it thinking it is the server, unaware of the backend architecture. This distinction matters for understanding security models, trust relationships, and what information each type of proxy hides."

- question: "A reverse proxy and a forward proxy perform the same underlying function — the distinction is only about physical placement (client side vs. server side), not about whose interests they serve."
  type: true-false
  answer: false
  explanation: "False. The distinction is not merely physical placement — it is about representation and trust. A forward proxy represents clients: it makes requests on their behalf, potentially hiding client identity or caching content for the client network. A reverse proxy represents servers: it intercepts requests before they reach the backend, handles caching and load balancing for the server's benefit, and hides the server architecture from clients. The different roles lead to fundamentally different configurations, security models, and use cases."

- question: "A reverse proxy can improve performance for requests that cannot be cached — such as API calls with unique parameters — by terminating TLS, compressing responses, and rate-limiting, even when the response itself is not stored."
  type: true-false
  answer: true
  explanation: "True. Caching is only one of several performance and security benefits that reverse proxies provide. TLS termination offloads expensive cryptographic operations from backend servers. Response compression (gzip/Brotli) reduces bandwidth. Rate limiting, access control, and header manipulation apply regardless of cacheability. For non-cacheable requests, the proxy still reduces latency (TLS termination closer to the client) and protects backends from overload (rate limiting, DDoS mitigation) — the full value of a reverse proxy is not captured by caching alone."

- question: "Why must cached content in a reverse proxy be carefully controlled, and what categories of responses should generally never be cached?"
  type: short-answer
  answer: "Cached responses are served to all clients requesting that resource, so caching content that differs per user or per session is a security and correctness risk. Categories that must not be cached: (1) authenticated or personalized content (account pages, dashboards) — would be served to wrong users; (2) responses to POST/PUT/DELETE requests — non-idempotent, so replaying them would be incorrect; (3) responses with Set-Cookie headers — would set the wrong session for other users; (4) responses with Cache-Control: private or no-store — the server has explicitly forbidden caching."
  explanation: "The core principle is that a cached response will be returned to any client making the same request, so the response must be identical and safe for all of them. Getting this wrong ranges from serving stale data (minor) to exposing one user's private data to another (severe security breach). HTTP cache headers (Cache-Control, ETag, Vary) exist specifically to communicate cacheability rules from the origin server to the proxy, and a reverse proxy must respect them — or configure explicit rules that achieve the same effect."
```

## Explainer

You already understand HTTP request-response cycles and how load balancers distribute traffic across servers. A **reverse proxy** sits in front of your origin servers and intercepts every incoming client request before it reaches the backend. From the client's perspective, the reverse proxy *is* the server — the client has no idea that its request might be forwarded to one of many backend machines. This is the "reverse" in the name: a forward proxy acts on behalf of clients (hiding client identity from servers), while a reverse proxy acts on behalf of servers (hiding server identity and architecture from clients).

The most powerful capability a reverse proxy adds is **caching**. When the reverse proxy forwards a request to an origin server and receives a response, it can store that response locally. The next time any client requests the same resource, the proxy serves the cached copy directly without contacting the origin server at all. For a popular webpage that gets 10,000 requests per minute, this means the origin server might handle just one request per cache lifetime instead of 10,000. The performance improvement is dramatic: responses come from a server that is often geographically and topologically closer to the client, and the origin server's CPU and database connections are freed for requests that genuinely need fresh computation.

Not everything should be cached, and the rules for what gets cached are controlled through **HTTP cache headers** that you know from studying HTTP. The `Cache-Control` header tells the proxy how long a response can be reused (`max-age=3600` means one hour). The `ETag` header provides a fingerprint of the content, allowing the proxy to ask the origin "has this changed?" with a lightweight conditional request instead of fetching the full response again. Responses to POST requests, authenticated sessions, and pages with `Set-Cookie` headers are typically excluded from caching because they are either non-idempotent or personalized. Getting these rules wrong leads to serious bugs — serving one user's account page to another, for instance.

When a cache entry expires or is explicitly invalidated, the proxy must decide what to do. **TTL-based expiration** (time-to-live) is the simplest: after a set duration, the cached response is considered stale and the next request triggers a fresh fetch. **LRU eviction** (least recently used) manages limited cache storage by discarding entries that haven't been requested recently. More sophisticated setups use **cache purge mechanisms** — API endpoints that let the application explicitly tell the proxy "this content has changed, discard your copy." Modern reverse proxies like Nginx, Varnish, and HAProxy combine these strategies, and configuring them well is the difference between a site that handles traffic spikes gracefully and one that collapses under load.

Beyond caching, reverse proxies provide several other benefits that complement load balancing. They can terminate TLS connections (handling encryption overhead so backend servers don't have to), compress responses to reduce bandwidth, add or modify HTTP headers for security (hiding server version information, adding CORS headers), and serve as a single point for rate limiting and access control. This layered architecture — clients talk to the reverse proxy, which talks to backend servers — is the standard pattern for production web applications and forms the foundation for content delivery networks, which extend this caching concept to servers distributed worldwide.
