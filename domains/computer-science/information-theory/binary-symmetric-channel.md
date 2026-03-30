---
id: binary-symmetric-channel
title: Binary Symmetric Channel
domain: computer-science
course: information-theory
prerequisites:
- id: channel-capacity
  type: hard
- id: shannon-entropy
  type: hard
builds-toward:
- channel-coding-theorem
tags:
- BSC
- binary symmetric channel
- crossover probability
- binary entropy
stage: advanced
status: validated
---

# Binary Symmetric Channel

## Core Idea
The binary symmetric channel (BSC) is the simplest model of a noisy digital communication channel. It transmits binary symbols (0 or 1), and each bit is independently flipped with crossover probability p. Its capacity is C = 1 - H(p) bits per use, where H(p) = -p log p - (1-p) log(1-p) is the binary entropy function. The BSC is symmetric in that both symbols suffer the same error probability, making the capacity-achieving input distribution uniform. It serves as the fundamental testbed for channel coding theory and illustrates how noise reduces capacity from the ideal of 1 bit per use.

## Questions

```yaml
- question: "A BSC has crossover probability p = 0.5. What is the channel capacity, and what does this mean physically?"
  type: multiple-choice
  options:
    - "C = 0.5 bits — you can transmit at half the rate of a noiseless channel"
    - "C = 0 bits — the output is completely independent of the input, so no information passes through"
    - "C = 1 bit — noise has no effect because the channel is symmetric"
    - "C = -1 bits — the channel inverts all bits"
  answer: 1
  explanation: "When p = 0.5, each output bit is equally likely to be 0 or 1 regardless of the input — the channel is pure noise. H(0.5) = 1, so C = 1 - 1 = 0 bits. No communication is possible. The output is statistically independent of the input: knowing the output tells you nothing about what was sent. Interestingly, p = 1 (all bits inverted) gives C = 1 - H(1) = 1 - 0 = 1 bit — a perfect inverter is as good as a perfect channel because the receiver simply flips every bit."

- question: "A BSC has crossover probability p = 0.1. The capacity is C = 1 - H(0.1) ≈ 0.531 bits per use. A naive scheme sends each message bit once with no coding. What is its effective reliable rate?"
  type: multiple-choice
  options:
    - "0.531 bits per use — the same as capacity"
    - "0.9 bits per use — since 90% of bits arrive correctly"
    - "0 bits per use reliably — uncoded transmission has a 10% bit error rate, which means information is unreliable"
    - "1 bit per use — each channel use carries one bit regardless of errors"
  answer: 2
  explanation: "Without coding, each bit has a 10% chance of error. While 90% arrive correctly, there is no way for the receiver to know WHICH bits are wrong. 'Reliable' communication means error probability approaching zero, not just low. Uncoded transmission at any positive rate has non-vanishing error probability on a noisy channel. The channel coding theorem says you CAN achieve rates up to 0.531 bits/use with vanishing error — but only with error-correcting codes that add redundancy."

- question: "The binary entropy function H(p) is symmetric around p = 0.5 and reaches its maximum of 1 bit at p = 0.5. Explain why BSC capacity C = 1 - H(p) is also symmetric around p = 0.5 and what this means for p > 0.5."
  type: short-answer
  answer: "H(p) = H(1-p), so C(p) = 1 - H(p) = 1 - H(1-p) = C(1-p). The capacity is symmetric around p = 0.5. For p > 0.5, the channel flips bits more often than not — it is a 'mostly-inverting' channel. But an inverter is still informative: if p = 0.9, the receiver simply flips every received bit mentally, obtaining the equivalent of a channel with p = 0.1. The receiver can exploit systematic inversion just as easily as systematic preservation. Only at p = 0.5 — where flipping is equally likely as non-flipping — is the channel truly useless."
  explanation: "This symmetry is specific to the BSC. It shows that what matters for capacity is not the raw error rate but the predictability of the channel's behavior. Both very low and very high error rates are highly predictable (bits usually preserved vs. bits usually flipped), leaving capacity high. Only maximum randomness (p = 0.5) destroys all information."
```

## Explainer

The binary symmetric channel is the "hydrogen atom" of information theory — the simplest non-trivial channel model. It takes a binary input (0 or 1) and independently flips each bit with probability p. With probability 1-p the bit passes through correctly. "Symmetric" means both 0 and 1 suffer the same error probability; there is no bias toward one symbol.

The capacity calculation is elegant. Since the channel is symmetric, the capacity-achieving input distribution is uniform: p(X=0) = p(X=1) = 1/2. This maximizes H(Y) = 1 bit. The noise entropy is H(Y|X) = H(p) — given the input, the output is a Bernoulli(p) flip, whose entropy is the binary entropy H(p). So C = H(Y) - H(Y|X) = 1 - H(p). When p = 0 (no noise), C = 1 bit. When p = 1/2 (maximum noise), C = 0 bits. The capacity decreases smoothly as noise increases from 0 to 0.5, then increases back to 1 as p approaches 1 (because a perfect inverter is a perfect channel in disguise).

The BSC makes the channel coding theorem concrete. At p = 0.1, the capacity is about 0.531 bits per use. This means you can reliably transmit 531 bits of information per 1000 channel uses — but only with error-correcting codes that spread each information bit across many channel uses. Without coding, the 10% error rate is irrecoverable. With coding at rate R < C, the decoder can use the redundancy to identify and correct errors, achieving arbitrarily low error probability. The coding theorem guarantees this is possible; practical codes like LDPC and turbo codes come remarkably close.

The BSC also illustrates a general principle: channel symmetry simplifies capacity computation. For symmetric channels, the uniform input distribution is always optimal, and the capacity is the log of the output alphabet size minus the entropy of each row of the transition matrix. This shortcut avoids the need for numerical optimization (like the Blahut-Arimoto algorithm) that general channels require.
