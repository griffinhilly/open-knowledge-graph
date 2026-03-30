---
id: zero-knowledge-proofs
title: Zero-Knowledge Proofs
domain: computer-science
course: cryptography
prerequisites:
- id: one-way-functions
  type: hard
- id: computational-hardness-assumptions
  type: hard
- id: complexity-class-np-definition
  type: hard
tags:
- zero-knowledge
- zkp
- simulation
- completeness
- soundness
- zk-snark
stage: expert
status: validated
---

# Zero-Knowledge Proofs

## Core Idea
A zero-knowledge proof lets a prover convince a verifier that a statement is true without revealing any information beyond the truth of the statement. It satisfies three properties: completeness (honest prover convinces honest verifier), soundness (no cheating prover convinces the verifier of a false statement), and zero-knowledge (the verifier learns nothing beyond the statement's validity, formalized via simulation — a simulator can produce transcripts indistinguishable from real interactions without knowing the witness). Every NP language has a zero-knowledge proof (assuming OWFs). ZK proofs are foundational for privacy-preserving authentication, blockchain privacy (Zcash), and verifiable computation.

## Questions

```yaml
- question: "The classic illustration: Peggy wants to prove to Victor she knows the secret to a cave with two passages connected by a locked door, without revealing the secret. Describe the protocol and identify which ZK property each step satisfies."
  type: short-answer
  answer: "Peggy enters the cave while Victor waits outside. She randomly takes passage A or B. Victor calls out which passage she must exit from. If Peggy knows the secret (can unlock the connecting door), she always exits the correct passage — completeness. If she doesn't know the secret and guessed wrong, she's caught — each round she cheats with probability 1/2, so after k rounds the chance of undetected cheating is 2^{-k} — soundness. Victor learns nothing about the secret because each round looks the same whether Peggy used the door or happened to be on the correct side — a simulator who randomly picks the correct side half the time produces an identical distribution — zero-knowledge."
  explanation: "This physical analogy captures the essential structure: the verifier's challenge forces the prover to demonstrate knowledge, repetition drives cheating probability to negligible, and the protocol's symmetry ensures no information leaks. Real ZK proofs replace physical caves with mathematical commitments and challenges."

- question: "What does the simulation paradigm mean in the context of zero-knowledge, and why is it the right formalization of 'learns nothing'?"
  type: multiple-choice
  options:
    - "The verifier can simulate the prover's computation on their own hardware"
    - "A polynomial-time simulator, given only the statement (not the witness), can produce transcripts that are computationally indistinguishable from real prover-verifier interactions. This means whatever the verifier could compute from the real interaction, they could also compute without the interaction — so the interaction provides no additional information"
    - "The simulation shows that the proof can be replayed by any third party"
    - "The simulator proves the statement is false to demonstrate no information was leaked"
  answer: 1
  explanation: "The simulation paradigm is the precise formalization of 'no information leaks.' If a simulator (without the witness) can produce fake transcripts indistinguishable from real ones, then the real transcript carries no computational information beyond what is already implied by the statement being true. The verifier could generate equivalent transcripts themselves without ever talking to the prover. This definition is non-trivial: it must hold even for malicious verifiers who deviate from the protocol."

- question: "Every language in NP has a computational zero-knowledge proof, assuming one-way functions exist."
  type: true-false
  answer: true
  explanation: "This landmark result (Goldreich, Micali, Wigderson, 1987) uses graph 3-coloring (an NP-complete problem) as the base case. They constructed a ZK proof for 3-coloring using commitment schemes (which exist if OWFs exist). Since every NP language reduces to 3-coloring, the ZK proof composes with the reduction to give ZK proofs for all of NP. This theorem means that any statement with an efficiently checkable witness can be proven without revealing the witness — a profound conceptual result."

- question: "A zk-SNARK (Succinct Non-interactive ARgument of Knowledge) provides a zero-knowledge proof that is constant-size and verifiable in milliseconds, regardless of the complexity of the statement being proved. What is the main tradeoff?"
  type: multiple-choice
  options:
    - "zk-SNARKs require quantum computers for proof generation"
    - "zk-SNARKs are ARguments, not proofs: soundness holds only against computationally bounded provers (not information-theoretically). Most zk-SNARKs also require a trusted setup — a one-time ceremony that generates common parameters. If the setup is compromised, fake proofs can be generated. Some newer constructions (STARKs) eliminate the trusted setup but produce larger proofs"
    - "zk-SNARKs cannot prove statements about encrypted data"
    - "zk-SNARKs are only zero-knowledge in the random oracle model, not under standard assumptions"
  answer: 1
  explanation: "The succinct proof size and fast verification come at the cost of computational soundness (an unbounded prover could forge proofs) and, typically, a trusted setup. The trusted setup generates a structured reference string; anyone who knows the randomness used in the setup can forge proofs. Techniques like multi-party computation for the setup ceremony and transparent constructions (STARKs, Bulletproofs) mitigate this, but with efficiency tradeoffs. Zcash uses zk-SNARKs to prove transaction validity without revealing sender, receiver, or amount."

- question: "A zero-knowledge proof of knowledge differs from a zero-knowledge proof of membership. What additional guarantee does it provide?"
  type: short-answer
  answer: "A ZK proof of membership proves that a statement x is in a language L (e.g., 'this graph is 3-colorable'). A ZK proof of knowledge additionally proves that the prover actually possesses a witness w for x — not just that one exists. This is formalized by an extractor: a polynomial-time algorithm that, given the ability to rewind the prover, can extract the witness from any convincing prover. This is crucial for authentication (proving you know a password) and blockchain applications (proving you know the secret key authorizing a transaction)."
  explanation: "The distinction matters: knowing that a graph is 3-colorable (perhaps because someone told you) is different from knowing a specific 3-coloring. Proofs of knowledge ensure the prover has constructive access to the secret, which is the relevant guarantee for cryptographic applications where the witness is a key, password, or authorization credential."
```

## Explainer

Imagine you know the password to a vault, and you want to convince a guard that you know it — without ever revealing the password. Not a single bit of it. Not even information that helps the guard narrow down what the password might be. This is the promise of **zero-knowledge proofs**: a prover can convince a verifier that a statement is true while revealing absolutely nothing beyond the truth of the statement. The three defining properties are: **completeness** (an honest prover with a valid witness always convinces the verifier), **soundness** (a cheating prover without a witness fails with overwhelming probability), and **zero-knowledge** (the verifier learns nothing they couldn't have computed on their own).

Zero-knowledge is formalized through the **simulation paradigm**. A protocol is zero-knowledge if there exists an efficient **simulator** that, without knowing the witness, can generate fake transcripts that are computationally indistinguishable from real prover-verifier interactions. If such a simulator exists, the real interaction provides no computational advantage to the verifier — whatever they could compute from the transcript, they could compute without it (by running the simulator). This definition elegantly handles arbitrary verifier strategies, including malicious verifiers who deviate from the protocol.

The most remarkable theoretical result is that **every NP language has a zero-knowledge proof**, assuming one-way functions exist. Goldreich, Micali, and Wigderson proved this in 1987 by constructing a ZK proof for graph 3-coloring (NP-complete) using commitment schemes. The prover commits to a random permutation of a valid 3-coloring, the verifier challenges by selecting a random edge, and the prover opens the commitments for that edge's two vertices, showing they have different colors. After enough rounds, the verifier is convinced the graph is 3-colorable, but learns nothing about which coloring the prover used (because each round reveals only two of three color classes under a random permutation). Since every NP problem reduces to 3-coloring, this gives ZK proofs for all NP statements.

Practical zero-knowledge has exploded in recent years, driven by blockchain applications. **zk-SNARKs** (Succinct Non-interactive Arguments of Knowledge) compress a proof to constant size (a few hundred bytes) verifiable in milliseconds, regardless of the statement's complexity. Zcash uses zk-SNARKs to prove that a cryptocurrency transaction is valid (inputs equal outputs, sender has sufficient balance, no double-spending) without revealing the sender, recipient, or amount. **zk-STARKs** achieve similar goals without a trusted setup, using hash functions instead of elliptic curves, but with larger proof sizes. These technologies represent a transition of zero-knowledge from a theoretical curiosity to a deployed infrastructure component for privacy and scalability in distributed systems.
