---
id: no-false-lemmas-condition
title: The No False Lemmas Condition
domain: philosophy
course: epistemology
prerequisites:
- id: gettier-cases-formal-analysis
  type: hard
builds-toward:
- defeasibility-conditions-knowledge
tags:
- gettier
- responses
- knowledge
- false-lemmas
stage: formal-systems
status: validated
---

# The No False Lemmas Condition

## Core Idea
The no false lemmas condition, developed by Lehrer and others, proposes that knowledge requires not only justified true belief but also that the belief not be based on any false lemmas or false intermediate steps. This condition aims to eliminate Gettier cases by excluding inferences that depend crucially on falsehoods, even if those falsehoods don't directly appear in the justification.

## Questions

```yaml
- question: "Smith justifiably believes 'Jones will get the job' and infers 'The person who gets the job has ten coins in their pocket' (after counting Jones's coins). Smith gets the job and happens to have ten coins. Does the no false lemmas condition explain why Smith lacks knowledge?"
  type: multiple-choice
  options:
    - "Yes — Smith's inference passed through the false lemma 'Jones will get the job'"
    - "No — Smith's belief is true and justified, so no additional condition is needed"
    - "No — the no false lemmas condition applies only to deductive, not inductive, inferences"
    - "Yes — but only because Smith counted the wrong person's coins"
  answer: 0
  explanation: "This is a canonical Gettier case. Smith's inference ran through the false lemma 'Jones will get the job.' That lemma is false — Smith gets the job, not Jones. The true conclusion happens to be true for a different reason (Smith has ten coins), making the truth of the belief accidental relative to Smith's evidence. The no false lemmas condition correctly diagnoses non-knowledge by identifying the false intermediate step in the inferential chain."

- question: "Henry is driving and perceives what he takes to be a barn, forming the belief 'That is a barn.' The region is full of convincing barn facades, but he happens to be looking at the one real barn. According to the no false lemmas condition, does Henry know there is a barn?"
  type: multiple-choice
  options:
    - "Yes — his belief is true, justified, and contains no false inferential lemma"
    - "No — his inference passed through the false lemma 'This region contains only real barns'"
    - "No — the condition correctly identifies that his perceptual process is unreliable"
    - "Yes — he has knowledge because he is actually looking at a real barn"
  answer: 0
  explanation: "This case reveals the condition's critical limitation. Henry's belief is formed directly through perception — there is no explicit inferential lemma in his reasoning. The no false lemmas condition has nothing to diagnose because there is no inferential chain with a false step. Yet many philosophers judge this not to count as knowledge (the truth is accidental relative to Henry's epistemic situation). The condition is insufficient: some Gettier-style cases escape its reach entirely."

- question: "The no false lemmas condition is a proposed fourth condition on knowledge, added to the traditional justified true belief account specifically to handle Gettier cases."
  type: true-false
  answer: true
  explanation: "Gettier (1963) showed that justified true belief is not sufficient for knowledge — some JTBs are merely luckily true. The no false lemmas condition adds a fourth requirement: the justification must not essentially depend on any false intermediate proposition. It is an attempt to close the Gettier gap by requiring that the inferential route from evidence to belief be free of false steps."

- question: "The no false lemmas condition successfully handles most Gettier cases, making it a complete theory of knowledge."
  type: true-false
  answer: false
  explanation: "The condition handles Gettier cases where inference passes through a false lemma — a significant class. But it fails for non-inferential Gettier cases, such as barn facade scenarios where a perceptual belief is formed directly with no inferential chain. Because some Gettier cases involve no lemmas at all, the condition's scope is too narrow. This limitation motivates defeasibility approaches, which address a broader range of epistemic defeaters."

- question: "Describe the type of Gettier case that the no false lemmas condition cannot handle, and explain why the condition fails there."
  type: short-answer
  answer: "The condition fails for non-inferential Gettier cases — situations where a true belief is formed directly through perception without passing through any explicit intermediate proposition. The barn facade case is canonical: Henry forms 'that is a barn' by looking, with no inferential chain. Since there are no lemmas, the condition has nothing to flag. Yet the belief seems not to count as knowledge because its truth is accidental relative to Henry's epistemic situation — he could just as easily have been looking at a facade. The condition's scope is limited to inferential beliefs, so it cannot diagnose cases where luck enters through the perceptual process itself."
  explanation: "This limitation also reveals something deeper: 'false lemma' is one type of epistemic defeater, but not the only type. Defeasibility theory generalizes the insight by asking whether any true information could undermine the justification — a broader test that captures perceptual Gettier cases too."
```

## Explainer

From your formal analysis of Gettier cases, you know the problem: there are situations where a person has a true, justified belief that nonetheless seems not to count as knowledge, because the route from justification to truth runs through luck. The challenge is to identify exactly what extra ingredient knowledge requires beyond JTB. The **no false lemmas condition** is one of the earliest and most intuitive proposals: knowledge fails whenever the inferential path from justification to belief passes through a false intermediate step, even if the final belief is true.

Consider the canonical Gettier-style case. Smith justifiably believes "Jones owns a Ford" (perhaps Jones drives one, has always owned one, etc.). From this, Smith infers "Either Jones owns a Ford, or Brown is in Barcelona" — a true disjunction, formed by adding a random second disjunct. As it happens, Jones does not own a Ford, but Brown genuinely is in Barcelona. So Smith has a justified true belief in the disjunction, but it seems wrong to say he *knows* it. The no false lemmas diagnosis: Smith's inference ran through the false lemma "Jones owns a Ford." Because that lemma is false, the epistemic connection between Smith's justification and the true conclusion is broken — the truth of the conclusion is accidental relative to his evidence.

The condition can be stated formally: S knows that p if and only if (i) p is true, (ii) S believes that p, (iii) S is justified in believing p, and (iv) S's justification does not essentially depend on any **false lemma** — that is, there is no false proposition q such that S's belief that p is inferred (explicitly or implicitly) from q. Condition (iv) is the addition. It targets the structure of inferential chains: even if the final product is true, if the chain passed through a falsehood, the inference is epistemically tainted.

The condition handles many Gettier cases cleanly and has a strong intuitive motivation: falsehoods in an inference are like forged links in a chain — the chain still holds the weight, but by luck rather than by its actual structure. However, the condition runs into **counterexamples from the other direction**. Some Gettier cases appear not to involve any false lemma: perception-based cases where you form a belief directly from a reliable perceptual process, without any inferential chain at all, can still generate Gettier-like luck. If you perceive a barn while driving through a region full of convincing barn facades (and you happen to be looking at the one real barn), your perceptual belief has no inferential lemmas — yet many philosophers judge it not to count as knowledge. No false lemmas cannot diagnose this case, because there are no lemmas at all.

This limitation motivates the move to **defeasibility conditions** — the next development in this line of thought. Instead of asking whether the inferential chain contains falsehoods, defeasibility approaches ask whether the justification would survive the addition of true information. The no false lemmas condition is, in effect, a special case of defeasibility: a false lemma is one salient way a justification can be defeated. But not all defeaters are false lemmas, and tracking that fuller space of potential defeaters requires a more general framework.
