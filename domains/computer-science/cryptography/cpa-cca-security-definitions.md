---
id: cpa-cca-security-definitions
title: "Security Definitions for Encryption: Indistinguishability, CPA, and CCA"
domain: computer-science
course: cryptography
prerequisites:
- id: perfect-secrecy-and-one-time-pad
  type: hard
- id: symmetric-encryption-block-ciphers
  type: hard
- id: pseudorandom-functions
  type: soft
builds-toward:
- modes-of-operation
- authenticated-encryption
tags:
- provable-security
- indistinguishability
- IND-CPA
- IND-CCA
- security-games
- negligible-functions
- malleability
stage: advanced
status: validated
---
# Security Definitions for Encryption: Indistinguishability, CPA, and CCA

## Core Idea
Modern cryptography defines security precisely, as a game between a challenger and an efficient adversary. In the indistinguishability game, the adversary picks two messages of equal length, receives the encryption of one chosen at random, and must guess which one it was. A scheme is secure if no efficient adversary guesses correctly with probability noticeably better than 1/2. The definitions differ in what the adversary may do: an eavesdropper only sees the challenge, a chosen-plaintext attacker (CPA) can also obtain encryptions of messages of its choice, and a chosen-ciphertext attacker (CCA) can also obtain decryptions of ciphertexts other than the challenge.

## How It's Best Learned
Follow the presentation in Katz and Lindell's *Introduction to Modern Cryptography*: write each game out step by step, then break simple schemes against it. Show that any deterministic scheme fails CPA security with a single oracle query, and that a malleable scheme such as counter mode fails CCA security by flipping one bit. Map each definition to a realistic threat, such as an attacker who can get a server to encrypt chosen data, or one who can observe how a server reacts to tampered ciphertexts.

## Common Misconceptions
- A scheme is secure if the key cannot be recovered. (A scheme can leak information about messages, or let ciphertexts be altered usefully, without revealing the key; the definitions target the messages, not just the key.)
- Encrypting the same message twice should give the same ciphertext. (Under CPA security, it must not, with overwhelming probability; otherwise an attacker learns when messages repeat. Secure schemes are randomized or stateful.)
- CPA security is enough for encrypted network traffic. (Active attackers can modify ciphertexts and watch the receiver's reaction, as in padding-oracle attacks; protection needs CCA security, usually achieved with authenticated encryption.)

## Questions

```yaml
- question: "Why can no deterministic encryption scheme (one where Enc(k, m) always gives the same output for the same k and m) be CPA-secure?"
  type: multiple-choice
  options:
    - "Deterministic schemes always use keys that are too short"
    - "The adversary can query the encryption oracle on m0, then compare the result with the challenge ciphertext to learn which message was encrypted"
    - "Deterministic schemes cannot be decrypted"
    - "The CPA game forbids the adversary from choosing messages"
  answer: 1
  explanation: "In the CPA game the adversary may request encryptions of any messages, including m0 itself. With a deterministic scheme, the challenge equals Enc(k, m0) exactly when b = 0, so the adversary wins with probability 1. CPA-secure schemes must therefore be randomized, for example by using a fresh random IV or nonce, or be stateful."

- question: "In the CCA indistinguishability game, which request is the adversary forbidden to make after receiving the challenge ciphertext c*?"
  type: multiple-choice
  options:
    - "Encryption of m0"
    - "Decryption of any ciphertext"
    - "Decryption of c* itself"
    - "Encryption of any message longer than m0"
  answer: 2
  explanation: "Decrypting c* would trivially reveal the answer, so that single query is excluded. Every other decryption query is allowed, including ciphertexts that differ from c* in one bit. That is what makes CCA security strong enough to rule out attacks based on tampering."

- question: "Counter (CTR) mode with a random initial counter, built from a secure pseudorandom function, is CCA-secure."
  type: true-false
  answer: false
  explanation: "CTR mode is CPA-secure but malleable: flipping a bit of the ciphertext flips the same bit of the decrypted plaintext. In the CCA game the adversary flips one bit of c*, asks for the decryption of the modified ciphertext (allowed, since it differs from c*), flips the bit back, and learns which message was encrypted."

- question: "In these definitions, what does it mean that an adversary's advantage is negligible, and why is the comparison made against probability 1/2?"
  type: short-answer
  answer: "Random guessing already identifies the encrypted message with probability 1/2, so security means no efficient (polynomial-time) adversary can do meaningfully better. Formally, its success probability is at most 1/2 + negl(n), where negl(n) shrinks faster than 1/p(n) for every polynomial p as the security parameter n grows."
  explanation: "Allowing a negligible advantage, instead of requiring exactly 1/2, is what makes computational security achievable with keys much shorter than the messages, unlike perfect secrecy."
```

## Explainer

Perfect secrecy, achieved by the one-time pad, demands that a ciphertext reveal nothing about the message even to an attacker with unlimited computing power. Shannon showed this requires a key at least as long as the message, which is impractical. Modern cryptography relaxes the goal in two ways. It considers only **efficient** adversaries, those running in time polynomial in a security parameter n. And it allows them a **negligible** chance of success beyond guessing, a probability that shrinks faster than any inverse polynomial in n.

The goal is then written as a **game**. In the basic indistinguishability experiment, a key k is generated. The adversary chooses two messages m0 and m1 of the same length. The challenger flips a fair coin b, encrypts m_b, and hands back the challenge ciphertext c*. The adversary outputs a guess b'. The scheme is secure if every efficient adversary has Pr[b' = b] ≤ 1/2 + negl(n). This captures a strong intuition. If an attacker cannot even tell which of two messages of its own choosing was encrypted, it cannot learn any partial information about real messages. Goldwasser and Micali formalized this idea, along with the equivalent notion of semantic security, in the early 1980s.

The basic game models a passive eavesdropper. **Chosen-plaintext attack (CPA) security** gives the adversary an encryption oracle: it may ask for encryptions of any messages, before and after seeing c*. This models attackers who can influence what gets encrypted. One consequence surprises many students: no deterministic scheme can be CPA-secure. The adversary simply asks for the encryption of m0 and compares. CPA-secure schemes must be randomized, which is why modes such as CBC and CTR use a fresh random IV or nonce for each message.

**Chosen-ciphertext attack (CCA) security** also gives the adversary a decryption oracle, usable on any ciphertext except c* itself. This models attackers who can send modified ciphertexts to a server and observe the results. Real attacks fit this model. Padding-oracle attacks, described by Serge Vaudenay in 2002, recover plaintexts from CBC encryption by learning whether the server reports a padding error. Malleable schemes such as CTR mode fail CCA security outright, since flipping a ciphertext bit flips the matching plaintext bit.

Achieving CCA security in practice usually means **authenticated encryption**. Encrypting with a CPA-secure scheme and then applying a strongly secure MAC to the ciphertext (encrypt-then-MAC) yields a CCA-secure scheme. Tampered ciphertexts are rejected before decryption, so the decryption oracle gives the attacker nothing useful.
