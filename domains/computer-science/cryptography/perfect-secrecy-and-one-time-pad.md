---
id: perfect-secrecy-and-one-time-pad
title: Perfect Secrecy and the One-Time Pad
domain: computer-science
course: cryptography
prerequisites:
- id: classical-ciphers-and-cryptanalysis
  type: hard
- id: discrete-random-variables
  type: hard
tags:
- perfect-secrecy
- one-time-pad
- shannon-theorem
- information-theoretic-security
stage: advanced
status: validated
---

# Perfect Secrecy and the One-Time Pad

## Core Idea
Shannon's definition of perfect secrecy requires that a ciphertext reveals absolutely nothing about the plaintext — formally, the posterior distribution over plaintexts given the ciphertext equals the prior. The one-time pad (XOR with a truly random key as long as the message) achieves this, but Shannon proved any perfectly secret scheme requires keys at least as long as messages. This impossibility result motivates computational security: since information-theoretic perfection demands impractical key lengths, modern cryptography settles for security against computationally bounded adversaries.

## Questions

```yaml
- question: "A colleague proposes using a one-time pad but reusing the same key for two different messages to save on key distribution. Why does this completely destroy the security guarantee?"
  type: short-answer
  answer: "If two messages m1 and m2 are encrypted with the same key k, the attacker can XOR the two ciphertexts: c1 XOR c2 = (m1 XOR k) XOR (m2 XOR k) = m1 XOR m2. The key cancels out, leaving the XOR of two plaintexts. With known plaintext statistics (letter frequencies, common words), the attacker can often recover both messages. Reuse converts the scheme from information-theoretically secure to trivially breakable."
  explanation: "The one-time pad's security depends entirely on each key bit being used exactly once. Reuse creates algebraic relationships between ciphertexts that eliminate the key from the equation. This was exploited in practice during the VENONA project, where Soviet intelligence reused one-time pad pages, allowing US cryptanalysts to decrypt thousands of messages over decades."

- question: "Shannon proved that any perfectly secret encryption scheme must have a key space at least as large as the message space. What is the intuitive reason this bound is tight?"
  type: multiple-choice
  options:
    - "Smaller key spaces mean the encryption algorithm runs faster, which attackers can exploit"
    - "If the key space is smaller than the message space, multiple messages must share a key, creating collisions that leak information"
    - "If the key space is smaller, some plaintexts produce the same ciphertext regardless of the key, so observing a ciphertext eliminates those plaintexts and changes the posterior"
    - "Shannon's proof relies on quantum mechanics, which limits key compression"
  answer: 2
  explanation: "With fewer keys than messages, the set of possible plaintexts consistent with a given ciphertext (the set {D_k(c) : k in K}) cannot cover the entire message space. Any plaintext outside this set has zero posterior probability given the ciphertext — the attacker knows it was not sent. This changes the posterior from the prior, violating perfect secrecy. The one-time pad achieves the bound exactly: each ciphertext is consistent with every possible plaintext of the same length, because for each (m, c) pair there exists exactly one key k = m XOR c."

- question: "Perfect secrecy means no adversary — regardless of computational power — can learn anything about the plaintext from the ciphertext."
  type: true-false
  answer: true
  explanation: "This is the defining strength of information-theoretic security: the guarantee holds against adversaries with unlimited computational resources, unlimited time, and arbitrary algorithms. No amount of computation changes the fact that every plaintext is equally consistent with the observed ciphertext. This contrasts with computational security, where the guarantee holds only against polynomially bounded adversaries. The tradeoff is that information-theoretic security demands impractically long keys."

- question: "A 256-bit AES key can encrypt terabytes of data securely, while a one-time pad key must be as long as the data. Why doesn't this contradict Shannon's theorem?"
  type: multiple-choice
  options:
    - "AES actually achieves perfect secrecy through a more efficient algorithm"
    - "Shannon's theorem only applies to substitution ciphers, and AES uses a different structure"
    - "AES does not achieve perfect secrecy — it achieves computational security, which is a weaker guarantee that holds only against bounded adversaries. Shannon's theorem says this tradeoff is unavoidable"
    - "AES keys are expanded internally to match the message length, satisfying Shannon's bound"
  answer: 2
  explanation: "Shannon's theorem is an impossibility result: perfect secrecy requires |K| >= |M|, period. AES sidesteps this by abandoning perfect secrecy in favor of computational security — no efficient algorithm can distinguish AES ciphertexts from random, but an adversary with unlimited computation could in principle break it. This is the foundational compromise of modern cryptography: accept a weaker (but still extremely strong) security guarantee in exchange for practical key sizes."

- question: "If you encrypt a 1000-bit message with a truly random 1000-bit one-time pad key, the mutual information between the plaintext and ciphertext is zero."
  type: true-false
  answer: true
  explanation: "Zero mutual information is equivalent to statistical independence between plaintext and ciphertext, which is equivalent to Shannon's definition of perfect secrecy. Observing the ciphertext provides literally no information about the plaintext — the posterior equals the prior. This is the strongest possible encryption guarantee and the formal content of 'the ciphertext reveals nothing.'"
```

## Explainer

After studying classical ciphers and their failures, a natural question arises: is it possible to build a cipher that is **provably** unbreakable, not just "hard to break with known techniques"? Claude Shannon answered this definitively in 1949. He defined **perfect secrecy**: an encryption scheme has perfect secrecy if, for every plaintext distribution, the ciphertext is statistically independent of the plaintext. Formally, Pr[M = m | C = c] = Pr[M = m] for all messages m and ciphertexts c. Observing the ciphertext gives the adversary zero additional information about which message was sent — no matter how much computational power they have.

The **one-time pad** achieves perfect secrecy. To encrypt a message, XOR each bit with the corresponding bit of a truly random key that is at least as long as the message and never reused. To decrypt, XOR the ciphertext with the same key. For any ciphertext c and any plaintext m of the same length, there exists exactly one key k = m XOR c that maps m to c. If the key is uniformly random, every plaintext is equally likely to have produced any given ciphertext. The scheme is simple, elegant, and provably unbreakable — but it has a devastating practical limitation.

Shannon proved that perfect secrecy **requires** the key to be at least as long as the message. The proof is clean: if the key space is smaller than the message space, then for some ciphertext c, the set of plaintexts reachable by decrypting c with all possible keys does not cover the full message space. Any plaintext outside this set has posterior probability zero — the adversary knows it was not sent, violating perfect secrecy. This means that to send a 1 GB file with perfect secrecy, you need a 1 GB key that was securely shared in advance and will never be reused. The key distribution problem is at least as hard as the original message delivery problem, making the one-time pad impractical for most applications.

This impossibility result is the intellectual foundation for all of modern cryptography. Since unconditional security demands impractical key lengths, the field pivots to **computational security**: schemes where breaking the encryption is not information-theoretically impossible but is computationally infeasible for any adversary running in reasonable (polynomial) time. A 256-bit AES key can encrypt terabytes of data not because it achieves perfect secrecy — Shannon's theorem says it cannot — but because no known efficient algorithm can distinguish AES output from random noise. The tradeoff is explicit: weaker theoretical guarantee (security against bounded adversaries rather than all adversaries) in exchange for practical key sizes. Every modern cipher lives in this tradeoff space, and understanding why perfect secrecy forces it is essential to understanding why computational assumptions pervade cryptographic design.
