---
id: underdetermination-duhem-quine
title: Underdetermination and the Duhem-Quine Thesis
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: theory-observation-distinction
  type: hard
- id: problem-of-induction-hume
  type: soft
builds-toward:
- confirmation-theory-science
- scientific-realism
tags:
- underdetermination
- holism
- theory-choice
stage: expert
status: validated
---

# Underdetermination and the Duhem-Quine Thesis

## Core Idea
The Duhem-Quine thesis states that no individual observation can conclusively test an isolated hypothesis because theories are tested holistically. When an experiment disagrees with prediction, we can always revise auxiliary hypotheses or background assumptions instead of rejecting the main theory. This means empirical evidence underdetermines theory choice: multiple incompatible theories can be consistent with all available evidence.

## How It's Best Learned
Examine historical cases: Fresnel vs Newton on light, or the perihelion of Mercury (Newton vs Einstein). Show how ambiguous observational data can support competing theoretical frameworks.

## Questions

```yaml
- question: "A physicist derives prediction P from main hypothesis H combined with auxiliary assumptions A. The experiment yields not-P. What does this logically establish?"
  type: multiple-choice
  options:
    - "H is false and should be abandoned"
    - "A is false and should be revised"
    - "At least one element of the conjunction H ∧ A is false, but logic alone cannot determine which"
    - "Both H and A are false, since both were required to derive P"
  answer: 2
  explanation: "This is the formal structure of the Duhem-Quine thesis. Modus tollens tells you that if (H ∧ A) → P and ¬P, then ¬(H ∧ A). But ¬(H ∧ A) is equivalent to ¬H ∨ ¬A — at least one is false. Logic alone cannot distribute the blame. You can save H by blaming A (miscalibrated instruments, wrong background assumption) or blame H by accepting A. This is why failed predictions never straightforwardly falsify a single hypothesis."

- question: "When Uranus's orbit deviated from Newtonian predictions, astronomers posited Neptune rather than abandoning Newton's laws. What does the Duhem-Quine thesis say about this strategy?"
  type: multiple-choice
  options:
    - "The strategy was invalid because Newtonian mechanics was the hypothesis actually being tested in isolation"
    - "The strategy was logically available — revising the auxiliary (the planet-count assumption) rather than the main law — and happened to be correct in this case"
    - "The strategy only works if the auxiliary hypothesis is independently verifiable before the experiment"
    - "The strategy proves that underdetermination does not apply to well-established theories like Newtonian mechanics"
  answer: 1
  explanation: "The Duhem-Quine thesis makes this a general logical point, not a special exception for Newton. Any time a prediction fails, revising an auxiliary is a logically available response. In the Uranus case, the auxiliary was 'we know all the planets perturbing Uranus's orbit' — a reasonable assumption to question. Le Verrier revised it by hypothesizing a new planet, and the telescope confirmed Neptune. The thesis says this was always an option; its success was an empirical discovery, not a logical necessity. The Mercury/Vulcan case shows the same strategy can fail."

- question: "According to the Duhem-Quine thesis, a single experiment that contradicts a theory's prediction conclusively refutes that theory."
  type: true-false
  answer: false
  explanation: "This is exactly what the Duhem-Quine thesis denies. A refuting observation shows that the conjunction H ∧ A is false, not that H alone is false. Scientists can always respond by revising one of the auxiliary hypotheses — about instruments, background conditions, or other known laws — rather than abandoning the main theory. Simple falsificationism (Popper's original view) overlooks this. Whether to revise H or A is a scientific judgment that appeals to criteria like simplicity, coherence, and prior probability — not a logical compulsion."

- question: "The Duhem-Quine thesis implies that when a prediction fails, logic alone does not determine which element of the theoretical web should be abandoned."
  type: true-false
  answer: true
  explanation: "This is the direct statement of the thesis. The failed prediction only entails that the total conjunction of hypotheses (H ∧ A₁ ∧ A₂ ∧ ... ∧ Aₙ) is false. Which element to reject is a choice underdetermined by logic. Scientists appeal to non-logical criteria — simplicity, conservatism (minimize revision), internal coherence, explanatory power — to make this choice. Quine argued this holism extends to the entire web of belief, with no sharp science/philosophy boundary."

- question: "The Neptune case and the Vulcan case both involved the same logical strategy in response to anomalous observations. Why does one count as science working correctly and the other as a research program that ultimately failed?"
  type: short-answer
  answer: "In both cases, astronomers protected Newton's laws by revising an auxiliary (the assumption that all gravitating bodies were known) and hypothesizing an undetected planet. The Neptune strategy succeeded: the hypothesized planet was found where predicted, confirming the auxiliary revision. The Vulcan strategy failed: no planet was found where predicted, and continued adjustments to the auxiliary grew increasingly implausible. Eventually, Einstein's general relativity explained Mercury's precession without any additional planet, making Newton's laws themselves the thing to revise. The Duhem-Quine thesis says both strategies were logically available; which was correct was an empirical question, not a logical one."
  explanation: "This is why the thesis does not make science arbitrary, even though it shows that no single experiment compels theory rejection. Scientists are always free to protect a theory by revising auxiliaries, but continued failures of that strategy — and the emergence of a better theory — eventually make theory revision the more rational choice. The thesis undermines naive falsificationism without collapsing into relativism: empirical evidence still constrains rational theory choice, just not by simple deduction."
```

## Explainer

From your study of the theory-observation distinction, you know that observations are never purely neutral: what we see is always interpreted through prior theoretical commitments. The Duhem-Quine thesis pushes this further, making a logical point about how scientific testing actually works. When a prediction fails, we cannot simply conclude that the hypothesis being tested is false — because that hypothesis was never doing the work alone. Any experiment tests a whole **web of beliefs** simultaneously.

Here is the formal structure: to derive a testable prediction, you need your main hypothesis H plus a set of **auxiliary hypotheses** A (assumptions about instruments, background conditions, other known laws). The prediction P follows only from H ∧ A together. When P turns out false, logic tells you that H ∧ A is false — but it does not tell you which component to reject. You could abandon H. Or you could blame one of the auxiliaries: the instruments were miscalibrated, the experimental conditions were not controlled, a background assumption was wrong. Pierre Duhem, the physicist-philosopher, first noticed this in the context of optics; W.V.O. Quine extended it into a global thesis about the entire web of belief.

The history of science is full of instructive cases. When Uranus's orbit deviated from Newtonian predictions, astronomers did not abandon Newton's law of gravitation. Instead, they adjusted an auxiliary: perhaps there is an undiscovered planet perturbing the orbit. Le Verrier calculated where Neptune must be, and the telescope confirmed it. That was the right call. But when Mercury's perihelion refused to cooperate with Newton, generations of astronomers tried the same strategy — a hypothetical planet Vulcan — without success. Eventually, Newtonian mechanics itself had to go. The **underdetermination** thesis captures why both responses were logically available: no observation *forces* you to give up any particular belief.

The philosophical implications are significant. If theory choice is underdetermined by evidence — if multiple incompatible theories can always be made consistent with all available data by adjusting auxiliaries — then what determines which theory we should choose? The answer must appeal to criteria beyond pure empirical adequacy: simplicity, coherence, explanatory power, conservatism (minimal departure from prior belief), fruitfulness. Quine argued this means there is no sharp distinction between empirical science and speculative philosophy; both are parts of the same web of belief, differing only in their distance from the observational periphery. The **Duhem-Quine thesis** thus motivates **holism**: confirmation and refutation always involve whole theoretical systems, never isolated hypotheses.
