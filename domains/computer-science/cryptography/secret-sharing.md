---
id: secret-sharing
title: Secret Sharing
domain: computer-science
course: cryptography
prerequisites:
- id: modular-arithmetic
  type: hard
- id: perfect-secrecy-and-one-time-pad
  type: soft
tags:
- secret-sharing
- shamir
- threshold-scheme
- polynomial-interpolation
- information-theoretic
stage: expert
status: validated
---

# Secret Sharing

## Core Idea
A (t, n) secret sharing scheme distributes a secret s among n parties such that any t parties can reconstruct s, but any t-1 parties learn absolutely nothing about s. Shamir's scheme (1979) uses polynomial interpolation: encode s as the constant term of a random degree-(t-1) polynomial over a finite field, and give each party a point on the polynomial. Any t points determine the polynomial (Lagrange interpolation); fewer than t points leave s information-theoretically hidden. Secret sharing is foundational for threshold cryptography, secure MPC (BGW protocol), key management, and distributed systems requiring fault-tolerant access to secrets.

## Questions

```yaml
- question: "In Shamir's (3,5) scheme, the secret is the constant term of a random degree-2 polynomial p(x) = s + a1*x + a2*x^2 over a finite field. Why do exactly 3 points determine s, but 2 points reveal nothing?"
  type: short-answer
  answer: "A degree-2 polynomial has 3 coefficients: s, a1, a2. Three points on the polynomial give three linear equations in three unknowns, which has a unique solution — determining all coefficients including s. Two points give two equations in three unknowns — for every possible value of s, there exists a polynomial consistent with the two known points. Since a1 and a2 were chosen uniformly at random, every value of s is equally likely given any two shares. This is information-theoretic security: no computational power helps."
  explanation: "The key insight is that the random coefficients a1, a2, ... provide 'degrees of freedom' that mask s when fewer than t points are known. With t-1 points, there is exactly one free parameter, and it ranges over all field elements, making s uniformly distributed over the field regardless of its actual value. This is perfect secrecy for the secret, not just computational security."

- question: "Shamir's secret sharing provides information-theoretic security (perfect secrecy) for the secret. What assumption does it NOT require?"
  type: multiple-choice
  options:
    - "A finite field large enough to hold the secret"
    - "Any computational hardness assumption — Shamir's scheme is unconditionally secure against adversaries with unlimited computing power, as long as fewer than t shares are compromised. This contrasts with most cryptographic schemes that rely on assumptions like factoring or LWE being hard"
    - "Honest behavior from the share dealer"
    - "A secure channel for distributing shares"
  answer: 1
  explanation: "Shamir's scheme achieves perfect secrecy in the information-theoretic sense: t-1 shares are statistically independent of the secret. No amount of computation changes this — it follows from the algebra of polynomial interpolation. This makes secret sharing one of the few cryptographic tools with unconditional security. The scheme does require secure channels for share distribution (otherwise an eavesdropper could collect shares) and an honest dealer (or verifiable secret sharing to protect against a dishonest dealer)."

- question: "An organization uses (3,5) secret sharing to protect a master encryption key. Two of the five shareholders collude and share their shares. What do they learn about the key?"
  type: multiple-choice
  options:
    - "They learn approximately 2/5 of the key's bits"
    - "They learn nothing — with only 2 of the required 3 shares, the key remains perfectly hidden. Every possible key value is equally consistent with their two shares"
    - "They learn the key but cannot prove it to others"
    - "They learn the key only if they also know the polynomial's degree"
  answer: 1
  explanation: "This is the essential security guarantee: t-1 shares are statistically independent of the secret. For any two shares and any candidate secret value, there exists exactly one degree-2 polynomial consistent with all three constraints. Since the polynomial's random coefficients are unknown, every secret value is equally likely. The colluding pair learns literally nothing — not a single bit of information — about the key."

- question: "Verifiable secret sharing (VSS) extends Shamir's scheme to protect against a dishonest dealer who distributes inconsistent shares. Why is this important?"
  type: short-answer
  answer: "In basic Shamir's scheme, the dealer could give some parties shares from one polynomial and other parties shares from a different polynomial — or shares that don't lie on any single polynomial at all. When parties try to reconstruct, they either get the wrong secret or fail entirely. VSS lets each party verify that their share is consistent with a committed polynomial, without revealing the secret or other shares. Feldman's VSS publishes commitments g^{a_i} for each coefficient; Pedersen's VSS uses Pedersen commitments for information-theoretic hiding. VSS is essential in MPC protocols where the dealer may be adversarial."
  explanation: "VSS transforms secret sharing from a protocol that requires a trusted dealer into one that works with a potentially malicious dealer. This is crucial for MPC: in the BGW protocol, each party acts as a dealer for their own input. Without VSS, a malicious party could send inconsistent shares and corrupt the computation."

- question: "Secret sharing can be used to build a simple (t, n) threshold signature scheme where t of n parties must cooperate to sign, but no individual party can sign alone."
  type: true-false
  answer: true
  explanation: "The signing key is shared using (t, n) Shamir sharing. To sign, t parties each compute a 'partial signature' using their share and combine the partial signatures to produce a full signature. No individual party ever sees the full signing key. Threshold ECDSA and threshold Schnorr signatures implement this for standard signature schemes. This is used in cryptocurrency custody (multi-sig wallets), certificate authority key protection, and organizational signing policies where multiple approvers are required."
```

## Explainer

**Secret sharing** addresses a fundamental problem in distributed systems: how do you store a secret so that it remains available even if some participants fail, yet remains hidden even if some participants are compromised? The answer is to split the secret into pieces (shares) distributed among n participants, such that any threshold t of them can reconstruct the secret, but fewer than t learn absolutely nothing. This is a **(t, n) threshold scheme**, and it achieves the remarkable property of being simultaneously fault-tolerant (survives n-t failures) and secure (resists up to t-1 compromises).

**Shamir's Secret Sharing** (1979) is the most elegant construction, based on polynomial interpolation over a finite field. To share a secret s with threshold t among n parties, the dealer constructs a random polynomial p(x) of degree t-1 with p(0) = s (the secret is the constant term). The remaining t-1 coefficients are chosen uniformly at random. Each party i receives the share p(i). Any t parties can reconstruct p(x) using **Lagrange interpolation** (t points uniquely determine a degree-(t-1) polynomial) and recover s = p(0). Any t-1 parties learn nothing: for any hypothesized value of s, there exists a polynomial of degree t-1 consistent with their shares, so all values of s are equally likely. This is **information-theoretic** security — no computational assumption is needed.

The applications of secret sharing pervade modern cryptography and distributed systems. In **threshold cryptography**, a signing or decryption key is shared among n parties, and t must cooperate to sign or decrypt — preventing any single party from unilateral action. Cryptocurrency custody solutions use threshold signatures so that stealing funds requires compromising t of n key holders. In **secure multi-party computation**, the BGW protocol uses Shamir sharing as its core mechanism: each party shares their input, and the function is computed on shares. In **key management**, organizations use (t, n) sharing to protect master keys: the key can be reconstructed when needed (e.g., for disaster recovery) but is never stored in any single location.

**Verifiable Secret Sharing (VSS)** extends the basic scheme to handle a dishonest dealer. In standard Shamir sharing, the dealer could distribute inconsistent shares — points that don't lie on any single polynomial — causing reconstruction to fail or produce wrong results. VSS adds a verification mechanism: the dealer publishes commitments to the polynomial's coefficients, and each party can check that their share is consistent with these commitments without learning the secret. Feldman's VSS and Pedersen's VSS are the two main constructions. VSS is essential in settings where the dealer may be adversarial (as in MPC, where each party acts as dealer for their own input), transforming secret sharing from a tool that requires a trusted third party into one that works in the fully adversarial model.
