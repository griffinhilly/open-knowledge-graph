---
id: message-authentication-codes
title: Message Authentication Codes (MACs)
domain: computer-science
course: cryptography
prerequisites:
- id: hash-functions-and-collision-resistance
  type: hard
- id: symmetric-encryption-block-ciphers
  type: hard
tags:
- mac
- hmac
- cbc-mac
- message-integrity
- unforgeability
stage: advanced
status: validated
---

# Message Authentication Codes (MACs)

## Core Idea
A MAC is a keyed function that takes a secret key and a message and produces a short tag. The sender transmits (message, tag); the receiver recomputes the tag with the shared key and checks for a match. Security requires existential unforgeability under chosen-message attack (EUF-CMA): an adversary who can obtain tags on messages of their choice still cannot forge a valid tag on any new message. HMAC (hash-based) and CBC-MAC (block-cipher-based) are the main constructions. MACs provide integrity and authenticity but not confidentiality — the message is sent in the clear alongside the tag.

## Questions

```yaml
- question: "A developer authenticates messages by computing Tag = SHA-256(key || message), appending the raw key before the message. Why is this insecure, and what construction fixes it?"
  type: short-answer
  answer: "SHA-256 uses Merkle-Damgard construction, which is vulnerable to length extension attacks. An attacker who sees Tag = SHA-256(key || message) can compute SHA-256(key || message || padding || extra) without knowing the key, because the tag IS the internal state after processing (key || message). This lets them forge valid tags on extended messages. HMAC fixes this by using a nested construction: HMAC(k, m) = H((k XOR opad) || H((k XOR ipad) || m)), which prevents length extension by hiding the internal state behind an outer hash."
  explanation: "The length extension vulnerability is specific to Merkle-Damgard hashes. HMAC's nested structure ensures the inner hash's output is processed through the outer hash with a different key derivation, so knowing HMAC(k, m) reveals nothing about the internal state needed to extend the computation. HMAC is provably secure as a MAC assuming the compression function of the hash is a PRF."

- question: "Encryption provides confidentiality. A MAC provides integrity and authenticity. Why doesn't encryption alone provide integrity?"
  type: multiple-choice
  options:
    - "Encryption algorithms are designed to be reversible, and any reversible function can be manipulated by an adversary"
    - "Standard encryption (without authentication) is malleable — an attacker can modify ciphertext in ways that produce predictable changes to the plaintext upon decryption, without detection. For example, flipping a bit in CTR-mode ciphertext flips the corresponding plaintext bit"
    - "Encryption keys are typically shorter than MAC keys, providing less security"
    - "Decryption always succeeds regardless of input, so corrupted ciphertext looks like a valid but different message"
  answer: 1
  explanation: "Malleability is the core issue. In CTR mode, c = p XOR keystream, so flipping ciphertext bit i flips plaintext bit i — the attacker controls exactly which bit changes. In CBC mode, manipulating ciphertext block i garbles plaintext block i but allows precise bit flips in block i+1. Without a MAC or authentication tag, the recipient decrypts the modified ciphertext and gets a modified plaintext with no indication of tampering. This is why authenticated encryption (encrypt + MAC, or integrated modes like GCM) is essential."

- question: "CBC-MAC is secure for fixed-length messages but insecure for variable-length messages without modification."
  type: true-false
  answer: true
  explanation: "For fixed-length messages, CBC-MAC is provably secure as a PRF. But for variable-length messages, an attacker can forge tags: given the tag t1 on a one-block message m1 (where t1 = E_k(m1)), the attacker can compute a valid tag on the two-block message (m1 || (m1 XOR t1)) because the second block's encryption input is t1 XOR (m1 XOR t1) = m1, producing t1 again. Variants like CMAC (which uses a final key-dependent transformation) or EMAC (which encrypts the CBC-MAC output with a second key) fix this."

- question: "A MAC guarantees that the message was sent by someone who knows the key, but it cannot prove which of the two key-holders sent it. Why is this a limitation compared to digital signatures?"
  type: short-answer
  answer: "Since both sender and receiver share the same secret key, either party could have computed the tag. The receiver cannot prove to a third party that the sender (specifically) created the message, because the receiver could have forged it themselves. Digital signatures use asymmetric keys: only the holder of the private key can sign, while anyone with the public key can verify. This provides non-repudiation — the signer cannot plausibly deny having signed."
  explanation: "MACs provide authentication between two parties who trust each other enough to share a key, but not accountability to third parties. This distinction matters in legal, financial, and protocol design contexts where proof of origin (not just integrity) is required."

- question: "HMAC uses two hash invocations. Why can't a single invocation H(key || message) serve as a secure MAC?"
  type: multiple-choice
  options:
    - "A single invocation is too slow for practical use"
    - "H(key || message) is vulnerable to length extension with Merkle-Damgard hashes. HMAC's two-pass structure prevents this and is provably secure assuming the hash's compression function is a PRF"
    - "The hash function needs to process the key twice to achieve 256-bit security"
    - "Single invocation MACs can only handle fixed-length messages"
  answer: 1
  explanation: "With Merkle-Damgard hashes (SHA-256, etc.), H(key || message) leaks the internal state as the output, enabling length extension. HMAC's construction H(k2 || H(k1 || m)) with derived keys k1 and k2 ensures the inner hash's output goes through a second keyed hash pass, preventing state exposure. The formal security proof shows HMAC is a PRF (and therefore a secure MAC) if the compression function of H is a PRF — a weaker assumption than collision resistance."
```

## Explainer

Encryption protects **confidentiality** — it hides what you said. But it does not protect **integrity** — it cannot tell you whether what arrived is what was sent. Standard encryption modes are **malleable**: an attacker can modify ciphertext in ways that produce controlled changes in the decrypted plaintext. Flipping a bit in CTR-mode ciphertext flips the corresponding plaintext bit. Without a separate integrity mechanism, the recipient decrypts tampered ciphertext into tampered plaintext and cannot detect the manipulation. A **Message Authentication Code (MAC)** fills this gap.

A MAC is a keyed function: Tag = MAC(key, message). The sender transmits both the message and the tag. The receiver, who shares the secret key, recomputes the tag and checks that it matches. If it does, the message has not been tampered with and was produced by someone who knows the key. The formal security definition is **EUF-CMA** (existential unforgeability under chosen-message attack): even an adversary who can request tags on any messages of their choosing cannot forge a valid tag on any message they haven't already queried. This is a strong guarantee — the attacker has adaptive access to a tagging oracle and still cannot cheat.

The two main constructions are **HMAC** and **CBC-MAC**. HMAC is built from a hash function: HMAC(k, m) = H((k XOR opad) || H((k XOR ipad) || m)), where ipad and opad are fixed constants. The nested structure prevents length extension attacks that plague the naive H(key || message) construction. HMAC is provably secure under the assumption that the hash's compression function is a pseudorandom function — a weaker assumption than collision resistance, which means HMAC can remain secure even if collision attacks on the hash are found. CBC-MAC encrypts the message in CBC mode and uses the final block as the tag. It is provably secure for fixed-length messages but requires modifications (CMAC, EMAC) for variable-length messages due to specific forgery attacks.

A critical limitation of MACs is that they provide **authentication** but not **non-repudiation**. Since both parties share the same key, either could have produced the tag — the receiver cannot prove to a third party that the sender specifically created the message, because the receiver could have forged it. Digital signatures, which use asymmetric cryptography, solve this by letting only the private key holder sign while anyone can verify. For many protocols, MACs suffice (two parties who already trust each other), but wherever proof of origin matters — legal documents, financial transactions, software distribution — signatures are needed instead.
