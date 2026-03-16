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

## Explainer

You already understand TCP — how it provides reliable, ordered byte streams between two endpoints using port numbers and sockets. **HTTP (Hypertext Transfer Protocol)** is the application-layer protocol built on top of TCP that powers the World Wide Web. It defines a simple conversation structure: the client sends a **request**, and the server sends back a **response**. Every time you load a web page, your browser is having dozens or hundreds of these request-response exchanges.

An HTTP request has three key parts: a **method** (what the client wants to do), a **URL** (which resource it wants), and **headers** (metadata about the request). The most common methods are **GET** (retrieve a resource — "give me this page"), **POST** (submit data — "here's a form submission"), **PUT** (replace a resource), and **DELETE** (remove a resource). A minimal request looks like: `GET /index.html HTTP/1.1` followed by headers like `Host: example.com`. The server processes the request and returns a response with a **status code** — a three-digit number indicating the outcome. Codes in the 200s mean success (200 OK), 300s mean redirection (301 Moved Permanently), 400s mean client errors (404 Not Found, 403 Forbidden), and 500s mean server errors (500 Internal Server Error).

A defining property of HTTP is that it is **stateless**: each request-response pair is completely independent, and the server retains no memory of previous requests from the same client. This is a deliberate design choice that makes servers simpler and more scalable — any server in a cluster can handle any request without needing to know what happened before. But web applications clearly need state (login sessions, shopping carts), so statefulness is layered on top of HTTP using **cookies** (small tokens the server sends to the client, which the client includes in every subsequent request) and **session tokens**. The state lives in the application logic, not in the protocol itself.

HTTP/1.0 opened a new TCP connection for every single request — expensive, since TCP's three-way handshake adds latency. **HTTP/1.1** introduced **persistent connections** (keep the TCP connection open for multiple requests) and **pipelining** (send multiple requests without waiting for each response). **HTTP/2** went further with **multiplexing** — multiple requests and responses interleaved on a single TCP connection as binary frames, eliminating head-of-line blocking at the HTTP level. **HTTP/3** replaces TCP entirely with **QUIC**, a UDP-based transport that builds reliability and multiplexing into the transport layer itself, reducing connection setup to a single round trip. Each version has made the web faster while keeping the fundamental request-response model and the same methods and status codes that HTTP/1.0 established.
