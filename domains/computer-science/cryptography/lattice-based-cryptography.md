---
id: lattice-based-cryptography
title: Lattice-Based Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: computational-hardness-assumptions
  type: hard
- id: modular-arithmetic
  type: hard
tags:
- lattice
- svp
- sis
- worst-case-hardness
- post-quantum
stage: expert
status: validated
---

# Lattice-Based Cryptography

## Core Idea
A lattice is the set of all integer linear combinations of a set of basis vectors in R^n. Lattice problems — finding short vectors (SVP), finding close vectors (CVP) — are believed hard even for quantum computers. Lattice-based cryptography builds encryption, signatures, FHE, and more on the hardness of these problems. The key advantage over number-theoretic schemes is worst-case to average-case reductions (Ajtai 1996): breaking a random lattice instance is as hard as solving the worst case of standard lattice problems. This provides stronger theoretical foundations and quantum resistance, making lattices the basis for NIST's post-quantum standards (ML-KEM, ML-DSA).

## Questions

```yaml
- question: "Classical cryptography (RSA, DH) relies on average-case hardness assumptions that have no connection to worst-case complexity. Lattice cryptography has worst-case to average-case reductions. Why is this a significant theoretical advantage?"
  type: short-answer
  answer: "Average-case hardness means random instances are hard, but this is an assumption — it's possible that random instances are easy even if worst cases are hard. Lattice-based schemes have reductions showing that breaking a random lattice instance implies solving the worst case of lattice problems (like approximate SVP). Since worst-case hardness is a weaker assumption (some instances being hard is more plausible than random instances being hard), lattice-based schemes rest on firmer theoretical ground. If the worst case of SVP is hard, then the average case used in cryptography is also hard."
  explanation: "This is Ajtai's landmark 1996 result. For RSA, we assume random products of large primes are hard to factor, but this has no proven connection to worst-case factoring. For lattices, the reduction connects the two: a polynomial-time algorithm breaking the cryptographic scheme would yield a polynomial-time algorithm for the worst case of an established lattice problem. This is the strongest type of evidence for a cryptographic assumption."

- question: "The Shortest Vector Problem (SVP) asks for the shortest nonzero vector in a lattice. The best known algorithms for exact SVP run in time 2^{O(n)}, while the best approximation algorithms achieve factors of 2^{O(n log log n / log n)}. What does this imply for parameter selection in lattice crypto?"
  type: multiple-choice
  options:
    - "Lattice parameters must be larger than RSA parameters for equivalent security"
    - "The dimension n of the lattice is the primary security parameter. Since the best known attacks are exponential in n (no sub-exponential algorithm like GNFS for factoring), moderate dimensions (n = 512 to 1024) suffice for 128-bit security. This is more efficient than RSA (which needs 3072+ bits) because lattice problems scale better with the security parameter"
    - "Lattice crypto requires quantum computers for key generation"
    - "SVP difficulty means lattice schemes are unconditionally secure"
  answer: 1
  explanation: "The exponential scaling of lattice attacks (vs. sub-exponential for factoring) means that doubling the dimension roughly squares the attack cost. NIST's ML-KEM (Kyber) uses dimension n = 768 for 128-bit security, with key sizes around 1 KB — larger than ECC keys but smaller than RSA keys at equivalent security. The absence of any sub-exponential attack (classical or quantum) is why lattices are the primary candidate for post-quantum cryptography."

- question: "The Short Integer Solution (SIS) problem asks: given a random matrix A in Z_q^{n x m}, find a short nonzero vector x such that Ax = 0 mod q. This is the basis for lattice-based hash functions and signatures."
  type: true-false
  answer: true
  explanation: "SIS captures collision-resistance: finding two short vectors x1 != x2 with Ax1 = Ax2 mod q is equivalent to finding short x = x1 - x2 with Ax = 0. Ajtai showed that SIS is as hard as worst-case SVP (with appropriate parameters), giving lattice-based hash functions with provable collision resistance under worst-case assumptions. SIS underpins the hash-and-sign paradigm in lattice signatures and is a foundational problem alongside LWE."

- question: "All NIST post-quantum standards are based on lattice problems. Why did lattices dominate over code-based, multivariate, and isogeny-based alternatives?"
  type: multiple-choice
  options:
    - "Lattice problems are the only problems believed to be quantum-resistant"
    - "Lattices offer the best combination of: theoretical foundations (worst-case hardness), versatility (supporting encryption, signatures, FHE, ZK proofs), efficiency (moderate key sizes, fast operations), and maturity (decades of cryptanalysis). Code-based schemes have large keys, multivariate schemes have large signatures, and isogeny-based schemes were catastrophically broken (SIDH, 2022)"
    - "NIST mandated lattice-based algorithms for regulatory reasons"
    - "Lattice problems have been proven hard, unlike alternatives"
  answer: 1
  explanation: "The NIST competition evaluated candidates across multiple criteria. Lattice-based schemes (Kyber/ML-KEM for encryption, Dilithium/ML-DSA for signatures) offered the strongest overall package. Code-based encryption (Classic McEliece) has excellent security confidence but enormous keys. Multivariate signatures (SPHINCS+) are conservative but slow. SIKE (isogeny-based) was initially a finalist but was completely broken by Castryck-Decru in 2022. Lattices are not proven hard but have the most extensive cryptanalysis and the richest functionality."

- question: "A lattice in R^n is generated by a 'good' basis (short, nearly orthogonal vectors) or a 'bad' basis (long, nearly parallel vectors). Both generate the same lattice. Why is the gap between good and bad bases useful for cryptography?"
  type: short-answer
  answer: "The good basis is the trapdoor (private key) — it enables efficient operations like decryption (finding close lattice points, solving CVP). The bad basis is public — it specifies the lattice but makes these operations hard. Anyone can encode messages using the lattice structure, but only the holder of the good basis can decode them efficiently. This is the lattice analog of the factoring trapdoor in RSA: the public key (n = pq) defines the mathematical structure, but only knowledge of the factorization (p, q) enables efficient inversion."
  explanation: "Lattice basis reduction algorithms (LLL, BKZ) can improve a bad basis but not sufficiently to recover the good basis in polynomial time for high-dimensional lattices. The gap between polynomial-time achievable basis quality and the quality needed for decryption is the source of computational hardness. This gap narrows as dimension decreases, which is why lattice parameters must be large enough to prevent reduction algorithms from closing it."
```

## Explainer

A **lattice** is a regular, repeating grid of points in n-dimensional space, generated by integer linear combinations of a set of basis vectors. In 2D, think of a parallelogram tiling of the plane — every vertex is a lattice point. In high dimensions, lattices exhibit a remarkable property: fundamental geometric problems become computationally hard. The **Shortest Vector Problem (SVP)** asks for the shortest nonzero vector in the lattice. The **Closest Vector Problem (CVP)** asks for the lattice point nearest to a given target point. Both are believed to be exponentially hard in the lattice dimension, even for quantum computers — making lattices the primary foundation for post-quantum cryptography.

The theoretical strength of lattice-based cryptography comes from **worst-case to average-case reductions**, first established by Ajtai in 1996. He showed that if there exists any efficient algorithm that can solve a random instance of certain lattice problems, then there exists an efficient algorithm that can solve the worst case of SVP. This is dramatically stronger than the assumptions underlying RSA or Diffie-Hellman, which assume that random instances are hard without any connection to worst-case complexity. For lattice cryptography, "random instances are easy" implies "ALL instances are easy" — a much harder claim to believe, providing stronger evidence for the assumption's truth.

Two core problems underpin most constructions. **SIS (Short Integer Solution)** asks for a short vector in the kernel of a random matrix — finding such a vector is at least as hard as worst-case SVP. SIS gives collision-resistant hash functions and forms the basis of lattice signatures. **LWE (Learning with Errors)** asks to distinguish noisy inner products from random values — it is at least as hard as worst-case lattice problems and forms the basis of lattice encryption, key exchange, and FHE. Ring variants (Ring-SIS, Ring-LWE) use polynomial rings instead of general vectors, achieving comparable security with smaller keys and faster operations.

NIST selected lattice-based schemes as the primary post-quantum standards: **ML-KEM (Kyber)** for key encapsulation and **ML-DSA (Dilithium)** for digital signatures, both based on Module-LWE. Lattices won the competition not by being the only quantum-resistant option but by offering the best balance of security confidence (decades of cryptanalysis, worst-case reductions), performance (key sizes around 1-2 KB, fast operations), and versatility (the same mathematical framework supports encryption, signatures, FHE, zero-knowledge proofs, and advanced primitives like identity-based encryption). The transition from RSA/ECC to lattice-based cryptography is underway and represents the most significant change in deployed cryptographic infrastructure since the adoption of public-key cryptography in the 1990s.
