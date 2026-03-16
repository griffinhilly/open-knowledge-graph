---
id: a-priori-and-a-posteriori
title: A Priori and A Posteriori Knowledge
domain: philosophy
course: epistemology
prerequisites:
- id: what-is-knowledge
  type: hard
- id: deductive-reasoning
  type: soft
- id: inductive-reasoning
  type: soft
- id: propositional-syntax
  type: soft
- id: modal-logic-intro
  type: soft
builds-toward:
- rationalism-vs-empiricism
- cartesian-skepticism
tags:
- a-priori
- a-posteriori
- necessity
- analyticity
- Kant
stage: formal-systems
status: validated
---

# A Priori and A Posteriori Knowledge

## Core Idea
A priori knowledge is justified independently of sensory experience — mathematics and logic provide the canonical examples, since we can establish that 2+2=4 or that all bachelors are unmarried through reasoning alone. A posteriori (empirical) knowledge depends essentially on sensory experience for its justification. Kant famously complicated this picture by arguing that some a priori knowledge is synthetic (genuinely informative about the world, not merely definitional), generating the puzzle of how pure reason can extend our knowledge beyond conceptual truths.

## How It's Best Learned
Contrast clear cases: 'All triangles have three sides' (a priori) vs. 'Water boils at 100°C at sea level' (a posteriori). Then examine boundary cases — mathematical knowledge, knowledge of modal truths, moral knowledge — to see where intuitions about priority become contested.

## Common Misconceptions
- A priori does not mean 'innate'; it means justifiable without appeal to experience.
- The a priori / a posteriori distinction (about justification) is orthogonal to the necessary / contingent distinction (about truth) — Kripke showed some necessary truths are knowable only a posteriori (e.g., 'Water is H₂O').

## Questions

```yaml
- question: "Which of the following is the clearest example of a priori knowledge?"
  type: multiple-choice
  options:
    - "Water freezes at 0°C at standard atmospheric pressure."
    - "All bachelors are unmarried."
    - "The Eiffel Tower is located in Paris."
    - "Gold has an atomic number of 79."
  answer: 1
  explanation: "'All bachelors are unmarried' is knowable through conceptual analysis alone — 'bachelor' just means 'unmarried man,' so no observation is required to verify it. The other three examples require empirical investigation: water's freezing point, the Eiffel Tower's location, and gold's atomic number are all discovered through experience, making them a posteriori."

- question: "A priori knowledge is the same as innate knowledge — truths that humans are born already knowing, prior to any experience or learning."
  type: true-false
  answer: false
  explanation: "A priori means justifiable without appeal to sensory experience, not that the knowledge is genetically hardwired. A child who learns the axioms of arithmetic and derives a theorem has acquired a priori knowledge through study and reasoning — not through being born with it. Kant separated the epistemic question (how is knowledge justified?) from the psychological question (how did it come to be in the mind?)."

- question: "Kant claimed that some knowledge is both 'synthetic' and 'a priori.' What does this mean, and why was it philosophically significant?"
  type: short-answer
  answer: "Synthetic a priori knowledge is genuinely informative about the world (synthetic — not merely a definitional truth) yet justifiable through pure reason without sensory experience (a priori). Kant's examples include mathematical truths like '7 + 5 = 12' and causal principles like 'every event has a cause.' This was significant because it challenged empiricists who claimed all non-trivial knowledge must come from experience, showing that reason alone can extend our knowledge beyond mere definitions."
  explanation: "Before Kant, the a priori was generally assumed to cover only analytic truths — statements true by definition. If 'bachelor means unmarried man,' then 'all bachelors are unmarried' adds nothing new. Kant argued that mathematics and fundamental principles of experience are different: they are not just unpacking definitions, yet we know them without running experiments. This opened a new question: how is synthetic a priori knowledge possible? His answer — that the mind imposes certain structures on experience — remains one of philosophy's most influential (and contested) ideas."
```

## Explainer

One of epistemology's most useful distinctions cuts across every field of knowledge: some things we can figure out by thinking alone, and other things we can only know by going out and looking. This is the **a priori / a posteriori** distinction. "A priori" (Latin: "from the earlier") means knowable before or independently of experience; "a posteriori" (Latin: "from the later") means knowable only through experience. The distinction is about **justification** — what entitles us to believe something — not about how we first encountered the claim.

The clearest cases are easy. "All triangles have three sides" is a priori: you can verify it by analyzing what a triangle is, without measuring any physical object. "The boiling point of water is 100°C at sea level" is a posteriori: you must run an experiment (or trust someone who did). Mathematics and logic supply the canonical body of a priori knowledge; natural science supplies the canonical body of a posteriori knowledge. Most philosophical work involves the boundary cases — moral claims, modal claims about what is possible or necessary, introspective reports — where it is genuinely contested which side applies.

Kant added a second dimension to this picture by crossing the a priori/a posteriori distinction with the **analytic/synthetic** distinction. An analytic statement is one where the predicate is already contained in the subject ("All bachelors are unmarried"). A synthetic statement genuinely extends our knowledge ("The cat is on the mat"). Before Kant, the dominant assumption was that all a priori knowledge was analytic — all you could know without experience was what was already packed into your concepts. Kant challenged this by arguing for **synthetic a priori** knowledge: claims that are both genuinely informative and knowable through pure reason. His examples included arithmetic, geometry, and fundamental causal principles. This claim is still debated today.

A third important wrinkle comes from Saul Kripke's 20th-century work, which showed that the a priori/a posteriori distinction is logically independent from the **necessary/contingent** distinction (about whether a truth could have been otherwise). We might assume: necessary truths are a priori, contingent truths are a posteriori. Kripke dismantled this assumption. "Water is H₂O" is a **necessary** truth — in any possible world, water just is H₂O — but we could only discover this empirically, through chemistry. So it is **necessary a posteriori**. Conversely, "the meter is the length of this particular rod in Paris" was once **contingently** true but was stipulated to be true by definition — making it **contingent a priori** in some sense. These cases reveal that what's necessary about a thing and how we come to know it are different questions.

For epistemology, the a priori/a posteriori distinction matters because it shapes debates about the limits of reason. Empiricists (Hume, Locke, the Logical Positivists) tend to restrict a priori knowledge to analytic truths — definitional or logical — and insist that anything substantive about the world requires experience. Rationalists (Descartes, Leibniz, Kant) argue that reason can reach further. Knowing which side of the line a given claim falls on is often itself the philosophical question under investigation.
