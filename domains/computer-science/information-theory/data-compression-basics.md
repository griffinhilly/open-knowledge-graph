---
id: data-compression-basics
title: Data Compression Basics
domain: computer-science
course: information-theory
prerequisites:
- id: source-coding-theorem
  type: hard
- id: huffman-coding
  type: hard
- id: arithmetic-coding
  type: soft
builds-toward:
- rate-distortion-theory
tags:
- data compression
- lossless
- lossy
- redundancy
- LZ77
- entropy coding
stage: advanced
status: validated
---

# Data Compression Basics

## Core Idea
Data compression reduces the number of bits needed to represent information by exploiting redundancy. Lossless compression (Huffman, arithmetic, LZ77, LZ78) allows perfect reconstruction and is bounded by the source entropy. Lossy compression (JPEG, MP3, H.264) sacrifices some fidelity for much higher compression ratios, governed by rate-distortion theory. Practical compressors combine a model (which identifies redundancy and predicts symbols) with a coder (which converts predictions into a compact bitstream). The model captures statistical structure; the coder approaches the entropy of the model's predictions.

## Questions

```yaml
- question: "A compressor uses LZ77 (sliding-window dictionary matching) followed by Huffman coding. What is the role of each component?"
  type: multiple-choice
  options:
    - "LZ77 provides lossy compression; Huffman provides lossless compression"
    - "LZ77 serves as the model, replacing repeated patterns with short references to reduce redundancy; Huffman serves as the entropy coder, compressing the references and literal symbols to near their entropy"
    - "LZ77 handles text data; Huffman handles binary data"
    - "Both perform the same function redundantly for error correction"
  answer: 1
  explanation: "This is the model-coder separation central to modern compression. LZ77 identifies and eliminates sequential redundancy by replacing repeated substrings with (distance, length) pairs pointing back to earlier occurrences. This transforms the data into a new representation with lower entropy. Huffman (or arithmetic) coding then compresses this representation close to its entropy. DEFLATE (used in gzip, PNG, ZIP) uses exactly this pipeline. The model captures structure; the coder converts it to bits."

- question: "A 1 MB file of truly random bytes (each byte uniformly and independently distributed) is fed to gzip. The output will be approximately:"
  type: multiple-choice
  options:
    - "Much smaller — gzip always compresses effectively"
    - "Approximately 1 MB plus a small overhead — random data has maximum entropy (8 bits/byte) and cannot be compressed"
    - "Exactly 0 bytes — gzip recognizes random data and discards it"
    - "Approximately 0.5 MB — compression always achieves at least 50% reduction"
  answer: 1
  explanation: "Truly random bytes have entropy 8 bits per byte — the maximum possible for a byte-valued source. The source coding theorem guarantees no lossless compressor can reduce this on average. gzip will find no repeated patterns (LZ77 matches) and the byte frequencies will be nearly uniform (no Huffman advantage). The output will be the original data plus gzip headers and metadata — slightly LARGER than 1 MB. This is a fundamental limit, not a deficiency of gzip."

- question: "Lossy compression can exceed the entropy limit that bounds lossless compression. Explain why this is not a contradiction."
  type: short-answer
  answer: "The entropy bound applies to LOSSLESS compression: if you must reconstruct the original data exactly, you need at least H bits per symbol. Lossy compression relaxes this requirement — it allows some distortion (error) in the reconstruction. By tolerating distortion D, you only need to distinguish between equivalence classes of sources that are within distance D of each other, not between every individual source. The number of distinguishable classes is smaller, requiring fewer bits. Rate-distortion theory formalizes this: the rate-distortion function R(D) gives the minimum bit rate needed to represent the source with average distortion at most D. R(0) = H (lossless), and R(D) decreases as D increases."
  explanation: "This is why JPEG (lossy) can compress a photo to 1/20th its raw size while PNG (lossless) might only achieve 1/2. Lossy compression exploits the fact that the human visual or auditory system cannot distinguish small differences, so the 'wasted' information is information the receiver doesn't need."
```

## Explainer

Data compression is the practical application of Shannon's source coding theorem. The theorem tells you the limit (entropy); compression algorithms try to approach it. Understanding compression requires separating two concerns: the **model** (what statistical structure does the data have?) and the **coder** (how do we turn predicted statistics into bits?).

**Lossless compression** guarantees perfect reconstruction. Entropy coding (Huffman, arithmetic) is the coder; it converts symbol probabilities into near-optimal bit assignments. But the entropy of raw bytes is high. The model's job is to reduce the effective entropy by capturing redundancy. LZ77 (used in gzip, DEFLATE) captures repeated substring patterns by replacing them with backward references. LZ78/LZW (used in classic GIF) builds a dictionary of seen patterns. PPM (prediction by partial matching) uses character-level context to predict the next symbol. Burrows-Wheeler Transform (used in bzip2) rearranges data to group similar characters together, making the result more compressible by subsequent entropy coding.

**Lossy compression** allows controlled degradation of the reconstructed output. JPEG transforms image blocks into frequency coefficients (via DCT), quantizes them (the lossy step — small coefficients are zeroed), and entropy-codes the result. MP3 uses a psychoacoustic model to identify sounds the human ear cannot perceive, then removes them. H.264/H.265 video codecs combine motion prediction (modeling temporal redundancy) with spatial prediction and quantization. In each case, the lossy step reduces the effective entropy of what remains, allowing the entropy coder to produce a much smaller output than any lossless method could.

The information-theoretic perspective unifies these: every compressor is trying to approach the entropy of the source (lossless) or the rate-distortion function (lossy). The gap between a compressor's output size and the theoretical limit reveals inefficiency — either the model is not capturing all the redundancy, or the coder is not converting predictions to bits efficiently. Modern machine-learned compressors (neural codecs for images, audio, and video) demonstrate that better models consistently yield better compression, validating the information-theoretic framework. Shannon's theorems do not just provide limits; they provide a blueprint.
