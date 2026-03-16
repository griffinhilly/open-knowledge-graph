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

## Explainer

From your study of Markov chains, you know that a system's future state depends only on its current state, not on how it got there. A **Hidden Markov Model (HMM)** adds a crucial twist: you cannot directly observe the states. Instead, each hidden state produces an observable output (called an **emission**) according to a probability distribution. You see the sequence of emissions but must infer the hidden states that generated them. The model is defined by three components: the transition probabilities (how likely is state j given that we are in state i), the emission probabilities (how likely is observation o given hidden state i), and the initial state distribution (which state does the system start in).

The classic teaching example makes this concrete. Suppose a friend lives in another city and tells you each day whether they went for a walk, shopped, or cleaned the house. You want to infer the weather in their city (sunny or rainy) from their activities. The weather is the hidden state — you never observe it directly. The activity is the emission — observable but only probabilistically related to the weather. On sunny days, your friend probably walks; on rainy days, they probably clean. The transition probabilities capture weather patterns (sunny days tend to follow sunny days), and the emission probabilities capture behavior given weather. Given a sequence of activities over a week, you want to figure out the most likely weather sequence.

This gives rise to three fundamental problems that HMMs solve. The **evaluation problem** asks: given a model and a sequence of observations, what is the probability of that sequence? The **forward algorithm** solves this efficiently using dynamic programming — instead of summing over all possible hidden state sequences (exponentially many), it builds up the answer left to right, at each time step computing the probability of being in each state having generated the observations so far. The **decoding problem** asks: what is the most likely sequence of hidden states? The **Viterbi algorithm** is structurally similar to the forward algorithm but replaces summation with maximization, tracking the best path into each state at each time step and backtracking at the end to recover the full optimal sequence.

The third problem — **learning** — is solved by the **Baum-Welch algorithm**, an instance of Expectation-Maximization (EM). Given only observed sequences (no labeled hidden states), Baum-Welch iteratively re-estimates the transition and emission probabilities to maximize the data likelihood. It alternates between computing expected state occupancies and transitions given the current parameters (the E-step, using the forward-backward algorithm) and updating the parameters to match those expectations (the M-step). Like all EM algorithms, it converges to a local maximum, making initialization important. HMMs have been foundational in speech recognition (hidden states = phonemes, observations = acoustic features), computational biology (hidden states = gene regions, observations = DNA bases), and any domain where you observe noisy outputs from a structured but invisible process.
