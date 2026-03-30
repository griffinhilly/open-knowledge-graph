---
id: identity-based-encryption
title: Identity-Based Encryption
domain: computer-science
course: cryptography
prerequisites:
- id: computational-hardness-assumptions
  type: hard
- id: elliptic-curve-cryptography-basics
  type: hard
tags:
- ibe
- boneh-franklin
- bilinear-pairing
- key-escrow
- pki-alternative
stage: expert
status: validated
---

# Identity-Based Encryption

## Core Idea
Identity-based encryption (IBE) allows a sender to encrypt to a recipient using only their identity (email address, phone number) as the public key — no certificate lookup needed. A trusted Key Generation Center (KGC) holds a master secret key and derives private keys from identities. Boneh and Franklin (2001) gave the first efficient IBE construction using bilinear pairings on elliptic curves. IBE simplifies key management (no PKI needed) but introduces key escrow (the KGC can decrypt all messages). IBE also enables advanced features like fuzzy/attribute-based encryption and hierarchical delegation.

## Questions

```yaml
- question: "IBE eliminates the need for certificates. Why is this a significant advantage over traditional PKI, and what is the corresponding disadvantage?"
  type: short-answer
  answer: "In PKI, a sender must obtain and verify the recipient's certificate before encrypting — this requires certificate distribution infrastructure, revocation checking, and trust chain validation. IBE eliminates this: the sender encrypts directly to 'alice@example.com' using only the system's public parameters. The disadvantage is key escrow: the KGC generates all private keys and therefore can decrypt any message. There is no way for a user to have a private key that the KGC doesn't know, which is unacceptable for many applications."
  explanation: "IBE trades the decentralized trust model of PKI (trust many CAs, no single point of decryption) for a centralized one (trust one KGC, which can decrypt everything). This tradeoff is acceptable in enterprise settings (the organization already controls all data) but problematic for general internet encryption where users expect end-to-end privacy."

- question: "Bilinear pairings are the mathematical tool enabling Boneh-Franklin IBE. What property does a pairing e: G1 x G2 → GT provide?"
  type: multiple-choice
  options:
    - "e(aP, bQ) = e(P, Q)^{ab} — the pairing is bilinear, meaning it 'transfers' scalar multiplication from the input groups to exponentiation in the target group. This creates algebraic relationships between group elements that don't exist without pairings"
    - "The pairing encrypts elements from G1 using elements from G2"
    - "The pairing provides a collision-resistant hash from G1 x G2 to GT"
    - "The pairing compresses two group elements into one smaller element"
  answer: 0
  explanation: "Bilinearity is the key: e(aP, bQ) = e(P, Q)^{ab}. This lets the Boneh-Franklin scheme work: the KGC computes a private key d_ID = s*H(ID) (master secret s times the hash of the identity), and encryption/decryption use the pairing to connect the identity-derived public key with the secret key, without anyone else being able to compute s. Pairings enabled a revolution in cryptography, yielding IBE, short signatures, and efficient non-interactive zero-knowledge proofs."

- question: "In IBE, a user can receive encrypted messages before they have even obtained their private key from the KGC."
  type: true-false
  answer: true
  explanation: "This is one of IBE's most useful properties. Anyone can encrypt to 'alice@example.com' using only Alice's identity and the system's public parameters — Alice doesn't need to have registered or obtained her key yet. When Alice eventually authenticates to the KGC and receives her private key, she can decrypt all messages that were encrypted to her identity. This enables 'encrypt-to-the-future' scenarios and simplifies deployment because the sender never needs to coordinate with the recipient."

- question: "IBE provides a natural solution to certificate revocation. How can time-based IBE key management replace CRLs and OCSP?"
  type: multiple-choice
  options:
    - "IBE keys never expire, eliminating the need for revocation"
    - "Encrypt to identity strings that include a time period, e.g., 'alice@example.com || 2026-Q1'. The KGC issues private keys for the current period only. A revoked user simply doesn't receive keys for future periods. No revocation lists or online checking needed — expired identities automatically become undecryptable"
    - "The KGC broadcasts revocation messages that invalidate specific identities"
    - "IBE uses the same CRL mechanism as PKI"
  answer: 1
  explanation: "This elegant approach was proposed by Boneh and Franklin. By embedding time into the identity string, revocation becomes key non-issuance: the KGC stops generating keys for revoked users in future periods. The sender's encryption automatically includes a time component, ensuring messages are only decryptable by users who are active during the relevant period. The main cost is that users must periodically obtain fresh keys from the KGC, but this is a feature — it enforces ongoing authentication."

- question: "Hierarchical IBE (HIBE) allows organizations to delegate key generation to sub-authorities. A university KGC generates keys for department KGCs, which generate keys for individual professors. Why is this valuable?"
  type: short-answer
  answer: "HIBE distributes the KGC's load and trust. The university root KGC issues a department-level secret key to 'cs.university.edu'. The CS department uses this key to derive individual keys like 'alice@cs.university.edu' without contacting the root KGC. This mirrors organizational hierarchies, scales better than a single KGC, and limits damage from compromise (a compromised department KGC can only forge keys within its sub-tree). The tradeoff is that ciphertext size and decryption cost grow with hierarchy depth."
  explanation: "HIBE extends IBE's identity-as-public-key paradigm to hierarchical namespaces, naturally matching organizations like companies (CEO → VP → Manager → Employee) or DNS (com → example → mail). Each level can independently manage its sub-tree, providing both scalability and compartmentalized trust."
```

## Explainer

Traditional public-key encryption requires the sender to know the recipient's public key, which means obtaining and verifying a certificate — the entire PKI infrastructure of certificate authorities, revocation lists, and trust chains. **Identity-Based Encryption (IBE)**, conceived by Adi Shamir in 1984 and first efficiently realized by Boneh and Franklin in 2001, eliminates this requirement. In IBE, the recipient's public key IS their identity — their email address, phone number, employee ID, or any arbitrary string. Anyone can encrypt to "alice@example.com" using only this string and the system's public parameters, without any certificate.

The scheme requires a **Key Generation Center (KGC)** that holds a master secret key. During setup, the KGC publishes system-wide public parameters. When Alice wants to decrypt, she authenticates to the KGC and receives her private key, derived from her identity and the master secret. The mathematical magic that makes this work is **bilinear pairings** on elliptic curves: a function e: G1 x G2 → GT satisfying e(aP, bQ) = e(P, Q)^{ab}. This bilinearity creates algebraic bridges between the identity-derived public key and the master-secret-derived private key that enable encryption and decryption to work, while the hardness of the Bilinear Diffie-Hellman (BDH) problem prevents anyone without the private key from decrypting.

The most notable feature and the most significant limitation of IBE are two sides of the same coin: **key escrow**. Since the KGC generates all private keys, it can decrypt any message in the system. This is unacceptable for many applications (users expect end-to-end privacy from everyone, including the system operator), but it is actually desirable in enterprise environments where the organization legitimately needs the ability to decrypt employee communications (legal compliance, departing employees, regulatory audits). For organizations that already have centralized authority over their users' cryptographic credentials, IBE offers dramatic simplification over PKI.

IBE's impact extends well beyond its direct use case. It demonstrated that **bilinear pairings** could solve long-standing open problems in cryptography, spawning an entire field of pairing-based cryptography that includes short signatures (Boneh-Lynn-Shacham), attribute-based encryption, functional encryption, and efficient non-interactive zero-knowledge proofs. **Hierarchical IBE (HIBE)** allows delegation of key generation authority, mirroring organizational structures. **Fuzzy IBE** (Sahai-Waters) allows decryption when the identity matches "approximately" — if the encryption identity and the key identity share enough attributes — which is the conceptual precursor to attribute-based encryption. The line of research from IBE through ABE to general functional encryption represents the progressive expansion of what "access control through cryptography" can achieve.
