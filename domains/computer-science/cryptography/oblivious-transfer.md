---
id: oblivious-transfer
title: Oblivious Transfer
domain: computer-science
course: cryptography
prerequisites:
- id: computational-hardness-assumptions
  type: hard
- id: rsa-cryptosystem
  type: soft
tags:
- oblivious-transfer
- ot-extension
- mpc-building-block
- complete-primitive
stage: expert
status: validated
---

# Oblivious Transfer

## Core Idea
1-out-of-2 oblivious transfer (OT) is a protocol where a sender has two messages (m0, m1) and a receiver has a choice bit b. After the protocol, the receiver learns m_b but nothing about m_{1-b}, while the sender learns nothing about b. OT is a complete primitive for secure computation: any function can be securely computed using only OT as a building block (Kilian 1988). OT requires computational assumptions — it is impossible information-theoretically. OT extension protocols amortize expensive public-key operations, enabling millions of OTs from a small number of base OTs using only symmetric cryptography.

## Questions

```yaml
- question: "Why can't oblivious transfer be achieved using only symmetric cryptography (without any public-key assumptions)?"
  type: short-answer
  answer: "OT requires an inherent asymmetry: the receiver must learn one message while being provably unable to learn the other, AND the sender must be unable to learn which message was chosen. With symmetric cryptography alone, any information the sender transmits is either decryptable by the receiver (who holds the symmetric key) or not — there is no mechanism for the sender to 'not know' which key the receiver has without public-key techniques. Impagliazzo and Rudich showed that OT cannot be built from one-way functions in a black-box way, suggesting it genuinely requires public-key-type assumptions."
  explanation: "This separation result is fundamental: OT (and therefore general MPC without honest majority) requires strictly stronger assumptions than private-key cryptography. One-way functions suffice for encryption, MACs, signatures, and ZK proofs, but OT needs something like CDH, RSA, or LWE. This is the theoretical boundary between what symmetric and public-key cryptography can achieve."

- question: "OT is 'complete' for secure computation. What does completeness mean in this context?"
  type: multiple-choice
  options:
    - "OT can compute any function by itself without additional communication"
    - "Any efficiently computable function can be securely evaluated by a protocol that uses only OT as its cryptographic building block (plus local computation). This was proven by Kilian (1988): OT plus garbled circuits gives general two-party secure computation, and extensions handle the multi-party case"
    - "OT is the most efficient building block for any computation"
    - "OT can replace all other cryptographic primitives, including encryption and signatures"
  answer: 1
  explanation: "Completeness means OT is sufficient for all of secure computation, not that it replaces all crypto primitives. Kilian's result shows: given access to OT, the parties can securely compute any function. The garbler sends the garbled circuit; the evaluator obtains their input labels via OT (one OT per input bit). This requires no additional cryptographic assumptions beyond what OT provides. Other primitives (encryption, signatures) serve different purposes and are not subsumed."

- question: "OT extension allows computing millions of OTs from a small number (say 128) of 'base' OTs using only hash function evaluations. Why is this important for practical MPC?"
  type: multiple-choice
  options:
    - "Hash functions are more secure than public-key operations"
    - "Base OTs require expensive public-key operations (one per OT). For a garbled circuit with millions of input bits, millions of public-key OTs would be prohibitively slow. OT extension (Ishai-Kilian-Nissim-Orlandi) bootstraps 128 base OTs into any number of additional OTs using only symmetric-key operations (hashing), reducing the amortized cost per OT to a few hash evaluations — orders of magnitude faster"
    - "OT extension eliminates the need for computational assumptions"
    - "Hash functions provide information-theoretic security for OT"
  answer: 1
  explanation: "OT extension is one of the most important practical optimizations in MPC. The base OTs (128 or 256, matching the security parameter) use expensive public-key crypto, but this cost is amortized over millions of extended OTs. The extension protocol uses a matrix transposition trick: the receiver sends a matrix of bits, and the sender uses the base OT keys to 'switch' rows, generating correlated random OT pairs. The cost drops from one RSA/ECC operation per OT to one hash evaluation per OT."

- question: "In a 1-out-of-2 OT, the sender is guaranteed to learn nothing about the receiver's choice bit b, even if the sender is malicious and deviates from the protocol."
  type: true-false
  answer: true
  explanation: "This is the receiver's privacy guarantee and must hold against a malicious sender. In Naor-Pinkas OT (based on DDH), the receiver sends a specially constructed message that information-theoretically hides b — the sender cannot determine which of the two messages the receiver will be able to decrypt, regardless of the sender's computational power. The sender's privacy (receiver learns only m_b) holds computationally against a malicious receiver."

- question: "Random OT (where the sender does not choose the messages — both parties receive correlated random values) is equivalent to chosen-message OT. Why is random OT useful as a building block?"
  type: short-answer
  answer: "Random OT can be converted to chosen-message OT: after a random OT produces random values (r0, r1) for the sender and r_b for the receiver, the sender sends (m0 XOR r0, m1 XOR r1). The receiver computes m_b = (m_b XOR r_b) XOR r_b. Random OT is useful because it can be precomputed in an offline phase (before the parties know their actual inputs), and then converted to chosen-message OT cheaply in the online phase. This offline/online split is a key optimization in practical MPC protocols."
  explanation: "The preprocessing model separates expensive cryptographic operations (done offline when inputs are unknown) from lightweight operations (done online with actual inputs). Random OTs are input-independent and can be stockpiled. When the real computation begins, converting them to chosen-message OTs requires only XOR operations — essentially free. This amortization strategy is fundamental to achieving practical MPC performance."
```

## Explainer

**Oblivious transfer (OT)** is deceptively simple to state but extraordinarily powerful. In 1-out-of-2 OT, a sender holds two messages m0 and m1, and a receiver holds a bit b. After the protocol, the receiver learns m_b (the message they chose) and nothing about m_{1-b}, while the sender learns nothing about which message was chosen. Both parties are simultaneously ignorant: the sender doesn't know which message was taken, and the receiver doesn't know the message they didn't take. This dual ignorance is what makes OT non-trivial and impossible to achieve without computational assumptions.

OT can be constructed from various public-key assumptions. In the **Naor-Pinkas protocol** (based on CDH), the receiver sends a pair of group elements, one of which encodes their choice bit. The sender encrypts each message under the corresponding element. The algebraic structure ensures the receiver can decrypt only one message, while the sender cannot determine which one. More recent constructions use lattice-based assumptions, providing post-quantum security. What cannot be done is build OT from one-way functions alone (Impagliazzo-Rudich) — OT genuinely requires public-key-level assumptions, placing it strictly above symmetric primitives in the cryptographic hierarchy.

The theoretical significance of OT lies in its **completeness for secure computation** (Kilian, 1988): any efficiently computable function can be securely evaluated using OT as the only cryptographic building block. Combined with Yao's garbled circuits, this means two parties can securely compute any function as follows — the garbler constructs the garbled circuit, and the evaluator obtains their input labels via OT (one OT per input bit), ensuring the garbler doesn't learn which labels were selected. For multi-party computation, OT extensions and related techniques generalize this approach. OT is therefore the minimal cryptographic assumption for general secure computation without honest majority.

In practice, OT's main bottleneck is that each invocation requires public-key operations. **OT extension** (Ishai, Kilian, Nissim, Orlandi, 2003) is the breakthrough optimization: starting from a small number of "base" OTs (128 or 256, performed with expensive public-key crypto), the protocol generates any number of additional OTs using only symmetric operations (hash evaluations). The technique involves exchanging a matrix of bits and using the base OT keys to correlate rows, enabling the amortized cost per OT to drop to a few hash evaluations. Combined with the **preprocessing model** (precompute random OTs offline, convert to chosen-message OTs online using XOR), this makes practical MPC with millions of OTs feasible. Modern MPC systems can execute billions of OTs per second, transforming OT from a theoretical primitive into a practical workhorse.
