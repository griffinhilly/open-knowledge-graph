---
id: popper-falsificationism
title: Popper's Falsificationism
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: demarcation-problem-science
  type: hard
- id: problem-of-induction
  type: soft
builds-toward:
- falsifiability-criterion
- kuhn-paradigm-theory
- lakatos-research-programs
tags:
- falsificationism
- demarcation
- critique
- hypothesis-testing
stage: expert
status: validated
---

# Popper's Falsificationism

## Core Idea
Karl Popper proposed that science be demarcated by falsifiability: a theory is scientific if there exist possible observations that would prove it false. Instead of seeking confirmation, Popper advocated bold conjecture and criticism: propose ambitious theories, vigorously attempt to refute them, and only accept provisionally until falsified. This avoids logical problems of induction while preserving empiricism. Popper argued that scientific progress comes through elimination of false theories, not accumulation of confirmed instances.

## How It's Best Learned
Compare falsifiability with verifiability on examples like 'God exists', 'the sun will rise tomorrow', quantum mechanics, and psychoanalysis. Examine why some unfalsifiable theories are considered unscientific.

## Questions

```yaml
- question: "Astronomers observe that Uranus's orbit deviates from Newtonian predictions. A strict Popperian might argue Newton's theory is falsified; actual scientists instead predicted an unknown planet (Neptune). What philosophical tension does this example reveal?"
  type: multiple-choice
  options:
    - "It shows that Newton's theory was not falsifiable, because it could always accommodate new observations"
    - "It shows that the Duhem-Quine problem is real — theories are tested alongside auxiliary assumptions, so a failed prediction can be resolved by revising an auxiliary hypothesis rather than the core theory"
    - "It shows that Popper's method was correct — scientists should have abandoned Newton after the first anomaly"
    - "It shows that falsifiability is irrelevant to actual scientific practice and should be abandoned"
  answer: 1
  explanation: "The Neptune case is the classic illustration of the Duhem-Quine problem that Popper acknowledged but struggled to fully answer. Newton's theory predicts planetary orbits given initial conditions and assumed bodies — revising the auxiliary assumption (how many planets exist) rather than the core theory was scientifically legitimate. Popper's response was that scientists must commit in advance to which auxiliary assumptions are fixed; critics like Kuhn and Lakatos argued this was too simplistic as a description of actual science."

- question: "A scientist conducts ten experiments, each confirming a theoretical prediction. Popper would say this makes the theory:"
  type: multiple-choice
  options:
    - "Confirmed — repeated successful predictions raise the probability that the theory is true"
    - "Verified — ten confirmations are sufficient to establish the theory as scientific fact"
    - "Corroborated — the theory has survived ten attempts to falsify it, which is not the same as increasing its probability of truth"
    - "Well-supported inductively — Popper accepted induction for well-tested theories"
  answer: 2
  explanation: "Popper explicitly rejected the concept of confirmation and replaced it with corroboration. A corroborated theory has survived attempts to falsify it — that is all we can say. It does not become more probably true with each successful test; Popper accepted Hume's argument that induction cannot logically justify universal claims. We hold corroborated theories provisionally as our best current conjectures, knowing they remain falsifiable."

- question: "According to Popper, a scientific theory becomes more strongly confirmed — and thus more probably true — the more successful predictions it makes."
  type: true-false
  answer: false
  explanation: "This is the core misconception about Popper. He rejected confirmation in favor of corroboration, and he accepted Hume's problem of induction as unanswerable. Surviving tests does not increase a theory's probability of truth — it only shows the theory has not yet been falsified. The theory remains a conjecture we provisionally accept, not a fact we have established. Popper's asymmetry runs in one direction only: falsification is logically decisive; confirmation is not."

- question: "On Popper's account, an unfalsifiable claim such as 'most events have a cause' is necessarily false or meaningless."
  type: true-false
  answer: false
  explanation: "Popper's demarcation criterion distinguishes scientific from non-scientific claims — not true from false, or meaningful from meaningless. An unfalsifiable claim may be true, profound, or philosophically important; it simply cannot be tested empirically in the way science requires. Popper was careful to say that metaphysical claims fall outside science without thereby dismissing them. His target was the pretense of scientific status, not the claim's truth or meaning."

- question: "Why does Popper argue that logical asymmetry between verification and falsification makes falsifiability the right demarcation criterion for science?"
  type: short-answer
  answer: "No finite number of confirming observations can logically entail a universal generalization — this is Hume's problem of induction, which Popper accepted as unanswerable. But a single counterexample can definitively refute a universal theory by modus tollens: if theory T implies observation O, and O is false, then T is false. Since falsification is logically decisive and verification is not, Popper proposed falsifiability — the existence of possible observations that would contradict the theory — as the mark of a genuinely empirical, scientific claim."
  explanation: "The key is the logical asymmetry: universal statements are asymmetric with respect to confirmation and refutation. 'All swans are white' cannot be proven true by any finite list of white swans, but it can be proven false by one black swan. Science should exploit this asymmetry by designing tests that could actually show the theory wrong, rather than searching for confirming instances — which can always be found for any sufficiently vague claim."
```

## Explainer

You already know Hume's problem of induction: no finite number of observations, however large, can logically justify a universal generalization. We've seen a million white swans, but the next swan could be black — logic gives us no guarantee. This seems to undermine science at its foundations, since science depends on universal laws derived from finite observation. Popper's falsificationism is, in part, a bold response to this problem: instead of solving induction, he proposed abandoning it as the basis for scientific method.

Popper's key insight is **logical asymmetry**: while a thousand confirmations can never prove a universal theory, a single counterexample can refute it. If Newton's theory predicts that planets move in ellipses, and one planet is observed to deviate, the theory is falsified — definitively, by deductive logic (modus tollens: if theory T, then observation O; not-O; therefore not-T). Popper concluded that the proper aim of science is not to confirm theories but to **conjecture boldly and attempt falsification**. Science advances by eliminating false theories through critical testing, not by accumulating confirmations.

This gives Popper his **demarcation criterion**: a theory is scientific if and only if it is falsifiable — if there exist possible observations that would contradict it. Unfalsifiable claims aren't necessarily wrong or meaningless, but they aren't scientific. By this criterion, Freudian psychoanalysis and Adlerian psychology fail: they can accommodate any observation. A patient who resists treatment shows repression; a patient who responds well shows the therapy worked. No possible observation rules out the theory. In contrast, Einstein's general relativity made the bold prediction that starlight would bend around the sun by a specific angle — a claim that could easily have been refuted, and which therefore counts as genuinely scientific.

The concept of **corroboration** replaces confirmation in Popper's framework. A theory isn't verified when it survives testing — it is *corroborated*, meaning it has survived attempts to falsify it so far. Corroboration is not inductive support; it says nothing about the probability that the theory is true. We accept theories provisionally, as our best current conjectures, knowing they may be overturned. Science is not a body of proven truths but a self-correcting process of conjecture and criticism.

The central objection is the **Duhem-Quine problem**: theories are never tested in isolation. Any prediction requires auxiliary assumptions (about instruments, initial conditions, background theories). When an observation conflicts with a prediction, you can always save the theory by revising an auxiliary assumption instead of rejecting the core theory. Popper acknowledged this but argued that such "immunizing stratagems" are methodologically forbidden — a scientist must commit in advance to what would count as falsification. Critics like Kuhn and Lakatos argued that actual scientific practice is far more complex, and that the history of science shows productive research programs surviving apparent falsifications through exactly the moves Popper prohibits.
