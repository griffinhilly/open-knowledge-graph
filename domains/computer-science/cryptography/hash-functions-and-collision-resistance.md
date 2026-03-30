---
id: hash-functions-and-collision-resistance
title: Hash Functions and Collision Resistance
domain: computer-science
course: cryptography
prerequisites:
- id: symmetric-encryption-block-ciphers
  type: hard
- id: complexity-class-p-definition
  type: soft
tags:
- hash-function
- collision-resistance
- preimage-resistance
- sha-256
- merkle-damgard
- birthday-attack
stage: advanced
status: validated
---

# Hash Functions and Collision Resistance

## Core Idea
A cryptographic hash function maps arbitrary-length inputs to fixed-length outputs and must satisfy three security properties: preimage resistance (given h, hard to find m with H(m) = h), second-preimage resistance (given m, hard to find m' != m with H(m) = H(m')), and collision resistance (hard to find any pair m != m' with H(m) = H(m')). Collision resistance is the strongest property and is limited by the birthday bound — O(2^{n/2}) for an n-bit hash. SHA-256 (256-bit output, birthday bound 2^128) is the current standard. Hash functions are foundational building blocks for MACs, digital signatures, commitment schemes, and proof-of-work systems.

## Questions

```yaml
- question: "A hash function produces 128-bit outputs. An attacker wants to find a collision. Approximately how many random inputs must they hash before expecting a collision, and what principle explains this?"
  type: short-answer
  answer: "Approximately 2^64 inputs, by the birthday paradox. In a set of n randomly chosen hash outputs from a space of 2^128 values, the probability of at least one collision exceeds 50% when n is roughly 2^{128/2} = 2^64. This is analogous to the birthday problem: in a room of 23 people, there's a >50% chance two share a birthday, despite 365 possible birthdays. The birthday bound means collision resistance is at most half the output length in bits of security."
  explanation: "The birthday bound is fundamental to hash function design. A 128-bit hash provides only 64 bits of collision resistance — potentially feasible for well-resourced attackers. This is why modern hash functions use 256-bit or larger outputs: SHA-256 provides 128 bits of collision resistance, which is currently considered secure. The birthday attack requires no cryptanalytic insight — it works against any hash function purely from output length."

- question: "Collision resistance implies second-preimage resistance, but second-preimage resistance does not imply collision resistance."
  type: true-false
  answer: true
  explanation: "If you can find second preimages efficiently (given m, find m' with H(m) = H(m')), you can find collisions — just pick any m and find its second preimage. So collision resistance implies second-preimage resistance. The reverse fails: a collision attacker gets to choose both messages freely, which is strictly more power than being given one message and searching for a match. The birthday attack finds collisions in O(2^{n/2}) time, while the best generic second-preimage attack requires O(2^n) time. A function could resist second preimages but fall to birthday-bound collision attacks."

- question: "A developer uses MD5 to hash passwords, arguing that while MD5 collisions have been found, preimage attacks are still infeasible. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "MD5 preimage attacks are actually practical and passwords can be directly recovered"
    - "Password hashing requires collision resistance, not preimage resistance, so MD5's broken collision resistance is the relevant vulnerability"
    - "While MD5's preimage resistance is not fully broken, password hashing has additional requirements (slowness, salting) that MD5 does not satisfy. MD5 is fast by design, enabling rapid brute-force and dictionary attacks. Dedicated password hashing functions like bcrypt or Argon2 are needed"
    - "MD5 is fine for password hashing as long as the passwords are longer than 128 bits"
  answer: 2
  explanation: "The reasoning conflates cryptographic hash security properties with password hashing requirements. Even a hash with perfect preimage resistance is unsuitable for passwords if it's fast — the attacker's strategy is not to invert the hash mathematically but to hash billions of candidate passwords per second and compare. Password hashing functions deliberately incorporate tunable slowness (key stretching), memory hardness, and salting. Using MD5 or SHA-256 directly for passwords is a design error independent of collision attacks."

- question: "The Merkle-Damgard construction builds a hash function from a fixed-size compression function. What structural vulnerability does it introduce that newer constructions like SHA-3 (sponge) avoid?"
  type: multiple-choice
  options:
    - "Merkle-Damgard hashes are vulnerable to timing attacks because they process blocks sequentially"
    - "Length extension attacks: knowing H(m) and |m| allows computing H(m || padding || m') without knowing m, because the hash output is the internal state after processing m"
    - "Merkle-Damgard cannot process messages longer than 2^64 bits"
    - "The compression function must be collision-resistant, but SHA-3's sponge construction does not need a compression function at all"
  answer: 1
  explanation: "In Merkle-Damgard, the final hash value IS the internal state. An attacker who knows H(m) can continue the computation by feeding additional blocks, computing H(m || pad || m') without knowing m. This enables signature forgery on schemes that MAC as H(key || message). SHA-3's sponge construction avoids this by using a capacity portion of the state that is never output, so the hash value does not reveal the full internal state. HMAC also works around this by using a nested hash construction."

- question: "SHA-256 always produces a 256-bit output regardless of whether the input is 1 byte or 1 terabyte."
  type: true-false
  answer: true
  explanation: "Fixed-length output from arbitrary-length input is a defining property of hash functions. SHA-256 always outputs exactly 256 bits (32 bytes). This compression from an infinite input domain to a finite output domain means collisions must exist (by the pigeonhole principle) — the security guarantee is that finding them is computationally infeasible, not that they don't exist."
```

## Explainer

A **cryptographic hash function** H takes an input of any length and produces a fixed-length output (the hash or digest). SHA-256, the current workhorse, produces 256-bit digests. Unlike encryption, hashing is a one-way operation with no key and no decryption — the same input always produces the same output, and the goal is to make it infeasible to work backward from output to input. Hash functions serve as the cryptographic equivalent of fingerprints: a compact, deterministic summary that is practically impossible to forge.

Three security properties define a good cryptographic hash. **Preimage resistance** means that given a hash value h, it is infeasible to find any message m such that H(m) = h. **Second-preimage resistance** means that given a message m, it is infeasible to find a different message m' with H(m') = H(m). **Collision resistance** means it is infeasible to find any pair of distinct messages m, m' with H(m) = H(m'). Collision resistance is the strongest property and implies second-preimage resistance (but not vice versa). The generic attack cost for collisions is determined by the **birthday bound**: approximately 2^{n/2} hash evaluations for an n-bit hash, because random collisions among 2^{n/2} values are expected by the birthday paradox.

Most deployed hash functions use the **Merkle-Damgard** construction, which processes a message in fixed-size blocks using a compression function. An initial value (IV) is updated by absorbing each block through the compression function, and the final state becomes the hash. This is elegant and provably collision-resistant if the compression function is — but it introduces **length extension vulnerabilities**: since the output is the full internal state, an attacker who knows H(m) can continue the computation without knowing m, computing H(m || padding || extra) directly. SHA-3 uses the **sponge construction** instead, which maintains a larger internal state than the output, preventing this attack by design.

Hash functions are ubiquitous in cryptography and systems. They underpin **HMAC** (hash-based message authentication), **digital signatures** (sign the hash of a message rather than the full message), **commitment schemes** (commit to a value by publishing its hash), **proof of work** (Bitcoin mining finds inputs whose hash starts with many zeros), and **data integrity** (verify file downloads match expected hashes). Their security is entirely computational — collisions exist by the pigeonhole principle (infinite inputs, finite outputs), but finding them should require brute-force effort proportional to the birthday bound. When this guarantee breaks, as happened with MD5 (practical collision attacks found in 2004) and SHA-1 (collision demonstrated in 2017), the hash function must be retired from security-critical applications.
