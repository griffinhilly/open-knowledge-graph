---
id: blockchain-consensus-cryptography
title: Blockchain Consensus Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: digital-signatures
  type: hard
- id: hash-functions-and-collision-resistance
  type: hard
- id: verifiable-computation
  type: soft
tags:
- blockchain
- consensus
- distributed-systems
- cryptography
stage: expert
status: validated
---

# Blockchain Consensus Cryptography

## Core Idea
Blockchain consensus protocols use cryptography to achieve distributed agreement on transaction history without a trusted central authority. Cryptographic primitives enable: (1) authenticity (digital signatures prove senders), (2) integrity (hash functions detect tampering), (3) consensus (proof-of-work uses computational puzzles; proof-of-stake uses signatures and slashing), (4) finality (cryptographic sortition, BFT protocols). Advanced protocols (proof-of-authority, proof-of-history) add efficiency or additional guarantees. Cryptographic security of blockchains is crucial: compromised signatures, hash collisions, or consensus protocol flaws can enable theft or double-spending. Understanding the cryptographic foundations of consensus is essential for evaluating blockchain security.

## Questions

```yaml
- question: "How do digital signatures and hash functions combine to enable transaction authenticity and immutability in blockchains?"
  type: short-answer
  answer: "Digital signatures enable authenticity: a transaction signed by a private key can be verified by anyone with the public key, proving the transaction originated from that key holder. Hash functions enable immutability: a block's hash depends on all transactions and the previous block's hash. Changing any transaction changes the block hash, which breaks the chain (all subsequent blocks become invalid). Combining these: each transaction is signed (authenticity), blocks are hashed (immutability), and the chain is public (anyone can verify). An attacker would need to forge a signature (break signatures) and recompute all subsequent hashes faster than the network (break hash collision resistance) to alter history."
  explanation: "Signatures + hashing create a chain of verifiable history. This is the cryptographic foundation of immutability."

- question: "Proof-of-Work (mining) requires solving computational puzzles (finding a hash below a target). Why is this cryptographically useful?"
  type: multiple-choice
  options:
    - "Proof-of-work has no cryptographic purpose; it is purely computational waste"
    - "Proof-of-work makes block creation expensive (in energy), creating an economic barrier to attacking the chain; reversing history requires re-doing all work"
    - "Proof-of-work encrypts the blockchain content to hide transactions"
    - "Proof-of-work signs all transactions cryptographically"
  answer: 1
  explanation: "Proof-of-work's cryptographic utility is indirect but essential: it makes block creation expensive in energy/compute, creating a cost barrier to attacks. Reversing the blockchain history requires recomputing all work from the attack point faster than the network continues (hard because the network has 51% hash power and continues growing the honest chain). This economic cost complements cryptographic security: even if an attacker forges signatures or breaks hashing (unlikely but possible), the high cost of PoW makes attacks prohibitively expensive."

- question: "Proof-of-Stake (PoS) uses cryptographic signatures and slashing (penalizing equivocation). How does slashing provide security without computational puzzles?"
  type: true-false
  answer: true
  explanation: "In PoS, validators are chosen to propose blocks based on stake (amount held). Instead of computational cost (PoW), PoS uses economic cost: validators put up collateral (stake), which is slashed (forfeited) if they equivocate (sign conflicting blocks). Cryptographic signatures prove equivocation (two conflicting signatures with the same key), triggering slashing. This economic punishment replaces computational expense as the barrier to attacks. If you own 33% of stake and try a 33% attack, you lose 33% of your wealth (slashing), making the attack more expensive than any benefit. Slashing requires careful Byzantine-Fault-Tolerant (BFT) protocol design to correctly identify and penalize attacks."
```

## Explainer

Blockchains are distributed systems solving the consensus problem: achieving agreement on a canonical ledger (transaction history) among many participants, some of whom may be adversarial. Cryptography is essential at multiple levels.

**Cryptographic Primitives**:

1. **Digital Signatures**: Validate transactions. Only the holder of a private key can authorize spending.

2. **Hash Functions**: Create immutable chains. Changing any transaction invalidates all subsequent blocks.

3. **Merkle Trees**: Efficient integrity checking. A block contains a Merkle root of transactions; changing one invalidates the root.

4. **Commitment Schemes**: Secret commitments revealed later (useful in multi-round protocols like PoS).

**Consensus Models**:

1. **Proof-of-Work (PoW)**: Participants compete to solve computational puzzles. The winner (first to find a hash below target) proposes the next block and receives a reward. Consensus emerges because extending the honest chain is most profitable. Attacks require >50% hash power, costing enormous energy.

2. **Proof-of-Stake (PoS)**: Validators are chosen to propose blocks proportional to stake. Validators are penalized (slashed) if they equivocate (sign conflicting blocks). Attacks require >33% stake but face economic penalties. Cryptographic signatures prove equivocation.

3. **Byzantine Fault Tolerance (BFT)**: Direct consensus protocols (PBFT, HotStuff) where validators communicate multiple rounds. Consensus is guaranteed if <1/3 validators are Byzantine. Requires strong cryptographic assumptions (unforgeable signatures).

**Security Properties**:

1. **Liveness**: The chain continues to grow (new blocks are finalized).

2. **Safety**: The history is immutable; once a block is finalized, reversing it is prohibitively expensive.

3. **Finality**: Transactions are irreversible after sufficient time/depth.

Cryptographic security enables safety and finality; consensus protocol design (economic incentives) enables liveness.

**Advanced Topics**:

- **Threshold Cryptography**: Multiple validators jointly sign blocks, requiring k-of-n cooperation.
- **Light Clients**: Verify blockchain state without storing full history, using cryptographic commitments.
- **Zero-Knowledge Proofs**: Privacy-preserving transactions (zcash-style) or verifiable computation of state transitions.

**Attacks & Vulnerabilities**:

1. **51% Attack**: Attacker controls majority hash power (PoW) or stake (PoS), enabling double-spending or censorship.

2. **Double-Spending**: Attacker authorizes same funds to multiple recipients, exploiting insufficient finality.

3. **Long-Range Attacks**: Rewriting old history with low-stake PoS (if stakes are lost).

4. **MEV (Maximal Extractable Value)**: Reordering transactions to profit unfairly, exploiting protocol specifics.

Blockchain security is a complex interplay of cryptography, distributed systems, and game theory. Understanding the cryptographic foundations is essential for evaluating blockchain claims and designing robust systems.
