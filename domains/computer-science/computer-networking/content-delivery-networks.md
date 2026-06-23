---
id: content-delivery-networks
title: Content Delivery Networks (CDNs)
domain: computer-science
course: computer-networking
prerequisites:
- id: dns-domain-name-system
  type: hard
- id: http-hypertext-transfer-protocol
  type: hard
- id: anycast-networking
  type: soft
- id: reverse-proxy-caching-architecture
  type: soft
tags:
- cdn
- content-distribution
- edge-caching
- latency-reduction
- geographical-distribution
stage: advanced
status: validated
---

# Content Delivery Networks (CDNs)

## Core Idea
A CDN is a geographically distributed network of caches (edge servers) that store copies of popular content. CDNs intercept DNS requests and direct clients to the nearest edge server, reducing latency and bandwidth costs. Modern CDNs like Akamai, Cloudflare, and AWS CloudFront are critical infrastructure for web performance.

## Questions

```yaml
- question: "A user in Sydney requests an image from a CDN-backed website whose origin server is in New York. The Sydney edge server does not have the image cached. What happens?"
  type: multiple-choice
  options:
    - "The request fails; the user must wait until a cache refresh propagates the image to the Sydney edge"
    - "The CDN's DNS redirects the user's browser directly to the New York origin for this request"
    - "The Sydney edge server fetches the image from the origin, caches it locally, then serves it to the user"
    - "The request is forwarded to the nearest edge server that does have the image cached"
  answer: 2
  explanation: "On a cache miss, the edge server acts as a proxy: it fetches the content from the origin server, stores a copy in its local cache, and serves it to the requesting user. Subsequent users in Sydney requesting the same image get a cache hit and are served directly from the Sydney edge, bypassing the origin. This is why the first user in a region pays the latency penalty but subsequent users do not."

- question: "A web developer says: 'Our CDN improves performance by inspecting each HTTP request and redirecting it to the nearest server.' What is fundamentally wrong with this description?"
  type: multiple-choice
  options:
    - "CDNs do not use HTTP — they operate at the IP routing level and cannot inspect request headers"
    - "CDN geographic routing happens at the DNS resolution stage, before the HTTP connection is established — not by inspecting HTTP requests"
    - "Redirection requires a 301 HTTP response, which introduces additional round trips that eliminate any latency savings"
    - "CDNs cannot determine a user's geographic location, so routing decisions are made randomly"
  answer: 1
  explanation: "CDN routing is DNS-based, not HTTP-based. When the user's browser resolves the domain, the CDN's authoritative DNS server returns the IP of the nearest edge server — the routing decision happens before any HTTP connection is made. The browser then connects directly to that edge server. If the CDN worked by inspecting HTTP requests after connection, the user would still have connected to a distant server first, negating much of the latency benefit."

- question: "CDN caching is most effective for dynamic, personalized content — such as a user's account dashboard — because that content generates the highest volume of requests."
  type: true-false
  answer: false
  explanation: "CDN caching is most effective for STATIC content: images, CSS, JavaScript files, and videos that are the same for all users and change infrequently. Dynamic or personalized content (account dashboards, shopping carts, real-time feeds) is difficult to cache because it varies per user and changes frequently. Caching a personalized page would serve the wrong user's data to someone else. CDNs handle dynamic content through short TTLs, edge computing, and cache key variations — but these are workarounds for the fundamental mismatch between caching and personalization."

- question: "When a CDN edge server serves a cache hit, the origin server receives no request and incurs no load for that content delivery."
  type: true-false
  answer: true
  explanation: "A cache hit means the edge server has a valid cached copy and serves it directly to the user without contacting the origin. This is the primary mechanism by which CDNs reduce origin server load and absorb traffic spikes. If a video goes viral and generates millions of requests, the vast majority are served from edge caches worldwide; the origin only had to serve the content once per edge location per cache TTL period, rather than millions of times."

- question: "Describe how a CDN uses DNS to route a user to the nearest edge server, starting from the moment the user's browser needs to load an image."
  type: short-answer
  answer: "The website's DNS configuration delegates the image subdomain to the CDN's authoritative DNS. When the browser resolves the hostname, the query reaches the CDN's authoritative DNS server. That server examines the IP address of the user's recursive DNS resolver to infer geographic location, then returns the IP address of the nearest edge server (point of presence). The browser connects to that edge server via HTTP — not to the origin. If the edge has the image cached (cache hit), it serves it immediately. If not (cache miss), it fetches from the origin, caches it, and serves it."
  explanation: "The key insight is that DNS is the routing mechanism — the geographic decision is made at name resolution time, before any content is transferred. This is why CDNs require DNS delegation rather than simply adding IP addresses to a load balancer: the CDN's DNS infrastructure performs the geographic intelligence. The user's browser never knows or cares that it connected to an edge server rather than the origin."
```

## Explainer

You understand how DNS resolves domain names to IP addresses and how HTTP delivers web content. Now consider the performance problem: if a website's server is in Virginia and a user is in Tokyo, every HTTP request must travel across the Pacific Ocean and back — roughly 150 milliseconds of round-trip latency just from the speed of light in fiber. Multiply this by the dozens of resources a modern web page loads (HTML, CSS, JavaScript, images), and the delay becomes intolerable. A **content delivery network** solves this by placing copies of content on servers distributed around the world, so users fetch from a nearby server instead of the distant origin.

The mechanism relies on DNS, which you already know. When a website uses a CDN, its DNS records are configured so that lookups for the domain (say, images.example.com) are delegated to the CDN's DNS infrastructure. When a user's browser resolves images.example.com, the CDN's **authoritative DNS server** examines the request — noting the user's geographic location (inferred from the DNS resolver's IP address) — and returns the IP address of the nearest **edge server** (also called a **point of presence** or PoP). The browser then connects to that edge server via HTTP. If the edge server has a cached copy of the requested content, it serves it immediately — a **cache hit**. If not, it fetches the content from the **origin server**, caches it locally, and then serves it to the user. Subsequent requests from the same region are served directly from the cache.

CDN caching behavior is controlled by **HTTP cache headers** like Cache-Control and Expires, which the origin server sets to tell edge servers how long content remains valid. Static content (images, CSS, JavaScript files) is ideal for CDN caching because it rarely changes. Dynamic or personalized content is harder — CDNs handle this through techniques like **edge computing** (running application logic at the edge), cache key variations based on cookies or query parameters, and short TTLs (time-to-live) that force frequent revalidation with the origin.

Beyond reducing latency, CDNs provide several additional benefits. They absorb traffic spikes — a viral video might generate millions of requests, but most are served from edge caches rather than overwhelming the origin server. They improve reliability through redundancy — if one edge server fails, DNS can redirect to another. And they provide **DDoS mitigation** by distributing attack traffic across many edge locations, each absorbing a fraction of the load. Modern CDNs have evolved far beyond simple caching to become programmable edge platforms that can perform TLS termination, image optimization, A/B testing, and even run serverless functions at the edge — all before a request ever reaches the origin.
