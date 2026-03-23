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
status: validated
---

# HTTPS and TLS (Transport Layer Security)

## Core Idea
HTTPS wraps HTTP with TLS (formerly SSL), adding encryption and authentication. TLS uses public-key cryptography to establish a secure session, then switches to symmetric encryption for efficiency. X.509 certificates prove server identity, protecting against man-in-the-middle attacks.

## Questions

```yaml
- question: "A browser successfully connects to a site via HTTPS. What specific security problem does the X.509 certificate solve that encryption alone does not?"
  type: multiple-choice
  options:
    - "It compresses HTTP headers to speed up the encrypted connection"
    - "It proves the server is who it claims to be, preventing an attacker from substituting their own key"
    - "It generates the symmetric session key used for encrypting data"
    - "It replaces public-key cryptography to make the handshake more efficient"
  answer: 1
  explanation: "Encryption alone does not tell you *who* you are encrypting data for. Without certificate authentication, an attacker could intercept your connection, present their own public key, and read your 'encrypted' traffic — a man-in-the-middle attack. The X.509 certificate, signed by a trusted Certificate Authority, proves the public key actually belongs to the claimed domain. Option C is a common confusion: the certificate contains the server's public key but does not generate the session key — that comes from the Diffie-Hellman exchange."

- question: "Why does TLS use public-key cryptography during the handshake but switch to symmetric encryption (like AES) for the actual data transfer?"
  type: multiple-choice
  options:
    - "Symmetric encryption is more secure than public-key encryption for bulk data"
    - "Public-key cryptography cannot encrypt data, only establish shared secrets"
    - "Public-key operations are hundreds of times slower than symmetric encryption, making them too costly for bulk data transfer"
    - "Regulatory standards require symmetric encryption for web traffic"
  answer: 2
  explanation: "The two-phase design is purely about performance. Public-key operations (RSA, Diffie-Hellman) are computationally expensive — viable for a one-time handshake but far too slow for encrypting megabytes of streaming data. Symmetric encryption (AES) is orders of magnitude faster. Option A is wrong: public-key cryptography is not less secure, just slower. Option B is wrong: public-key encryption can encrypt data, but the performance cost makes it impractical for bulk transfer."

- question: "TLS provides integrity protection through message authentication codes, meaning that if any bit of an encrypted message is altered in transit, the receiver will detect the tampering."
  type: true-false
  answer: true
  explanation: "TLS includes a MAC with each encrypted message — a cryptographic checksum computed over the message content. The receiver recomputes the MAC and compares. Even a single altered bit produces a completely different MAC, causing the check to fail and the message to be rejected. This integrity guarantee means that even if an attacker cannot decrypt traffic, they also cannot silently modify it."

- question: "HTTPS guarantees that a website is trustworthy and that its operator will not misuse your data."
  type: true-false
  answer: false
  explanation: "HTTPS provides three guarantees: confidentiality (no eavesdropping), authentication (the server is who the certificate claims), and integrity (data has not been modified). It says nothing about the intentions or trustworthiness of the server operator. A malicious website can — and often does — use a valid HTTPS certificate. The padlock means 'your connection to this server is secure,' not 'this server is safe to trust.'"

- question: "Explain why the combination of certificate authorities and TLS prevents man-in-the-middle attacks, and what would happen if browsers trusted all certificates equally without a CA hierarchy."
  type: short-answer
  answer: "TLS prevents MITM attacks by requiring the server to present a certificate signed by a CA that the browser already trusts. An attacker cannot forge a valid certificate for a domain they don't control because they cannot obtain a CA's signature. Without a CA hierarchy, any entity could generate a self-signed certificate for any domain — an attacker could intercept a connection to bank.com, present their own certificate claiming to be bank.com, and the browser would accept it, allowing the attacker to decrypt all traffic."
  explanation: "The security of HTTPS is only as strong as the trust placed in CAs. This is why a compromised CA is a catastrophic security incident — it can issue fraudulent certificates for any domain, enabling MITM attacks against that site's users globally. The browser's trust store (the list of trusted root CAs) is the anchor of the entire system."
```

## Explainer

You already understand HTTP — how browsers send requests and servers return responses in plaintext. The problem with plain HTTP is that anyone positioned between client and server (on the same Wi-Fi network, at an ISP, or anywhere along the route) can read every byte: passwords, credit card numbers, personal messages. **HTTPS** solves this by wrapping the HTTP conversation inside a **TLS (Transport Layer Security)** encrypted tunnel. From the application's perspective, nothing about HTTP changes — the same methods, headers, and status codes work identically. TLS simply ensures that the data is encrypted before it leaves the sender and decrypted only after it arrives at the intended recipient.

The TLS connection begins with a **handshake** that solves two problems simultaneously: authenticating the server's identity and establishing a shared encryption key. The server presents an **X.509 certificate** — a digitally signed document containing the server's public key and domain name, issued by a trusted **Certificate Authority (CA)**. Your browser checks that the certificate is valid (not expired, not revoked), that it matches the domain you are visiting, and that it was signed by a CA in the browser's trust store. This chain of trust — from the server's certificate through intermediate CAs up to a root CA — is what makes the padlock icon meaningful. Without it, an attacker could intercept your connection, present their own certificate, and decrypt your traffic (a **man-in-the-middle attack**).

Once the server's identity is verified, TLS uses **public-key cryptography** to securely exchange a **session key**. In modern TLS 1.3, this happens via **Diffie-Hellman key exchange**: both sides contribute random values that, combined mathematically, produce a shared secret that neither side transmitted in the clear. This session key is then used for **symmetric encryption** (like AES) for the actual data transfer. The reason for this two-phase approach is performance: public-key operations are computationally expensive (hundreds of times slower than symmetric encryption), so they are used only once during the handshake to establish the shared secret. All subsequent data flows through the fast symmetric cipher.

TLS also provides **integrity protection** through message authentication codes (MACs). Each encrypted message includes a cryptographic checksum that the receiver verifies, ensuring that no one has tampered with the data in transit. If even a single bit is altered — whether by an attacker or a network error — the MAC check fails and the message is rejected. Combined with encryption and authentication, this gives HTTPS three guarantees: **confidentiality** (no one can read your data), **authentication** (you are talking to the real server), and **integrity** (no one has modified the data). These properties are why HTTPS has become the default for virtually all web traffic, not just banking and login pages.
