---
id: logical-consistency-and-contradiction
title: Logical Consistency and Contradiction
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: argument-premise-and-conclusion
  type: hard
- id: tautologies-and-contradictions
  type: soft
- id: propositional-logic-introduction
  type: soft
- id: formal-logical-fallacies
  type: soft
- id: reductio-ad-absurdum-method
  type: soft
builds-toward:
- paradox-and-self-reference
- argument-evaluation-holistic
tags:
- consistency
- contradiction
- logical-form
stage: formal-systems
status: validated
---
# Logical Consistency and Contradiction

## Core Idea
A set of claims is consistent if they can all be true simultaneously; inconsistent if they cannot. Detecting contradictions reveals when premises undermine each other or when a conclusion conflicts with an accepted principle. An argument with inconsistent premises 'proves' anything, so consistency is a baseline requirement.

## Questions

```yaml
- question: "A legal brief relies on two premises: 'A contract requires consideration to be binding' and 'This contract is binding even though no consideration was exchanged.' What is the logical consequence of using these premises together?"
  type: multiple-choice
  options:
    - "The argument is weakened but can still support a narrow conclusion"
    - "The argument fails only if the conclusion is also false"
    - "From these contradictory premises, any conclusion whatsoever can be derived in classical logic"
    - "The argument is invalid but not necessarily unsound"
  answer: 2
  explanation: "The two premises directly contradict each other: the first says consideration is required; the second says the contract is binding without it. In classical logic, a contradictory set of premises entails everything — this principle is called ex contradictione quodlibet ('from contradiction, anything'). An argument 'proving' everything proves nothing; its conclusion carries no evidential weight. The inconsistency must be resolved before any valid inference can be drawn."

- question: "Which of the following sets of statements is logically consistent?"
  type: multiple-choice
  options:
    - "'No mammals can fly.' 'Bats are mammals.' 'Bats can fly.'"
    - "'The defendant was in Paris.' 'The defendant was in Chicago.' 'The clocks in both cities were accurate.' (same moment in time)"
    - "'She arrived before noon.' 'She arrived at 2 PM.' 'The clock was accurate.'"
    - "'All prime numbers greater than 2 are odd.' '17 is prime.' '17 is odd.'"
  answer: 3
  explanation: "Options A, B, and C all contain contradictions — no possible situation makes all their claims simultaneously true. Option D is consistent: all three statements are true simultaneously (17 is prime, all primes > 2 are odd, so 17 is odd — the claims reinforce each other). Consistency requires only that the claims *can* all be true at once, not that they are mutually supportive or even interesting together."

- question: "A consistent set of premises guarantees that an argument is sound."
  type: true-false
  answer: false
  explanation: "Consistency means the premises can all be true simultaneously — but they might all be consistently false. Soundness requires both that the argument is valid (conclusion follows from premises) AND that the premises are actually true. A consistent set of false premises produces an unsound argument even if it's valid. Consistency is a necessary condition to avoid ex contradictione quodlibet, but it is nowhere near sufficient for soundness."

- question: "If a set of premises is inconsistent, then every conclusion that can be derived from them using valid inference rules is technically entailed by those premises."
  type: true-false
  answer: true
  explanation: "This is the principle of explosion (ex contradictione quodlibet): in classical logic, if you accept P and not-P, you can derive any proposition Q. The proof uses disjunction introduction (from P, derive P ∨ Q) and disjunctive syllogism (from P ∨ Q and not-P, derive Q). Because every proposition is entailed by a contradiction, a contradictory argument cannot distinguish true conclusions from false ones — it 'proves' everything and therefore nothing of use."

- question: "Why does an argument with contradictory premises 'prove' nothing, even when each individual inference step is logically valid?"
  type: short-answer
  answer: "Because in classical logic, a contradiction entails every proposition. If premises include both P and not-P, any conclusion Q can be derived using valid steps (disjunction introduction and disjunctive syllogism). Since the argument can equally 'prove' Q and not-Q, it provides no evidence for either — the proof is technically valid but epistemically worthless."
  explanation: "This exposes why consistency is a prerequisite, not just a preference. Valid reasoning preserves truth: if the premises are true and the reasoning is valid, the conclusion must be true. But contradictory premises can never all be true simultaneously, so the truth-preservation guarantee breaks down entirely. The argument form becomes a machine that outputs anything, which means it outputs nothing meaningful. Consistency is the minimum standard a set of premises must meet before logical analysis of the argument can proceed."
```

## Explainer

From your study of argument structure, you know that an argument moves from premises to a conclusion, and the central question is whether the premises provide adequate support for the conclusion. Logical consistency is a prerequisite even more basic than that: before asking whether an argument is good, you need to check whether the premises can all be true at once. If they can't, the argument is broken at the foundation.

A **contradiction** is the simplest case of inconsistency: two claims of the form P and not-P. "The defendant was in Chicago at noon" and "The defendant was not in Chicago at noon." Both cannot be true simultaneously — they negate each other directly. A broader inconsistency arises when no possible situation makes all the claims true together, even without an explicit negation pair. "All ravens are black," "There exists a non-black raven," and "Ravens are a single species" form an inconsistent trio — the first two clash, and the third doesn't repair the contradiction.

Here is why inconsistency is so damaging: in classical logic, a contradiction **entails everything**. This principle — sometimes called *ex contradictione quodlibet* — means that from a contradictory set of premises, you can derive any conclusion whatsoever, using valid inference rules. If you accept both P and not-P, you can prove that the moon is made of cheese. This makes inconsistent premises useless: an argument that "proves" everything actually proves nothing. Identifying hidden contradictions in a position therefore exposes that the position has no genuine logical content.

In practice, inconsistencies are often subtle. A politician might advocate austerity on principle but oppose every specific cut when constituents object — consistent-sounding individually, collectively incoherent. A theory might have a general rule and a set of specific commitments that generate contradictory predictions. The skill is to ask: is there any coherent world in which all these claims are simultaneously true? If not, something must give. Consistency is not the same as truth — a position can be consistently wrong — but inconsistency is a decisive objection, because a self-contradicting position cannot possibly be entirely correct. Mastering this check makes you a far sharper evaluator of arguments in philosophy, law, science, and everyday reasoning.
