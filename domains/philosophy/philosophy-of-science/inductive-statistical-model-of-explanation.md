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

## Questions

```yaml
- question: "Jones had streptococcal infection and took penicillin; the statistical law says penicillin cures strep with 90% probability; Jones recovered. An IS explanation is constructed. However, Jones also wore a red hat during treatment, and patients with strep who took penicillin and wore red hats also have a 90% recovery rate. What does this reveal about the IS model?"
  type: multiple-choice
  options:
    - "The IS explanation is strengthened because two factors contributed to Jones's recovery"
    - "The irrelevance problem: the IS model cannot exclude causally irrelevant factors, since any premise set yielding high probability qualifies"
    - "The IS explanation is weakened because the red hat introduces a confound"
    - "This shows the IS model is robust — the same probability in both reference classes confirms the explanation"
  answer: 1
  explanation: "The irrelevance problem: the IS model accepts any premise set that makes the explanandum highly probable, regardless of causal relevance. The red hat is causally irrelevant to strep recovery — including it neither raises nor lowers probability. But the IS model has no mechanism for excluding it; any high-probability argument counts as an explanation. This shows the IS model captures statistical association, not causal explanation. Salmon developed his causal-statistical account precisely to require that explanatory factors be causally, not just statistically, connected to the outcome."

- question: "According to the IS model, which of the following constitutes a scientific explanation of an event?"
  type: multiple-choice
  options:
    - "A deductively valid argument showing the event was the only possible outcome given the laws"
    - "An inductive argument from a statistical law and initial conditions that renders the event highly probable"
    - "An argument that identifies the causal mechanisms responsible for the event"
    - "A narrative description of the sequence of events leading to the outcome"
  answer: 1
  explanation: "The IS model extends Hempel's covering-law framework to probabilistic cases. An IS explanation has the structure: statistical law L + initial conditions C → (with high probability) → event E. The 'high probability' requirement distinguishes it from the DN model's deductive entailment. Option A describes the deductive-nomological model. Option C describes Salmon's causal-statistical model, developed *in response to* the IS model's failures. Option D is a narrative, not an explanation in Hempel's sense."

- question: "Under the IS model, a single event can simultaneously receive a high-probability IS explanation and a low-probability IS 'explanation,' depending on which reference class is chosen."
  type: true-false
  answer: true
  explanation: "This is Salmon's problem of ambiguity. Under 'patients who received penicillin,' John's recovery has probability 0.9 — a successful IS explanation. Under 'patients who received penicillin and had a drug-resistant strain,' recovery has probability 0.1 — no IS explanation, and the event is surprising. Same event, same person, contradictory IS verdicts. The IS model provides no principled basis for choosing the 'correct' reference class, which Salmon regarded as a fatal flaw showing that statistical association alone cannot underwrite genuine explanation."

- question: "The IS model improves on the DN model primarily by requiring that explanatory laws be universal and exceptionless."
  type: true-false
  answer: false
  explanation: "The IS model improves on the DN model by *relaxing* the requirement for universal laws, allowing statistical laws to figure in explanations. The DN model already required universal, exceptionless laws. The IS model expands the framework by accepting probabilistic laws as legitimate explanatory premises, substituting high-probability inductive support for deductive entailment. The challenge for the IS model is not finding stricter laws but handling problems created by probabilistic laws: the vagueness of 'high' probability, the irrelevance problem, and the ambiguity problem."

- question: "What is the problem of ambiguity in the IS model, and why did it lead Salmon to propose a causal-statistical account of explanation instead?"
  type: short-answer
  answer: "The problem of ambiguity: the IS model's verdict on whether an event is explained depends on the reference class used to describe it, but the model provides no principled method for selecting the correct class. The same event can be rendered highly probable (a successful IS explanation) by one reference class and improbable (no IS explanation) by another. Salmon argued this shows IS explanations are not objective — they depend on how we describe the explanandum. His causal-statistical account responds by requiring that explanations cite actual causal mechanisms, making the causally homogeneous reference class the one that picks out all and only the causally relevant factors."
  explanation: "The deeper issue is that statistical regularities can be causally spurious. The IS model, because it only requires high probability, is blind to the difference between correlation and causation. Causal explanation requires identifying the mechanism by which C brought about E, not just showing that events like C are usually followed by events like E. Salmon's insight was that the reference class problem is not a technical glitch but a symptom of a fundamental inadequacy: statistical association is not the same as causal explanation."
```

## Explainer

You already understand the **deductive-nomological (DN) model**: a good scientific explanation is an argument in which the explanandum (what is to be explained) follows deductively from premises that include at least one general law. The DN model has intuitive appeal for deterministic science — if you know the laws and the initial conditions, the outcome follows necessarily. But much of science is irreducibly probabilistic. Quantum mechanics, genetics, epidemiology, and evolutionary biology all cite statistical laws. Does that mean they cannot explain? Hempel's **inductive-statistical (IS) model** extends the DN framework to cover these cases.

The structure of an IS explanation mirrors the DN structure, but with a crucial difference: instead of deductive entailment, the explanans (the explaining premises) *inductively support* the explanandum to a high degree of probability. Consider a simple case: Jones had streptococcal infection; penicillin is highly effective against streptococcal infection (a statistical law); therefore, Jones recovered. This is not deductively valid — Jones might have been one of the unlucky few for whom penicillin fails. But the premises make the recovery highly probable, and this high-probability inductive support is what constitutes the explanation. The argument form is: L (statistical law) + C (initial conditions) → [high probability] → E (event to be explained). The double line (⟹) signals that the inference is inductive, not deductive.

The **requirement of high probability** is where the model immediately runs into trouble. What counts as "high"? 0.9? 0.99? Hempel himself acknowledged that this threshold is vague. But a deeper problem emerges even if we accept some threshold: you can sometimes produce a high-probability argument that intuitively explains nothing. Suppose the statistical law is "people who take vitamin C very rarely get scurvy." If Jones takes vitamin C and does *not* get scurvy, the IS model says this is explained by the vitamin C, since scurvy had low probability given the dose. But surely vitamin C didn't explain the absence of scurvy — the explanation is adequate vitamin C from *any* dietary source, and the pill is irrelevant if diet was already sufficient. This is the **irrelevance problem**, which your probabilistic reasoning background will help you see clearly: high probability by itself does not guarantee that the cited factors are the *causally relevant* ones.

The most devastating challenge to the IS model is called the **problem of ambiguity**, introduced by Wesley Salmon. Statistical explanations are sensitive to the reference class under which you describe the event. Suppose John recovered from his infection. Under the reference class "patients who received penicillin," recovery has probability 0.9 — a good IS explanation. But under the reference class "patients who received penicillin *and* had a penicillin-resistant strain," recovery has probability 0.1 — no IS explanation, and in fact the event is surprising. The same event receives contradictory IS verdicts depending on which reference class we choose. Salmon's solution was to move away from the IS model entirely, toward **causal-statistical explanation** — the view that genuine explanation requires identifying the actual causal mechanisms responsible for the outcome, not merely high-probability statistical arguments. The IS model, for all its limitations, was historically essential in showing that explanation need not be deductive, clearing space for more sophisticated probabilistic and causal theories of explanation.

