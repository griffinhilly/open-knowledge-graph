---
id: source-coding-theorem
title: Source Coding Theorem
domain: computer-science
course: information-theory
prerequisites:
- id: shannon-entropy
  type: hard
- id: probability-distributions
  type: hard
builds-toward:
- huffman-coding
- arithmetic-coding
- data-compression-basics
- typical-sequences-aep
tags:
- source coding
- lossless compression
- noiseless coding
- Shannon
- first theorem
stage: advanced
status: validated
---

# Source Coding Theorem

## Core Idea
Shannon's source coding theorem (noiseless coding theorem) states that the entropy H(X) of a source is the fundamental limit of lossless compression. No lossless code can achieve an average rate below H(X) bits per symbol, and there exist codes that get arbitrarily close to H(X). For a sequence of n i.i.d. symbols, the compressed length approaches nH(X) bits as n grows. This theorem established entropy as the operationally meaningful measure of information content and launched the field of information theory.

## Questions

```yaml
- question: "A source produces symbols from an alphabet of size 8 with entropy H = 2.5 bits/symbol. A naive fixed-length encoding uses 3 bits per symbol. What does the source coding theorem guarantee about compression?"
  type: multiple-choice
  options:
    - "No code can do better than 3 bits per symbol because the alphabet has 8 symbols"
    - "There exist codes achieving average rate arbitrarily close to 2.5 bits per symbol, but no lossless code can go below 2.5"
    - "Shannon's theorem guarantees a code achieving exactly 2.5 bits per symbol for every individual sequence"
    - "The savings of 0.5 bits per symbol is not achievable because Huffman codes require integer-length codewords"
  answer: 1
  explanation: "The source coding theorem sets the limit at H = 2.5 bits/symbol. Codes like arithmetic coding can get arbitrarily close to this limit for long sequences. Option 3 is wrong because the theorem is about average rate over long sequences, not individual sequences. Option 4 is wrong because while Huffman coding is limited to integer-length codewords (achieving between H and H+1 bits per symbol), arithmetic coding and block Huffman codes can approach H arbitrarily closely."

- question: "The source coding theorem guarantees that every individual sequence from a source with entropy H can be compressed to exactly H bits per symbol."
  type: true-false
  answer: false
  explanation: "The source coding theorem is an asymptotic, average-case result. It guarantees that the AVERAGE code length per symbol approaches H as the block length grows to infinity. Individual sequences may compress to more or fewer bits. Some sequences (like all-zeros from a biased source) compress much below H; others (rare sequences) require more. What the theorem rules out is an average rate below H — over many sequences drawn from the source, you cannot beat entropy on average."

- question: "A colleague claims to have developed a lossless compression algorithm that compresses every possible file to a smaller file. Use the source coding theorem (or a counting argument) to explain why this is impossible."
  type: short-answer
  answer: "If the algorithm maps every n-bit file to a shorter file, then all 2^n possible inputs would map to files of at most n-1 bits. But there are only 2^0 + 2^1 + ... + 2^(n-1) = 2^n - 1 shorter files. By the pigeonhole principle, at least two inputs must map to the same output, making the mapping non-invertible and thus not lossless. More fundamentally, the source coding theorem says the average compressed length cannot be below H, and for a uniform distribution over all n-bit strings, H = n bits — there is no redundancy to exploit. Any compression algorithm that shrinks some files must expand others."
  explanation: "This is one of the most important consequences of information theory: universal compression of all data is impossible. Compression works by exploiting statistical redundancy in the source. Random or already-compressed data has near-maximum entropy and cannot be further compressed. Claims of universal compression algorithms are a reliable indicator of misunderstanding."
```

## Explainer

Shannon entropy tells you the average uncertainty per symbol. The source coding theorem gives this number operational teeth: entropy is the compression limit. If a source has entropy H bits per symbol, you need at least H bits per symbol on average to represent the output losslessly, and you can get arbitrarily close to H with a sufficiently clever code.

The achievability proof relies on the concept of **typical sequences**. For a long sequence of n i.i.d. symbols from a source with entropy H, the law of large numbers implies that the empirical frequency of each symbol concentrates around its true probability. The "typical set" — sequences whose empirical statistics match the source distribution — contains approximately 2^(nH) sequences, even though the total number of possible sequences is |alphabet|^n = 2^(n log |alphabet|). Since 2^(nH) << 2^(n log |alphabet|) when H < log|alphabet|, we only need nH bits to index the typical sequences. Atypical sequences have negligible total probability and can be handled with a small overhead.

The converse — that you cannot beat H — follows from the non-negativity of KL divergence. Any lossless code induces a probability distribution over codewords, and the expected codeword length is at least the entropy of the source. Attempting to assign shorter codewords to all symbols violates the Kraft inequality (the constraint that ensures unique decodability). Shorter codes for some symbols necessarily mean longer codes for others, and the probability-weighted average cannot go below H.

The practical impact is enormous. Before Shannon, engineers designed compression schemes by intuition and heuristics. After Shannon, there was a target: entropy. Huffman coding (1952) achieves within 1 bit of entropy per symbol. Arithmetic coding achieves within a fraction of a bit. Modern compressors (gzip, zstd, lossless PNG) all operate in the shadow of this theorem, exploiting statistical redundancy to approach the entropy rate of their input. The theorem also explains why some data cannot be compressed: truly random data has maximum entropy, and no algorithm can shrink it.
