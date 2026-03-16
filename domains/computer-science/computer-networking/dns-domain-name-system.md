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

## Explainer

You know from studying UDP that it provides a lightweight, connectionless way to send datagrams without the overhead of TCP's connection setup. DNS uses UDP (on port 53) for most queries because name lookups need to be fast — a single question-and-answer exchange, not a prolonged conversation. Understanding DNS means understanding how the Internet translates the human-readable names you type into a browser into the numeric IP addresses that routers actually use to deliver packets.

The DNS namespace is organized as a **hierarchical tree**. At the top is the **root zone**, represented by a dot (.). Below the root are **top-level domains (TLDs)** like `.com`, `.org`, `.uk`. Below those are **second-level domains** like `example.com`. Each level can have further subdomains: `mail.example.com`, `api.staging.example.com`. This hierarchy is not just organizational — it determines how queries are resolved. Each level has its own **authoritative nameservers** that know about the domains directly beneath them. The root servers know which nameservers handle `.com`; the `.com` nameservers know which nameservers handle `example.com`; and `example.com`'s nameservers know the IP address for `www.example.com`.

When you type `www.example.com` into your browser, a **recursive resolver** (typically run by your ISP or a service like 8.8.8.8) does the heavy lifting. If the answer is not already in its cache, it queries a root server, which responds with a referral to the `.com` TLD servers. The resolver then queries a `.com` server, which refers it to `example.com`'s authoritative nameserver. Finally, the resolver queries that nameserver and gets the IP address. This **iterative referral chain** means no single server needs to know everything — each server only knows about its own level and where to point for the next level down. The resolver then caches the result with a **TTL (time to live)** so that subsequent requests for the same name are answered instantly without repeating the chain.

DNS is far more than a phone book for IP addresses. Different **record types** serve different purposes: **A records** map names to IPv4 addresses, **AAAA records** map to IPv6, **CNAME records** create aliases (so `www.example.com` can point to `example.com`), **MX records** specify mail servers for a domain, and **TXT records** hold arbitrary text often used for email authentication (SPF, DKIM) and domain verification. **NS records** delegate authority to nameservers for subdomains. This extensible record system makes DNS a general-purpose distributed database, not just an address lookup service.

The entire architecture depends on **caching** for performance. Without caching, every web page load would trigger multiple round trips to nameservers scattered around the globe. In practice, your operating system caches recent lookups, your recursive resolver caches aggressively (popular domains may be cached for hours or days based on their TTL), and even your browser maintains its own DNS cache. This layered caching means that the vast majority of DNS queries never reach an authoritative server — they are answered locally in microseconds. The tradeoff is that DNS changes (like pointing a domain to a new server) take time to propagate as old cached entries expire, which is why DNS propagation delays exist.
