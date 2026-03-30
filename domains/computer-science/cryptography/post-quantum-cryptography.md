---
id: post-quantum-cryptography
title: Post-Quantum Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: lattice-based-cryptography
  type: hard
- id: learning-with-errors
  type: hard
- id: elliptic-curve-cryptography-basics
  type: soft
tags:
- post-quantum
- nist-pqc
- kyber
- dilithium
- harvest-now-decrypt-later
stage: expert
status: validated
---

# Post-Quantum Cryptography

## Core Idea
Shor's quantum algorithm solves factoring and discrete logarithms in polynomial time, breaking RSA, DH, ECDH, and ECDSA. Post-quantum cryptography (PQC) develops replacements based on problems believed resistant to quantum attack: lattices (ML-KEM, ML-DSA), hash functions (SPHINCS+/SLH-DSA), codes (Classic McEliece), and multivariate polynomials. NIST standardized ML-KEM and ML-DSA in 2024, based on Module-LWE/Module-SIS. The "harvest now, decrypt later" threat (adversaries store encrypted traffic for future quantum decryption) motivates immediate transition, even before large quantum computers exist. Hybrid approaches pair PQC with classical algorithms during the migration.

## Questions

```yaml
- question: "An organization argues they don't need post-quantum cryptography because large-scale quantum computers are at least 10-15 years away. What threat model are they ignoring?"
  type: short-answer
  answer: "The 'harvest now, decrypt later' threat: adversaries (especially state-level) can record encrypted network traffic today and store it. Once quantum computers become available, they can retroactively decrypt everything they captured. Data with long-term sensitivity — state secrets, medical records, financial data, intellectual property — needs quantum-resistant protection NOW, because it must remain confidential for decades beyond the point when quantum computers arrive."
  explanation: "The transition timeline matters: deploying new cryptographic standards across global infrastructure takes years. If migration starts when quantum computers arrive, the window of vulnerability extends years further. NIST and NSA recommend immediate migration planning, with hybrid deployments (classical + PQC) as the transitional approach."

- question: "NIST selected lattice-based schemes (ML-KEM, ML-DSA) as primary standards but also standardized a hash-based signature scheme (SLH-DSA/SPHINCS+). Why include both?"
  type: multiple-choice
  options:
    - "Hash-based signatures are faster than lattice-based ones"
    - "SLH-DSA relies only on the security of hash functions, which have decades of analysis and no known algebraic structure to exploit. If a breakthrough breaks lattice assumptions, SLH-DSA survives. Including it provides cryptographic diversity — not putting all eggs in the lattice basket"
    - "Hash-based signatures provide shorter keys than lattice-based ones"
    - "NIST was required by law to standardize at least two different mathematical foundations"
  answer: 1
  explanation: "Cryptographic diversity is a hedge against catastrophic assumption failure. All lattice-based schemes share related mathematical foundations — a breakthrough in lattice cryptanalysis could break them all simultaneously. Hash-based signatures rest on a completely different foundation (the security of hash functions, a much older and more conservative assumption). The tradeoff is performance: SLH-DSA signatures are ~8-50 KB and signing is slower, compared to ML-DSA's ~2.4 KB signatures and faster signing. The diversity premium justifies the performance cost."

- question: "Shor's algorithm breaks RSA and ECDSA but does not break AES or SHA-256. Does this mean symmetric cryptography is unaffected by quantum computers?"
  type: multiple-choice
  options:
    - "Correct — symmetric cryptography is completely quantum-safe"
    - "Partially — Grover's algorithm provides a quadratic speedup for brute-force key search, halving the effective security. AES-128 drops to ~64 bits of quantum security, so AES-256 (providing ~128 quantum bits) is recommended. SHA-256 collision resistance drops from 128 to ~85 bits. These are manageable by doubling key/hash sizes, unlike the exponential-to-polynomial collapse for public-key schemes"
    - "Symmetric cryptography is equally broken by quantum computers"
    - "Grover's algorithm breaks AES in linear time"
  answer: 1
  explanation: "Grover's algorithm searches an unstructured space of N items in O(sqrt(N)) quantum operations. For AES-128 with 2^128 keys, this means ~2^64 quantum operations — feasible for a large quantum computer. AES-256 requires ~2^128 quantum operations, which remains secure. The impact on symmetric crypto is quantitative (double key sizes) rather than qualitative (completely broken). This is why the PQC transition focuses on public-key algorithms, which face an existential threat."

- question: "During the PQC transition, hybrid key exchange combines a classical algorithm (like ECDH) with a PQC algorithm (like ML-KEM). Security holds if EITHER algorithm is secure."
  type: true-false
  answer: true
  explanation: "Hybrid key exchange derives the shared secret by combining outputs from both algorithms (typically via a key derivation function). If ML-KEM turns out to be broken but ECDH is secure (no quantum computers), the combined key is still secure. If ECDH is broken by a quantum computer but ML-KEM is secure, the combined key is still secure. Only if both are simultaneously broken does the system fail. This belt-and-suspenders approach provides safety during the uncertain transition period where confidence in PQC schemes is still building."

- question: "The SIKE/SIDH isogeny-based key exchange was a NIST PQC finalist before being catastrophically broken in 2022. What lesson does this carry for the PQC transition?"
  type: short-answer
  answer: "SIDH survived over 10 years of cryptanalysis before Castryck-Decru found a polynomial-time key recovery attack in 2022 — a complete break, not a marginal improvement. This demonstrates that even well-studied schemes can harbor fundamental vulnerabilities. Lessons: (1) cryptographic diversity is essential — relying on a single mathematical foundation is risky, (2) longer cryptanalysis history provides more confidence but never certainty, (3) hybrid deployments protect against surprise breaks in new schemes. NIST's decision to include hash-based signatures alongside lattice schemes reflects this lesson."
  explanation: "SIDH's break was enabled by known mathematical connections between isogenies and abelian varieties that the cryptographic community had not fully explored. The attack used theta functions and the structure of product isogenies. It was a reminder that the security of a scheme depends on the full depth of mathematical understanding of the underlying problem — and that understanding evolves."
```

## Explainer

**Post-quantum cryptography (PQC)** is the urgent project of replacing the public-key algorithms (RSA, DH, ECDH, ECDSA) that secure the internet with alternatives that resist quantum computers. The threat is specific and devastating: **Shor's algorithm** solves integer factoring and discrete logarithms in polynomial time on a quantum computer, completely breaking RSA (factoring), Diffie-Hellman (discrete logs in multiplicative groups), and elliptic curve cryptography (discrete logs in elliptic curve groups). A sufficiently large quantum computer would break every HTTPS connection, every digital signature, and every encrypted email that relies on these algorithms.

The urgency comes from the **"harvest now, decrypt later"** threat model. State-level adversaries are believed to be recording encrypted internet traffic today, storing it for future decryption once quantum computers mature. Data that must remain confidential for 20+ years (classified information, medical records, long-term business secrets) is already at risk if encrypted with quantum-vulnerable algorithms. The migration timeline compounds the urgency: replacing cryptographic algorithms across global infrastructure — browsers, servers, hardware security modules, embedded systems, satellites — takes years. Starting the transition after quantum computers arrive means years of additional vulnerability.

NIST finalized its first PQC standards in 2024 after an 8-year evaluation process. **ML-KEM** (Module-Lattice Key Encapsulation Mechanism, based on Kyber) replaces ECDH for key exchange, with public keys around 800-1500 bytes and encapsulation times under a millisecond. **ML-DSA** (Module-Lattice Digital Signature Algorithm, based on Dilithium) replaces ECDSA for signatures, with ~2.4 KB signatures. Both are based on Module-LWE/Module-SIS, lattice problems believed to resist quantum attacks. **SLH-DSA** (Stateless Hash-based Digital Signature Algorithm, based on SPHINCS+) provides an alternative signature scheme relying only on hash function security — larger signatures (8-50 KB) but based on the most conservative assumptions. The devastating 2022 break of SIDH/SIKE (an isogeny-based finalist that fell to a polynomial-time attack after a decade of study) reinforced the importance of this algorithmic diversity.

The transition strategy involves **hybrid approaches**: pairing classical algorithms with PQC counterparts so that security holds if either algorithm survives. Chrome and Firefox already support hybrid TLS key exchange (X25519 + ML-KEM). The combined key is derived from both algorithms' outputs, ensuring that a break in ML-KEM (if lattice assumptions fail) leaves ECDH protection intact, while a quantum attack on ECDH leaves ML-KEM protection intact. This belt-and-suspenders approach will likely persist for years as the cryptographic community builds confidence in the new standards. The PQC transition is the largest coordinated change in deployed cryptographic infrastructure since the adoption of public-key cryptography itself, touching every system that establishes secure connections or verifies digital signatures.
