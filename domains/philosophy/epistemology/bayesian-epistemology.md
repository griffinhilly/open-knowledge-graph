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

## Explainer

Two threads from your prerequisites converge here. From **justified true belief**, you know that knowledge requires more than true belief — your belief must be backed by adequate justification, good reasons that connect your mental state to the truth. From **probabilistic reasoning**, you know that Bayes' theorem gives a precise formula for updating a probability estimate in light of new evidence: P(H|E) = P(E|H) × P(H) / P(E). Bayesian epistemology brings these together by asking a radical question: what if justification is not binary but comes in *degrees*?

The central move is replacing the binary picture of belief with **credences** — degrees of belief measured on a probability scale from 0 to 1. Rather than asking "does this agent believe P or not?", Bayesian epistemology asks "what is this agent's credence that P?" — a number representing how strongly the agent takes P to be true. Your credence that a fair coin will land heads is 0.5; your credence that the sun will rise tomorrow might be 0.9999. These **prior probabilities** represent your starting degrees of belief before receiving new evidence. When you observe evidence E, you update by **conditionalization**: your new credence in hypothesis H equals your old conditional credence in H given E — exactly what Bayes' theorem calculates. The mechanics are the same as probabilistic reasoning; the philosophical claim is that this is the *normative* standard for rational belief revision.

Why should credences satisfy the probability axioms? The **Dutch book argument** provides a pragmatic justification. If your credences violate the axioms — for example, if your credence that it rains tomorrow plus your credence that it doesn't rain tomorrow adds up to something other than 1 — then a clever bookmaker can offer you a set of individually acceptable bets that guarantee you a net loss no matter how the world turns out. This is a **sure loss**: irrational by any practical standard. Probabilistic incoherence is, in effect, choosing to be exploitable. This argument doesn't prove that beliefs *are* probabilities in nature; it shows that rational beliefs *must behave* like probabilities.

Bayesian epistemology competes with the reliabilism you may have encountered as a soft prerequisite. Reliabilism evaluates belief-forming processes: a belief is justified if it was produced by a process that reliably generates true beliefs. Bayesianism evaluates the internal coherence of a credence structure and the correctness of its updating procedure. These approaches are not mutually exclusive — a reliabilist might accept that reliable processes tend to produce well-calibrated credences — but they identify different targets for epistemic criticism. The central challenge Bayesianism faces is the **problem of priors**: the framework tells you how to update correctly, but it doesn't specify where prior probabilities should come from. Two agents who start with radically different priors can both conditionalize flawlessly and still arrive at very different posteriors after examining the same evidence. With enough evidence, different priors tend to converge — a result called "washing out" — but in realistic conditions with limited evidence, prior choice can dominate, making the theory's prescriptions feel less determinate than they appear.
