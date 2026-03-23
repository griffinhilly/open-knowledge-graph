---
id: demarcation-problem-science
title: The Demarcation Problem
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: philosophy-of-science-intro
  type: hard
builds-toward:
- popper-falsificationism
- logical-positivism
tags:
- demarcation
- criteria
- pseudo-science
stage: expert
status: validated
---

# The Demarcation Problem

## Core Idea
The demarcation problem asks: What criteria distinguish science from non-science, pseudo-science, or metaphysics? Different philosophical schools propose different answers: falsifiability (Popper), verifiability (logical positivists), normal puzzle-solving (Kuhn), or research program progressivity (Lakatos). Each criterion captures something important but faces counterexamples.

## How It's Best Learned
Examine boundary cases: astrology vs astronomy, alchemy vs chemistry, Intelligent Design vs evolutionary biology. For each, apply different demarcation criteria and note which succeed or fail.

## Common Misconceptions
- There is a sharp, obvious line between science and non-science.
- A single universal criterion works for all cases.
- If something is not science, it is worthless or false.

## Questions

```yaml
- question: "Popper's falsifiability criterion faces the Duhem-Quine objection. What is the core of that objection?"
  type: multiple-choice
  options:
    - "Some perfectly good scientific theories have never actually been tested empirically"
    - "When an experiment fails, it could falsify any of the auxiliary assumptions bundled with the theory, not necessarily the core hypothesis — so no individual claim is ever straightforwardly falsified"
    - "Falsifiable claims can never be positively confirmed, only tentatively accepted, which is too weak a basis for scientific knowledge"
    - "Falsifiability cannot explain why astrology and astronomy are different in practice"
  answer: 1
  explanation: "The Duhem-Quine thesis points out that scientific theories are never tested in isolation — a prediction requires the core theory plus auxiliary assumptions (about instruments, background conditions, etc.). When a prediction fails, logic alone cannot tell you which component to reject. Scientists routinely protect core theories by revising auxiliaries (predicting Neptune rather than abandoning Newton). This shows that falsification in practice is a matter of judgment, not automatic logical invalidation, which is a deeper challenge to Popper than any of the other options."

- question: "A critic argues that psychotherapy is unscientific because practitioners can interpret any patient outcome as consistent with their theoretical framework. A Lakatosian would assess this claim by asking:"
  type: multiple-choice
  options:
    - "Whether psychotherapy is practiced by licensed and credentialed professionals"
    - "Whether the therapeutic research programme generates novel predictions that are subsequently confirmed, or merely adds protective assumptions after the fact to accommodate failures"
    - "Whether the therapy's practitioners believe their framework is falsifiable in principle"
    - "Whether the therapy has been endorsed by the current scientific paradigm's puzzle-solving community"
  answer: 1
  explanation: "For Lakatos, the key distinction is between a *progressive* research programme (one that generates new, confirmed predictions) and a *degenerative* one (one that only adds epicycles to protect a core that keeps failing). A therapy that accommodates every outcome by reinterpreting it after the fact, without making advance predictions that are then confirmed, is degenerative in Lakatos's sense — not because it is unfalsifiable in Popper's sense, but because it produces no new empirical content."

- question: "According to Popper, a theory that can accommodate any possible observation — that is never contradicted by evidence — is the most powerful kind of scientific theory."
  type: true-false
  answer: false
  explanation: "This is precisely what Popper argued *against*. For him, a theory that can accommodate anything predicts nothing — it has no empirical content. Popper worried about Freudian psychoanalysis and Adlerian psychology for exactly this reason: any patient behavior could be interpreted as confirming either theory. Scientific theories must be bold enough to risk falsification. The appearance of explaining everything is, for Popper, evidence of unscientific status rather than strength."

- question: "The failure to find a single sufficient criterion for demarcating science from non-science means the demarcation project has produced no practically useful tools for evaluating whether a field counts as scientific."
  type: true-false
  answer: false
  explanation: "The debate has produced a rich diagnostic toolkit: falsifiability, testability, novel predictive success, progressive research programmes, intersubjective verifiability. No single criterion works universally, but applied together they allow nuanced assessment of candidate disciplines. Astrology, for instance, scores poorly on multiple dimensions simultaneously — its predictions are vague, it insulates itself from failure, it generates no progressive research, and it invokes no known mechanisms. The absence of a bright line does not mean the tools are useless."

- question: "Why is the inability to find a single universal criterion for scientific status not a failure of the demarcation project?"
  type: short-answer
  answer: "Because the demarcation project's practical value lies in generating multiple diagnostic criteria — falsifiability, novel prediction, progressive research programmes, intersubjective verifiability — that can be applied simultaneously. Paradigmatic sciences score high on most of these; pseudosciences typically score low on several. The project reveals that 'science' is not a category with a sharp edge but a cluster concept, and the diagnostic tools it produced allow careful, multi-dimensional assessment of any candidate discipline."
  explanation: "The analogy to family resemblance concepts is useful: just as there is no single feature all games share, there is no single feature all sciences share. The demarcation debate clarified this and identified which overlapping features are characteristic. That is genuine philosophical progress, even without a knock-down criterion."
```

## Explainer

From your introduction to philosophy of science you know that science is not simply "what scientists do" — it involves specific methods of inquiry, distinctive standards of evidence, and a particular relationship between theory and observation. The demarcation problem asks the sharper question: can we specify, in precise terms, what separates scientific claims from non-scientific ones? This matters practically. Courts have had to decide whether Intelligent Design counts as science. Funding agencies allocate billions based on implicit demarcation judgments. The question is not merely academic.

Karl Popper's answer is the most famous: **falsifiability**. A claim is scientific if it is in principle refutable by observation. "All ravens are black" is scientific because a single white raven would falsify it. "God loves those who suffer" is not scientific because no possible observation could refute it — the believer can always reinterpret any outcome as consistent with divine love. Falsifiability elegantly handles why astrology feels unscientific: astrologers read favorable predictions into any outcome, insulating their claims from disconfirmation. The criterion also explains why psychoanalysis worried Popper — Freudian theory seemed capable of accommodating any patient behavior, which meant it predicted nothing and therefore risked explaining everything.

Falsificationism faces serious objections, however. The **Duhem-Quine thesis** (which you may encounter in later study) shows that scientific theories are never tested in isolation — when an experiment fails, it could falsify any of the auxiliary assumptions bundled with the theory, not necessarily the core hypothesis. Scientists routinely protect central theories by revising peripheral assumptions. This is not bad science; it is how science actually works. Newton's mechanics predicted a slight precession of Uranus's orbit that didn't match observation. Astronomers didn't abandon Newtonian gravity — they predicted a new planet (Neptune) to account for the discrepancy. The theory was not falsified; an auxiliary assumption about the number of planets was revised. Popper's criterion, applied strictly, would have required abandoning some of the most productive theories in scientific history.

Kuhn and Lakatos offer more historically grounded accounts. Kuhn holds that normal science is defined by commitment to a **paradigm** — a shared exemplary practice, not a criterion. Scientists solve puzzles within the paradigm; anomalies accumulate until a crisis forces a paradigm shift. On Kuhn's view, demarcation is sociological before it is logical. Lakatos refines this with the concept of **research programmes**: a progressive programme generates novel predictions that are confirmed; a degenerative one only adds epicycles after the fact to protect a failing core theory. These accounts explain better than Popper why scientists behave as they do — but they arguably push demarcation into degree and judgment rather than sharp criteria.

The lesson of the demarcation debate is not that the question is unanswerable but that **no single criterion is sufficient**. Falsifiability, testability, explanatory fruitfulness, novel prediction, intersubjective verifiability — these are all markers of scientific quality, and paradigmatic sciences score high on most of them while pseudosciences typically score low on several. Astrology makes predictions but they are vague; it insulates itself from failure; it generates no progressive research programme; its mechanisms invoke no known physical processes. The demarcation problem remains unsolved as a matter of sharp logical definition, but the diagnostic tools it has generated let us assess any candidate discipline on multiple dimensions rather than seeking a single bright line.

