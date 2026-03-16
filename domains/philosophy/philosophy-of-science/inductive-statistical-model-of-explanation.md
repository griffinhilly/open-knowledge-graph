---
id: inductive-statistical-model-of-explanation
title: Inductive-Statistical Explanation
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: deductive-nomological-model-of-explanation
  type: hard
- id: probabilistic-reasoning
  type: soft
builds-toward:
- causal-explanation-theories
tags:
- explanation
- induction
- probability
stage: advanced
status: draft
---

# Inductive-Statistical Explanation

## Core Idea
Not all explanations are deductive; many cite probabilistic laws and statistical regularities. Hempel's inductive-statistical (IS) model allows that an event is explained when its occurrence is rendered highly probable by statistical laws and conditions. However, defining adequate probability thresholds and handling irrelevance pose persistent difficulties.

## Explainer

You already understand the **deductive-nomological (DN) model**: a good scientific explanation is an argument in which the explanandum (what is to be explained) follows deductively from premises that include at least one general law. The DN model has intuitive appeal for deterministic science — if you know the laws and the initial conditions, the outcome follows necessarily. But much of science is irreducibly probabilistic. Quantum mechanics, genetics, epidemiology, and evolutionary biology all cite statistical laws. Does that mean they cannot explain? Hempel's **inductive-statistical (IS) model** extends the DN framework to cover these cases.

The structure of an IS explanation mirrors the DN structure, but with a crucial difference: instead of deductive entailment, the explanans (the explaining premises) *inductively support* the explanandum to a high degree of probability. Consider a simple case: Jones had streptococcal infection; penicillin is highly effective against streptococcal infection (a statistical law); therefore, Jones recovered. This is not deductively valid — Jones might have been one of the unlucky few for whom penicillin fails. But the premises make the recovery highly probable, and this high-probability inductive support is what constitutes the explanation. The argument form is: L (statistical law) + C (initial conditions) → [high probability] → E (event to be explained). The double line (⟹) signals that the inference is inductive, not deductive.

The **requirement of high probability** is where the model immediately runs into trouble. What counts as "high"? 0.9? 0.99? Hempel himself acknowledged that this threshold is vague. But a deeper problem emerges even if we accept some threshold: you can sometimes produce a high-probability argument that intuitively explains nothing. Suppose the statistical law is "people who take vitamin C very rarely get scurvy." If Jones takes vitamin C and does *not* get scurvy, the IS model says this is explained by the vitamin C, since scurvy had low probability given the dose. But surely vitamin C didn't explain the absence of scurvy — the explanation is adequate vitamin C from *any* dietary source, and the pill is irrelevant if diet was already sufficient. This is the **irrelevance problem**, which your probabilistic reasoning background will help you see clearly: high probability by itself does not guarantee that the cited factors are the *causally relevant* ones.

The most devastating challenge to the IS model is called the **problem of ambiguity**, introduced by Wesley Salmon. Statistical explanations are sensitive to the reference class under which you describe the event. Suppose John recovered from his infection. Under the reference class "patients who received penicillin," recovery has probability 0.9 — a good IS explanation. But under the reference class "patients who received penicillin *and* had a penicillin-resistant strain," recovery has probability 0.1 — no IS explanation, and in fact the event is surprising. The same event receives contradictory IS verdicts depending on which reference class we choose. Salmon's solution was to move away from the IS model entirely, toward **causal-statistical explanation** — the view that genuine explanation requires identifying the actual causal mechanisms responsible for the outcome, not merely high-probability statistical arguments. The IS model, for all its limitations, was historically essential in showing that explanation need not be deductive, clearing space for more sophisticated probabilistic and causal theories of explanation.

