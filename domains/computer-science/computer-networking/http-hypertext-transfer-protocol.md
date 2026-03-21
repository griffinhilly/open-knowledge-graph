---
id: http-hypertext-transfer-protocol
title: 'HTTP: Hypertext Transfer Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: port-addressing-sockets
  type: hard
builds-toward:
- https-and-tls
tags:
- http
- web
- request-response
- stateless
- methods
stage: advanced
status: draft
---

# HTTP: Hypertext Transfer Protocol

## Core Idea
HTTP is a stateless request-response application protocol used by the World Wide Web. Clients send HTTP requests (GET, POST, etc.) to servers over TCP port 80, and servers respond with status codes (200, 404, 500, etc.) and content. HTTP is the foundation for web applications and APIs.

## How It's Best Learned
Use curl or browser developer tools to inspect HTTP headers and responses; manually construct HTTP requests to understand the protocol format.

## Common Misconceptions
- HTTP is stateless; applications build stateful sessions using cookies or tokens.
- HTTP/1.1 is the current standard; HTTP/3 is now available and uses QUIC instead of TCP.

## Questions

```yaml
- question: "A user logs into a website on Monday. On Tuesday, they visit the same website and are still logged in. How does the server recognize the returning user, given that HTTP is stateless?"
  type: multiple-choice
  options:
    - "HTTP maintains a persistent session internally; the server remembers TCP connection history"
    - "The server stored a cookie on the client during login; the browser sends this cookie with every subsequent request"
    - "The user's IP address is recorded and used to look up their session automatically"
    - "HTTP/1.1 introduced stateful sessions, so the server maintains login state natively"
  answer: 1
  explanation: "HTTP itself retains no memory between requests — each request arrives as if the client is a stranger. To simulate state, the server sends a session cookie (a small token) to the browser during login, and the browser includes this cookie in the header of every subsequent request. The server maps that token to the user's session data stored server-side. Option A is wrong: TCP connections have no session semantics at the HTTP level. Option C is unreliable and would break behind NAT. Option D is wrong: HTTP/1.1 added persistent connections, not stateful sessions."

- question: "A client sends 'GET /api/products HTTP/1.1' to a server. According to HTTP semantics, what should the server do?"
  type: multiple-choice
  options:
    - "Return a list of products without modifying any server-side data"
    - "Create a new product entry and return its ID"
    - "Delete the products resource since GET triggers retrieval then cleanup"
    - "Return an error — GET requests cannot target API endpoints, only HTML pages"
  answer: 0
  explanation: "GET is explicitly defined as a safe and idempotent method: it retrieves a resource without modifying server state. A GET request should have no side effects. Creating data is the role of POST; replacing a resource is PUT; deleting is DELETE. This is not merely convention — HTTP-aware infrastructure (caches, proxies) rely on GET being safe to cache, replay, or retry without consequences. Using GET to trigger mutations is a violation of HTTP semantics that can cause serious bugs when requests are unexpectedly cached or retried."

- question: "HTTP is stateless by design, meaning it is a limitation that developers must work around to build real web applications."
  type: true-false
  answer: false
  explanation: "Statelessness is a deliberate architectural choice, not a limitation. Because each request carries all necessary information (no server-side session memory required), any server in a cluster can handle any request. This makes horizontal scaling straightforward: add more servers and distribute requests freely. A stateful protocol would require all requests from a given user to reach the same server (sticky sessions), complicating load balancing and failover. The 'workaround' — cookies and tokens — is actually the right design: state that exists lives explicitly in the application layer, not hidden in the protocol."

- question: "HTTP/3 uses a different underlying transport protocol than HTTP/1.1 and HTTP/2."
  type: true-false
  answer: true
  explanation: "HTTP/1.1 and HTTP/2 both run over TCP. HTTP/3 runs over QUIC, which is built on UDP. QUIC reimplements reliability, ordering, and multiplexing directly in the transport layer, allowing it to combine TCP's guarantees with the ability to avoid head-of-line blocking at the transport level (a limitation of TCP multiplexing in HTTP/2). QUIC also reduces connection setup latency: TLS and transport setup happen in a single round trip instead of multiple. The application-level model — requests, responses, methods, status codes — remains the same across all HTTP versions."

- question: "What does it mean that HTTP is stateless, and why does this design make web servers easier to scale?"
  type: short-answer
  answer: "Stateless means each HTTP request is fully self-contained — the server processes it without any memory of previous requests from the same client. Every request must include all information needed to fulfill it (URL, headers, authentication tokens, etc.). This enables horizontal scaling because any server in a pool can handle any request: there is no session affinity requirement and no shared session state to synchronize. Adding a new server to a cluster requires no migration of client state. Failures are also simpler to handle — a failed server leaves no dangling session that must be recovered."
  explanation: "The trade-off is that statefulness the application needs (login sessions, shopping carts) must be explicitly implemented in the application layer using tokens or cookies — the server looks up a session from a token on each request. This is more visible and controllable than hidden protocol-level state, which is one reason the design ages well: the mechanism for managing state is application code, not an opaque protocol feature."
```

## Explainer

You already understand TCP — how it provides reliable, ordered byte streams between two endpoints using port numbers and sockets. **HTTP (Hypertext Transfer Protocol)** is the application-layer protocol built on top of TCP that powers the World Wide Web. It defines a simple conversation structure: the client sends a **request**, and the server sends back a **response**. Every time you load a web page, your browser is having dozens or hundreds of these request-response exchanges.

An HTTP request has three key parts: a **method** (what the client wants to do), a **URL** (which resource it wants), and **headers** (metadata about the request). The most common methods are **GET** (retrieve a resource — "give me this page"), **POST** (submit data — "here's a form submission"), **PUT** (replace a resource), and **DELETE** (remove a resource). A minimal request looks like: `GET /index.html HTTP/1.1` followed by headers like `Host: example.com`. The server processes the request and returns a response with a **status code** — a three-digit number indicating the outcome. Codes in the 200s mean success (200 OK), 300s mean redirection (301 Moved Permanently), 400s mean client errors (404 Not Found, 403 Forbidden), and 500s mean server errors (500 Internal Server Error).

A defining property of HTTP is that it is **stateless**: each request-response pair is completely independent, and the server retains no memory of previous requests from the same client. This is a deliberate design choice that makes servers simpler and more scalable — any server in a cluster can handle any request without needing to know what happened before. But web applications clearly need state (login sessions, shopping carts), so statefulness is layered on top of HTTP using **cookies** (small tokens the server sends to the client, which the client includes in every subsequent request) and **session tokens**. The state lives in the application logic, not in the protocol itself.

HTTP/1.0 opened a new TCP connection for every single request — expensive, since TCP's three-way handshake adds latency. **HTTP/1.1** introduced **persistent connections** (keep the TCP connection open for multiple requests) and **pipelining** (send multiple requests without waiting for each response). **HTTP/2** went further with **multiplexing** — multiple requests and responses interleaved on a single TCP connection as binary frames, eliminating head-of-line blocking at the HTTP level. **HTTP/3** replaces TCP entirely with **QUIC**, a UDP-based transport that builds reliability and multiplexing into the transport layer itself, reducing connection setup to a single round trip. Each version has made the web faster while keeping the fundamental request-response model and the same methods and status codes that HTTP/1.0 established.
