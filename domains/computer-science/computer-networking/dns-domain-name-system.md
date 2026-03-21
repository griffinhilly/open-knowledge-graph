---
id: dns-domain-name-system
title: 'DNS: Domain Name System'
domain: computer-science
course: computer-networking
prerequisites:
- id: udp-user-datagram-protocol
  type: hard
- id: port-addressing-sockets
  type: soft
builds-toward:
- http-hypertext-transfer-protocol
- content-delivery-networks
tags:
- dns
- domain-name
- resolution
- recursive-lookup
- caching
stage: advanced
status: draft
---

# DNS: Domain Name System

## Core Idea
DNS translates human-readable domain names (e.g., example.com) to IP addresses using a hierarchical, distributed database of authoritative nameservers. DNS queries are typically recursive (a resolver queries nameservers on behalf of the client) and heavily cached at multiple levels, making DNS central to Internet usability.

## How It's Best Learned
Use `nslookup` or `dig` to perform DNS lookups and observe the hierarchy of nameservers; enable DNS query logging to see cached vs. authoritative responses.

## Common Misconceptions
- DNS always performs full resolution from root; most queries hit cached resolvers.
- DNS is only for A records; DNS also handles CNAME, MX, TXT, and other record types.

## Questions

```yaml
- question: "You type a domain name your computer has never seen before into your browser. Which sequence correctly describes the DNS resolution process, assuming no caches hold the answer?"
  type: multiple-choice
  options:
    - "Browser → root server → TLD server → authoritative server → IP address returned directly to browser"
    - "Browser → OS → recursive resolver → root server → TLD server → authoritative server → answer cached and returned"
    - "Browser → ISP nameserver → DNS root zone database → IP address returned"
    - "Browser → recursive resolver → authoritative server (which queries root and TLD on its own) → IP address returned"
  answer: 1
  explanation: "The recursive resolver (typically your ISP's or a public resolver like 8.8.8.8) does the iterative work on the client's behalf. It first contacts a root server, which returns a referral to the relevant TLD server; the resolver then contacts the TLD server, which returns a referral to the domain's authoritative nameserver; finally the resolver contacts the authoritative nameserver for the actual IP address. The resolver caches the result (respecting TTL) and returns it to the OS, which passes it to the browser. Option A skips the resolver and option D misrepresents which party performs the iterative chain."

- question: "After you move your website to a new server and update its DNS A record, some visitors worldwide still reach the old server for hours or days. What is the most direct cause?"
  type: multiple-choice
  options:
    - "Root servers cache A records permanently and must be manually purged"
    - "Authoritative nameservers require 48 hours to synchronize with each other after any change"
    - "Recursive resolvers and operating systems cached the old A record with a positive TTL that has not yet expired"
    - "Browser caches override DNS and must be manually cleared by each visitor"
  answer: 2
  explanation: "DNS is designed around aggressive caching for performance. When a recursive resolver fetches an A record, it stores the result for the duration specified by the TTL (time to live). Until that TTL expires, the resolver serves the old cached answer to all clients — even though the authoritative nameserver now has the updated record. Different resolvers cached the record at different times and have different TTLs remaining, which is why propagation is gradual rather than instantaneous. The fix is to lower the TTL well before making a planned change, giving caches time to drain."

- question: "Every DNS query must contact a root nameserver to begin the resolution chain, since root servers are the authoritative source for all DNS information."
  type: true-false
  answer: false
  explanation: "In practice, the vast majority of DNS queries are answered from cache — in the recursive resolver, the operating system, or even the browser — without ever contacting a root server. Root servers only come into play when the recursive resolver has no cached information about the relevant TLD. Popular domains may have their cached answers served millions of times between any root-server contacts. Root servers are critical infrastructure, but they are rarely the bottleneck for ordinary queries. Without this caching architecture, the ~13 root server clusters could never handle the global query volume."

- question: "DNS uses UDP rather than TCP for most queries because name resolution is a single question-and-answer exchange that benefits from low latency and does not require connection setup."
  type: true-false
  answer: true
  explanation: "UDP is connectionless and adds virtually no overhead — the client sends a datagram with the query, and the server sends a datagram with the answer. A typical DNS query fits in a single UDP packet. TCP requires a three-way handshake before any data is exchanged, nearly doubling the round trips needed for a lookup. Since DNS lookups happen for virtually every network connection (loading a webpage may trigger dozens), the latency savings of UDP are significant at scale. DNS does fall back to TCP for large responses (like zone transfers or responses exceeding 512 bytes) but uses UDP as its default."

- question: "Why is caching fundamental to DNS performance, and what tradeoff does it introduce?"
  type: short-answer
  answer: "Without caching, every DNS query would require multiple round trips to nameservers that may be geographically distant — a root server, a TLD server, and an authoritative server — adding tens or hundreds of milliseconds of latency before any actual network connection can begin. Since virtually every TCP connection starts with DNS resolution, this overhead would make the Internet noticeably slower. Caching — at the recursive resolver, OS, and browser levels — means most queries are answered locally in microseconds. The tradeoff is staleness: when a DNS record changes (e.g., a server moves), old answers persist in caches until their TTL expires, creating a propagation delay where different clients may reach different servers."
  explanation: "The TTL field on each DNS record is the operator's control knob for this tradeoff. A low TTL (e.g., 60 seconds) means changes propagate quickly but increases load on authoritative servers. A high TTL (e.g., 86400 seconds / 1 day) means excellent caching performance but slow change propagation. Common practice is to lower the TTL before a planned change, wait for caches to drain, make the change, then restore a long TTL afterward."
```

## Explainer

You know from studying UDP that it provides a lightweight, connectionless way to send datagrams without the overhead of TCP's connection setup. DNS uses UDP (on port 53) for most queries because name lookups need to be fast — a single question-and-answer exchange, not a prolonged conversation. Understanding DNS means understanding how the Internet translates the human-readable names you type into a browser into the numeric IP addresses that routers actually use to deliver packets.

The DNS namespace is organized as a **hierarchical tree**. At the top is the **root zone**, represented by a dot (.). Below the root are **top-level domains (TLDs)** like `.com`, `.org`, `.uk`. Below those are **second-level domains** like `example.com`. Each level can have further subdomains: `mail.example.com`, `api.staging.example.com`. This hierarchy is not just organizational — it determines how queries are resolved. Each level has its own **authoritative nameservers** that know about the domains directly beneath them. The root servers know which nameservers handle `.com`; the `.com` nameservers know which nameservers handle `example.com`; and `example.com`'s nameservers know the IP address for `www.example.com`.

When you type `www.example.com` into your browser, a **recursive resolver** (typically run by your ISP or a service like 8.8.8.8) does the heavy lifting. If the answer is not already in its cache, it queries a root server, which responds with a referral to the `.com` TLD servers. The resolver then queries a `.com` server, which refers it to `example.com`'s authoritative nameserver. Finally, the resolver queries that nameserver and gets the IP address. This **iterative referral chain** means no single server needs to know everything — each server only knows about its own level and where to point for the next level down. The resolver then caches the result with a **TTL (time to live)** so that subsequent requests for the same name are answered instantly without repeating the chain.

DNS is far more than a phone book for IP addresses. Different **record types** serve different purposes: **A records** map names to IPv4 addresses, **AAAA records** map to IPv6, **CNAME records** create aliases (so `www.example.com` can point to `example.com`), **MX records** specify mail servers for a domain, and **TXT records** hold arbitrary text often used for email authentication (SPF, DKIM) and domain verification. **NS records** delegate authority to nameservers for subdomains. This extensible record system makes DNS a general-purpose distributed database, not just an address lookup service.

The entire architecture depends on **caching** for performance. Without caching, every web page load would trigger multiple round trips to nameservers scattered around the globe. In practice, your operating system caches recent lookups, your recursive resolver caches aggressively (popular domains may be cached for hours or days based on their TTL), and even your browser maintains its own DNS cache. This layered caching means that the vast majority of DNS queries never reach an authoritative server — they are answered locally in microseconds. The tradeoff is that DNS changes (like pointing a domain to a new server) take time to propagate as old cached entries expire, which is why DNS propagation delays exist.
