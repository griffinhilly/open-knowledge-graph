---
id: code-based-cryptography
title: Code-Based Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: post-quantum-cryptography
  type: hard
- id: computational-hardness-assumptions
  type: hard
tags:
- code-based
- post-quantum
- cryptography
- error-correcting-codes
stage: expert
status: validated
---

# Code-Based Cryptography

## Core Idea
Code-based cryptography constructs public-key encryption and signatures from error-correcting codes. The most famous is McEliece encryption, which hides a systematic error-correcting code as a random matrix. Encryption adds random errors; decryption uses the hidden code structure to correct errors and recover the message. Code-based schemes are post-quantum secure: no known polynomial-time quantum algorithms break them, and the underlying problem (syndrome decoding) is NP-hard. Challenges include large public keys and ciphertexts, but recent improvements (quasi-dyadic codes, rank metrics) reduce overhead. Code-based cryptography is standardized (NIST lattice-based competition) and increasingly deployed.

## How It's Best Learned
Start with a small code you can decode by hand, such as the [7,4] Hamming code. Encode a 4-bit message, flip one bit, and use the parity-check matrix to compute the syndrome and find the error. Then scramble the generator matrix with a random invertible matrix and a permutation, and notice that the scrambled matrix still encodes but no longer shows how to decode. That gap is the McEliece trapdoor.

## Common Misconceptions
- McEliece is secure because decoding every linear code is NP-hard. (NP-hardness is a worst-case statement about general codes. McEliece security also assumes that the scrambled public code looks like a random code and that typical instances are hard to decode.)
- Any error-correcting code works as the hidden code. (Some code families have been broken because their structure shows through the scrambled public key. Binary Goppa codes have resisted structural attacks in the original McEliece design.)
- Code-based schemes are a new idea built for the quantum era. (McEliece was proposed in the 1970s, long before quantum attacks drove interest in post-quantum cryptography.)
- Adding more random errors to the ciphertext makes McEliece safer. (The number of errors must stay within what the hidden code can correct. With too many errors, the legitimate receiver cannot decrypt either.)

## Questions

```yaml
- question: "Why is syndrome decoding hard, and how does this enable encryption?"
  type: short-answer
  answer: "Syndrome decoding is NP-hard: given a parity-check matrix H and syndrome s = H * e, recover the error vector e. This is hard for random codes because there are many possible error vectors. However, specific code structures (e.g., Goppa codes) have polynomial-time decoders. McEliece encryption hides a code with a known decoder: the private key is the code structure, the public key is a scrambled version of the parity-check matrix. Encryption adds random errors; the ciphertext is corrupted codeword + errors. Decoding requires the private code structure. An attacker sees only the scrambled matrix and must solve syndrome decoding (NP-hard)."
  explanation: "The security relies on hiding structure in a random-looking matrix, exploiting the hard average case (random codes) while maintaining easy worst-case (known codes)."

- question: "What is the main practical disadvantage of code-based cryptography compared to RSA?"
  type: multiple-choice
  options:
    - "Code-based schemes are slower to encrypt/decrypt"
    - "Code-based schemes have much larger public keys (kilobytes vs. bytes)"
    - "Code-based schemes are less secure than RSA"
    - "Code-based schemes do not provide digital signatures"
  answer: 1
  explanation: "McEliece public keys are several kilobytes, while RSA keys are typically 256-512 bytes. This large key size is the main obstacle to adoption. Recent improvements reduce key size, but code-based schemes remain bulkier than classical cryptosystems. Decryption/encryption time is comparable, and digital signature schemes exist (CFS signatures, though slower). The post-quantum advantage (resistance to quantum attacks) justifies the overhead for applications where quantum threats are real."

- question: "Why is code-based cryptography post-quantum secure?"
  type: true-false
  answer: true
  explanation: "The hardness of syndrome decoding (and the related Decoding Problem) has no known polynomial-time quantum algorithm. Grover's algorithm provides only quadratic speedup on brute-force search, which is insufficient to break the parameters used. Shor's algorithm (which breaks RSA, ECC) does not apply because syndrome decoding is not a hidden-structure problem like factoring/discrete log. This provides strong confidence (though not proof) that code-based schemes remain secure against quantum computers."
```

## Explainer

Code-based cryptography provides an alternative to number-theoretic assumptions (RSA, discrete log, elliptic curves). It is grounded in coding theory, with security reduced to the hardness of syndrome decoding. This geometric perspective on cryptography offers both theoretical and practical advantages.

**McEliece Cryptosystem**: (1) Privately choose an [n, k] error-correcting code with efficient decoder (e.g., Goppa code). (2) Compute parity-check matrix H. (3) Scramble H with invertible matrices to create public key H'. (4) Encryption: choose message m (k bits), compute ciphertext c = m * G' + e (where G' is generator from H', e is random error). (5) Decryption: use private code decoder to correct e and recover m.

Security: An attacker sees H' and ciphertexts c. To decrypt, must recover e from c and H' (syndrome decoding), which is NP-hard for random codes.

**Post-Quantum Security**: No known polynomial-time quantum algorithms solve syndrome decoding. Grover's algorithm provides only quadratic speedup (1/2 exponent reduction), insufficient to break parameters.

**Challenges**:
- Large public keys (kilobytes vs. RSA's hundreds of bytes).
- Large ciphertexts (overhead from error correction).
- Slow encryption/decryption (matrix-vector operations over finite fields).

**Optimizations**:
- Quasi-dyadic codes: structured codes reducing key size to kilobytes.
- Rank-metric codes: exploit rank over finite fields; smaller parameters.
- Hybrid schemes: combine code-based with other PQC for smaller keys.

Code-based cryptography is a leading post-quantum candidate, with implementations now available and potential for wider deployment as quantum computing approaches.
