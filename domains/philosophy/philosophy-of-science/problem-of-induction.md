---
id: problem-of-induction
title: The Problem of Induction
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: inductive-reasoning
  type: hard
- id: rationalism-vs-empiricism
  type: soft
- id: probabilistic-reasoning
  type: soft
builds-toward:
- popper-falsificationism
- logical-positivism-and-vienna-circle
tags:
- induction
- justification
- logic
stage: expert
status: validated
---

# The Problem of Induction

## Core Idea
Hume showed that inductive inference—concluding universal laws from repeated observations—cannot be logically justified. The fact that the sun has risen every day in the past does not logically guarantee it will tomorrow. This challenge remains central to philosophy of science because all empirical science relies on generalizing from observed instances to universal claims.

## How It's Best Learned
Start with Hume's original problem formulation. Then study Popper's falsificationist response and modern Bayesian approaches to see the landscape of proposed solutions.

## Common Misconceptions
Thinking induction is illogical (Hume allows practical induction, just denies its theoretical justification). Confusing induction with deduction. Assuming the problem is purely logical rather than epistemological.

## Questions

```yaml
- question: "A scientist argues: 'Induction must be reliable because in the past, inductive reasoning has always led to correct predictions.' What is wrong with this argument?"
  type: multiple-choice
  options:
    - "The argument is valid — past success is the best evidence we have for any method's reliability"
    - "The argument is circular: it uses inductive reasoning (past success implies future reliability) to justify induction, which is exactly the inference whose validity is in question"
    - "The argument is valid only if applied to natural sciences, not social sciences"
    - "The argument fails because science has made wrong predictions in the past, so induction hasn't always succeeded"
  answer: 1
  explanation: "This is Hume's circularity problem. Any attempt to justify induction by appeal to its past success is itself an inductive argument — it assumes the future will resemble the past, which is precisely the assumption that needs justification. Option D gets the point wrong: induction's occasional failures aren't the core issue. The deeper problem is that even if induction had always worked, appealing to that track record still commits the very reasoning move under scrutiny."

- question: "Which of the following best captures what Hume concluded from the problem of induction?"
  type: multiple-choice
  options:
    - "We should stop using inductive reasoning in science because it is logically unjustified"
    - "Our practice of inductive inference is psychologically compelled by habit and custom, but we cannot provide a non-circular rational foundation for it"
    - "Induction is valid only when sample sizes are sufficiently large"
    - "The problem of induction shows that probabilistic reasoning is the correct framework for scientific knowledge"
  answer: 1
  explanation: "Hume was not a skeptic about the practice of induction — he recognized we cannot help but reason inductively. His conclusion was that our inductive habits stem from custom and psychological compulsion, not rational justification. We cannot give a non-circular argument for why the future should resemble the past. Option C confuses sample size (an empirical concern) with the philosophical justification problem. Option D describes the Bayesian response to Hume, not Hume's own position."

- question: "The problem of induction shows that inductive reasoning is unreliable and should be replaced with deductive reasoning in science."
  type: true-false
  answer: false
  explanation: "Hume did not argue that induction is unreliable or that we should abandon it. He argued that it cannot be given a non-circular logical justification. We continue to rely on induction because we cannot help it — custom and habit compel us. Moreover, deductive reasoning alone cannot generate new empirical knowledge; it can only draw out what is already implicit in premises. Science requires both."

- question: "Popper's falsificationism completely solves the problem of induction by showing how science can proceed without inductive inference."
  type: true-false
  answer: false
  explanation: "Popper's response sidesteps rather than solves the problem. By focusing on falsification (one contrary observation refutes a universal claim), Popper avoids needing to justify accumulating confirming instances. But this creates a new problem: Popper cannot explain why we should act on or believe unfalsified theories. If we have tested a bridge design 1,000 times without failure, Popper's logic doesn't tell us it's safe to use — he denies that confirming instances justify belief. Most philosophers consider this an inadequate response."

- question: "Why can no finite number of confirming observations logically prove a universal scientific law, and why does any attempt to justify this inference seem to require assuming what we're trying to prove?"
  type: short-answer
  answer: "A universal law covers infinitely many cases; observations cover only finitely many. The inference from 'all observed F are G' to 'all F are G' is not deductively valid — the premises don't guarantee the conclusion. The future could deviate from the past in any way logic permits. Any attempt to justify induction by saying 'it has worked before' uses inductive inference itself (past success predicts future success), making the argument circular. There is no non-circular path from particular observations to universal conclusions."
  explanation: "This is the heart of Hume's problem: induction is not deductively valid, and any non-deductive justification of induction must itself rely on inductive reasoning. The circularity is unavoidable within the framework of requiring rational justification. Responses (Popper, Bayesianism) either change what justification means or abandon the requirement for it — they do not derive justification within Hume's original framework."
```

## Explainer

You already understand inductive reasoning: it is the move from particular observations to general conclusions. The sun has risen every day in recorded history, so we conclude it will rise tomorrow. Every copper sample we have tested conducts electricity, so we generalize that copper is electrically conductive. Science depends on this pattern constantly. Hume's devastating observation was simple: this inference is never deductively valid. The premises — all the past sunrises — do not *guarantee* the conclusion. The future could, as far as logic is concerned, deviate from the past in any way whatsoever. No number of observed instances logically compels the universal conclusion.

The deeper problem is that attempts to justify induction seem to require using induction itself. Why do we trust that the future will resemble the past? The most natural answer is: "Because in the past, the future has always resembled the past." But this is precisely the kind of inductive argument whose validity is in question. Any defense of induction that appeals to past success of induction is viciously circular. Hume concluded that our habit of inductive inference is psychologically irresistible — custom and habit, not rational justification — and that we cannot provide a non-circular philosophical foundation for it.

This cuts to the heart of science. From empiricism you know that scientific knowledge is grounded in observation and experiment. But observations give us particular facts; scientific laws are universal claims. **Every** generalization in science — Newton's laws, the laws of thermodynamics, evolutionary theory — makes a claim that goes beyond the finite observations supporting it. If induction cannot be rationally justified, how can science claim to produce genuine knowledge rather than merely well-confirmed belief? Hume's problem is not a logical puzzle to be solved and set aside; it is an open wound in the foundations of empirical knowledge.

Karl Popper's response — which you will study in falsificationism — was to abandon justification entirely. We cannot verify universal laws, but we can **falsify** them: a single contrary observation logically refutes the universal claim. Science proceeds not by accumulating confirming instances but by making bold conjectures and subjecting them to rigorous attempts at refutation. The **Bayesian** response takes a different route: rather than demanding logical certainty, it replaces the demand for justification with a probabilistic framework. Prior credences are updated by evidence using Bayes' theorem, and "justified" comes to mean having high posterior probability given the evidence. Neither solution fully dissolves Hume's challenge — Popper does not explain why we should act on unfalsified theories, and Bayesianism must still assume that past evidence is relevant to future credences — but they represent the two most influential frameworks for living with the problem rather than solving it.
