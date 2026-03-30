---
id: garbled-circuits
title: Garbled Circuits
domain: computer-science
course: cryptography
prerequisites:
- id: oblivious-transfer
  type: hard
- id: symmetric-encryption-block-ciphers
  type: hard
tags:
- garbled-circuit
- yao-protocol
- two-party-computation
- free-xor
- half-gates
stage: expert
status: validated
---

# Garbled Circuits

## Core Idea
Yao's garbled circuits enable two-party secure computation. The garbler converts a Boolean circuit into a "garbled" version where each wire carries random labels instead of 0/1 values, and each gate's truth table is encrypted so that knowing input labels reveals only the output label — not whether it represents 0 or 1. The evaluator obtains their input labels via oblivious transfer and evaluates the garbled circuit gate by gate, learning only the final output. Key optimizations (point-and-permute, free XOR, half-gates) reduce cost from 4 ciphertexts per gate to 1.5 for AND gates and zero for XOR gates, making garbled circuits practical for real applications.

## Questions

```yaml
- question: "In a garbled gate, the garbler encrypts four entries: one for each combination of input labels. The evaluator has one label per input wire and can decrypt exactly one entry. Why can't the evaluator try all four entries to learn extra information?"
  type: short-answer
  answer: "Each entry is encrypted under the corresponding pair of input labels using a symmetric cipher (keyed hash or AES). The evaluator knows only one label per wire, giving them exactly one valid decryption key pair. The other three entries decrypt to random-looking garbage because the evaluator doesn't have the correct key pairs. With point-and-permute optimization, each label includes a signal bit that directly identifies which entry to decrypt, so the evaluator doesn't even attempt the others."
  explanation: "The encryption ensures that each combination of input labels acts as a unique key. Without both correct labels, decryption produces meaningless output. This is the core mechanism that hides intermediate wire values — the evaluator computes the correct function but never learns whether any intermediate wire carried 0 or 1."

- question: "The 'free XOR' optimization allows XOR gates to be evaluated without any ciphertext or communication. How does this work?"
  type: multiple-choice
  options:
    - "XOR gates are removed from the circuit during preprocessing"
    - "The garbler chooses a global random offset R. For every wire, the two labels differ by XOR with R (label_1 = label_0 XOR R). XOR gate output labels are computed as the XOR of input labels: if label_a and label_b are inputs, the output label is label_a XOR label_b, which automatically encodes the XOR of the underlying bits due to the algebraic relationship with R"
    - "XOR gates use a special hash function that requires no encryption"
    - "The evaluator already knows XOR results from the input labels without computation"
  answer: 1
  explanation: "The free XOR technique (Kolesnikov-Schneider 2008) is one of the most important garbled circuit optimizations. By maintaining the invariant that labels for 0 and 1 on every wire differ by the same global R, XOR gates require zero ciphertexts and zero communication — just a local XOR of labels. Since many circuits are rich in XOR gates (especially those designed with this optimization in mind), this dramatically reduces both communication and computation."

- question: "A garbled circuit can only be evaluated once. If the evaluator could evaluate it on two different inputs, they could learn the garbler's input."
  type: true-false
  answer: true
  explanation: "Each garbled gate entry is encrypted under specific input labels. If the evaluator learns labels for both 0 and 1 on any wire (by evaluating with different inputs), they can decrypt multiple entries per gate, eventually reconstructing the full truth table and recovering the garbler's input. This one-time-use property means each computation requires a fresh garbled circuit. This is a significant practical constraint, driving research into reusable garbled circuits and alternative MPC approaches for repeated computations."

- question: "Half-gates (Zahur-Rosulek-Evans 2015) reduce the cost of a garbled AND gate from 3 ciphertexts to 2. What is the conceptual idea?"
  type: multiple-choice
  options:
    - "Half-gates split the circuit in half, garbling each half independently"
    - "An AND gate is decomposed into two 'half-gates': one where the garbler knows one input bit, and one where the evaluator knows one input bit. Each half-gate requires only one ciphertext (using the free XOR technique internally), totaling 2 ciphertexts per AND gate"
    - "Half-gates use elliptic curve operations to compress the gate representation"
    - "The optimization skips half the AND gates by approximating the circuit"
  answer: 1
  explanation: "Half-gates exploit the observation that AND(a,b) can be decomposed based on which party knows which input. The garbler-half-gate handles the case where the garbler knows bit a (from their input), requiring 1 ciphertext. The evaluator-half-gate handles the case where the evaluator knows bit b (from their input), requiring 1 ciphertext. The final output combines both half-gates using free XOR. This is provably optimal: 2 ciphertexts per AND gate is the minimum for garbled circuits under standard techniques."

- question: "Garbled circuits achieve security against semi-honest adversaries directly. Achieving security against malicious adversaries requires additional techniques."
  type: true-false
  answer: true
  explanation: "In the semi-honest model, both parties follow the protocol but try to learn extra information from the transcript. Yao's basic protocol is secure here. Against malicious adversaries (who may deviate arbitrarily), additional protections are needed: the garbler might construct an incorrect circuit, and the evaluator might use OT maliciously. Techniques include cut-and-choose (the garbler sends multiple garbled circuits and the evaluator randomly checks some, evaluating the rest), authenticated garbling, and dual execution. These add overhead but are necessary for strong security guarantees."
```

## Explainer

**Yao's garbled circuits** (1986) are the foundational technique for two-party secure computation. The idea is elegant: convert the function to be computed into a Boolean circuit, then "garble" the circuit so it can be evaluated on encrypted values without revealing any intermediate results. The construction involves two parties — the **garbler** (who builds the garbled circuit) and the **evaluator** (who evaluates it) — and achieves the remarkable property that the evaluator learns the function's output but nothing else, while the garbler learns nothing at all.

The garbling process works as follows. For each wire in the circuit, the garbler generates two random labels — one representing 0 and one representing 1. For each gate, the garbler creates a **garbled truth table**: four entries, one for each combination of input values, where each entry encrypts the corresponding output label under the two input labels. The entries are randomly permuted so their position doesn't reveal information. The garbler sends the garbled circuit (all garbled truth tables) to the evaluator, along with the labels corresponding to the garbler's own input bits. The evaluator obtains labels for their own input bits via **oblivious transfer** (ensuring the garbler doesn't learn the evaluator's input). The evaluator then evaluates gate by gate: for each gate, they use their two input labels to decrypt exactly one truth table entry, obtaining the output label. At the final output wires, a decoding table maps labels back to 0/1.

Three optimizations have transformed garbled circuits from a theoretical construct into a practical tool. **Point-and-permute** attaches a signal bit to each label, allowing the evaluator to identify the correct truth table entry directly (without trial decryption), reducing from 4 decryption attempts to 1. **Free XOR** establishes a global offset R such that the two labels on every wire differ by R; XOR gates then require zero ciphertexts — the output label is simply the XOR of input labels. **Half-gates** reduce AND gate cost from 3 to 2 ciphertexts by decomposing each AND into two specialized "half-gates." Together, these optimizations mean a garbled circuit costs essentially 2 AES evaluations per AND gate and nothing per XOR gate.

The main limitations of garbled circuits are **one-time use** (each garbled circuit can be evaluated only once, requiring a fresh circuit per computation) and **linear communication** (the garbled circuit must be transmitted in its entirety, costing bandwidth proportional to the circuit size). For repeated evaluations of the same function, secret-sharing-based MPC protocols (like SPDZ) may be more efficient because they amortize setup cost. Garbled circuits excel for one-shot computations and when minimizing round complexity is important (the basic protocol requires only constant rounds of interaction). Modern MPC frameworks like EMP-toolkit and ABY combine garbled circuits with other techniques, automatically selecting the most efficient approach for each sub-computation.
