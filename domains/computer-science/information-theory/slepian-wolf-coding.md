---
id: slepian-wolf-coding
title: Slepian-Wolf Coding
domain: computer-science
course: information-theory
prerequisites:
- id: joint-and-conditional-entropy
  type: hard
- id: source-coding-theorem
  type: hard
- id: network-information-theory
  type: soft
tags:
- Slepian-Wolf
- distributed compression
- correlated sources
- lossless
stage: expert
status: validated
---

# Slepian-Wolf Coding

## Core Idea
The Slepian-Wolf theorem characterizes the achievable rate region for distributed lossless compression of correlated sources. Two encoders observe correlated sources X and Y respectively and compress them independently (no communication between encoders), while a joint decoder reconstructs both. The achievable rate region is R_X >= H(X|Y), R_Y >= H(Y|X), and R_X + R_Y >= H(X,Y). Remarkably, the sum rate H(X,Y) matches what is achievable with joint encoding — distributed compression loses nothing in total rate compared to centralized compression. This surprising result shows that correlation can be exploited even without encoder cooperation.

## Questions

```yaml
- question: "Two sensors observe correlated data X and Y with H(X) = 4, H(Y) = 3, H(X,Y) = 5 bits. What are the Slepian-Wolf rate constraints?"
  type: multiple-choice
  options:
    - "R_X >= 4 and R_Y >= 3, totaling at least 7 bits — each source must be compressed independently"
    - "R_X >= H(X|Y) = 2, R_Y >= H(Y|X) = 1, and R_X + R_Y >= H(X,Y) = 5 — the sum rate equals joint encoding, despite no communication between encoders"
    - "R_X = R_Y = H(X,Y)/2 = 2.5 bits each"
    - "R_X >= 0 and R_Y >= 0 with no sum constraint"
  answer: 1
  explanation: "H(X|Y) = H(X,Y) - H(Y) = 5-3 = 2. H(Y|X) = H(X,Y) - H(X) = 5-4 = 1. The Slepian-Wolf region requires each rate to be at least the conditional entropy and the sum to be at least the joint entropy. The corner points are (R_X, R_Y) = (2, 3) or (4, 1). At (2, 3), encoder X sends only the 'new information' about X given Y, and encoder Y sends H(Y) = 3 bits. At (4, 1), the roles reverse. The sum R_X + R_Y >= 5 = H(X,Y) matches centralized compression — no rate penalty for distributed encoding."

- question: "The Slepian-Wolf theorem requires the encoders to know each other's source statistics but NOT each other's actual source realizations."
  type: true-false
  answer: true
  explanation: "The encoders must know the joint distribution p(x,y) to design their codebooks, but they do NOT need to see each other's actual data — they encode independently based only on their own observations. The decoder, which sees both compressed streams, uses knowledge of the correlation to jointly decode. This is the surprising part: the correlation is exploited at the DECODER, not the encoder. Random binning (the proof technique) assigns source sequences to bins, and the joint typicality decoder uses the correlation structure to identify the correct sequences from their bins."

- question: "Explain the intuition behind why distributed compression (Slepian-Wolf) can achieve the same sum rate as joint compression, despite the encoders not communicating."
  type: short-answer
  answer: "The key insight is that the correlation between X and Y is a property of the SOURCES, not of the encoding. The decoder sees both compressed representations and knows the joint distribution. Even though encoder X does not know Y's realization, encoder X can use random binning to send only H(X|Y) bits — the 'new information' in X that Y does not contain. The decoder, knowing both the bin index of X and the actual value of Y (or Y's bin index), uses joint typicality to uniquely recover X. The decoder effectively provides the 'side information' that each encoder lacks. The total information transmitted is H(X|Y) + H(Y) = H(X,Y), matching joint encoding."
  explanation: "Random binning is the proof technique: each typical sequence of X is randomly assigned to one of 2^(nR_X) bins. With high probability, the joint typicality decoder can identify the unique X-sequence in the bin that is jointly typical with Y. This works because the bin is large enough to contain many X-sequences but only one that is jointly typical with the actual Y."
```

## Explainer

Consider two sensors monitoring correlated data — say, temperature sensors at nearby locations. If both sensors could share their data before compression, they could jointly compress to H(X,Y) bits total. But what if they must compress independently and only a central server sees both compressed streams? Intuitively, you might expect a penalty for the lack of coordination. The Slepian-Wolf theorem says there is none: the sum rate achievable with distributed compression equals H(X,Y), the same as joint compression.

The achievable rate region is a pentagon defined by three constraints: R_X >= H(X|Y), R_Y >= H(Y|X), and R_X + R_Y >= H(X,Y). The corner point (H(X|Y), H(Y)) represents encoder X sending only the information in X that Y does not have, while encoder Y sends its full entropy. The other corner (H(X), H(Y|X)) reverses the roles. All points on the dominant face R_X + R_Y = H(X,Y) are achievable by time-sharing or random binning.

The proof uses **random binning**, one of the most important techniques in information theory. Each typical X-sequence is randomly assigned to a bin (index). The encoder for X sends only the bin index, using about nH(X|Y) bits. The decoder receives the bin index and the full (or binned) Y-sequence. Among all X-sequences in the bin, the decoder finds the unique one that is jointly typical with Y. This works because the bin contains about 2^(n(H(X)-H(X|Y))) = 2^(nI(X;Y)) sequences, but only one is jointly typical with Y — the correct one. The correlation acts as "side information" at the decoder that disambiguates the bin.

Slepian-Wolf coding has practical applications in distributed sensor networks, video coding (where multiple camera views have correlation but are encoded independently), and genomic compression (where related genomes have high correlation). The Wyner-Ziv extension handles lossy distributed compression with decoder side information. These results demonstrate a recurring theme in network information theory: information-theoretic limits are often more favorable than naive intuition suggests, because joint decoding can exploit structure that separate encoding cannot.
