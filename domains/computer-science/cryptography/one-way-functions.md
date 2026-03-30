---
id: one-way-functions
title: One-Way Functions
domain: computer-science
course: cryptography
prerequisites:
- id: computational-hardness-assumptions
  type: hard
- id: complexity-class-p-definition
  type: hard
- id: complexity-class-np-definition
  type: soft
tags:
- one-way-function
- preimage-resistance
- minimal-assumption
- complexity-theory
stage: expert
status: validated
---

# One-Way Functions

## Core Idea
A one-way function (OWF) is a function that is easy to compute (polynomial time) but hard to invert (no polynomial-time algorithm succeeds on a non-negligible fraction of inputs). OWFs are the minimal assumption of cryptography: they exist if and only if P != NP for certain structured problems, and their existence is necessary and sufficient for private-key cryptography (pseudorandom generators, pseudorandom functions, MACs, symmetric encryption, digital signatures, commitment schemes). Candidate OWFs include integer multiplication (easy to multiply, hard to factor) and modular exponentiation. Proving any function is one-way remains an open problem equivalent in difficulty to separating P from NP.

## Questions

```yaml
- question: "A function is computable in polynomial time but hard to invert. Why is 'hard to invert' defined in terms of negligible probability of success across random inputs, rather than worst-case hardness?"
  type: short-answer
  answer: "Worst-case hardness means some inputs are hard to invert, but an attacker might succeed on most inputs. Cryptographic security requires that inversion fails on almost all inputs — an adversary who can invert even a non-negligible fraction (say 1/n^c for any constant c) would break any scheme built on the OWF. The average-case hardness requirement (no PPT algorithm inverts with more than negligible probability over random inputs) ensures the function is reliably hard, not just occasionally hard."
  explanation: "This distinction is fundamental. NP-completeness guarantees worst-case hardness (some instances are hard), but cryptography needs average-case hardness (random instances are hard). An NP-hard problem might still have efficient algorithms that work on 99% of instances. OWFs require that no efficient algorithm works on more than a negligible fraction of inputs, which is a much stronger (and harder to prove) statement."

- question: "If one-way functions exist, then P != NP. Does P != NP imply that one-way functions exist?"
  type: multiple-choice
  options:
    - "Yes — P != NP is exactly equivalent to the existence of OWFs"
    - "No — P != NP guarantees worst-case hardness, but OWFs require average-case hardness. It is believed that P != NP implies OWFs exist, but this has not been proven. There could be a world where P != NP but every efficiently computable function can be inverted on most inputs"
    - "P != NP is irrelevant to one-way functions because they are defined over finite domains"
    - "Yes, but only for functions based on number-theoretic problems"
  answer: 1
  explanation: "OWF existence implies NP-hardness of inversion (so P != NP). But the reverse is open. P != NP means some decision problems have no efficient solution, but this is a worst-case statement. Constructing OWFs requires average-case hard problems — the gap between worst-case and average-case hardness is a major open question in complexity theory. Most complexity theorists believe OWFs exist (and most believe P != NP), but the implication from P != NP to OWFs is not proven."

- question: "Integer multiplication (computing n = p * q from primes p, q) is a candidate one-way function. Why is it only a 'candidate' rather than a proven OWF?"
  type: multiple-choice
  options:
    - "Because multiplication is not actually in polynomial time"
    - "Because proving multiplication is one-way requires proving factoring has no polynomial-time algorithm, which would resolve P vs NP-type questions that remain open"
    - "Because quantum computers can factor integers, so multiplication is not one-way"
    - "Because multiplication is invertible using the extended Euclidean algorithm"
  answer: 1
  explanation: "We believe factoring is hard based on centuries of mathematical effort, but we cannot prove it. Proving any specific function is one-way would establish that P != NP (for certain structured variants), which is the most important open problem in theoretical computer science. Candidate OWFs are functions we believe are one-way based on empirical evidence (failed attack attempts) rather than proof. Quantum computers threaten factoring specifically, but that just means multiplication may not be one-way against quantum adversaries — the general concept of OWFs is not disproven."

- question: "One-way functions are sufficient to construct pseudorandom generators, pseudorandom functions, MACs, commitment schemes, digital signatures, and CPA-secure symmetric encryption."
  type: true-false
  answer: true
  explanation: "This is a central theorem of theoretical cryptography, established through a sequence of results by Goldreich, Goldwasser, Micali, Levin, Luby, Naor, Rompel, and others. OWFs → PRGs (Hastad-Impagliazzo-Levin-Luby) → PRFs (Goldreich-Goldwasser-Micali) → MACs → symmetric encryption. OWFs → universal one-way hash functions → signatures (Rompel). OWFs → commitment schemes → zero-knowledge proofs (for NP). The existence of OWFs is both necessary and sufficient for all of private-key cryptography and many public-key primitives."

- question: "A one-way permutation is a one-way function that is also a bijection. Why is this additional structure useful?"
  type: short-answer
  answer: "A one-way permutation (OWP) maps the domain onto itself bijectively, meaning every output has exactly one preimage. This eliminates ambiguity about what 'inverting' means and simplifies many constructions. The Goldreich-Levin theorem shows that any OWP can be converted into a pseudorandom generator by extracting a hard-core bit (a bit of the preimage that is unpredictable given the output). This PRG construction is cleaner and more efficient with OWPs than with general OWFs, which may have variable-size preimage sets."
  explanation: "OWPs are a stronger assumption than OWFs (every OWP is an OWF, but not conversely). However, many candidate OWFs (like RSA, which is a permutation on Z_n*) are naturally permutations. The OWP assumption simplifies theoretical constructions and gives tighter security proofs, which is why many foundational results in cryptography are first proven for OWPs and then generalized to OWFs."
```

## Explainer

The concept of a **one-way function** is the minimal mathematical abstraction underlying all of computational cryptography. Informally, a OWF is a function f that is easy to compute but hard to invert: given x, computing f(x) takes polynomial time, but given f(x), no efficient algorithm can find any preimage x' with f(x') = f(x) except with negligible probability. The hardness is **average-case** — inversion must fail on a random input with overwhelming probability, not just on carefully constructed worst-case inputs. This is a stronger requirement than NP-hardness, which only guarantees that some instances are hard.

The importance of OWFs stems from a remarkable theoretical result: **one-way functions are both necessary and sufficient for private-key cryptography**. If OWFs exist, you can build pseudorandom generators (Hastad-Impagliazzo-Levin-Luby), pseudorandom functions (Goldreich-Goldwasser-Micali), message authentication codes, CPA-secure symmetric encryption, commitment schemes, and even digital signatures (Rompel). Conversely, if OWFs do not exist, none of these primitives can exist — every function can be efficiently inverted, so secret keys can be recovered from public information. OWFs are the **minimal assumption**: prove they exist and you get all of symmetric cryptography; prove they don't exist and computational cryptography is impossible.

Candidate OWFs abound but none are proven. Integer multiplication (easy to compute p * q, believed hard to factor), modular exponentiation (easy to compute g^x mod p, believed hard to compute discrete logarithms), and subset sum (easy to add selected numbers, believed hard to find which were selected) are all candidates. **Proving that any of these is one-way would effectively resolve the P vs NP question** — specifically, it would show that NP is not contained in BPP, which is a major open problem in complexity theory. This is why OWF existence remains a conjecture despite decades of effort: we believe these functions are one-way because the smartest mathematicians and computer scientists have tried and failed to invert them, but belief is not proof.

The gap between OWFs and public-key cryptography is significant. OWFs suffice for private-key (symmetric) primitives but are not known to imply public-key encryption or key exchange. Public-key schemes require **trapdoor** one-way functions (functions that are hard to invert in general but easy to invert with a secret trapdoor) or specific algebraic structure (like the group structure in Diffie-Hellman). Whether OWFs imply public-key encryption is a major open question — it is possible that a world exists where private-key cryptography works but public-key cryptography is impossible. This hierarchy of assumptions — OWFs for symmetric crypto, trapdoor OWFs or CDH/DDH/LWE for public-key crypto — is the structural backbone of the field.
