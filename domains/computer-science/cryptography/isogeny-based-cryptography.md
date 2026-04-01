---
id: isogeny-based-cryptography
title: Isogeny-Based Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: elliptic-curve-cryptography-basics
  type: hard
- id: post-quantum-cryptography
  type: hard
tags:
- isogeny
- post-quantum
- elliptic-curves
- cryptography
stage: expert
status: validated
---

# Isogeny-Based Cryptography

## Core Idea
Isogeny-based cryptography uses the structure of isogenies (maps) between elliptic curves to build post-quantum public-key cryptosystems. Unlike lattice or code-based cryptography, isogeny schemes are based on algebraic geometry. The most developed scheme is SIKE/CSIDH, which constructs encryption by finding a path of isogenies through a graph of elliptic curves. Security relies on the hardness of the endomorphism ring computation problem, which has no known polynomial-time classical OR quantum algorithms. Isogeny schemes offer small keys and ciphertexts (advantages over lattices/codes), though key generation is slow. NIST selected SIKE as a finalist in the post-quantum cryptography standardization process.

## Questions

```yaml
- question: "What is an isogeny, and why is computing endomorphism rings hard?"
  type: short-answer
  answer: "An isogeny is a morphism between elliptic curves preserving group structure. The endomorphism ring of an elliptic curve is the set of isogenies from the curve to itself. Computing endomorphism rings is hard because it requires finding lattice structures in very high-dimensional spaces (typically dimension 1000+). No polynomial-time algorithm is known for classical or quantum computers. This hardness is the cryptographic foundation: in SIKE/CSIDH, the private key encodes endomorphisms, the public key is the isogenized curve, and computing the private key from the public key requires solving the endomorphism ring problem."
  explanation: "Isogeny-based cryptography exploits a different hard problem than lattices or codes, providing diversity in post-quantum assumptions."

- question: "Isogeny-based schemes have smaller keys/ciphertexts than lattice-based, but key generation is slow. Why?"
  type: true-false
  answer: true
  explanation: "Isogenies over elliptic curves are very structured objects. Computing them requires careful algebraic geometry (e.g., computing Hilbert class polynomials). This computational overhead during key generation is unavoidable. The trade-off is: small, elegant parameters (suitable for embedded devices, bandwidth-constrained networks) at the cost of slow key generation. For applications where keys are reused or generated infrequently, this trade-off is acceptable."
```

## Explainer

Isogeny-based cryptography is a geometric approach to post-quantum cryptography, leveraging the deep structure of elliptic curves and isogenies. Unlike lattice-based cryptography (linear algebra) or code-based (coding theory), isogeny schemes use algebraic geometry.

**CSIDH/SIKE**: The main constructions. Both work in a graph of elliptic curves, where vertices are curves and edges are isogenies. A secret path through the graph encodes a private key; the public key is the destination curve. To compute the private key from the public key requires finding the secret path, equivalent to the endomorphism ring computation problem.

**Hardness**: The hardness of isogeny-based schemes rests on:
1. Endomorphism Ring Computation: Given an elliptic curve, compute its endomorphism ring (hard).
2. Path Finding: Given start and end vertices in the isogeny graph, find the path (hard on random graphs).

Both are believed hard for classical and quantum computers.

**Advantages**:
- Small keys: ~100-200 bytes (vs. lattice ~1-2 KB, codes ~1-2 KB).
- Small ciphertexts: ~200-500 bytes.
- Elegant mathematical structure.

**Disadvantages**:
- Slow key generation (seconds to minutes on modern hardware).
- Limited implementation experience.
- Recent attacks found vulnerabilities in some schemes; ongoing research.

**NIST Standardization**: SIKE was selected as a finalist in the NIST post-quantum cryptography competition, though later withdrawn due to new attacks. CSIDH remains active, with improvements addressing prior vulnerabilities.

Isogeny-based cryptography remains a promising post-quantum avenue, combining mathematical elegance with practical efficiency, though standardization and real-world deployment are still maturing.
