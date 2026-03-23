---
id: credences-and-epistemic-probabilities
title: Credences and Epistemic Probabilities
domain: philosophy
course: epistemology
prerequisites:
- id: what-is-knowledge
  type: soft
- id: probabilistic-reasoning
  type: soft
- id: probabilistic-computation
  type: soft
builds-toward:
- conditionalization-and-bayesian-updating
- evidential-support-formalization
- permissible-probability-distributions
tags:
- degrees-of-belief
- probability
- bayesian
stage: formal-systems
status: draft
---

# Credences and Epistemic Probabilities

## Core Idea
A credence is a numerical degree of belief: a real number between 0 and 1 representing how strongly an agent believes a proposition. Rather than all-or-nothing knowledge and belief, credences model rational partial belief and uncertainty. They are subject to coherence constraints (probability axioms): P(p) ≥ 0, P(tautology) = 1, and P(p ∨ q) = P(p) + P(q) when p and q are incompatible.

## Questions

```yaml
- question: "Sarah assigns credence 0.7 to 'it will rain tomorrow' and credence 0.5 to 'it will NOT rain tomorrow.' What is the problem with her credences?"
  type: multiple-choice
  options:
    - "Her credences are fine as long as experience shows she's right about 70% of the time"
    - "Her credences are incoherent — they violate the probability axiom that P(A) + P(¬A) = 1, making her exploitable by a Dutch Book"
    - "It is acceptable for credences in a proposition and its negation to exceed 1 if the agent is genuinely uncertain"
    - "She simply needs to pick her higher credence as her 'true' belief and discard the other"
  answer: 1
  explanation: "For mutually exclusive and exhaustive propositions A and ¬A, the probability axioms require P(A) + P(¬A) = 1. Sarah's credences sum to 1.2, which violates this. A coherent set of credences must satisfy the probability axioms — this is not a recommendation but a rationality requirement. An incoherent agent can be subjected to a Dutch Book: a set of individually acceptable bets that, taken together, guarantee a loss regardless of what actually happens."

- question: "What is the fundamental difference between binary belief and credences as models of epistemic states?"
  type: multiple-choice
  options:
    - "Binary belief is more rigorous because it avoids the imprecision of continuous numbers"
    - "Credences represent continuous degrees of belief from 0 to 1, capturing gradations of uncertainty, while binary belief treats all belief as all-or-nothing"
    - "Credences are only used in formal Bayesian statistics, not in philosophical epistemology"
    - "Binary belief and credences describe identical epistemic states using different notation — one can always be translated into the other"
  answer: 1
  explanation: "The core claim of credence theory is that belief comes in degrees. Binary belief has two states: believe or don't believe. Credences allow for the full range from 0 (certain it's false) to 1 (certain it's true), with intermediate values representing partial belief. This captures ordinary usage ('I'm pretty sure,' 'I doubt it,' 'I'm uncertain') that binary belief flattens. They cannot be translated into each other without loss — a credence of 0.7 is genuinely different from both 'believes' and 'doesn't believe.'"

- question: "A credence of 0.5 in a proposition represents genuine uncertainty — the agent has no evidential reason to favor the proposition over its negation."
  type: true-false
  answer: true
  explanation: "Exactly right. A credence of 0.5 is the numerical representation of genuine uncertainty — it is analogous to a fair coin flip: no evidential pull in either direction. This is different from a credence of 0.9 (strong lean toward true) or 0.1 (strong lean toward false). The 0.5 credence is not a default or placeholder; it is a specific epistemic state representing maximum uncertainty between two alternatives."

- question: "Because credences must satisfy probability axioms, any rational agent must assign a credence of 1 to any proposition they consider very likely to be true."
  type: true-false
  answer: false
  explanation: "The probability axioms only require credence of exactly 1 for necessary truths (tautologies). For contingent empirical propositions — even highly probable ones — any credence strictly between 0 and 1 is compatible with coherence. A credence of 0.99 is coherent and appropriate for something nearly certain; only a contradiction must receive credence 0, and only a logical truth must receive credence 1. Conflating 'very confident' with 'certain' (credence 1) is a category error that credence theory is specifically designed to avoid."

- question: "What does it mean for an agent's credences to be 'incoherent,' and why does incoherence matter practically?"
  type: short-answer
  answer: "An agent's credences are incoherent when they violate the probability axioms — for example, assigning credences to mutually exclusive events that sum to more than 1, or less than 1 to a set of exhaustive possibilities. Incoherence matters because an incoherent agent can be Dutch-Booked: a clever bookie can construct a set of bets that the agent will each individually accept (because each looks favorable given their stated credences) but that together guarantee the agent loses money no matter what happens. Coherence is thus the minimum rationality requirement for degrees of belief — the credence analog of logical consistency."
  explanation: "The Dutch Book argument gives incoherence practical teeth: it's not just a formal violation but an exploitable irrationality. This is why coherence — satisfying the probability axioms — is treated as a necessary condition for rational credences, not merely a useful convention. An incoherent agent has committed themselves to a sure loss, which is the hallmark of practical irrationality."
```

## Explainer

From your study of knowledge and probabilistic reasoning, you already have two familiar frameworks for thinking about belief. The epistemological tradition treats belief as binary: you either believe something or you don't, and knowledge adds justification and truth to that belief. The mathematical tradition of probability theory treats uncertainty quantitatively. Credence theory is the proposal that we should combine these frameworks — that belief itself admits of degrees, and that rationality constrains what those degrees can be.

The core insight is that ordinary language already implicitly uses degrees of belief. When you say "I'm pretty sure it will rain," "I doubt she'll arrive on time," or "I'm certain this is correct," you're not just reporting a binary attitude — you're reporting something more like a probability estimate. **Credences** make this precise: your credence in a proposition is a number from 0 (complete disbelief) to 1 (complete certainty). A credence of 0.9 in "it will rain tomorrow" means you believe it quite strongly but not with certainty. A credence of 0.5 is genuine uncertainty, equivalent to a coin flip.

What makes credence theory epistemically interesting — and not merely descriptive — is that credences are subject to rational constraints. These constraints are exactly the **probability axioms** you know from probabilistic reasoning. A tautology must receive credence 1 (you can't rationally be uncertain about something necessarily true). The credences of mutually exclusive possibilities must sum to at most 1. Most importantly, your credence in a disjunction P(A or B) = P(A) + P(B) when A and B can't both be true. A rational agent whose credences violate these axioms is **incoherent** — they can be shown to accept a series of bets that guarantee a loss regardless of what happens, a result called a **Dutch Book**. Coherence is the minimum rationality requirement; it's the credence analog of logical consistency.

The move from binary belief to credences has far-reaching consequences. Questions in epistemology that seemed simple become more nuanced: Does justification come in degrees? Can you know something you're not certain of? How should you update your credences when you get new evidence? Credences build toward **Bayesian updating**, which gives a precise rule (Bayes' theorem) for how rational credences should change in light of evidence. This framework has become central not just to philosophy but to statistics, artificial intelligence, and decision theory — anywhere that rational reasoning under uncertainty is needed.
