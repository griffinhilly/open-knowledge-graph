---
id: gettier-problems
title: Gettier Problems
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
- id: counterexample-method
  type: hard
builds-toward:
- responses-to-gettier
- epistemic-luck
- reliabilism
tags:
- Gettier
- counterexample
- JTB
- luck
- knowledge-analysis
stage: formal-systems
status: validated
---

# Gettier Problems

## Core Idea
In a three-page 1963 paper, Edmund Gettier refuted the JTB analysis by constructing cases where an agent has justified true belief but intuitively lacks knowledge. In one case, Smith justifiably believes Jones will get the job and has ten coins in his pocket; Smith also (unknowingly) has ten coins in his own pocket. Smith infers 'the man who will get the job has ten coins in his pocket' — a belief that turns out true, but for the wrong reason, since Smith himself gets the job. Such Gettier cases share a structure: justification is present, truth is present, belief is present, yet knowledge seems absent because the truth and justification are connected only by accident.

## How It's Best Learned
Construct several Gettier cases yourself, trying to vary the structure. Identify what each case has in common: the belief is justified by evidence that fails to track the actual truth-maker. Then ask what additional condition, if added to JTB, would block all such cases.

## Common Misconceptions
- Gettier cases are not exotic philosophical puzzles with no practical relevance; they reveal a deep structural gap between reliable justification and actual truth-tracking.
- Adding 'no false lemmas' to JTB blocks Gettier's original cases but not all Gettier-style cases.

## Questions

```yaml
- question: "Smith justifiably believes his colleague Jones will get a promotion (based on reliable inside information). From this, Smith infers: 'The person getting the promotion drives a red car' — because he knows Jones drives a red car. Unknown to Smith, it is actually Smith himself who gets the promotion, and Smith also drives a red car. Smith's belief is justified, true, and based on valid inference. Does Smith know that the person getting the promotion drives a red car?"
  type: multiple-choice
  options:
    - "Yes — the belief is justified, true, and based on a valid inference, which is all JTB requires"
    - "No — because Smith's belief, though justified and true, is true for the wrong reason: his justification tracked Jones, but the truth-maker is his own car"
    - "No — because Smith's original belief about Jones was false, so the inference is also false"
    - "Yes — truth and justification are both present, and the reason for truth is irrelevant to knowledge"
  answer: 1
  explanation: "This is a Gettier case. Smith's belief is justified (he had good evidence about Jones), true (the promotee does drive a red car), and believed. But he does not know it, because the truth is connected to his justification only accidentally. His justification was about Jones; the actual truth-maker is his own situation. This is the structural feature of all Gettier cases: justification and truth are present, but they are linked by luck rather than by the justification tracking the actual truth-maker. Options A and D represent the JTB view that Gettier's cases refute."

- question: "Henry is driving through a region filled with realistic barn facades, though he doesn't know this. He looks directly at the one real barn in the area and forms the justified true belief 'that's a barn.' What makes this a Gettier-style case, and what does it reveal that the 'no false lemmas' response to Gettier cannot handle?"
  type: multiple-choice
  options:
    - "Henry's belief is unjustified because he should have checked whether it was a facade"
    - "The case is not a Gettier problem because Henry's belief happens to be true"
    - "Henry's belief contains a false intermediate step: he assumed all barn-like shapes are real barns"
    - "Henry has no false intermediate beliefs, yet most philosophers say he doesn't know — revealing that epistemic luck, not false lemmas, is the core problem with JTB"
  answer: 3
  explanation: "The 'no false lemmas' response to Gettier says: your belief cannot depend on any false intermediate belief. This blocks Gettier's original cases, but the fake barns case has no false lemma — Henry's inference is direct, and his perceptual belief is formed without any false intermediate step. Yet the environment was rigged against reliable barn-perception. Henry's belief could easily have been false (he was lucky to look at the one real barn). This case reveals that the real problem is not false lemmas but epistemic luck: the belief is true, but only by coincidence, given how the world was arranged around Henry."

- question: "Gettier cases demonstrate that justification is not necessary for knowledge — that you can have knowledge without any justification at most."
  type: true-false
  answer: false
  explanation: "Gettier cases demonstrate that justification is not *sufficient* for knowledge — that JTB (justified true belief) is not enough. They do not challenge the necessity of justification. In all Gettier cases, the agent has justification; that is precisely why the cases are puzzling. The problem is that justification, truth, and belief can all be present yet knowledge can still be absent, because the three components are connected only accidentally. The long-standing response to Gettier seeks a *fourth* condition to add to JTB, not to remove justification."

- question: "Adding a 'no false lemmas' condition to JTB — requiring that your belief not depend on any false intermediate belief — successfully blocks most Gettier-style counterexamples."
  type: true-false
  answer: false
  explanation: "The 'no false lemmas' response blocks Gettier's original cases (both depend on the false belief that Jones will get the job or that Jones has coins in his pocket). But Gettier-style cases can be constructed without any false intermediate beliefs. The fake barns case is the canonical example: Henry's justified true belief that 'that's a barn' involves no false lemma, yet intuitively he doesn't know it. This shows that the real issue is epistemic luck — the belief being true in a way that could easily have been false — which 'no false lemmas' does not address."

- question: "What structural feature do all Gettier cases share, and why does this feature mean that having justified true belief is not enough for knowledge?"
  type: short-answer
  answer: "In every Gettier case, the justification is a reliable indicator of some fact, but the belief turns out true for a different reason than the one the justification tracks. Justification and truth are present, but they are connected only accidentally — the belief could easily have been false despite the justification, or is true because of a lucky coincidence rather than because the justification reliably tracked the truth-maker."
  explanation: "The recipe for constructing a Gettier case makes the structure explicit: start with justified belief in a false proposition P; from P, validly infer a true proposition Q. The belief in Q is justified (by inheritance from P), true (by construction), but not known — because the false P was the epistemic route to Q, and the truth of Q is a coincidence unrelated to that route. What genuine knowledge requires is that the justification actually track the truth-maker — the connection between why you believe something and why it's true must not be merely accidental. This is what drives post-Gettier epistemology toward concepts like reliability, proper function, and the elimination of epistemic luck."
```

## Explainer

You already know that the **justified true belief** (JTB) analysis proposes three necessary and jointly sufficient conditions for knowledge: you know that P if and only if you believe P, P is true, and your belief is justified. This seemed to capture what knowledge is — not lucky guessing (you need justification), not false belief (you need truth), not mere inclination (you need actual belief). Gettier's 1963 paper showed in three pages that the analysis is wrong, and it changed epistemology permanently.

The key to understanding Gettier cases is the **accidental connection** between justification and truth. In standard cases of knowledge, your justification is a reliable indicator of the truth — you see a red barn, and that perception justifies "there's a red barn," and the truth and the justification are connected because the barn itself caused your perception. Gettier cases sever this connection. Your justification is legitimate, the belief turns out true, but the truth is reached by a route different from the one your justification tracks. The coin-in-the-pocket case is the original: Smith justifiably believes "Jones will get the job" (on good evidence) and "Jones has ten coins in his pocket" (having personally counted them). Smith infers "the man who will get the job has ten coins in his pocket." The inference is valid; the conclusion is true. But it's true because Smith himself gets the job, and Smith happens to have ten coins in his pocket — facts Smith didn't know. Smith's justification was for a true belief that reached the truth by accident.

The **counterexample method** you know is precisely what Gettier deployed: find a case that satisfies the definition yet clearly lacks the property being defined. The philosophical power of his cases comes from their simplicity and reproducibility — you can construct Gettier cases yourself by following a simple recipe. Start with a justified belief in a false proposition P. From P, infer a true proposition Q. Your belief in Q is justified (because it follows from a justified belief), it is true (by construction), but you don't know Q because the false proposition P was your route to it. The truth of Q and your justification are accidentally related.

Post-Gettier epistemology spent decades trying to add a fourth condition to JTB that would close the gap. The **no false lemmas** response says: your belief must not depend on any false intermediate belief. This blocks Gettier's original cases (both depend on the false belief "Jones will get the job"). But Gettier-style cases can be constructed without false lemmas. In a classic **fake barns** case: you're driving through a region filled with barn facades, indistinguishable from real barns. You look at the one real barn in the area and form the justified true belief "that's a barn." No false intermediate belief — yet most philosophers say you don't know. The environment was rigged against reliable barn-perception. This reveals that the real problem isn't false lemmas; it's **epistemic luck**: your belief is true, but it could easily have been false given how things were arranged. Eliminating luck from the conditions for knowledge became the central project of post-Gettier epistemology.


