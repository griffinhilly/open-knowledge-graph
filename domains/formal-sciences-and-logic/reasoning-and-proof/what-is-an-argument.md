---
id: what-is-an-argument
title: What Is an Argument?
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: true-and-false-statements
    type: hard
  - id: if-then-statements
    type: soft
builds-toward:
  - valid-vs-invalid-arguments
  - deductive-vs-inductive-reasoning
  - conjectures-and-testing
tags: [arguments, reasoning, evidence, claims]
stage: abstract-reasoning
status: validated
---

# What Is an Argument?

## Core Idea
In logic, an argument is not a disagreement or a fight — it is a structured set of statements where some statements (called premises) are offered as reasons to believe another statement (called the conclusion). Every argument has exactly this structure: one or more premises and a single conclusion. Learning to identify and construct arguments is the foundation of all formal reasoning, because it forces you to separate what you believe from why you believe it.

## How It's Best Learned
Start with everyday examples: "It's raining, so I should bring an umbrella" has one premise and one conclusion. Have students identify the premise and conclusion in newspaper editorials, sports commentary, and mathematical claims. Then introduce signal words: "because," "since," and "given that" signal premises; "therefore," "so," and "it follows that" signal conclusions. Practice converting informal reasoning into explicit premise-conclusion form.

## Common Misconceptions
- Confusing the everyday meaning of "argument" (a dispute) with the logical meaning (a structured chain of reasoning). In logic, an argument can be perfectly calm and cooperative.
- Thinking that having more premises always makes an argument stronger. A single strong premise can outweigh five weak ones.
- Believing the conclusion must come last. In natural language, the conclusion often appears first ("You should study harder, because the test is tomorrow").

## Questions

```yaml
- question: "Which of the following best describes an argument in logic?"
  type: multiple-choice
  options:
    - "A heated disagreement between two people"
    - "A set of premises offered as reasons to accept a conclusion"
    - "Any statement that is true"
    - "A question that requires evidence to answer"
  answer: 1
  explanation: "In logic, an argument is a structured set of statements: premises (the evidence or reasons) and a conclusion (the claim being supported). It has nothing to do with emotional conflict — a logical argument can be written by one person in complete calm."

- question: "In the statement 'Since most metals conduct electricity, and copper is a metal, copper should conduct electricity,' the conclusion is 'most metals conduct electricity.'"
  type: true-false
  answer: false
  explanation: "The word 'since' signals a premise, not a conclusion. The two premises are 'all metals conduct electricity' and 'copper is a metal.' The conclusion — signaled by 'must' — is 'copper conducts electricity.' Signal words help you locate which part of an argument is being supported and which parts do the supporting."

- question: "Identify the premises and conclusion in this argument: 'The park closes at sunset. Sunset is at 7pm today. Therefore, the park closes at 7pm today.'"
  type: short-answer
  answer: "Premise 1: The park closes at sunset. Premise 2: Sunset is at 7pm today. Conclusion: The park closes at 7pm today."
  explanation: "The word 'therefore' directly signals the conclusion. Everything before it provides the reasons (premises) that lead to that conclusion. This argument has two premises that work together — neither alone would be sufficient to reach the conclusion."
```

## Explainer

You already know what it means for a statement to be true or false. An argument takes this further: it is a structured attempt to show that one statement (the conclusion) follows from other statements (the premises). The premises are your evidence; the conclusion is what you claim the evidence supports. Every argument you will ever encounter in logic, mathematics, science, or everyday life has this basic architecture.

Consider a simple example: "All squares have four sides. This shape is a square. Therefore, this shape has four sides." There are two premises (the general rule about squares, and the specific claim about this shape) and one conclusion (what follows about this shape's sides). The argument works because the conclusion is forced by the premises — if both premises are true, the conclusion cannot be false.

The crucial skill is learning to separate the structure of an argument from whether you agree with it. A well-structured argument can have false premises ("All birds can fly; penguins are birds; therefore penguins can fly"). And a poorly structured argument can accidentally reach a true conclusion ("Some animals swim; dogs are animals; therefore some dogs swim" — the conclusion happens to be true, but the premises do not guarantee it). The structure is what logic evaluates, not the real-world truth of individual statements.

Signal words are your best tool for dissecting arguments in natural language. Words like "because," "since," "given that," and "as" introduce premises. Words like "therefore," "so," "thus," "hence," and "it follows that" introduce conclusions. But be careful: everyday speech often omits signal words entirely, and sometimes the conclusion comes first. "You should wear a coat — it is freezing outside" puts the conclusion before the premise. Training yourself to spot the claim-and-evidence structure regardless of word order is fundamental to everything that follows in reasoning and proof.

Once you can reliably identify arguments, you are ready to ask the deeper question: is this argument any good? That question splits into two parts — are the premises true, and does the conclusion actually follow from them? The second question is the domain of logic, and it leads directly to the concepts of validity and soundness that you will study next.
