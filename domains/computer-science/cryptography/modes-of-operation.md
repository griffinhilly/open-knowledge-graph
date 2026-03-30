---
id: modes-of-operation
title: 'Modes of Operation: CBC, CTR, and GCM'
domain: computer-science
course: cryptography
prerequisites:
- id: symmetric-encryption-block-ciphers
  type: hard
tags:
- cbc
- ctr
- gcm
- initialization-vector
- nonce
- chosen-plaintext-security
stage: advanced
status: validated
---

# Modes of Operation: CBC, CTR, and GCM

## Core Idea
A block cipher encrypts one fixed-size block deterministically. Modes of operation extend it to arbitrary-length messages while achieving semantic security (identical plaintexts produce different ciphertexts). ECB fails this by encrypting blocks independently. CBC chains blocks via XOR with the previous ciphertext (requiring a random IV). CTR turns the block cipher into a stream cipher by encrypting sequential counter values. GCM combines CTR encryption with a polynomial MAC for authenticated encryption. Each mode has distinct properties regarding parallelism, error propagation, and the consequences of nonce/IV misuse.

## Questions

```yaml
- question: "ECB mode encrypts each block independently with the same key. A developer argues this is fine because AES itself is secure. What specific attack demonstrates ECB's failure?"
  type: short-answer
  answer: "Identical plaintext blocks produce identical ciphertext blocks, leaking structural patterns. The classic demonstration is the ECB penguin: encrypting a bitmap image in ECB mode preserves the visual structure because regions of identical pixel blocks produce identical ciphertext blocks. The image is recognizable despite encryption. This violates semantic security — an adversary can distinguish encryptions of different messages by checking for repeated blocks."
  explanation: "ECB fails because semantic security requires that an adversary cannot tell which of two messages was encrypted, even when choosing the messages. With ECB, the adversary submits two messages — one with repeated blocks, one without — and checks for repeated ciphertext blocks. This works regardless of how strong the underlying block cipher is. The mode, not the cipher, is the vulnerability."

- question: "In CBC mode, a single-bit error in ciphertext block i affects which plaintext blocks after decryption?"
  type: multiple-choice
  options:
    - "Only block i is affected"
    - "Block i is completely garbled, and block i+1 has a single-bit flip in the same position as the ciphertext error; all other blocks decrypt correctly"
    - "All blocks from i onward are garbled"
    - "No blocks are affected because the error-correcting properties of AES fix it"
  answer: 1
  explanation: "In CBC decryption, plaintext block i = D_k(c_i) XOR c_{i-1}. A bit error in c_i causes D_k(c_i) to produce a completely different (garbled) output for block i. But c_i also feeds into block i+1's decryption as the XOR mask: p_{i+1} = D_k(c_{i+1}) XOR c_i. The single-bit error in c_i causes a single-bit flip in p_{i+1}. Blocks i+2 onward are unaffected because their decryption depends on c_{i+1} (which is uncorrupted) and later blocks. This error propagation pattern is limited but shows CBC has no integrity protection — bit-flip attacks on block i+1 are possible."

- question: "CTR mode turns a block cipher into a stream cipher by encrypting counter values and XORing the result with plaintext. Reusing the same nonce with the same key for two different messages is equivalent to reusing a one-time pad."
  type: true-false
  answer: true
  explanation: "With the same key and nonce, CTR mode generates the same keystream for both messages. XORing the two ciphertexts cancels the keystream, yielding the XOR of the two plaintexts — exactly the same vulnerability as one-time pad reuse. The attacker can then use known-plaintext techniques to recover both messages. This is why nonce uniqueness is critical in CTR mode: a single nonce repetition completely breaks confidentiality for the affected messages."

- question: "GCM mode provides both encryption and authentication. Why is combining these in a single mode preferable to encrypting with CTR and then computing a separate MAC?"
  type: multiple-choice
  options:
    - "GCM is faster because it skips the authentication step for most blocks"
    - "Composing CTR encryption with a separate MAC can be insecure depending on the order of operations (encrypt-then-MAC is secure, MAC-then-encrypt has known vulnerabilities). GCM is a single, analyzed construction that provides authenticated encryption correctly by design"
    - "Separate MACs cannot authenticate encrypted data — they can only authenticate plaintext"
    - "GCM uses stronger encryption than CTR mode"
  answer: 1
  explanation: "The composition order matters critically. Encrypt-then-MAC (compute MAC over ciphertext) is the secure generic composition. MAC-then-encrypt (MAC the plaintext, then encrypt both) has led to real attacks like padding oracles in TLS (the BEAST and Lucky 13 attacks). Encrypt-and-MAC (encrypt plaintext, MAC plaintext separately) can leak plaintext information through the MAC. GCM avoids these pitfalls as an integrated authenticated encryption with associated data (AEAD) scheme, providing confidentiality, integrity, and authenticity with a single key and nonce."

- question: "CTR mode is fully parallelizable for both encryption and decryption, while CBC mode is parallelizable only for decryption."
  type: true-false
  answer: true
  explanation: "In CTR, each ciphertext block is computed as E_k(nonce || counter_i) XOR p_i — each block's encryption is independent, enabling full parallelism. In CBC encryption, c_i = E_k(p_i XOR c_{i-1}), so each block depends on the previous ciphertext — encryption is inherently sequential. However, CBC decryption is parallelizable: p_i = D_k(c_i) XOR c_{i-1}, where all D_k(c_i) computations are independent. This parallelism advantage is one reason CTR mode (and GCM, which uses CTR) is preferred in high-throughput applications."
```

## Explainer

A block cipher like AES is a **primitive** — it securely encrypts exactly one 128-bit block. Real messages are longer than 128 bits, and encrypting each block independently (ECB mode) leaks catastrophic information: identical plaintext blocks produce identical ciphertext blocks, preserving patterns visible to any observer. **Modes of operation** solve this by introducing randomness or state that ensures identical plaintexts produce different ciphertexts, achieving **semantic security** (formally, IND-CPA: indistinguishability under chosen-plaintext attack).

**CBC (Cipher Block Chaining)** XORs each plaintext block with the previous ciphertext block before encryption: c_i = E_k(p_i XOR c_{i-1}), with c_0 being a random initialization vector (IV). This chaining means identical plaintext blocks in different positions (or under different IVs) produce different ciphertexts. CBC is sequential for encryption (each block depends on the previous ciphertext) but parallelizable for decryption. Its main vulnerability is sensitivity to IV handling — a predictable IV enables chosen-plaintext attacks (as exploited in the BEAST attack on TLS). CBC also provides no integrity protection: an attacker can flip specific bits in the decrypted plaintext by manipulating ciphertext blocks.

**CTR (Counter) mode** takes a different approach: it turns the block cipher into a **stream cipher** by encrypting a sequence of counter values (nonce || 0, nonce || 1, nonce || 2, ...) to produce a keystream, then XORs the keystream with the plaintext. Both encryption and decryption are fully parallelizable since each block's keystream segment is computed independently. Random access is possible — you can decrypt block i without processing blocks 0 through i-1. The critical requirement is **nonce uniqueness**: reusing a nonce with the same key generates the same keystream, reducing security to XOR of two plaintexts (identical to one-time pad reuse).

**GCM (Galois/Counter Mode)** combines CTR-mode encryption with a polynomial-based authentication tag computed over the ciphertext and any associated data (like packet headers that must be authenticated but not encrypted). GCM is an **AEAD** (Authenticated Encryption with Associated Data) scheme: it guarantees confidentiality, integrity, and authenticity in a single pass. The authentication uses multiplication in a Galois field (GF(2^128)), which is fast in hardware. GCM is the dominant mode in modern protocols (TLS 1.3, IPsec) because it provides the complete security package — encryption plus tamper detection — without requiring users to correctly compose separate encryption and MAC primitives, a task that has historically produced vulnerabilities when done incorrectly.
