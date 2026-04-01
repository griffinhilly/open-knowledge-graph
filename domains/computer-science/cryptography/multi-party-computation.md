---
id: multi-party-computation
title: Multi-Party Computation
domain: computer-science
course: cryptography
prerequisites:
- id: secure-multi-party-computation
  type: hard
- id: oblivious-transfer
  type: hard
- id: zero-knowledge-proofs-advanced
  type: soft
tags:
- mpc
- secure-computation
- privacy
- cryptography
stage: expert
status: validated
---

# Multi-Party Computation

## Core Idea
Multi-party computation (MPC) enables n parties to jointly compute a function f(x_1, ..., x_n) where party i holds input x_i, without revealing individual inputs to each other. Parties learn only the output f(x_1, ..., x_n), not intermediate values or others' inputs. MPC is theoretically proven possible for any computable function (universal), with various constructions: secret sharing (Shamir, additive), garbled circuits, homomorphic encryption, and oblivious transfer. Practical MPC protocols balance security (information-theoretic vs. computational), robustness (honest majority vs. dishonest majority), and efficiency. Applications include privacy-preserving data analysis, secure auctions, and collaborative machine learning.

## Questions

```yaml
- question: "Why is MPC considered 'universal' despite being computationally expensive?"
  type: short-answer
  answer: "MPC is universal in the theoretical sense: for any function f that can be computed by a Turing machine, there exists an MPC protocol enabling n parties to compute f on secret inputs without revealing the inputs. This does not mean MPC is practical (it is exponentially slower than plaintext computation), but it proves no function is inherently uncomputable in the MPC setting. Universality is the fundamental theorem of MPC; practicality is engineering."
  explanation: "Universality is a theoretical guarantee; achieving practical efficiency requires domain-specific optimizations and careful protocol design."

- question: "In secret-sharing-based MPC (e.g., Shamir secret sharing), how does computation on shared secrets work?"
  type: multiple-choice
  options:
    - "Shared secrets cannot be operated on; the scheme is only for storage"
    - "Addition and multiplication of secret shares can be performed locally without revealing the underlying secret; addition is linear, multiplication requires interaction (communication)"
    - "Only addition is possible; multiplication of secrets is impossible"
    - "Computation on secrets requires reconstructing them, revealing secrets to all parties"
  answer: 1
  explanation: "Secret sharing enables computation on shared values without reconstruction. Addition of secrets is linear: if a is shared as (a_1, ..., a_n) and b as (b_1, ..., b_n), then a+b is shared as (a_1+b_1, ..., a_n+b_n), computed locally by each party. Multiplication is nonlinear: computing a*b from shares requires interaction (typically one round). This property enables designing MPC protocols where most computation is local, with minimal interaction for multiplications."
```

## Explainer

Multi-party computation is the cryptographic foundation for privacy-preserving collaborative computation. Parties can jointly solve problems without trusting a central authority or revealing individual data.

**Secret Sharing Foundations**: Shamir secret sharing enables sharing a secret s among n parties such that any k parties can reconstruct s, but fewer than k parties learn nothing. Shares are computed as s_i = p(i) where p is a polynomial of degree k-1 with p(0) = s. Reconstruction uses polynomial interpolation. This scheme is information-theoretically secure for honest players.

**MPC Construction**: Parties execute a protocol in rounds. Each round involves: (1) local computation on shared values, (2) exchange of messages (shares), (3) threshold operations if necessary. The protocol is designed so that at no point does any coalition of parties gain information beyond the final output.

**Security Models**:

1. **Semi-Honest**: Parties follow the protocol but may try to learn extra information from transcripts. Achievable with secret sharing under honest majority.

2. **Malicious**: Parties may deviate arbitrarily. Requires additional mechanisms (verifiable secret sharing, commitments, zero-knowledge proofs) to ensure correctness.

3. **Honest Majority vs. Dishonest Majority**: Honest majority (>50% honest parties) is easier; dishonest majority requires more complex protocols and typically higher overhead.

**Communication Rounds**: The number of rounds (communication phases) is a key complexity measure. Garbled circuits achieve constant rounds; secret sharing can require many rounds. Protocols minimize rounds for latency-sensitive applications.

**Practical Protocols**:

- **GMW Protocol**: Based on garbled circuits and oblivious transfer; secure against semi-honest adversaries; O(depth) rounds.
- **BGW Protocol**: Based on secret sharing; secure against honest majority; works for arbitrary functions.
- **SPDZ**: Practical protocol for malicious adversaries; uses homomorphic encryption and MACs to verify correctness.

**Applications**:

1. **Secure Auctions**: Bidders submit bids without revealing them; auctioneer computes winner and price without bid knowledge.

2. **Privacy-Preserving Data Analysis**: Multiple organizations share data for joint statistics (average, correlation) without revealing individual records.

3. **Collaborative Machine Learning**: Train models on data from multiple parties without centralizing data.

4. **Secure Voting**: Count votes without revealing individual votes or intermediate tallies.

**Practical Considerations**:

- **Efficiency**: MPC is expensive (100x-1000x slowdown vs. plaintext), limiting scale.
- **Network Latency**: Many-round protocols suffer from network latency; reducing rounds is critical.
- **Composability**: Protocols must remain secure when combined; careful design is necessary.

MPC bridges cryptographic theory and practice, enabling privacy-preserving computation on distributed, sensitive data—increasingly important for finance, healthcare, and data analytics.
