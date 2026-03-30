---
id: authenticated-encryption
title: Authenticated Encryption
domain: computer-science
course: cryptography
prerequisites:
- id: modes-of-operation
  type: hard
- id: message-authentication-codes
  type: hard
tags:
- aead
- encrypt-then-mac
- gcm
- chacha20-poly1305
- chosen-ciphertext
stage: expert
status: validated
---

# Authenticated Encryption

## Core Idea
Authenticated encryption (AE) combines confidentiality and integrity in a single primitive, guaranteeing that ciphertext cannot be read or tampered with. AEAD (AE with Associated Data) additionally authenticates unencrypted metadata (headers, routing info). The correct generic composition is encrypt-then-MAC (encrypt first, then MAC the ciphertext). MAC-then-encrypt and encrypt-and-MAC have led to devastating attacks (padding oracles, BEAST, Lucky13). Dedicated AEAD constructions (GCM, ChaCha20-Poly1305, OCB) integrate encryption and authentication for efficiency and resistance to misuse. AE is the modern standard — standalone encryption without authentication is considered a design error.

## Questions

```yaml
- question: "Three generic composition methods exist: Encrypt-then-MAC, MAC-then-Encrypt, Encrypt-and-MAC. Only one is generically secure. Which, and why do the others fail?"
  type: short-answer
  answer: "Encrypt-then-MAC is the only generically secure composition. The MAC covers the ciphertext, so the verifier can reject tampered ciphertexts without decrypting — no information about the plaintext leaks through decryption errors. MAC-then-Encrypt computes MAC(m), then encrypts (m || MAC(m)). The receiver must decrypt before verifying the MAC, and differences in decryption error behavior (e.g., padding oracle attacks in CBC mode) can leak plaintext byte by byte. Encrypt-and-MAC encrypts m and separately MACs m (the plaintext). The MAC tag may leak information about m since MAC is not required to hide its input."
  explanation: "This is one of the most practically important results in applied cryptography. TLS up through version 1.2 used MAC-then-Encrypt, leading to the BEAST (2011), Lucky 13 (2013), and POODLE (2014) attacks that exploited padding oracle behavior. TLS 1.3 mandates AEAD constructions (GCM, ChaCha20-Poly1305) that integrate encryption and authentication, eliminating composition errors entirely."

- question: "A developer implements AES-GCM correctly but reuses a nonce for two different messages under the same key. How severe is this failure?"
  type: multiple-choice
  options:
    - "Confidentiality is mildly reduced but authentication remains intact"
    - "Catastrophic — nonce reuse in GCM breaks both confidentiality (same keystream XORed with different plaintexts, revealing their XOR) and authenticity (the authentication key H can be recovered from two ciphertexts with the same nonce, enabling universal forgeries on all past and future messages)"
    - "Only the two affected messages are compromised; other messages remain secure"
    - "GCM detects and rejects nonce reuse automatically"
  answer: 1
  explanation: "GCM nonce reuse is uniquely catastrophic because it breaks not just confidentiality but also authentication — permanently. The authentication tag is a polynomial evaluation at a secret point H. Two tags with the same nonce reveal H (solve the polynomial equation). Once H is known, the attacker can forge valid tags for any ciphertext. This is why nonce-misuse resistant schemes like SIV (Synthetic IV) and GCM-SIV exist: they degrade more gracefully under nonce reuse, losing only indistinguishability of repeated messages while preserving authentication."

- question: "ChaCha20-Poly1305 was designed as an alternative to AES-GCM for platforms without hardware AES support. What are its advantages?"
  type: multiple-choice
  options:
    - "ChaCha20-Poly1305 provides stronger security guarantees than AES-GCM"
    - "ChaCha20 uses only ARX operations (add, rotate, XOR) that execute in constant time on all CPUs without special instructions, avoiding timing side channels that affect software AES implementations. Poly1305 is a similarly simple polynomial MAC. Together they provide excellent performance on mobile/embedded devices lacking AES-NI instructions"
    - "ChaCha20-Poly1305 supports larger message sizes than GCM"
    - "Poly1305 provides stronger authentication than GHASH"
  answer: 1
  explanation: "On CPUs with AES-NI (hardware AES acceleration), AES-GCM is typically faster. On CPUs without it (many ARM chips, older x86), software AES is slow and vulnerable to cache-timing attacks. ChaCha20-Poly1305's ARX operations are naturally constant-time and fast on all architectures. This is why TLS 1.3 includes both: servers select AES-GCM when AES-NI is available and ChaCha20-Poly1305 otherwise. Google deployed ChaCha20-Poly1305 for HTTPS to Android devices, where AES-NI is rare."

- question: "Standalone encryption (encryption without authentication) should never be used in modern systems."
  type: true-false
  answer: true
  explanation: "This is now the consensus of the cryptographic community. Unauthenticated encryption is malleable — attackers can modify ciphertexts to produce controlled changes in the plaintext, and the recipient has no way to detect tampering. Every major attack on TLS encryption (BEAST, Lucky 13, POODLE, Bleichenbacher) exploited the lack of early authentication. Modern protocols (TLS 1.3, Signal, WireGuard) mandate AEAD, and all NIST and IETF guidelines treat standalone encryption as deprecated."

- question: "AEAD's 'associated data' (AD) is authenticated but not encrypted. Give an example of data that should be associated data rather than part of the encrypted payload."
  type: short-answer
  answer: "Network packet headers are the classic example. In a TLS record, the header specifies the protocol version, content type, and length — routing information that network infrastructure needs to process the packet. This data must be authenticated (to prevent an attacker from changing the content type or length without detection) but not encrypted (because routers and load balancers need to read it for packet handling). AEAD binds the header to the ciphertext cryptographically: any modification to either the header or the encrypted payload invalidates the authentication tag."
  explanation: "Other examples include database row IDs (authenticate which row the ciphertext belongs to, preventing row-swapping attacks), message sequence numbers (prevent reordering attacks), and algorithm identifiers (prevent algorithm-downgrade attacks). The AD mechanism ensures that context surrounding the ciphertext is tamper-proof even when it's visible."
```

## Explainer

For decades, cryptographic textbooks taught encryption and authentication as separate concerns. Encryption hides the message; MACs ensure integrity. In practice, you need both — but how you combine them matters critically. **Authenticated encryption (AE)** integrates confidentiality and integrity into a single primitive, eliminating the composition pitfalls that have caused some of the most devastating attacks in the history of deployed cryptography.

The history of composition failures is instructive. **MAC-then-Encrypt** (compute MAC on plaintext, then encrypt both) was used in TLS through version 1.2. The problem: the receiver must decrypt before checking the MAC, and the decryption process can leak information through error behavior. CBC-mode decryption produces different error types for valid and invalid padding, creating a **padding oracle** that an attacker can exploit to decrypt the entire ciphertext byte by byte. The BEAST, Lucky 13, and POODLE attacks all exploited this pattern in real TLS implementations. **Encrypt-and-MAC** (encrypt plaintext, separately MAC plaintext) risks leaking plaintext information through the MAC tag, since MACs are not required to hide their input. Only **Encrypt-then-MAC** (encrypt plaintext, MAC the ciphertext) is generically secure: the MAC is verified before any decryption occurs, so invalid ciphertexts are rejected without processing, eliminating oracle attacks entirely.

Modern cryptography avoids these pitfalls by using dedicated **AEAD** (Authenticated Encryption with Associated Data) constructions that integrate both operations. **AES-GCM** combines CTR-mode encryption with a polynomial MAC (GHASH) computed over the ciphertext and any unencrypted associated data. **ChaCha20-Poly1305** pairs the ChaCha20 stream cipher with the Poly1305 MAC, offering excellent performance on platforms without hardware AES acceleration. Both are AEAD schemes: a single function call takes a key, nonce, plaintext, and associated data, and produces a ciphertext with an integrated authentication tag. Decryption either succeeds (tag verifies, plaintext returned) or fails atomically (tag invalid, nothing returned) — no partial decryption leakage.

The "associated data" in AEAD is a crucial feature. Some data must be authenticated (tamper-proof) but not encrypted (visible to intermediaries). Network headers, database row identifiers, and protocol version numbers are examples: they provide context that must be bound to the ciphertext but readable by routing infrastructure. AEAD binds all of this — the encrypted payload plus the unencrypted associated data — under a single authentication tag. Modifying any bit of either the ciphertext or the associated data invalidates the tag. This comprehensive binding is why AEAD is the mandatory encryption mode in TLS 1.3, IPsec, QUIC, and essentially every modern security protocol. Standalone encryption — encryption without built-in authentication — is now considered a deprecated practice.
