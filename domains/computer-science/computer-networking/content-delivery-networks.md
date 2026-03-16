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
tags:
- cdn
- content-distribution
- edge-caching
- latency-reduction
- geographical-distribution
stage: advanced
status: draft
---

# Content Delivery Networks (CDNs)

## Core Idea
A CDN is a geographically distributed network of caches (edge servers) that store copies of popular content. CDNs intercept DNS requests and direct clients to the nearest edge server, reducing latency and bandwidth costs. Modern CDNs like Akamai, Cloudflare, and AWS CloudFront are critical infrastructure for web performance.

## Explainer

You understand how DNS resolves domain names to IP addresses and how HTTP delivers web content. Now consider the performance problem: if a website's server is in Virginia and a user is in Tokyo, every HTTP request must travel across the Pacific Ocean and back — roughly 150 milliseconds of round-trip latency just from the speed of light in fiber. Multiply this by the dozens of resources a modern web page loads (HTML, CSS, JavaScript, images), and the delay becomes intolerable. A **content delivery network** solves this by placing copies of content on servers distributed around the world, so users fetch from a nearby server instead of the distant origin.

The mechanism relies on DNS, which you already know. When a website uses a CDN, its DNS records are configured so that lookups for the domain (say, images.example.com) are delegated to the CDN's DNS infrastructure. When a user's browser resolves images.example.com, the CDN's **authoritative DNS server** examines the request — noting the user's geographic location (inferred from the DNS resolver's IP address) — and returns the IP address of the nearest **edge server** (also called a **point of presence** or PoP). The browser then connects to that edge server via HTTP. If the edge server has a cached copy of the requested content, it serves it immediately — a **cache hit**. If not, it fetches the content from the **origin server**, caches it locally, and then serves it to the user. Subsequent requests from the same region are served directly from the cache.

CDN caching behavior is controlled by **HTTP cache headers** like Cache-Control and Expires, which the origin server sets to tell edge servers how long content remains valid. Static content (images, CSS, JavaScript files) is ideal for CDN caching because it rarely changes. Dynamic or personalized content is harder — CDNs handle this through techniques like **edge computing** (running application logic at the edge), cache key variations based on cookies or query parameters, and short TTLs (time-to-live) that force frequent revalidation with the origin.

Beyond reducing latency, CDNs provide several additional benefits. They absorb traffic spikes — a viral video might generate millions of requests, but most are served from edge caches rather than overwhelming the origin server. They improve reliability through redundancy — if one edge server fails, DNS can redirect to another. And they provide **DDoS mitigation** by distributing attack traffic across many edge locations, each absorbing a fraction of the load. Modern CDNs have evolved far beyond simple caching to become programmable edge platforms that can perform TLS termination, image optimization, A/B testing, and even run serverless functions at the edge — all before a request ever reaches the origin.
