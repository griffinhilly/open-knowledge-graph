---
id: epistemic-luck
title: Epistemic Luck
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
- id: gettier-problems
  type: soft
builds-toward:
- responses-to-gettier
- reliabilism
- epistemic-virtues
tags:
- luck
- safety
- sensitivity
- modal-epistemology
stage: formal-systems
status: validated
---

# Epistemic Luck

## Core Idea
Epistemic luck is the phenomenon by which a belief turns out true in a way that is too coincidental to count as knowledge. Gettier cases are one species of epistemic luck, but the concept is broader: a stopped clock that is right twice a day yields a true belief by luck; a clairvoyant who accidentally guesses correctly has a true belief by luck. Two modal conditions have been proposed to exclude epistemic luck: sensitivity (if p were false, S would not believe p) and safety (S could not easily have had a false belief formed in the same way). Safety is generally preferred because sensitivity yields counterintuitive results for known necessary truths.

## How It's Best Learned
Evaluate safety and sensitivity against a range of cases: lottery beliefs, knowledge of necessary truths, standard perceptual beliefs. Check whether each condition correctly classifies the cases as knowledge or not-knowledge.

## Common Misconceptions
- Sensitivity and safety are not equivalent; they diverge on cases involving necessary truths and some counterfactual structures.
- Eliminating epistemic luck does not require certainty — safety is a modal condition, not a psychological one.

## Questions

```yaml
- question: "You glance at a stopped clock that happens to display the correct time (3:15), and you form the belief 'It is 3:15.' Your belief is true and you have no reason to doubt the clock. Does this count as knowledge?"
  type: multiple-choice
  options:
    - "Yes — the belief is true and you have a reliable-seeming justification"
    - "No — the belief is true by luck; in most nearby possible situations the same method would yield a false belief"
    - "Yes — knowledge only requires truth and belief; justification is secondary"
    - "No — you can never have knowledge of the current time without a certified timepiece"
  answer: 1
  explanation: "This is a paradigm case of epistemic luck. The belief is true and justified — you looked at a clock, which is normally a reliable method — but in almost every nearby possible world where you check that same clock, it displays 3:15 whether or not it is 3:15. The safety condition captures what's missing: a safe belief is one that could not easily have been false. Here, the belief could very easily have been false (the clock was stopped; it is correct only twice a day). Option A describes a belief that passes the JTB test but fails to be knowledge — exactly the problem epistemic luck theory addresses."

- question: "Which of the following best characterizes the safety condition on knowledge?"
  type: multiple-choice
  options:
    - "S's belief that p is safe if S is certain of p — doubt would indicate unsafe belief"
    - "S's belief that p is safe if S could not easily have formed a false belief using the same method in the same situation"
    - "S's belief that p is safe if S could have arrived at the belief through a different method"
    - "S's belief that p is safe if p is a necessary truth that cannot be false in any possible world"
  answer: 1
  explanation: "Safety is a modal condition: it concerns what could easily have happened, not what did happen. A belief is safe if in nearby possible worlds — worlds that are very similar to the actual world — the same belief-forming process would not have produced a false belief. This is different from certainty (a psychological state) and different from necessity (a logical property of propositions). Option A confuses psychological confidence with modal reliability. Option D misdescribes safety as a property of the believed proposition rather than the belief-forming process."

- question: "A belief can be both true and justified yet still fail to constitute knowledge because it is true by luck."
  type: true-false
  answer: true
  explanation: "This is the central lesson of Gettier cases and the broader theory of epistemic luck. The traditional justified-true-belief (JTB) analysis of knowledge held that justification + truth was sufficient for knowledge. Gettier showed otherwise: you can have a justified true belief where the belief happens to be true for reasons unrelated to the justification. The stopped clock, the broken thermometer that happens to read the ambient temperature, and Gettier's original cases all share this structure: truth and justification are present, but the truth is coincidental relative to the justification, which is why epistemic luck theories add a further condition."

- question: "The sensitivity condition and the safety condition always classify beliefs identically — any belief that passes one passes the other."
  type: true-false
  answer: false
  explanation: "Sensitivity and safety are not equivalent and diverge on important cases. Sensitivity says: if p were false, S would not believe p. Safety says: S could not easily have had a false belief via the same method. They come apart on necessary truths: 'If 2+2=4 were false, would you still believe it?' is a meaningless counterfactual (there is no possible world where 2+2≠4), so sensitivity cannot classify beliefs in necessary truths. But you can have safe beliefs in necessary truths (your belief-forming process reliably tracks them). This is why safety is generally preferred — it handles necessary truths without counterintuitive results."

- question: "Why does the safety condition, rather than mere justification, rule out the stopped-clock case as knowledge?"
  type: short-answer
  answer: "Justification is present in the stopped-clock case — the believer used a normally reliable method (checking a clock). What's missing is that the belief could very easily have been false: in the vast majority of nearby possible worlds where the same clock is consulted at a random time, it displays 3:15 regardless of the actual time, so the belief would be false. Safety requires that in nearby possible worlds where the same belief-forming process is used, the belief is not false. The stopped clock fails this condition because its reliability is accidental — it produces a true belief only twice a day, making the actual true belief a matter of luck rather than reliable connection to the facts."
  explanation: "The key move is shifting from asking 'Was the belief justified?' (which it was — clocks are normally reliable) to asking 'Could this belief easily have been false?' (which it could — the clock is stopped). Safety is designed to capture this modal dimension: knowledge requires not just that you happened to get it right, but that your belief-forming method is reliably connected to the truth in nearby circumstances, not just in this lucky instance."
```
