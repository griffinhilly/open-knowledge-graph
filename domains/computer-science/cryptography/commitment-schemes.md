---
id: commitment-schemes
title: Commitment Schemes
domain: computer-science
course: cryptography
prerequisites:
- id: hash-functions-and-collision-resistance
  type: hard
- id: one-way-functions
  type: soft
tags:
- commitment
- hiding
- binding
- pedersen
- hash-commitment
stage: expert
status: validated
---

# Commitment Schemes

## Core Idea
A commitment scheme lets a party commit to a value while keeping it hidden (hiding), with the guarantee that they cannot later change the committed value (binding). Think of sealing a value in an envelope: the envelope hides the value, and you cannot change it after sealing. Commitments have two phases: commit (produce a commitment c to value v) and reveal (open c to show v). Hash-based commitments (c = H(v || r) for random r) provide computational hiding and binding. Pedersen commitments (c = g^v * h^r) provide information-theoretic hiding with computational binding. Commitments are essential building blocks for zero-knowledge proofs, coin-flipping protocols, secure computation, and blockchain applications.

## Questions

```yaml
- question: "A hash-based commitment c = H(v || r) is computationally hiding and computationally binding. What would happen if we used c = H(v) without the random nonce r?"
  type: short-answer
  answer: "Without randomness, the commitment is deterministic — an adversary who knows the set of possible values (e.g., 'yes' or 'no') can compute H(yes) and H(no) and compare with c to determine v. The random nonce r ensures that c = H(v || r) is uniformly distributed even for small value spaces, making the commitment indistinguishable from random. Without r, the scheme has no hiding property for low-entropy values."
  explanation: "This is analogous to why encryption must be randomized (semantic security): deterministic commitments leak the committed value through exhaustive search over the value space. The nonce r must be long enough (128+ bits) to prevent brute-force search over both v and r."

- question: "The hiding and binding properties of a commitment scheme are in tension — perfect hiding and perfect binding cannot both be achieved simultaneously. Why?"
  type: multiple-choice
  options:
    - "The commitment would require infinite storage"
    - "Perfect hiding means that for any value v, there exists a randomness r' that makes c consistent with a different value v'. But if this is true, the committer CAN find v' and r' to change their commitment — violating perfect binding. Conversely, perfect binding means c uniquely determines v, but then an unbounded adversary could search for the unique v, violating perfect hiding"
    - "Quantum computers break both properties simultaneously"
    - "The two properties require contradictory key lengths"
  answer: 1
  explanation: "This is a fundamental impossibility result. Commitment schemes must choose: information-theoretic hiding + computational binding (Pedersen: the commitment statistically reveals nothing, but changing the value requires solving DLP), or computational hiding + information-theoretic binding (hash-based: the commitment computationally hides the value, but is information-theoretically bound to exactly one value because the hash is deterministic given v and r). The choice depends on which adversary you're more worried about — a computationally unlimited observer or a computationally unlimited committer."

- question: "Pedersen commitments (c = g^v * h^r mod p, where the discrete log relationship between g and h is unknown) provide information-theoretic hiding. Why?"
  type: multiple-choice
  options:
    - "The modular exponentiation is a one-way function"
    - "For any commitment c and any target value v', there exists a randomness r' such that c = g^{v'} * h^{r'} — the commitment is consistent with every possible value. An unbounded adversary cannot determine v because every v is equally plausible. Finding r' requires knowing the discrete log of g base h, so opening to a different value (binding) is computationally hard"
    - "The Pedersen commitment uses a random oracle"
    - "The prime p is so large that brute force is infeasible"
  answer: 1
  explanation: "This is the cleanest example of information-theoretic hiding: the commitment is literally a uniform random group element regardless of v (given uniform r). No amount of computation reveals v. Binding relies on the DLP assumption: to open c as both v and v' (with different r and r'), you'd need g^{v-v'} = h^{r'-r}, which reveals log_g(h) — assumed hard. Pedersen commitments are heavily used in zero-knowledge proofs and blockchain privacy (Monero's confidential transactions)."

- question: "Commitment schemes are essential for fair coin-flipping over a telephone line (Blum's protocol). Without commitments, the first party to announce their coin flip can cheat by choosing based on the other's announcement."
  type: true-false
  answer: true
  explanation: "Blum's protocol: Alice commits to a random bit a (sends commitment c_a to Bob). Bob sends his random bit b in the clear. Alice opens her commitment, revealing a. The coin flip result is a XOR b. Alice cannot cheat because she committed to a before seeing b (binding). Bob cannot cheat because he doesn't know a when choosing b (hiding). Without the commitment, if Alice announced a first, Bob could choose b to make a XOR b whatever he wants."

- question: "Vector commitments generalize standard commitments: instead of committing to a single value, you commit to a vector (v_1, ..., v_n) and can later open any individual position i without revealing other positions. Why is this useful for blockchain?"
  type: short-answer
  answer: "A blockchain block contains thousands of transactions. A vector commitment to all transactions in a block lets anyone verify that a specific transaction is included in the block by opening just that position — without downloading or processing the other transactions. Merkle trees are the most common vector commitment: the root hash commits to all leaves, and a Merkle proof (O(log n) hashes) opens one leaf. Polynomial commitments (KZG) achieve constant-size openings but require trusted setup. These are used in light clients, state proofs, and blockchain interoperability."
  explanation: "Vector commitments with efficient opening proofs are fundamental to scalable blockchain architecture. Light clients (like mobile wallets) trust the block header's commitment and verify individual transactions on demand, without storing the full blockchain. Ethereum's state tree is essentially a vector commitment over all account balances and contract states."
```

## Explainer

A **commitment scheme** is one of the most fundamental primitives in cryptography, enabling a party to "lock in" a value while keeping it secret, and later reveal it with proof that they haven't changed it. The protocol has two phases: in the **commit phase**, the committer produces a commitment c to a value v (like sealing v in an envelope). In the **reveal phase**, the committer opens c by revealing v and any randomness used, and anyone can verify that c was indeed a commitment to v. Two security properties must hold: **hiding** (the commitment reveals nothing about v to an observer) and **binding** (the committer cannot open c to a different value v').

The simplest construction is hash-based: c = H(v || r) where r is a random nonce. Revealing means sending v and r; verification checks that H(v || r) = c. Hiding holds because the random r makes c computationally indistinguishable from a random hash output (even if v comes from a small set). Binding holds because finding v' != v and r' with H(v' || r') = H(v || r) requires a hash collision — computationally infeasible. The **Pedersen commitment** (c = g^v * h^r in a group where log_g(h) is unknown) achieves **information-theoretic hiding**: for any c and any target v', there exists an r' making c = g^{v'} * h^{r'}, so the commitment is consistent with every possible value — no computation can extract v. Binding is computational: opening to two different values would reveal log_g(h).

A fundamental impossibility result constrains the design space: **perfect hiding and perfect binding cannot coexist**. If the commitment is consistent with every value (perfect hiding), the committer could in principle find an alternative opening (breaking perfect binding, though this requires solving a hard problem). If the commitment uniquely determines the value (perfect binding), an unbounded adversary could find that value (breaking perfect hiding). Every scheme must choose one property to be information-theoretic and the other computational.

Commitments are ubiquitous in cryptographic protocols. **Zero-knowledge proofs** use commitments to let the prover lock in their responses before seeing the verifier's challenges (preventing cheating). **Fair coin-flipping** (Blum's protocol) uses commitments so neither party can bias the outcome. **Secure computation** protocols use commitments to enforce honest behavior. **Blockchain applications** use commitments extensively: Merkle trees (vector commitments for block contents), Pedersen commitments (hiding transaction amounts in confidential transactions), and polynomial commitments (KZG, used in blockchain proof systems). The humble commitment — "I've decided, but I'm not telling you yet" — is one of the most versatile building blocks in the entire cryptographic toolkit.
