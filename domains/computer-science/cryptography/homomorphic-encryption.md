---
id: homomorphic-encryption
title: Homomorphic Encryption
domain: computer-science
course: cryptography
prerequisites:
- id: lattice-based-cryptography
  type: hard
- id: learning-with-errors
  type: hard
- id: computational-hardness-assumptions
  type: soft
tags:
- fhe
- homomorphic
- bootstrapping
- noise-management
- gentry
stage: expert
status: validated
---

# Homomorphic Encryption

## Core Idea
Homomorphic encryption (HE) allows computation on encrypted data without decrypting it. Partially homomorphic schemes support one operation (RSA: multiplication; Paillier: addition). Fully homomorphic encryption (FHE), first achieved by Gentry (2009), supports arbitrary computations — both addition and multiplication, and therefore any circuit. The key technique is bootstrapping: using the scheme to homomorphically evaluate its own decryption circuit, refreshing noisy ciphertexts. Modern FHE schemes (BGV, BFV, CKKS, TFHE) are based on lattice problems (LWE/RLWE) and are ~10,000x slower than plaintext computation, but improving rapidly. Applications include private cloud computation, encrypted machine learning, and private database queries.

## Questions

```yaml
- question: "In lattice-based HE, each ciphertext carries a 'noise' term that grows with each operation. What happens if the noise exceeds a threshold, and how does bootstrapping solve this?"
  type: short-answer
  answer: "If noise exceeds the threshold, decryption fails — the noisy ciphertext no longer decodes to the correct plaintext. Addition increases noise linearly; multiplication increases it quadratically (multiplying errors). After enough operations, the noise budget is exhausted. Bootstrapping solves this by homomorphically evaluating the decryption circuit: encrypt the secret key, feed the noisy ciphertext and encrypted key into a homomorphic decryption, producing a fresh ciphertext with reset noise. This requires the scheme to evaluate its own decryption circuit, which Gentry showed is achievable using 'squashing' and modular arithmetic tricks."
  explanation: "Bootstrapping is the conceptual breakthrough of FHE. Without it, you can only perform a limited number of operations (leveled HE). With it, you can evaluate arbitrary circuits by periodically refreshing ciphertexts. The cost is significant: bootstrapping is the most expensive operation, often taking seconds per gate. Optimizing bootstrapping speed is the central challenge in practical FHE research."

- question: "RSA is multiplicatively homomorphic: E(m1) * E(m2) = E(m1 * m2). Why doesn't this make RSA a useful homomorphic encryption scheme?"
  type: multiple-choice
  options:
    - "RSA multiplication is too slow for practical use"
    - "RSA supports only multiplication, not addition. Without both operations, you cannot compute arbitrary functions — you're limited to multiplication chains. Fully homomorphic encryption requires both addition and multiplication (since any Boolean circuit can be built from AND and XOR/OR). Additionally, textbook RSA lacks semantic security, making even its multiplicative homomorphism a vulnerability rather than a feature"
    - "RSA's homomorphic property only works for prime plaintexts"
    - "The homomorphic property disappears when RSA uses padding"
  answer: 1
  explanation: "Partially homomorphic schemes (RSA for multiplication, Paillier for addition, ElGamal for multiplication) each support one operation. The 30-year quest for FHE sought a scheme supporting both, because addition + multiplication computes any function (any Boolean circuit can be expressed as arithmetic operations). Gentry's 2009 construction finally achieved this using ideal lattices. The observation that RSA's multiplicative homomorphism is actually a textbook RSA vulnerability (enabling chosen-ciphertext attacks) highlights the tension between homomorphic properties and standard encryption security."

- question: "CKKS is an HE scheme designed for approximate arithmetic on real numbers. Unlike BFV/BGV (which compute on integers exactly), CKKS treats the noise as part of the computation, allowing some precision loss. Why is this useful?"
  type: multiple-choice
  options:
    - "CKKS is faster because it uses smaller parameters"
    - "Machine learning and statistical computations inherently involve floating-point approximations. CKKS encodes real numbers and performs additions and multiplications that preserve values up to a controllable precision, matching the natural error tolerance of these applications. Exact schemes waste resources maintaining precision that the application doesn't need"
    - "CKKS provides stronger security guarantees than exact schemes"
    - "CKKS supports division while exact schemes do not"
  answer: 1
  explanation: "CKKS is tailored for machine learning inference, statistical analysis, and scientific computation — domains where results with 10-15 decimal digits of precision are perfectly acceptable. By embracing approximate arithmetic, CKKS can encode real numbers directly (rather than mapping them to integers), pack multiple values into one ciphertext via SIMD-style batching, and treat unavoidable noise as rounding error rather than a correctness failure. This makes it significantly more practical for applications like encrypted neural network inference."

- question: "FHE allows a cloud server to compute on encrypted data without learning anything about the data or the result. The client sends encrypted inputs and receives an encrypted result."
  type: true-false
  answer: true
  explanation: "This is the canonical FHE use case. The client encrypts their data, sends it to the cloud, and the cloud evaluates a function homomorphically — each operation on ciphertexts corresponds to the same operation on the underlying plaintexts. The cloud sees only ciphertexts throughout and returns an encrypted result that only the client can decrypt. The cloud learns nothing about the data, the intermediate values, or the final result. This enables outsourced computation with full privacy."

- question: "Current FHE schemes are roughly 10,000-1,000,000x slower than computing on plaintext. What is the main source of this overhead?"
  type: short-answer
  answer: "The primary overhead comes from operating on large mathematical objects rather than native machine integers. LWE/RLWE ciphertexts are polynomials with coefficients in large moduli, and each homomorphic operation involves polynomial multiplication, modular reduction, and noise management. Bootstrapping (refreshing noise) is particularly expensive, involving homomorphic evaluation of the decryption circuit. Ciphertexts are also much larger than plaintexts (thousands of bits per encrypted bit), creating memory bandwidth bottlenecks. Hardware acceleration (GPU, FPGA, ASIC) and algorithmic improvements are steadily reducing this gap."
  explanation: "The overhead is inherent to the approach: computing on encrypted data requires working in a larger algebraic structure that encodes both the data and the encryption. Each plaintext bit becomes a polynomial ring element, and each logical operation becomes polynomial arithmetic. The 10,000x figure is for optimized implementations of specific applications (like neural network inference); unoptimized or complex computations can be much worse. The trajectory is improving: 2009 FHE was millions of times slower; practical applications are now emerging for specific use cases."
```

## Explainer

**Homomorphic encryption (HE)** is the holy grail of encrypted computation: perform arbitrary computations on encrypted data without ever decrypting it. The cloud sees only ciphertexts, performs operations that correspond to additions and multiplications on the underlying plaintexts, and returns an encrypted result that only the data owner can decrypt. The cloud learns nothing — not the inputs, not the intermediate values, not the output. This enables private cloud computing, encrypted machine learning inference, and secure data analysis without trusting the compute provider.

The distinction between partial and full homomorphism is critical. **Partially homomorphic** schemes have existed for decades: RSA supports multiplication (E(a) * E(b) = E(ab)), Paillier supports addition (E(a) * E(b) = E(a+b)), and ElGamal supports multiplication. But supporting only one operation limits the computable functions to linear combinations (Paillier) or monomial products (RSA). **Fully homomorphic encryption (FHE)** supports both addition and multiplication, which is sufficient for any computation (since AND and XOR form a complete Boolean basis, and these correspond to multiplication and addition modulo 2).

Craig Gentry achieved the first FHE construction in 2009, solving a problem open since Rivest, Adleman, and Dertouzos posed it in 1978. The central challenge is **noise growth**: lattice-based ciphertexts carry a small error term that grows with each operation. Addition increases noise linearly, multiplication quadratically. After enough operations, the noise exceeds the decryption threshold and the ciphertext becomes garbled. Gentry's breakthrough was **bootstrapping**: homomorphically evaluating the scheme's own decryption circuit to "refresh" a noisy ciphertext into a fresh one with reduced noise. This requires the scheme to be powerful enough to compute its own decryption (a somewhat circular requirement that Gentry resolved using a technique called squashing). Bootstrapping converts a **leveled** HE scheme (supporting a fixed number of operations) into a fully homomorphic one (supporting arbitrary computations).

Modern FHE schemes — BGV, BFV, CKKS, and TFHE — are based on the **Learning with Errors (LWE)** and **Ring-LWE** problems, providing security believed to resist quantum attacks. BGV and BFV compute exact integer arithmetic (useful for database queries, financial computations). CKKS computes approximate real-number arithmetic (useful for machine learning, where small precision loss is acceptable). TFHE evaluates Boolean circuits gate by gate with fast bootstrapping (useful for arbitrary computations). Performance remains the main barrier: current FHE is roughly 10,000x slower than plaintext computation for optimized applications, with ciphertexts thousands of times larger than plaintexts. But the field is improving rapidly — hardware accelerators, better algorithms, and application-specific optimizations are making practical deployment feasible for specific use cases like encrypted inference, private set intersection, and confidential analytics.
