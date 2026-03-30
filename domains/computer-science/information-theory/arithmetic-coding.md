---
id: arithmetic-coding
title: Arithmetic Coding
domain: computer-science
course: information-theory
prerequisites:
- id: source-coding-theorem
  type: hard
- id: shannon-entropy
  type: hard
- id: huffman-coding
  type: soft
builds-toward:
- data-compression-basics
tags:
- arithmetic coding
- lossless compression
- entropy coding
- interval coding
stage: advanced
status: validated
---

# Arithmetic Coding

## Core Idea
Arithmetic coding represents an entire message as a single number in the interval [0, 1), achieving compression rates arbitrarily close to the source entropy. Unlike Huffman coding, which assigns a discrete codeword to each symbol, arithmetic coding encodes sequences by successively narrowing a subinterval: each symbol shrinks the current interval proportionally to its probability. The final interval width is the product of all symbol probabilities, and specifying a point within it requires approximately -log2 of that product = sum of -log2(p_i) bits — exactly the information content. Arithmetic coding is theoretically optimal and is the basis of modern entropy coders like ANS (asymmetric numeral systems).

## Questions

```yaml
- question: "Why can arithmetic coding achieve rates closer to entropy than Huffman coding, especially for highly skewed distributions?"
  type: multiple-choice
  options:
    - "Arithmetic coding uses a larger alphabet internally"
    - "Arithmetic coding effectively assigns fractional bit lengths to symbols — a symbol with probability 0.9 uses only -log2(0.9) ≈ 0.15 bits — while Huffman is limited to integer-length codewords (minimum 1 bit per symbol)"
    - "Arithmetic coding compresses each symbol independently with a better algorithm"
    - "Huffman coding is not actually prefix-free, causing decoding overhead"
  answer: 1
  explanation: "Huffman coding must assign at least 1 bit per symbol, so for a source with a 0.9-probability symbol (entropy ≈ 0.469 bits/symbol), Huffman wastes ~0.531 bits per symbol. Arithmetic coding encodes the entire sequence as one number, effectively amortizing the cost across many symbols. A symbol with probability 0.9 narrows the interval by a factor of 0.9, costing only -log2(0.9) ≈ 0.152 bits of interval precision. Over long sequences, the average rate approaches entropy to within a negligible rounding overhead."

- question: "Arithmetic coding can compress a sequence of n symbols from a memoryless source to within 2 bits of nH(X) regardless of the distribution."
  type: true-false
  answer: true
  explanation: "The total compressed length for an arithmetic code on n i.i.d. symbols is between nH(X) and nH(X) + 2 bits (the +2 accounts for specifying a point in the final interval and termination overhead). The per-symbol overhead is at most 2/n bits, which vanishes as n grows. This is a much tighter bound than Huffman's guarantee of H(X) to H(X) + 1 per symbol, and the advantage is especially large for skewed distributions where Huffman's integer constraint causes significant waste."

- question: "In arithmetic coding, encoding the message 'ABAC' given P(A)=0.6, P(B)=0.3, P(C)=0.1 involves narrowing an interval four times. Explain the process conceptually and why the final interval width equals the probability of the specific message."
  type: short-answer
  answer: "Start with [0, 1). Partition it according to symbol probabilities: A gets [0, 0.6), B gets [0.6, 0.9), C gets [0.9, 1.0). The first symbol A selects [0, 0.6). Within this interval, re-partition proportionally: A->[0, 0.36), B->[0.36, 0.54), C->[0.54, 0.6). The second symbol B selects [0.36, 0.54). Continue: within [0.36, 0.54), A selects [0.36, 0.468), then C selects [0.462, 0.468). The final interval has width 0.006 = 0.6 * 0.3 * 0.6 * 0.1 = P(ABAC). The compressed message is any binary fraction inside this interval, requiring approximately -log2(0.006) ≈ 7.38, so about 8 bits. The key insight: the interval width equals the sequence probability, so more probable sequences yield wider intervals requiring fewer bits to specify."
  explanation: "This is why arithmetic coding achieves entropy: the number of bits to specify a point in an interval of width w is about -log2(w) = -sum log2(p_i) = sum of self-information values. The total bits used equals the total information content of the specific message."
```

## Explainer

Huffman coding assigns integer-length codewords to individual symbols, which limits it to at most 1 bit above entropy per symbol. Arithmetic coding removes this limitation by encoding entire messages as single numbers, effectively achieving fractional bit lengths per symbol.

The idea is beautifully simple. The unit interval [0, 1) is partitioned among the alphabet symbols proportionally to their probabilities. The first symbol in the message selects the corresponding subinterval. That subinterval is then partitioned again in the same proportions, and the second symbol selects a sub-subinterval. This continues for every symbol. After processing the entire message, you have a tiny interval whose width equals the probability of the specific message (the product of all symbol probabilities for i.i.d. sources). To transmit the message, you send enough bits to uniquely identify a point inside that interval — approximately -log2(width) bits.

The magic is that -log2(product of probabilities) = sum of -log2(p_i), which is exactly the information content of the message. More probable messages produce wider intervals requiring fewer bits; improbable messages produce narrow intervals requiring more bits. Over many symbols, the average rate converges to the entropy H(X). The overhead is at most 2 bits for the entire message (to handle interval boundaries and termination), making the per-symbol overhead negligible for long sequences.

In practice, arithmetic coding operates on integers using finite-precision arithmetic, with a "renormalization" step that outputs bits as the interval narrows and shifts, keeping the working precision manageable. Modern variants like **ANS (asymmetric numeral systems)**, used in Facebook's Zstandard and Apple's LZFSE, achieve the same theoretical optimality with higher throughput by encoding the state as a single integer rather than maintaining interval endpoints. Context-adaptive arithmetic coding (as in H.265/HEVC video compression) pairs the arithmetic coder with a sophisticated context model, achieving compression rates that track the conditional entropy given recent context — far surpassing what per-symbol Huffman can achieve.
