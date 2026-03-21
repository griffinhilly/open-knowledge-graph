---
id: lakatos-research-programs
title: Lakatos and Research Programs
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: kuhn-paradigm-theory
  type: hard
- id: popper-falsificationism
  type: soft
builds-toward:
- feyerabend-methodology-anarchy
- scientific-realism
tags:
- lakatos
- research-program
- hard-core
- protective-belt
stage: advanced
status: draft
---

# Lakatos and Research Programs

## Core Idea
Imre Lakatos attempted to reconcile Popper's falsificationism with Kuhn's historical observations. He proposed that science progresses through research programs with a hard core (fundamental assumptions protected from refutation) surrounded by a protective belt of auxiliary hypotheses that face empirical tests. A research program is progressive if it generates new theories with novel predictive content. Scientists rationally continue with a progressive program even as it faces anomalies, but switch to a better program when the old becomes degenerating.

## Questions

```yaml
- question: "An anomalous planetary orbit threatens the Newtonian research program. Scientists hypothesize an undiscovered planet whose gravitational pull would explain the anomaly. Astronomers search and find the planet at the predicted location. According to Lakatos, how should this protective-belt adjustment be evaluated?"
  type: multiple-choice
  options:
    - "The adjustment was degenerating — scientists should have abandoned Newton's Laws at the first anomaly rather than adding auxiliary hypotheses"
    - "The adjustment was ad hoc — it was invented specifically to explain a known anomaly"
    - "The adjustment was progressive — it successfully predicted a novel fact (the planet's existence and location) that was subsequently confirmed, expanding the program's empirical content"
    - "The evaluation is impossible — Lakatos's framework only applies to transitions between entire research programs, not individual auxiliary adjustments"
  answer: 2
  explanation: "This is Lakatos's canonical example of a progressive auxiliary hypothesis — the discovery of Neptune from Newtonian predictions. The adjustment was progressive rather than ad hoc because it did not merely accommodate the known anomaly; it generated a new, independently testable prediction (the planet exists at position X) that was then confirmed. This expanded the program's empirical content. An ad hoc adjustment would have explained the anomaly without predicting anything new — for instance, postulating an undetectable medium that only affected that orbit."

- question: "Ptolemaic astronomers repeatedly modified the system of epicycles to accommodate newly observed planetary positions. No modification ever predicted a previously unknown astronomical phenomenon. According to Lakatos, this pattern shows the Ptolemaic program is:"
  type: multiple-choice
  options:
    - "Progressive — it successfully explains each new astronomical observation by adding the appropriate epicycles"
    - "Degenerating — it only accommodates known observations without generating novel predictions, exhibiting ad hoc adjustment"
    - "In a phase of normal science — adjusting auxiliary hypotheses within an established framework is always rational"
    - "Falsified — Lakatos holds that research programs should be abandoned as soon as anomalies appear"
  answer: 1
  explanation: "Accommodating known observations is not enough for Lakatos; a progressive program must predict genuinely new phenomena. The Ptolemaic program could always be patched to fit any orbit by adding epicycles, but the patches never revealed anything unexpected. This is the mark of a degenerating program: its theoretical content grows only retrospectively, absorbing what we already know rather than pushing into new empirical territory. Lakatos explicitly contrasts this with the progressive Newtonian program that predicted Neptune — the Ptolemaic system never had a comparable predictive triumph."

- question: "According to Lakatos, scientists who continue working within a research program that faces persistent anomalies are acting irrationally, since anomalies constitute refutations of the program."
  type: true-false
  answer: false
  explanation: "This is Popper's view, not Lakatos's. One of Lakatos's central arguments against naive falsificationism is precisely that continuing with an anomaly-ridden program can be perfectly rational — if the program remains progressive (still generating confirmed novel predictions). Anomalies are part of the normal life of any research program and do not constitute decisive refutations. Scientists switch programs rationally only when the current program has become genuinely degenerating AND a better progressive alternative is available. Demanding immediate abandonment at the first anomaly would have killed Newtonian mechanics in its infancy."

- question: "For Lakatos, the hard core of a research program is deliberately protected from refutation by directing all empirical tests toward the auxiliary hypotheses in the protective belt."
  type: true-false
  answer: true
  explanation: "This is Lakatos's key structural claim. The hard core consists of the fundamental theoretical commitments that scientists treat as non-negotiable — Newton's laws, Darwin's selection principles, etc. By methodological decision (not necessity), scientists protect the hard core: when a prediction fails, they look for ways to adjust the auxiliary hypotheses (initial conditions, measurement assumptions, background theories) before questioning the core. This deliberate protective strategy is what makes research programs differ from isolated theories, and it explains why Popperian falsification of individual theories misses how science actually works."

- question: "What is the difference between a 'progressive' and a 'degenerating' research program in Lakatos's framework, and why does this distinction matter for scientific rationality?"
  type: short-answer
  answer: "A progressive research program generates new theories with genuinely novel predictive content — it makes successful predictions about phenomena that were not used to construct those theories, expanding its empirical scope. A degenerating program only accommodates already-known observations through ad hoc adjustments that generate no new testable predictions. The distinction matters for scientific rationality because it gives a criterion for rational theory choice that Popper's falsificationism lacked (single anomalies don't refute) while avoiding Kuhn's sociological relativism (paradigm shifts are not purely gestalt switches). Scientists can rationally continue with a currently anomalous program that remains progressive, and rationally switch to a better program when the old one has become degenerating."
  explanation: "The key is that 'progressive' is defined prospectively — a prediction made before the confirming observation — not retrospectively. Any program can accommodate past data; the question is whether it leads you to discover new things. This is why the Neptune case is paradigmatic for Lakatos: the planet was predicted, searched for, and found. A program that could only explain Neptune after it was already known would not count as progressive by this standard."
```

## Explainer

You enter this topic knowing two foundational views in philosophy of science. **Popper's falsificationism** holds that scientific theories are defined by their falsifiability — a good theory makes risky predictions that could be decisively refuted. When a prediction fails, the theory must be abandoned. This gives science its progressive, self-correcting character. **Kuhn's paradigm theory** (your hard prerequisite) complicates this picture: science doesn't actually operate by Popperian rules. Scientists defend paradigms against anomalies, engage in normal science without questioning core assumptions, and shift paradigms only in dramatic, gestalt-switch-like revolutions. Falsifying evidence, on Kuhn's historical account, rarely leads to immediate rejection of the core theory.

Lakatos aimed to preserve what was right in both views while avoiding their weaknesses. His central concept is the **scientific research program** — a structured sequence of theories united by a common **hard core** of fundamental assumptions that scientists agree to treat as non-negotiable. For Newtonian mechanics, the hard core includes Newton's three laws and the law of gravitation. For Darwinian biology, it includes the principles of variation, heredity, and selection. When an anomaly appears — an orbit that doesn't fit predictions — scientists don't abandon the hard core. Instead, they adjust the **protective belt**: the auxiliary hypotheses, initial conditions, and background assumptions that surround and protect the core. An anomalous orbit can be explained by positing an undetected planet, by revising measurement assumptions, or by complicating initial conditions.

This is where Lakatos adds normative bite that Kuhn lacks. Not all protective belt adjustments are equally rational. An adjustment is **ad hoc** if it merely patches over the anomaly without generating new testable predictions. But an adjustment is **progressive** if it leads to new theories that successfully predict novel facts. When the Newtonian program predicted Neptune's existence (and Neptune was subsequently found), the auxiliary hypothesis was progressive — it genuinely expanded the program's empirical content. When the Ptolemaic system kept adding epicycles to save the phenomena, the adjustments were increasingly ad hoc and the program was **degenerating** — it accommodated past observations but stopped making successful new predictions.

For Lakatos, the rational unit of scientific evaluation is not a single theory at a single moment (Popper's target) or an incommensurable paradigm (Kuhn's unit), but a **research program over time**. Scientists are rational to continue with a degenerating program for a while — perhaps new data will revive it, perhaps a young theorist will find a progressive variant. But there is a rational point at which switching to a better program is not a gestalt switch driven by sociology but a scientifically motivated decision. This is Lakatos's attempt to restore methodological rationality to science while accommodating Kuhn's historical realism. The key question his critics press: does the progressive/degenerating distinction give real normative guidance, or can every program look progressive in retrospect?
