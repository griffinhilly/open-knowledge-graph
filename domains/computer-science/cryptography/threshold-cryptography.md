---
id: threshold-cryptography
title: Threshold Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: secret-sharing
  type: hard
- id: digital-signatures
  type: hard
tags:
- threshold-signature
- distributed-key-generation
- proactive-security
- key-management
stage: expert
status: validated
---

# Threshold Cryptography

## Core Idea
Threshold cryptography distributes a cryptographic key among n parties so that t must cooperate to perform operations (signing, decryption) but no t-1 colluding parties learn anything about the key. Unlike basic secret sharing (which reconstructs the key before use), threshold schemes compute directly on shares — the full key is never assembled in any single location. Distributed Key Generation (DKG) eliminates even the trusted dealer. Applications include cryptocurrency custody (multi-sig wallets), CA key protection, and organizational policy enforcement. Threshold ECDSA and threshold Schnorr are deployed in production systems.

## Questions

```yaml
- question: "Basic secret sharing requires reconstructing the key to use it. Threshold signatures avoid this. Why is never assembling the key a critical security improvement?"
  type: short-answer
  answer: "If the key is reconstructed in any single location — even temporarily — that location becomes a single point of compromise. An attacker who compromises the reconstructing party during the brief window of reconstruction obtains the full key. Threshold signing computes partial signatures on shares, which are combined into a full signature without any party ever seeing the full key. The key exists only as shares distributed across multiple parties, so no single compromise reveals it."
  explanation: "This is the fundamental difference between secret sharing (storage protection) and threshold cryptography (computation protection). Secret sharing protects the key at rest; threshold cryptography protects it during use. A banking analogy: secret sharing is like splitting a vault combination among three people — they must gather and enter it together. Threshold signing is like a vault that opens only when three people simultaneously turn their individual keys, without any of them learning the others' keys."

- question: "Distributed Key Generation (DKG) allows n parties to jointly generate a shared key without any trusted dealer. Why is this important?"
  type: multiple-choice
  options:
    - "DKG produces stronger keys than a single dealer could"
    - "With a trusted dealer, the dealer knows the full key during generation — they are a single point of trust and failure. DKG uses each party as a simultaneous dealer (each sharing a random value via VSS) and combines the shares additively. The result is a shared key that no individual party — including any dealer — ever knew. This eliminates the trusted setup problem"
    - "DKG is faster than centralized key generation"
    - "Regulatory requirements mandate DKG for financial applications"
  answer: 1
  explanation: "DKG typically uses Pedersen's DKG protocol: each party i picks a random secret s_i and shares it among all parties via VSS. The combined secret s = s_1 + s_2 + ... + s_n is the final key. No party knows s because each party only knows their own s_i. Each party's share of s is the sum of shares they received from all other parties. This is secure as long as fewer than t parties are corrupted — the corrupt parties collectively know their own s_i values but not the honest parties'."

- question: "Proactive secret sharing periodically refreshes shares without changing the underlying secret. Why is this useful against a mobile adversary who gradually compromises different parties over time?"
  type: multiple-choice
  options:
    - "Refreshing changes the secret, so old compromised shares become useless"
    - "Without proactive refresh, an adversary who compromises t parties at ANY point over the system's lifetime (even different parties at different times) obtains t shares and can reconstruct the secret. Proactive refresh generates new shares of the same secret in each epoch. Shares from different epochs are algebraically incompatible — mixing old and new shares yields nothing. The adversary must compromise t parties within a single epoch to succeed"
    - "Refreshing makes the shares smaller, improving performance"
    - "Proactive refresh protects against quantum attacks"
  answer: 1
  explanation: "The mobile adversary model is realistic: over months or years, different machines may be compromised, patched, and compromised again. Without proactive refresh, the adversary accumulates shares from each compromise. Proactive secret sharing ensures that shares from different epochs are useless together — each epoch uses a fresh random polynomial with the same constant term (secret). The adversary's window of attack is bounded to a single epoch, regardless of the system's total lifetime."

- question: "Threshold ECDSA is more complex than threshold Schnorr signatures because ECDSA's signing equation involves a multiplicative inverse of the nonce, which is hard to compute distributedly on secret shares."
  type: true-false
  answer: true
  explanation: "Schnorr signatures are naturally threshold-friendly: the signing equation is s = k + ex (linear in the secret key x and nonce k), so partial signatures on shares combine additively. ECDSA's signing equation is s = k^{-1}(H(m) + rx) — the inverse of k and the product kx require multi-party multiplication and inversion protocols, which are expensive. This is why threshold ECDSA took decades longer to develop efficiently than threshold Schnorr, and why the shift toward Schnorr-based signatures (Ed25519, BIP-340) in modern systems partly reflects the desire for threshold-friendliness."

- question: "A cryptocurrency exchange uses (3,5) threshold ECDSA to protect its hot wallet key. An attacker compromises 2 of the 5 key servers. What can the attacker do?"
  type: short-answer
  answer: "With 2 of 5 shares (below the threshold of 3), the attacker learns nothing about the signing key and cannot produce any valid signature — even a partial one that could be useful later. The exchange can still sign transactions using any 3 of the remaining 3 uncorrupted servers (the scheme is fault-tolerant). The exchange should then run a proactive refresh to invalidate the compromised shares, preventing the attacker from accumulating shares over time toward the threshold."
  explanation: "The (3,5) design provides both security (tolerates 2 compromises) and availability (tolerates 2 failures). The exchange can lose or quarantine the compromised servers and continue operating with the remaining 3. Proactive refresh is the recommended response to partial compromise — it generates new shares incompatible with the old ones, resetting the adversary's progress."
```

## Explainer

**Threshold cryptography** takes the idea of secret sharing and extends it from secure storage to secure computation. In basic secret sharing, the key must be reconstructed before use — creating a window of vulnerability when the full key exists in a single location. Threshold cryptography eliminates this window: parties compute directly on their shares, producing partial results that combine into a valid cryptographic operation (signature, decryption) without the full key ever existing anywhere. The key is born distributed, lives distributed, and operates distributed.

A **(t, n) threshold signature scheme** works as follows. During setup (via DKG or a trusted dealer), the signing key sk is shared among n parties, each holding a share sk_i. To sign a message, at least t parties compute **partial signatures** using their individual shares. These partial signatures are combined (typically via Lagrange coefficients) to produce a standard signature verifiable by anyone with the public key. No individual party ever sees the full signing key. For Schnorr signatures, this is elegant: the signing equation s = k + ex is linear in the secret key x, so partial signatures s_i = k_i + e * x_i (computed on shares k_i and x_i) sum to the correct full signature. For ECDSA, the multiplicative inverse in s = k^{-1}(H(m) + rx) makes distributed computation harder, requiring multi-party multiplication protocols.

**Distributed Key Generation (DKG)** eliminates the trusted dealer, the last centralized trust point. Each party acts as a dealer: party i generates a random secret s_i and distributes shares of s_i to all parties using verifiable secret sharing. The aggregate secret s = sum(s_i) is the signing key. No party knows s because no party knows all the s_i values — each knows only their own contribution and the shares they received from others. Their share of s is the sum of all shares they received. This construction is secure as long as fewer than t parties collude, and it handles malicious parties through the verification mechanisms of VSS.

**Proactive security** addresses the realistic threat of a **mobile adversary** — an attacker who compromises different parties over time. Without countermeasures, an adversary who compromises party 1 in January and party 2 in March has accumulated 2 shares, regardless of whether party 1 has since been patched. **Proactive secret sharing** divides time into epochs and refreshes shares at each epoch boundary. Each party distributes shares of zero (a random degree-(t-1) polynomial with constant term 0) and everyone adds the received shares to their existing share. The result is a new set of shares for the same secret, but algebraically incompatible with shares from the previous epoch. The adversary must compromise t parties within a single epoch — their accumulated shares from different epochs are useless. This is deployed in production systems for cryptocurrency custody (Fireblocks, Coinbase), certificate authority key protection, and organizational signing infrastructure where keys must remain secure for years.
