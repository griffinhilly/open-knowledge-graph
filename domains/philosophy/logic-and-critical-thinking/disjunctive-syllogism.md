---
id: disjunctive-syllogism
title: Disjunctive Syllogism
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inference-patterns-and-validity
  type: hard
- id: propositional-logic-introduction
  type: soft
builds-toward:
- argument-evaluation-holistic
tags:
- disjunction
- or
- deductive-reasoning
stage: formal-systems
status: draft
---

# Disjunctive Syllogism

## Core Idea
Disjunctive syllogism uses 'or' statements: either A or B (or both); one of them is false; therefore the other is true. This pattern applies when we must choose among alternatives or eliminate possibilities. Understanding disjunctive reasoning helps us reason through situations where multiple options exist but some are ruled out.

## Questions

```yaml
- question: "A doctor reasons: 'Your symptoms indicate either a viral infection or a bacterial infection. You tested negative for bacterial infection. Therefore you have a viral infection.' This reasoning is valid only if:"
  type: multiple-choice
  options:
    - "The test for bacterial infection was administered correctly and recently"
    - "The initial disjunction is exhaustive — viral and bacterial infections are the only possible explanations for those specific symptoms"
    - "The doctor has already ruled out other conditions earlier in the visit"
    - "The patient has no history of atypical immune responses"
  answer: 1
  explanation: "Disjunctive syllogism is valid as an argument form, but its soundness in any application depends on whether the initial disjunction genuinely covers all possibilities. If there is a third explanation — a fungal infection, an autoimmune response, a drug reaction — then eliminating bacterial infection does not establish viral infection. The argument's logical machinery is correct; the danger lies in the scope of the disjunction. This is why process-of-elimination reasoning must begin by asking: have I actually listed all possibilities?"

- question: "A commentator argues: 'Either you support this policy or you are against prosperity. The senator does not support this policy. Therefore the senator is against prosperity.' The logical error is:"
  type: multiple-choice
  options:
    - "The argument uses modus ponens incorrectly"
    - "The initial disjunction artificially excludes other positions — opposing this specific policy does not exhaust the ways one can support prosperity — making this a false dilemma, not a valid disjunctive syllogism"
    - "Disjunctive syllogism cannot be applied to political statements because they are neither true nor false"
    - "The argument commits the fallacy of affirming a disjunct"
  answer: 1
  explanation: "The argument form is disjunctive syllogism, and the form itself is valid. The problem is that the initial disjunction is false: there are many ways to support prosperity other than supporting this particular policy. By artificially constraining the options to two — forcing a choice between 'support this policy' and 'oppose prosperity' — the arguer constructs a false dilemma. The conclusion follows from the form, but the form is being applied to a rigged disjunction. This is precisely the exploitation the explainer describes: 'The fallacy of false dilemma exploits precisely this: artificially narrowing a disjunction to force a predetermined conclusion.'"

- question: "The argument 'P or Q; P is true; therefore Q is false' is a valid application of disjunctive syllogism."
  type: true-false
  answer: false
  explanation: "This is the fallacy of affirming a disjunct, not disjunctive syllogism. Standard logical 'or' is inclusive: 'P or Q' means at least one is true, but possibly both. If P is true, Q might still be true — we cannot conclude Q is false. Disjunctive syllogism requires ELIMINATING one disjunct (showing it is false) to conclude the other is true. Confirming one disjunct tells us nothing about the other. The confusion arises because everyday English 'or' is sometimes exclusive (you can have cake OR pie, not both), but in logic the default is inclusive unless stated otherwise."

- question: "Disjunctive syllogism is formally valid whether the 'or' connecting the disjuncts is inclusive or exclusive, provided one disjunct is shown to be false."
  type: true-false
  answer: true
  explanation: "If 'not-P' is established, then Q must be true regardless of whether the disjunction is inclusive or exclusive. Under inclusive or: 'P or Q' means at least one is true; since P is false, Q must be the one that's true. Under exclusive or: 'P or Q but not both' — since P is false, Q is again the only way to satisfy the disjunction. In both cases, eliminating P leaves Q as the conclusion. The inclusive/exclusive distinction matters for the fallacy of affirming a disjunct (confirming P), but not for valid elimination."

- question: "What distinguishes a valid disjunctive syllogism from the fallacy of false dilemma, and what question should you ask to detect when a disjunctive argument is committing that fallacy?"
  type: short-answer
  answer: "A valid disjunctive syllogism applies the inference form (P or Q; not-P; therefore Q) to a genuinely exhaustive disjunction — one that truly covers all the relevant possibilities. The fallacy of false dilemma uses the same inference form but applies it to an artificially narrowed disjunction that excludes live alternatives. The argument's logical machinery is valid; the problem is the premise 'P or Q' is false because there are other options. The key diagnostic question is: 'Are these really the only possibilities, or has the arguer excluded some alternatives without justification?' If you can identify a third option that the disjunction ignores, the argument commits the false dilemma fallacy."
  explanation: "The false dilemma is so rhetorically effective precisely because the disjunctive syllogism form is valid — once you accept the two-option framing, the conclusion follows. The work of critical thinking is to resist the framing before accepting it. Asking 'what are the other options?' before evaluating the rest of the argument is the core diagnostic habit."
```

## Explainer

**Disjunctive syllogism** is one of the most useful inference patterns in everyday reasoning. Its formal structure is: (1) P or Q; (2) not-P; (3) therefore, Q. In plain language: if you know that at least one of two options is true, and you can rule out one of them, the other must hold. The detective who reasons "The suspect was either in London or Paris that night — we've confirmed he was not in London — therefore he was in Paris" is using disjunctive syllogism. The validity of this pattern follows directly from the meaning of "or" in logic.

You've already encountered **validity** and **argument forms** as a prerequisite. Disjunctive syllogism is formally valid: there is no possible world in which both premises are true and the conclusion is false. If "P or Q" is true (meaning at least one is true) and "not-P" is true (P is definitely false), then Q is the only remaining way to satisfy the first premise. The inference is airtight. This distinguishes it from invalid elimination patterns — for instance, "P or Q; P is true; therefore Q is false" commits the fallacy of affirming a disjunct, because inclusive or allows both to be true simultaneously.

The most important subtlety is the distinction between **inclusive or** and **exclusive or**. Standard logical "or" is inclusive: "P or Q" means at least one is true, possibly both. Disjunctive syllogism works the same either way — if we know not-P, we conclude Q whether or not both could have been true. But in natural language, "or" is sometimes exclusive: "You can have cake or pie" often implies not both. Recognizing which sense is intended matters for constructing valid disjunctive arguments. When analyzing arguments in ordinary language, you may need to check whether the disjunction is meant inclusively or exclusively before applying this pattern.

In practice, disjunctive syllogism is the engine behind **process of elimination**. Whenever you have an exhaustive set of possibilities and start ruling them out, you are implicitly chaining disjunctive syllogisms. Doctors diagnosing by exclusion, detectives eliminating suspects, engineers testing components one by one — all rely on this pattern. The key requirement is that the initial disjunction genuinely covers all possibilities. If you set up "either A or B" but there's actually a third option C you've overlooked, eliminating A doesn't establish B. The fallacy of false dilemma exploits precisely this: artificially narrowing a disjunction to force a predetermined conclusion. Disjunctive syllogism is valid; setting up a false disjunction is not.

