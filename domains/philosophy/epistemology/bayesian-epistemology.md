---
id: bayesian-epistemology
title: Bayesian Epistemology
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
- id: reliabilism
  type: soft
- id: probabilistic-reasoning
  type: hard
- id: probabilistic-computation
  type: soft
- id: bayesian-confirmation-and-evidence
  type: soft
tags:
- Bayesianism
- credences
- conditionalization
- Dutch-book
- probabilistic-coherence
stage: formal-systems
status: draft
---
# Bayesian Epistemology

## Core Idea
Bayesian epistemology replaces the traditional binary conception of belief (believe or not believe) with degrees of belief — credences — measured on a probability scale from 0 to 1. Rational agents, on this view, must satisfy two requirements: their credences at any given time must be probabilistically coherent (they must satisfy the axioms of probability), and they must update their credences by conditionalization when they receive new evidence — that is, their new credence in a hypothesis after receiving evidence E should equal their prior conditional probability of the hypothesis given E. The Dutch book argument provides a pragmatic justification: an agent whose credences violate probability axioms can be offered a series of bets that guarantee a net loss regardless of how the world turns out. Bayesian epistemology provides powerful tools for modeling confirmation, theory choice, and the accumulation of evidence, though it faces challenges regarding the selection of prior probabilities and the problem of old evidence.

## How It's Best Learned
Work through a concrete example: you suspect a coin is biased. Start with a prior credence of 0.5 that it is fair. Flip it ten times, observe the results, and update by Bayes' theorem. The mechanics of conditionalization become intuitive quickly, and the philosophical questions — where does the prior come from? what counts as evidence? — emerge naturally.

## Common Misconceptions
- Bayesian epistemology does not require that agents consciously perform probability calculations; it is a normative theory about the structure rational credences should have, not a descriptive theory of how people actually reason.
- The subjectivity of prior probabilities does not make Bayesianism relativistic; with sufficient shared evidence, agents with different priors will converge on the same posterior credences (the 'washing out' of priors).
