---
id: diffie-hellman-key-exchange
title: Diffie-Hellman Key Exchange
domain: computer-science
course: cryptography
prerequisites:
- id: modular-arithmetic
  type: hard
- id: discrete-logarithms
  type: hard
- id: symmetric-encryption-block-ciphers
  type: soft
tags:
- diffie-hellman
- key-exchange
- discrete-logarithm-problem
- man-in-the-middle
stage: advanced
status: validated
---

# Diffie-Hellman Key Exchange

## Core Idea
Diffie-Hellman (1976) allows two parties to establish a shared secret key over a public channel without any prior shared secret. Both parties agree on a public prime p and generator g. Alice picks secret a, sends g^a mod p; Bob picks secret b, sends g^b mod p. Both compute the shared key g^{ab} mod p. Security rests on the Computational Diffie-Hellman (CDH) assumption: given g^a and g^b, computing g^{ab} is hard without knowing a or b. DH is vulnerable to man-in-the-middle attacks without authentication. The protocol also works over elliptic curve groups (ECDH), offering equivalent security with smaller parameters.

## Questions

```yaml
- question: "Alice and Bob perform Diffie-Hellman over a public channel. Eve observes g, p, g^a mod p, and g^b mod p. To compute the shared key g^{ab} mod p, what problem must Eve solve?"
  type: multiple-choice
  options:
    - "The integer factorization problem — Eve must factor p to recover a and b"
    - "The discrete logarithm problem — Eve must compute a from g^a mod p (or b from g^b mod p)"
    - "The Computational Diffie-Hellman (CDH) problem — Eve must compute g^{ab} mod p given g^a and g^b, without necessarily finding a or b individually"
    - "The RSA problem — Eve must find the private exponent d"
  answer: 2
  explanation: "The CDH problem is precisely: given g, g^a, g^b in a group, compute g^{ab}. This is believed hard in well-chosen groups. Note that CDH is potentially easier than the discrete logarithm problem (DLP) — if Eve could solve DLP, she could find a from g^a and compute (g^b)^a, but CDH might be solvable without finding either discrete logarithm. In practice, we use groups where both CDH and DLP are hard. The Decisional Diffie-Hellman (DDH) assumption — that (g^a, g^b, g^{ab}) is indistinguishable from (g^a, g^b, g^c) — is an even stronger assumption used to prove semantic security of ElGamal encryption."

- question: "Diffie-Hellman by itself is secure against passive eavesdroppers but vulnerable to active man-in-the-middle attacks. Describe the attack."
  type: short-answer
  answer: "An active attacker Mallory intercepts the exchange. When Alice sends g^a, Mallory blocks it, picks her own secret m1, and sends g^{m1} to Bob. When Bob sends g^b, Mallory blocks it, picks m2, and sends g^{m2} to Alice. Now Alice computes key1 = g^{a*m2}, and Bob computes key2 = g^{b*m1}. Mallory knows both keys. She decrypts messages from Alice with key1, reads them, re-encrypts with key2, and forwards to Bob. Neither party detects the interception."
  explanation: "The vulnerability exists because basic DH provides no authentication — neither party can verify who they're communicating with. The fix is to authenticate the DH exchange using digital signatures (as in the Station-to-Station protocol), certificates (as in TLS), or pre-shared keys. Authenticated DH is the standard in all modern protocols."

- question: "The Diffie-Hellman key exchange was published in 1976, one year before RSA. Why is it historically significant that DH solved key distribution without requiring a prior shared secret?"
  type: short-answer
  answer: "Before DH, all known encryption required both parties to share a secret key in advance — the key distribution problem. If Alice and Bob wanted to communicate securely, they needed a secure channel to exchange keys first, creating a chicken-and-egg problem. DH solved this by allowing secure key agreement over a completely public channel, using only publicly known parameters. This breakthrough enabled secure communication between parties who had never met, which is the foundation of internet security (HTTPS, SSH, etc.)."
  explanation: "The key distribution problem was considered the fundamental limitation of cryptography. DH showed that public-key techniques could solve it, opening the era of public-key cryptography. Every secure connection on the internet ultimately relies on some form of DH or its elliptic curve variant for session key establishment."

- question: "Choosing a safe prime p = 2q + 1 (where q is also prime) for Diffie-Hellman is important because it ensures the group of order q has no small subgroups that would weaken the discrete logarithm problem."
  type: true-false
  answer: true
  explanation: "If p - 1 has small prime factors, the multiplicative group mod p contains small subgroups. An attacker can exploit the Pohlig-Hellman algorithm to decompose the discrete logarithm into smaller problems in each subgroup. With p = 2q + 1, the order of the multiplicative group is p - 1 = 2q, and working in the subgroup of order q (a large prime) eliminates all small-subgroup attacks. This is why safe primes are standard for DH parameter selection."

- question: "In Elliptic Curve Diffie-Hellman (ECDH), a 256-bit key provides security comparable to a 3072-bit classical DH key."
  type: true-false
  answer: true
  explanation: "Elliptic curve groups lack the index calculus algorithms that accelerate discrete logarithms in multiplicative groups mod p. The best known attack on well-chosen elliptic curves is Pollard's rho, which runs in O(sqrt(n)) time where n is the group order. A 256-bit elliptic curve group provides approximately 128 bits of security (2^128 operations). Achieving 128-bit security with classical DH requires a ~3072-bit prime because the Number Field Sieve for discrete logarithms runs in sub-exponential time. This efficiency advantage makes ECDH the default choice in modern protocols like TLS 1.3."
```

## Explainer

In 1976, Whitfield Diffie and Martin Hellman published a protocol that solved one of the oldest problems in cryptography: how can two people who have never met establish a shared secret over a channel that anyone can listen to? Before their work, all encryption required a pre-existing shared key — to communicate securely, you first needed a secure channel to exchange keys, which was precisely the problem you were trying to solve. **Diffie-Hellman key exchange** breaks this circularity using the one-way nature of modular exponentiation.

The protocol is remarkably simple. Alice and Bob publicly agree on a large prime p and a generator g of a multiplicative group modulo p. Alice picks a random secret integer a and sends A = g^a mod p to Bob. Bob picks a random secret b and sends B = g^b mod p to Alice. Alice computes K = B^a = g^{ba} mod p; Bob computes K = A^b = g^{ab} mod p. Both arrive at the same shared secret K = g^{ab} mod p. An eavesdropper sees g, p, g^a, and g^b, but computing g^{ab} from this information appears to require solving the **Computational Diffie-Hellman (CDH) problem**, which is believed hard in well-chosen groups. The eavesdropper would need to either compute a discrete logarithm (find a from g^a) or find some other way to compute g^{ab} — and no efficient method is known.

The main vulnerability of basic DH is **man-in-the-middle attack**. An active attacker Mallory can intercept Alice's message, replace it with her own public value, and do the same to Bob. She ends up sharing one key with Alice and a different key with Bob, relaying (and reading) all messages between them. Neither Alice nor Bob detects the interception because basic DH provides no authentication — they have no way to verify whose public value they received. The solution is to **authenticate** the DH exchange, typically by having each party sign their DH public value with a long-term digital signature key (as in the TLS handshake) or by using certificates from a trusted authority.

Modern deployments predominantly use **Elliptic Curve Diffie-Hellman (ECDH)**, which performs the same protocol in an elliptic curve group rather than a multiplicative group modulo a prime. Elliptic curve groups resist the index calculus attacks that apply to modular arithmetic, so a 256-bit elliptic curve provides approximately the same security as a 3072-bit prime — dramatically smaller keys and faster computation. TLS 1.3, the protocol securing most web traffic, mandates ECDH (or its post-quantum successors) and has removed classical DH entirely. The conceptual contribution of Diffie and Hellman — that secure key agreement is possible over public channels — remains the intellectual foundation of internet security, even as the specific groups and parameters evolve.
