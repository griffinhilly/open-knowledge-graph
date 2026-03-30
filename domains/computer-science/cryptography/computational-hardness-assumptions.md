---
id: computational-hardness-assumptions
title: Computational Hardness Assumptions
domain: computer-science
course: cryptography
prerequisites:
- id: rsa-cryptosystem
  type: hard
- id: diffie-hellman-key-exchange
  type: hard
- id: complexity-class-np-definition
  type: hard
tags:
- hardness-assumption
- factoring
- cdh
- ddh
- reduction
stage: expert
status: validated
---

# Computational Hardness Assumptions

## Core Idea
Modern cryptography is built on unproven mathematical assumptions: specific computational problems (factoring, CDH, DDH, LWE) are believed to be intractable for polynomial-time algorithms. A cryptographic scheme's security is proven by reduction — showing that any efficient attacker breaks the scheme only if they can also solve the underlying hard problem. Assumptions are arranged in a hierarchy: DDH implies CDH implies DLP; factoring implies RSA. Weaker assumptions yield stronger results. The gap between "no one knows how to solve X" and "X is provably hard" is the foundational epistemic limitation of cryptography — no hardness assumption has been proven unconditionally (doing so would resolve P != NP).

## Questions

```yaml
- question: "A cryptographer proves that breaking scheme S is at least as hard as factoring 2048-bit integers. A colleague says this means S is unconditionally secure. What is the flaw?"
  type: short-answer
  answer: "The proof shows security relative to the factoring assumption — if factoring is hard, then S is secure. But no one has proven factoring is hard (this would imply P != NP). The reduction means S is secure under the factoring assumption, which is a widely believed but unproven conjecture. If someone discovers an efficient factoring algorithm, both the assumption and every scheme reduced to it collapse simultaneously."
  explanation: "This is the fundamental limitation of computational cryptography. All security proofs are conditional on unproven assumptions. The cryptographic community gains confidence in assumptions through decades of failed attacks by experts, but this is empirical evidence, not mathematical proof. Unconditional security (information-theoretic) requires impractically long keys (Shannon's theorem)."

- question: "The Decisional Diffie-Hellman (DDH) assumption states that (g^a, g^b, g^{ab}) is computationally indistinguishable from (g^a, g^b, g^c) for random a, b, c. Why is DDH a stronger assumption than CDH?"
  type: multiple-choice
  options:
    - "DDH requires larger group elements than CDH"
    - "DDH asks adversaries to distinguish (a harder task than computing), but DDH implies CDH: if you can compute g^{ab} from (g^a, g^b), you can certainly distinguish (g^a, g^b, g^{ab}) from (g^a, g^b, g^c) by computing g^{ab} and comparing. So DDH being hard is a stronger claim than CDH being hard"
    - "DDH applies to elliptic curves while CDH applies to integers"
    - "CDH is a special case of DDH where a = b"
  answer: 1
  explanation: "In the hierarchy: DDH ⇒ CDH ⇒ DLP. Breaking DLP (computing a from g^a) solves CDH (compute (g^b)^a); breaking CDH solves DDH (compute g^{ab} and compare). Each implication is one-directional — no one has shown the reverse. DDH is actually false in some groups where CDH appears hard (e.g., groups with bilinear pairings), which is why pairing-based cryptography uses different assumptions."

- question: "A security proof via reduction shows: 'If adversary A breaks scheme S with advantage epsilon in time t, then algorithm B solves hard problem H with advantage epsilon/q in time t + O(q).' What do epsilon and the 'tightness' of the reduction tell us?"
  type: short-answer
  answer: "Epsilon is the adversary's advantage in breaking the scheme. The reduction's tightness — the ratio between the adversary's advantage against S and the resulting advantage against H — determines how the scheme's concrete security relates to the assumed hardness of H. A tight reduction (epsilon vs epsilon, or close) means the scheme is about as hard to break as the underlying problem. A loose reduction (epsilon vs epsilon/q for large q) means the scheme could be significantly easier to break than the problem, requiring larger security parameters to compensate."
  explanation: "Tightness matters for concrete parameter selection. If the reduction loses a factor of 2^30, you need to add 30 bits to your security parameter. Loose reductions are a major practical concern: a scheme with a security proof but a loose reduction may need impractically large keys. Much research aims to tighten reductions or find schemes with inherently tight proofs."

- question: "If P = NP, all commonly used computational hardness assumptions in cryptography would collapse."
  type: true-false
  answer: true
  explanation: "All standard assumptions (factoring, RSA, CDH, DDH, LWE) assert that certain problems in NP cannot be solved in polynomial time. If P = NP, every NP problem is solvable in polynomial time, so every such assumption is false. This would break all public-key cryptography, most symmetric cryptography beyond one-time pads, and all zero-knowledge proofs. The belief that P != NP is therefore a meta-assumption underlying the entire field. However, some cryptographic primitives might survive specific collapses — if factoring becomes easy but LWE remains hard, lattice-based cryptography would survive even as RSA falls."

- question: "Cryptographers prefer to base schemes on the weakest possible assumption. Why?"
  type: multiple-choice
  options:
    - "Weaker assumptions require less computation to verify"
    - "A scheme based on a weaker assumption is secure under more scenarios — if the stronger assumption turns out to be false but the weaker one holds, the scheme survives. Fewer assumptions mean fewer potential points of failure"
    - "Weaker assumptions always lead to more efficient schemes"
    - "Regulatory standards require the use of minimal assumptions"
  answer: 1
  explanation: "If scheme A is based on DDH and scheme B is based on CDH, then B is secure in strictly more worlds — it survives even if DDH is broken (as long as CDH holds). Since DDH failing does not imply CDH failing, B is more robust. The ideal is to base cryptography on the weakest assumptions that allow the desired functionality. However, there are tradeoffs: weaker assumptions sometimes lead to less efficient constructions, so practical schemes balance assumption strength against performance."
```

## Explainer

Every modern cryptographic scheme's security proof has the form: "If assumption X holds, then this scheme is secure." **Computational hardness assumptions** are the unproven mathematical beliefs on which the entire field rests. The most important are the **factoring assumption** (factoring the product of two large primes is computationally intractable), the **RSA assumption** (computing e-th roots modulo n = pq is hard without the factorization), the **Computational Diffie-Hellman (CDH) assumption** (computing g^{ab} from g^a and g^b in a well-chosen group is hard), and the **Decisional Diffie-Hellman (DDH) assumption** (the triple (g^a, g^b, g^{ab}) is computationally indistinguishable from (g^a, g^b, g^c) for random a, b, c).

These assumptions are arranged in a **hierarchy of strength**. DDH implies CDH (if you can compute g^{ab}, you can certainly distinguish it from random), and CDH implies DLP (if you can compute discrete logarithms, you can solve CDH). A stronger assumption is one that is easier to break — DDH is stronger than CDH because there are more potential ways to break DDH (distinguish without computing). Cryptographers prefer to base schemes on the **weakest** possible assumption because it is the hardest to break: a scheme based on CDH remains secure even if DDH turns out to be false. The gold standard is basing everything on one-way functions (the weakest useful assumption), which exist if and only if P != NP for specific function families.

Security proofs work by **reduction**: the cryptographer constructs an algorithm that, given any efficient attacker against the scheme, converts it into an efficient solver for the assumed hard problem. If the hard problem is believed unsolvable in polynomial time, the scheme must be secure — any efficient attacker would contradict the assumption. The **tightness** of the reduction matters practically: if the reduction introduces a large loss factor (converting an advantage of epsilon against the scheme into an advantage of epsilon/2^30 against the hard problem), the scheme's concrete security is much weaker than the raw assumption suggests, requiring larger parameters to compensate.

The deepest limitation of this approach is that **no hardness assumption has been proven unconditionally**. Proving that factoring is hard would separate complexity classes in ways that would effectively resolve the P vs NP question. The entire edifice of computational cryptography rests on empirical confidence — decades of smart people failing to solve these problems — rather than mathematical proof. This is why the field maintains a portfolio of assumptions: if factoring falls (to quantum computers or new classical algorithms), schemes based on lattice assumptions (LWE, SIS) may survive. Diversifying assumptions is cryptography's hedge against the inherent uncertainty of unproven conjectures.
