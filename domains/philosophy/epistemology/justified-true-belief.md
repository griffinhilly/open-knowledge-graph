---
id: justified-true-belief
title: The Justified True Belief Account of Knowledge
domain: philosophy
course: epistemology
prerequisites:
- id: what-is-knowledge
  type: hard
- id: validity-and-soundness
  type: soft
- id: propositional-semantics
  type: soft
builds-toward:
- gettier-problems
- the-regress-problem
- epistemic-luck
- reliabilism
- testimony-as-knowledge
tags:
- JTB
- justification
- truth
- belief
- classical-analysis
stage: formal-systems
status: validated
---

# The Justified True Belief Account of Knowledge

## Core Idea
The classical analysis, traced to Plato's Meno and Theaetetus and codified in 20th-century analytic philosophy, holds that knowledge is justified true belief (JTB): an agent S knows that p if and only if (1) p is true, (2) S believes that p, and (3) S is justified in believing that p. The truth condition ensures knowledge tracks reality; the belief condition ensures the knower actually assents; and the justification condition distinguishes knowledge from true belief that is merely lucky. Each condition appeared independently necessary and jointly sufficient until Edmund Gettier's 1963 challenge.

## How It's Best Learned
Work through the three conditions one at a time, constructing counterexamples that violate each in isolation (believing something false, a true proposition you don't believe, a true belief held without justification). This builds intuition for why all three conditions are needed before Gettier destabilizes the picture.

## Common Misconceptions
- 'Justified' does not mean 'certain' — justification comes in degrees and is compatible with fallibility.
- The JTB analysis does not claim all true beliefs are knowledge, only that knowledge requires all three conditions.

## Questions

```yaml
- question: "Maria believes it is raining because she sees water on the sidewalk — though the water came from a burst pipe, not rain. It is actually raining elsewhere in the city. Which JTB condition does Maria's belief fail?"
  type: multiple-choice
  options: ["The truth condition — her belief is false", "The belief condition — she doesn't really believe it", "The justification condition — her evidence doesn't properly support the belief", "None — this is a genuine case of knowledge"]
  answer: 2
  explanation: "Maria's belief is true (it is raining in the city) and she believes it, but her justification is defective — she infers rain from evidence (wet sidewalk) that is actually caused by a burst pipe. Her belief is true and believed but not properly justified by the evidence available to her. This type of case is structurally close to the Gettier counterexamples."

- question: "According to the JTB account, if your belief is justified, it must be true."
  type: true-false
  answer: false
  explanation: "Justification and truth are independent conditions. You can have excellent justification for a belief that turns out to be false — a doctor carefully examining symptoms may be fully justified in a diagnosis that is nonetheless wrong. JTB requires all three conditions to hold simultaneously; justification alone does not guarantee truth."

- question: "What work does the 'justification' condition do in the JTB analysis — what cases does it rule out that truth and belief alone would allow in?"
  type: short-answer
  answer: "Justification rules out true beliefs held for bad reasons or by sheer luck — for example, a broken clock that happens to show the right time. Without justification, any true belief would count as knowledge, even one formed by guessing, wishful thinking, or coincidence."
  explanation: "The justification condition distinguishes knowledge from lucky true belief. If you guess that a coin will land heads and it does, you had a true belief but not knowledge — you had no principled reason to expect that outcome. Justification requires that your belief be based on good evidence or reliable reasoning: something that connects your belief to the truth in a non-accidental way."
```

## Explainer

Philosophy has long distinguished between merely believing something and actually *knowing* it. The justified true belief (JTB) account, traceable to Plato's *Meno* and *Theaetetus* and formalized in 20th-century analytic epistemology, proposes that three conditions are necessary and jointly sufficient for knowledge: truth, belief, and justification.

Each condition rules out a class of cases that clearly fall short of knowledge. The truth condition eliminates false beliefs: you cannot know that the earth is flat, because it isn't true — no matter how sincerely you believe it. The belief condition eliminates propositions you accept abstractly but don't genuinely assent to: a student who has memorized a theorem but doesn't really believe it applies to the current problem doesn't "know" it in the relevant sense. The justification condition — the most philosophically interesting — eliminates true beliefs held by luck or for bad reasons. A stopped clock is right twice a day; if you glance at it at exactly the right moment, your belief about the time is true, but you don't *know* the time, because your evidence is defective.

It is crucial not to confuse justification with certainty. Justification is not all-or-nothing and does not require infallibility. A detective who carefully assembles evidence and forms a reasonable conclusion is justified even if that conclusion turns out to be wrong. Justification is about the quality of the reasoning process, not a guarantee of truth. This is why the JTB account requires truth as a separate condition — because even good reasoning can occasionally produce false beliefs.

The elegance of the JTB analysis is that each condition appears necessary: remove any one of them and you get cases that fall short of knowledge. And the three conditions together appeared sufficient — philosophers thought that true belief held for good reasons just *is* knowledge. This confidence held for roughly two millennia until Edmund Gettier published a three-page paper in 1963 constructing cases where all three conditions are satisfied, yet intuitions strongly resist calling them knowledge. The JTB framework is thus both the starting point and the first target of contemporary epistemology.

Understanding JTB matters not just as historical background but because the three conditions continue to structure all subsequent theories of knowledge. Reliabilism, virtue epistemology, and contextualism each preserve the core insight — that knowledge requires more than a lucky true belief — while revising or supplementing the justification condition. Learning what JTB gets right prepares you to understand exactly where and why it falls short.
