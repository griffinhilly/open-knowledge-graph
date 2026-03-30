---
id: huffman-coding
title: Huffman Coding
domain: computer-science
course: information-theory
prerequisites:
- id: source-coding-theorem
  type: hard
- id: shannon-entropy
  type: hard
builds-toward:
- data-compression-basics
tags:
- Huffman coding
- prefix code
- optimal code
- variable-length
- lossless compression
stage: advanced
status: validated
---

# Huffman Coding

## Core Idea
Huffman coding is an optimal prefix-free variable-length coding scheme for lossless compression of a known discrete source. It assigns shorter codewords to more probable symbols and longer codewords to less probable ones, achieving the minimum expected codeword length among all prefix codes. The algorithm builds a binary tree bottom-up by repeatedly merging the two least probable symbols. The resulting code satisfies H(X) <= L < H(X) + 1, where L is the average code length and H(X) is the source entropy. Huffman coding is optimal per-symbol; arithmetic coding can outperform it by encoding sequences as a whole.

## Questions

```yaml
- question: "A source has four symbols with probabilities {0.5, 0.25, 0.125, 0.125}. What is the Huffman code, and what is its average length?"
  type: multiple-choice
  options:
    - "All symbols get 2-bit codes; average length = 2 bits"
    - "Codewords: 0, 10, 110, 111; average length = 1*0.5 + 2*0.25 + 3*0.125 + 3*0.125 = 1.75 bits"
    - "Codewords: 00, 01, 10, 11; average length = 2 bits"
    - "Codewords: 0, 1, 00, 01; average length = 1.25 bits"
  answer: 1
  explanation: "Huffman's algorithm merges the two smallest (0.125 + 0.125 = 0.25), then the two smallest remaining (0.25 + 0.25 = 0.5), then the final two (0.5 + 0.5 = 1.0). This produces codewords of length 1, 2, 3, 3. The average length is 1.75 bits, which exactly equals the entropy H = -0.5*log2(0.5) - 0.25*log2(0.25) - 2*0.125*log2(0.125) = 1.75 bits. When probabilities are all powers of 2, Huffman coding achieves entropy exactly."

- question: "Huffman codes are guaranteed to achieve the exact entropy rate H(X) for any source distribution."
  type: true-false
  answer: false
  explanation: "Huffman codes achieve average length L satisfying H(X) <= L < H(X) + 1 bits per symbol. They reach H(X) exactly only when all probabilities are powers of 2 (like 1/2, 1/4, 1/8). For other distributions, the constraint of integer-length codewords forces L above H(X). For example, a source with two equally likely symbols has H = 1 bit, and Huffman achieves L = 1. But a source with p(A) = 0.9, p(B) = 0.1 has H ≈ 0.469, while Huffman gives both symbols 1-bit codes (L = 1), wasting 0.531 bits/symbol. Arithmetic coding can approach H more closely."

- question: "Why must a practical compression code be prefix-free (no codeword is a prefix of another), and how does Huffman coding guarantee this property?"
  type: short-answer
  answer: "A prefix-free code allows instantaneous, unambiguous decoding: as bits arrive, the decoder can identify the end of each codeword without looking ahead or needing delimiters. If a codeword were a prefix of another, the decoder would face ambiguity when it encounters the shorter pattern — it wouldn't know whether the symbol ends here or continues. Huffman coding guarantees prefix-freeness by construction: symbols are assigned to LEAVES of a binary tree. Since no leaf is an ancestor of another leaf, no codeword is a prefix of another. The tree structure means each codeword corresponds to a unique path from root to leaf."
  explanation: "The Kraft inequality, sum 2^(-l_i) <= 1 where l_i are codeword lengths, is the mathematical condition for the existence of a prefix-free code with those lengths. Huffman's algorithm finds the assignment that minimizes expected length subject to this constraint."

- question: "A colleague proposes using Huffman coding on individual bytes of a file for compression. Why might this perform poorly compared to more sophisticated methods?"
  type: short-answer
  answer: "Per-byte Huffman coding only exploits the frequency distribution of individual bytes, ignoring correlations between consecutive bytes. Natural data has substantial sequential structure — in English text, 'q' is almost always followed by 'u'; in code, opening braces predict closing braces. Per-byte Huffman treats each byte independently, missing all this context. Better approaches include: block Huffman (encoding multi-byte sequences), adaptive Huffman (updating the code as statistics change), or using Huffman as a backend after a context model (as LZ77+Huffman in gzip does). Arithmetic coding on a context model can approach the true conditional entropy H(X_n | X_{n-1}, ..., X_1), which is much lower than the marginal byte entropy."
  explanation: "This is why practical compressors combine modeling and coding. The model captures statistical structure (LZ77 captures repeated patterns, PPM captures character-level context), and the coder (Huffman or arithmetic) converts the model's predictions into a compressed bitstream. Huffman coding alone is a coder without a model."
```

## Explainer

The source coding theorem says you can compress a source to its entropy rate, but it doesn't tell you how. Huffman coding, invented by David Huffman in 1952 as a student at MIT, provides a concrete, optimal algorithm for constructing variable-length binary codes for known discrete sources.

The algorithm is simple and elegant. Start with each symbol as a leaf node weighted by its probability. Repeatedly find the two nodes with the smallest weights, merge them into a new internal node whose weight is the sum, and assign the left branch a 0 and the right branch a 1 (or vice versa). Continue until only one root node remains. Each symbol's codeword is the sequence of bits on the path from the root to its leaf. More probable symbols end up near the root (short codewords); less probable symbols end up deeper in the tree (long codewords).

The resulting code is **prefix-free** — no codeword is a prefix of any other — which means the decoder can identify each symbol immediately without needing lookahead or delimiters. It is **optimal** among all prefix-free codes for that source: no other assignment of variable-length codewords achieves a lower expected length. The average code length L satisfies H(X) <= L < H(X) + 1. The gap comes from the restriction to integer-length codewords. When all symbol probabilities are powers of 2, the gap is zero and Huffman achieves entropy exactly.

Despite its elegance, Huffman coding has limitations. It works on one symbol at a time, so it cannot exploit correlations between symbols. It requires knowing the source statistics in advance (or using a two-pass approach). And the integer-length constraint means it can waste nearly 1 bit per symbol for highly skewed distributions. Arithmetic coding addresses all three limitations: it encodes entire sequences as a single number in [0,1), achieving rates arbitrarily close to entropy for any distribution. In practice, Huffman coding remains widely used (JPEG, DEFLATE/gzip) because it is fast, simple to implement, and the per-symbol overhead is acceptable for many applications.
