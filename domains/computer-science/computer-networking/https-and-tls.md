---
id: https-and-tls
title: HTTPS and TLS (Transport Layer Security)
domain: computer-science
course: computer-networking
prerequisites:
- id: http-hypertext-transfer-protocol
  type: hard
builds-toward:
- network-security-fundamentals
tags:
- https
- tls
- ssl
- encryption
- certificate
- public-key
stage: advanced
status: draft
---

# HTTPS and TLS (Transport Layer Security)

## Core Idea
HTTPS wraps HTTP with TLS (formerly SSL), adding encryption and authentication. TLS uses public-key cryptography to establish a secure session, then switches to symmetric encryption for efficiency. X.509 certificates prove server identity, protecting against man-in-the-middle attacks.

## Explainer

You already understand HTTP — how browsers send requests and servers return responses in plaintext. The problem with plain HTTP is that anyone positioned between client and server (on the same Wi-Fi network, at an ISP, or anywhere along the route) can read every byte: passwords, credit card numbers, personal messages. **HTTPS** solves this by wrapping the HTTP conversation inside a **TLS (Transport Layer Security)** encrypted tunnel. From the application's perspective, nothing about HTTP changes — the same methods, headers, and status codes work identically. TLS simply ensures that the data is encrypted before it leaves the sender and decrypted only after it arrives at the intended recipient.

The TLS connection begins with a **handshake** that solves two problems simultaneously: authenticating the server's identity and establishing a shared encryption key. The server presents an **X.509 certificate** — a digitally signed document containing the server's public key and domain name, issued by a trusted **Certificate Authority (CA)**. Your browser checks that the certificate is valid (not expired, not revoked), that it matches the domain you are visiting, and that it was signed by a CA in the browser's trust store. This chain of trust — from the server's certificate through intermediate CAs up to a root CA — is what makes the padlock icon meaningful. Without it, an attacker could intercept your connection, present their own certificate, and decrypt your traffic (a **man-in-the-middle attack**).

Once the server's identity is verified, TLS uses **public-key cryptography** to securely exchange a **session key**. In modern TLS 1.3, this happens via **Diffie-Hellman key exchange**: both sides contribute random values that, combined mathematically, produce a shared secret that neither side transmitted in the clear. This session key is then used for **symmetric encryption** (like AES) for the actual data transfer. The reason for this two-phase approach is performance: public-key operations are computationally expensive (hundreds of times slower than symmetric encryption), so they are used only once during the handshake to establish the shared secret. All subsequent data flows through the fast symmetric cipher.

TLS also provides **integrity protection** through message authentication codes (MACs). Each encrypted message includes a cryptographic checksum that the receiver verifies, ensuring that no one has tampered with the data in transit. If even a single bit is altered — whether by an attacker or a network error — the MAC check fails and the message is rejected. Combined with encryption and authentication, this gives HTTPS three guarantees: **confidentiality** (no one can read your data), **authentication** (you are talking to the real server), and **integrity** (no one has modified the data). These properties are why HTTPS has become the default for virtually all web traffic, not just banking and login pages.
