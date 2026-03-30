---
id: channel-capacity
title: Channel Capacity
domain: computer-science
course: information-theory
prerequisites:
- id: mutual-information
  type: hard
- id: shannon-entropy
  type: hard
builds-toward:
- channel-coding-theorem
- binary-symmetric-channel
- gaussian-channel
- multiple-access-channel
- broadcast-channel
tags:
- channel capacity
- noisy channel
- Shannon
- communication
stage: advanced
status: validated
---

# Channel Capacity

## Core Idea
The capacity of a discrete memoryless channel is C = max_{p(x)} I(X;Y), the maximum mutual information between input X and output Y over all possible input distributions. Capacity represents the highest rate (in bits per channel use) at which information can be transmitted with arbitrarily low error probability. The channel's noise characteristics are fixed; the only freedom is choosing the input distribution. Shannon showed that capacity is achievable — there exist coding schemes that transmit at any rate below C with error probability approaching zero — and that rates above C are impossible. This is the channel coding theorem, the most celebrated result in information theory.

## Questions

```yaml
- question: "A binary channel flips each bit independently with probability 0. What is the channel capacity, and what does this mean operationally?"
  type: multiple-choice
  options:
    - "C = 0 bits per use, because a noiseless channel carries no information"
    - "C = 1 bit per use, because each input bit arrives perfectly at the output, so every channel use conveys one full bit of information"
    - "C = 2 bits per use, because you can encode two bits per transmission in a noiseless channel"
    - "C = infinity, because there is no noise to limit transmission"
  answer: 1
  explanation: "With no noise, Y = X always, so H(Y|X) = 0 and I(X;Y) = H(Y). Maximizing H(Y) over binary inputs gives H(Y) = 1 bit (achieved by uniform input). So C = 1 bit per channel use. A noiseless binary channel transmits exactly 1 bit per use — each symbol perfectly distinguishes between the two possibilities. Capacity is limited by the alphabet size, not just the noise level."

- question: "Why does finding channel capacity require maximizing mutual information over the input distribution p(x), rather than simply computing I(X;Y) for any particular input?"
  type: multiple-choice
  options:
    - "Different input distributions change the channel's noise characteristics"
    - "The channel transition probabilities p(y|x) are fixed by the physical channel, but the input distribution p(x) determines how much of the channel's capacity is actually utilized — a poor input distribution wastes capacity"
    - "Maximization is required for mathematical convenience but has no operational significance"
    - "The input distribution must match the output distribution for reliable communication"
  answer: 1
  explanation: "The channel p(y|x) is given — it describes the physics of the medium. But the communicator chooses what to send. Different input distributions lead to different amounts of mutual information. For example, on a binary symmetric channel, using only the symbol '0' gives I(X;Y) = 0 (no information). Using uniform input maximizes I(X;Y). Capacity is the best you can do given the channel — it is a property of the channel itself, obtained by optimizing over the only degree of freedom available: what you choose to send."

- question: "If a channel has capacity C = 0 bits per use, reliable communication is impossible at any positive rate."
  type: true-false
  answer: true
  explanation: "C = 0 means the output Y provides zero information about the input X for every possible input distribution. The channel is completely useless — the output is statistically independent of the input. No coding scheme, no matter how sophisticated, can transmit any information reliably. This happens, for example, when the channel replaces every input with a fixed output regardless of what was sent, or when the noise completely overwhelms the signal."

- question: "Explain why channel capacity is a single number that characterizes the channel, even though mutual information depends on the input distribution."
  type: short-answer
  answer: "Capacity C = max_{p(x)} I(X;Y) takes the supremum over all possible input distributions, leaving only the channel's transition probabilities p(y|x) as the determining factor. Once you optimize over the input, the result depends only on the channel itself. This is why capacity is a property of the channel, not of any particular communication scheme. It answers: given this channel's noise structure, what is the absolute best any communicator could achieve? The optimal input distribution that achieves C depends on the channel but need not be known by the receiver."
  explanation: "For many important channels, the capacity-achieving distribution has a known form. For the binary symmetric channel, it is uniform. For the Gaussian channel, it is Gaussian. For general channels, the Blahut-Arimoto algorithm computes the capacity-achieving distribution iteratively."
```

## Explainer

A communication channel takes an input symbol and produces an output that may be corrupted by noise. The channel is characterized by its transition probabilities p(y|x) — for each input x, the probability of receiving each output y. The fundamental question is: how fast can you communicate reliably through this noisy channel?

Shannon's answer is **channel capacity**: C = max over all input distributions p(x) of the mutual information I(X;Y). The mutual information I(X;Y) = H(Y) - H(Y|X) measures how much the output reveals about the input. H(Y|X) is the "noise entropy" — the uncertainty in the output that is purely due to channel noise and carries no information about the input. H(Y) is the total output uncertainty. The difference is the useful information. By choosing p(x) to maximize this difference, you find the channel's intrinsic capacity.

The conceptual beauty is that capacity separates the problem into two parts. The channel capacity C is a fixed property of the physical medium. The coding scheme is the engineering that exploits it. Shannon proved that for any rate R < C, there exist codes (sequences of input symbols) that achieve error probability approaching zero as the block length grows. Conversely, for R > C, every code has error probability bounded away from zero. The coding theorem does not tell you how to construct good codes — it is an existence proof. The quest for practical codes that approach capacity drove decades of research, leading to turbo codes, LDPC codes, and polar codes, which come within a fraction of a dB of the Shannon limit.

For the **binary symmetric channel** (BSC) with crossover probability p, C = 1 - H(p) bits per use, where H(p) is the binary entropy function. When p = 0 (no noise), C = 1; when p = 1/2 (random output), C = 0. For the **Gaussian channel** with signal power P and noise power N, C = (1/2) log2(1 + P/N) bits per use — the famous Shannon-Hartley formula. These specific results are among the most important formulas in engineering, setting the theoretical limits for everything from Wi-Fi to deep-space communication.
