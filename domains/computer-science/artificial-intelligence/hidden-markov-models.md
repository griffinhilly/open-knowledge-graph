---
id: hidden-markov-models
title: Hidden Markov Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-chains
  type: hard
- id: conditional-probability
  type: soft
- id: probability-mass-functions
  type: hard
- id: probability-axioms-and-rules
  type: soft
tags:
- markov-models
- sequence-models
- probabilistic-reasoning
stage: advanced
status: draft
---

# Hidden Markov Models

## Core Idea
HMMs model systems with hidden states emitting observable outputs, where state transitions follow Markov assumption. The forward algorithm computes likelihood, Viterbi decodes hidden states, and Baum-Welch learns parameters. Applications include speech recognition and sequence labeling.

## How It's Best Learned
Implement forward and Viterbi algorithms for weather prediction with hidden/observable variables.

## Common Misconceptions
Viterbi finds the most likely state sequence, not the most likely individual states. Baum-Welch convergence depends on initialization.

## Questions

```yaml
- question: "In an HMM, the Viterbi algorithm is used to find which of the following?"
  type: multiple-choice
  options:
    - "The probability of the observed sequence given the model"
    - "The most likely state at each individual time step, independently"
    - "The single most likely complete sequence of hidden states"
    - "Updated transition and emission probabilities from unlabeled data"
  answer: 2
  explanation: "Viterbi finds the most probable entire path — the complete sequence of hidden states that jointly maximizes the probability of the observations. This is subtly different from finding the individually most likely state at each time step (which the posterior marginals from the forward-backward algorithm provide). The distinction matters: it is possible for the Viterbi path to pass through states that are not the individually most probable at each step, because the joint probability of the full sequence depends on valid transitions. Option A is the evaluation problem (solved by the forward algorithm); option D is learning (solved by Baum-Welch)."

- question: "A speech recognizer observes a sequence of acoustic feature vectors. It uses an HMM where hidden states represent phonemes. What are the 'emissions' in this model?"
  type: multiple-choice
  options:
    - "The phonemes — they are inferred from the audio signal"
    - "The acoustic feature vectors — the directly observed output at each time step"
    - "The words — they are the final decoded output"
    - "The transition probabilities between phonemes"
  answer: 1
  explanation: "In an HMM, emissions are the observable outputs produced by each hidden state. Here, the acoustic feature vectors (measurable quantities from the audio) are the emissions — they are what you directly observe. The phonemes are the hidden states — they are what you are trying to infer. This is the core HMM structure: hidden states (phonemes) generate observable emissions (acoustic features) according to emission probabilities, and your goal is to decode the most likely state sequence from the observations."

- question: "The forward algorithm computes the probability of an observation sequence by dynamic programming, avoiding the need to enumerate all possible hidden state sequences."
  type: true-false
  answer: true
  explanation: "True. For a sequence of length T with K hidden states, the brute-force approach would sum over all K^T possible state sequences — exponential in T. The forward algorithm exploits the Markov property: the probability of being in state i at time t, having generated observations up to t, depends only on the probability of being in each state at time t-1 (not on earlier history). This allows left-to-right dynamic programming that runs in O(K²T) time rather than O(K^T)."

- question: "Baum-Welch is guaranteed to find the globally optimal HMM parameters if run to convergence."
  type: true-false
  answer: false
  explanation: "False. Baum-Welch is an instance of the Expectation-Maximization (EM) algorithm, which converges to a *local* maximum of the likelihood function, not necessarily the global one. The final parameters depend on initialization — different starting points can lead to different local optima. In practice, multiple random restarts are used to improve the chance of finding a good solution. Global optimality would require exhaustive search over parameter space, which is computationally intractable."

- question: "Explain why finding 'the most likely state sequence' (Viterbi) is a different problem from finding 'the most likely state at each time step,' and describe a case where the two answers could differ."
  type: short-answer
  answer: "The most likely state sequence maximizes the joint probability P(s₁, s₂, ..., sT | observations). The most likely state at each time step maximizes the marginal posterior P(sₜ | observations) independently. These can differ because the Viterbi path must follow valid transitions — a high-probability path through a state sequence must remain internally consistent. For example, if being in state A at time 2 is individually probable, but the transition from the best state at time 1 to A is very unlikely, the Viterbi algorithm might assign state B at time 2, even though B is marginally less probable at that step, because the overall joint sequence probability is higher."
  explanation: "This distinction matters for applications like gene finding or speech recognition where you need a coherent, consistent sequence rather than a set of independent per-step guesses. The per-step marginals (computed via the forward-backward algorithm) are useful for other tasks — computing expected state occupancies for Baum-Welch or quantifying uncertainty — but they can produce contradictory sequences (e.g., consecutive states with zero-probability transitions between them). Viterbi always produces a valid path."
```

## Explainer

From your study of Markov chains, you know that a system's future state depends only on its current state, not on how it got there. A **Hidden Markov Model (HMM)** adds a crucial twist: you cannot directly observe the states. Instead, each hidden state produces an observable output (called an **emission**) according to a probability distribution. You see the sequence of emissions but must infer the hidden states that generated them. The model is defined by three components: the transition probabilities (how likely is state j given that we are in state i), the emission probabilities (how likely is observation o given hidden state i), and the initial state distribution (which state does the system start in).

The classic teaching example makes this concrete. Suppose a friend lives in another city and tells you each day whether they went for a walk, shopped, or cleaned the house. You want to infer the weather in their city (sunny or rainy) from their activities. The weather is the hidden state — you never observe it directly. The activity is the emission — observable but only probabilistically related to the weather. On sunny days, your friend probably walks; on rainy days, they probably clean. The transition probabilities capture weather patterns (sunny days tend to follow sunny days), and the emission probabilities capture behavior given weather. Given a sequence of activities over a week, you want to figure out the most likely weather sequence.

This gives rise to three fundamental problems that HMMs solve. The **evaluation problem** asks: given a model and a sequence of observations, what is the probability of that sequence? The **forward algorithm** solves this efficiently using dynamic programming — instead of summing over all possible hidden state sequences (exponentially many), it builds up the answer left to right, at each time step computing the probability of being in each state having generated the observations so far. The **decoding problem** asks: what is the most likely sequence of hidden states? The **Viterbi algorithm** is structurally similar to the forward algorithm but replaces summation with maximization, tracking the best path into each state at each time step and backtracking at the end to recover the full optimal sequence.

The third problem — **learning** — is solved by the **Baum-Welch algorithm**, an instance of Expectation-Maximization (EM). Given only observed sequences (no labeled hidden states), Baum-Welch iteratively re-estimates the transition and emission probabilities to maximize the data likelihood. It alternates between computing expected state occupancies and transitions given the current parameters (the E-step, using the forward-backward algorithm) and updating the parameters to match those expectations (the M-step). Like all EM algorithms, it converges to a local maximum, making initialization important. HMMs have been foundational in speech recognition (hidden states = phonemes, observations = acoustic features), computational biology (hidden states = gene regions, observations = DNA bases), and any domain where you observe noisy outputs from a structured but invisible process.
