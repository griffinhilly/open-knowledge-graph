---
id: secure-multi-party-computation
title: Secure Multi-Party Computation
domain: computer-science
course: cryptography
prerequisites:
- id: zero-knowledge-proofs
  type: hard
- id: commitment-schemes
  type: hard
- id: oblivious-transfer
  type: hard
tags:
- mpc
- secure-computation
- ideal-real-paradigm
- bgw-protocol
- honest-majority
stage: expert
status: validated
---

# Secure Multi-Party Computation

## Core Idea
Secure multi-party computation (MPC) allows n parties, each holding private input x_i, to jointly compute a function f(x_1,...,x_n) such that each party learns only the output and nothing about others' inputs beyond what the output implies. Security is defined by the ideal/real paradigm: the real protocol must be indistinguishable from an ideal world where a trusted third party collects inputs and distributes outputs. MPC is feasible for any function: with honest majority, information-theoretic security is achievable (BGW protocol); without honest majority, computational security is achievable using oblivious transfer. Applications include private auctions, joint statistical analysis, and threshold key management.

## Questions

```yaml
- question: "Three hospitals want to compute the average patient outcome across their databases without sharing individual patient data. Describe how MPC solves this and what security guarantee it provides."
  type: short-answer
  answer: "Each hospital is a party with private input (their aggregate statistics). An MPC protocol computes the combined average, revealing only the final result to all parties. The security guarantee (via ideal/real simulation) is that each hospital learns nothing about the other hospitals' data beyond what is implied by the final average combined with their own input. For example, if the average is 75 and Hospital A's average is 80, Hospital A learns that the combined average of B and C is lower than 80, but learns nothing more specific about B or C individually."
  explanation: "MPC cannot prevent information that is logically implied by the output — if only two hospitals participate, each can deduce the other's average from the combined average and their own input. This is inherent: it's information the output reveals, not a protocol weakness. MPC guarantees that the protocol leaks nothing beyond this logical minimum."

- question: "The ideal/real paradigm defines MPC security by comparison to an ideal world with a trusted third party. Why is this approach better than listing specific attacks the protocol must resist?"
  type: multiple-choice
  options:
    - "Listing attacks is equivalent but less elegant"
    - "The ideal/real paradigm provides a universal security guarantee: anything that could go wrong in the real protocol could also go wrong in the ideal world (where the only possible 'attack' is choosing a bad input or learning from the output). This automatically protects against all possible attacks — known and unknown — without needing to enumerate them. A specific attack list would inevitably miss some attacks"
    - "The ideal/real paradigm is easier to prove but provides weaker guarantees"
    - "The paradigm only applies to protocols with three or more parties"
  answer: 1
  explanation: "The ideal world is maximally secure by construction — a trusted party handles everything, so the only 'leakage' is the function output. Proving that the real protocol is indistinguishable from this ideal means the real protocol inherits all security properties of the ideal world. This captures privacy (inputs are hidden), correctness (output is accurate), independence of inputs (parties can't choose inputs based on others' inputs), and more — all from a single definition."

- question: "With an honest majority of participants (more than half are non-corrupted), MPC can achieve information-theoretic security without any computational assumptions."
  type: true-false
  answer: true
  explanation: "The BGW protocol (Ben-Or, Goldwasser, Wigderson, 1988) achieves this using Shamir secret sharing and local computation on shares. Each party secret-shares their input among all parties. The function is computed on shares using addition (free — add shares locally) and multiplication (requires one round of interaction per gate). With an honest majority, corrupted parties cannot reconstruct any secret, providing unconditional privacy. Without an honest majority (e.g., two-party computation), information-theoretic security is impossible and computational assumptions (typically OT) are required."

- question: "MPC for a function f guarantees that corrupted parties learn nothing beyond f's output. But what if f's output itself reveals sensitive information — for example, computing 'does any party's salary exceed $1M' reveals something about high earners?"
  type: multiple-choice
  options:
    - "MPC prevents this by encrypting the output"
    - "MPC cannot solve this — it guarantees the protocol leaks nothing beyond the output, but the function choice determines what the output reveals. If the function itself leaks too much, the parties must choose a different function. This is a function design problem, not a protocol problem"
    - "Adding more rounds of interaction prevents output-based leakage"
    - "Differential privacy inside MPC solves this automatically"
  answer: 1
  explanation: "MPC faithfully computes the agreed function and ensures nothing extra leaks. If the function is 'output all inputs,' MPC computes it securely but the output reveals everything. The parties must agree on a function whose output reveals only what they're comfortable sharing. Combining MPC with differential privacy (adding noise to the output) can address output-based leakage, but this is a complementary technique, not part of MPC itself."

- question: "Yao's garbled circuits enable two-party computation where one party 'garbles' the circuit and the other evaluates it. Why can't the evaluator learn intermediate wire values?"
  type: short-answer
  answer: "Each wire carries a random label (one for 0, one for 1) rather than the actual bit value. The evaluator processes garbled truth tables that map input labels to output labels using symmetric encryption — they can decrypt exactly one entry per gate (the one matching their input labels) and learn the output label, but cannot determine whether the label represents 0 or 1. Only the final output wires have their labels decoded to actual bits. The evaluator computes the correct output without ever learning any intermediate bit value."
  explanation: "The garbled circuit construction is the foundation of practical two-party MPC. The garbler (who constructs the circuit) must not learn the evaluator's input — this is achieved by the evaluator obtaining their input labels via oblivious transfer, which ensures the garbler does not learn which labels were selected."
```

## Explainer

**Secure multi-party computation (MPC)** addresses a fundamental question: can multiple parties compute a joint function of their private inputs without trusting anyone — not each other, not a central server, not any individual participant? The answer, remarkably, is yes. MPC protocols enable n parties, each holding a secret input, to compute any agreed-upon function and learn only the output, with the guarantee that the protocol reveals nothing about any party's input beyond what the output logically implies.

Security is defined via the **ideal/real paradigm**. In the **ideal world**, a perfectly trusted third party collects all inputs, computes the function, and returns the output — this is maximally secure because the only information anyone learns is the output. In the **real world**, parties run a cryptographic protocol with no trusted party. The protocol is secure if no efficient adversary can distinguish the real-world execution from the ideal world. This definition automatically captures every conceivable security property (privacy, correctness, input independence, fairness) without enumerating attacks — if the real and ideal worlds are indistinguishable, any property that holds in the ideal world also holds in the real one.

Two foundational results establish MPC's feasibility. **Yao's garbled circuits** (1986) solve the two-party case: one party converts the function into a Boolean circuit and "garbles" it — replacing wire values with random labels and encrypting truth tables. The other party evaluates the garbled circuit using their input labels (obtained via oblivious transfer) without learning intermediate wire values. **The BGW protocol** (1988) handles the multi-party case with honest majority using **Shamir secret sharing**: each party distributes shares of their input, and the function is computed on shares. Addition is free (add shares locally); multiplication requires one round of communication using the honest majority to reconstruct intermediate products securely. With honest majority, BGW achieves information-theoretic security — no computational assumptions needed.

MPC has moved from theory to practice over the past decade. Deployment scenarios include **private auctions** (bidders submit sealed bids; the protocol determines the winner without revealing losing bids), **medical research** (hospitals compute statistics across patient databases without sharing records), **financial regulation** (banks demonstrate compliance without revealing proprietary trading data), and **threshold key management** (a signing key is split among n parties, and t of them must cooperate to sign). Protocol efficiency has improved dramatically: modern MPC systems process millions of gates per second using optimized garbled circuits, oblivious transfer extensions, and preprocessing models that move expensive computation offline. While still orders of magnitude slower than direct computation, MPC is now fast enough for many practical applications.
