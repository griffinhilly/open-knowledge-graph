---
id: underdetermination-of-theory-by-evidence
title: Underdetermination of Theory by Evidence
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: duhem-quine-thesis
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: underdetermination-duhem-quine
  type: soft
builds-toward:
- scientific-realism
- theoretical-virtues-in-theory-choice
tags:
- underdetermination
- empiricism
- realism
stage: expert
status: validated
---
# Underdetermination of Theory by Evidence

## Core Idea
Since empirical evidence underdetermines theory, the choice between empirically equivalent but incompatible theories cannot be made on purely empirical grounds. Scientists must appeal to pragmatic criteria like simplicity and fruitfulness, or potentially embrace relativism about which theory is true.

## Questions

```yaml
- question: "Two theories make identical predictions for every possible experiment — past, present, and future. A scientist argues that Theory A is preferable because it is mathematically simpler. What does the underdetermination thesis imply about this argument?"
  type: multiple-choice
  options:
    - "The argument is invalid — if the theories make identical predictions, they are the same theory expressed differently"
    - "The argument succeeds: simplicity is an empirical virtue, and simpler theories are better confirmed by the evidence"
    - "The argument invokes a non-empirical criterion; underdetermination shows that evidence alone cannot settle the choice, so simplicity is doing epistemological work the evidence cannot do"
    - "The argument fails because empirically equivalent theories are always both false"
  answer: 2
  explanation: "When theories are empirically equivalent, the choice between them genuinely cannot be made on purely empirical grounds — that is the core claim of underdetermination. The scientist's appeal to simplicity is an appeal to a theoretical virtue, not more evidence. The deeper debate — which the thesis opens up — is whether simplicity is truth-tracking (as realists argue) or merely a pragmatic preference (as empiricists argue). Underdetermination does not show the choice is arbitrary; it shows that making the choice requires going beyond the evidence."

- question: "What are empirically equivalent theories?"
  type: multiple-choice
  options:
    - "Theories that use the same mathematical formalism but different physical interpretations"
    - "Theories that have been confirmed by the same set of past experiments"
    - "Theories that make identical observational predictions for every possible experiment yet describe metaphysically different realities"
    - "Theories from different scientific fields that describe the same phenomenon at different levels of analysis"
  answer: 2
  explanation: "Empirically equivalent theories are ones that agree on every observational prediction — not just the experiments done so far, but all possible future observations — yet disagree about the underlying nature of reality. Newton's mechanics with absolute space versus without a preferred rest frame is the classic case: no mechanical experiment can distinguish them, yet they describe different objective realities. This is more radical than merely being confirmed by the same data — it means no future data could discriminate between them either."

- question: "Underdetermination implies that any scientific theory is just as well-supported as any competing alternative theory."
  type: true-false
  answer: false
  explanation: "This is a common overstatement of the thesis. Underdetermination applies specifically to cases where theories are empirically equivalent — making identical predictions for all possible observations. Most competing theories are NOT empirically equivalent; they make different predictions that can in principle be tested. The thesis shows that in the specific (and philosophically significant) cases of empirical equivalence, evidence alone cannot decide — not that all theories are equally supported by evidence in general."

- question: "The scientific realist and the empiricist differ over whether theoretical virtues like simplicity and fruitfulness are evidence of a theory's truth or merely reflect pragmatic cognitive preferences."
  type: true-false
  answer: true
  explanation: "This is precisely the fault line the underdetermination thesis exposes. The realist argues: if simplicity is a reliable guide in science, it must be because simpler theories tend to be truer — the virtue is truth-tracking. The empiricist (or instrumentalist) counters: we prefer simple theories because they are easier to use and compute with, not because reality is itself simple; theoretical virtues select for useful tools, not true descriptions of unobservables. Underdetermination makes this dispute concrete and unavoidable."

- question: "Why does the problem of underdetermination pose a fundamental challenge to scientific realism?"
  type: short-answer
  answer: "Scientific realism holds that our best theories describe how reality actually is — including unobservable entities and processes. Underdetermination challenges this by showing that for any set of observations, multiple incompatible theories can account for them equally well. If the total evidence cannot uniquely determine which theory is true, the realist cannot claim that the theory we currently accept is the uniquely correct description of unobservable reality — it is just one of many empirically equivalent alternatives. This opens the door to instrumentalism: perhaps theories are just predictive tools, not true descriptions."
  explanation: "The threat is not to science's predictive success but to its metaphysical ambitions. A theory can be empirically adequate (save all the phenomena) without being uniquely true. Underdetermination makes it difficult to argue that theoretical virtues like simplicity are reliable guides to truth rather than convenience — and scientific realism needs those virtues to do epistemological work, because the evidence alone isn't enough."
```

## Explainer

Your prerequisite — the Duhem-Quine thesis — showed that individual hypotheses cannot be tested in isolation: whenever an experiment goes against expectations, we can always pin the failure on some auxiliary assumption rather than the central hypothesis. Underdetermination takes this a step further, from the local level (any single test is inconclusive) to a global level (the total body of evidence cannot uniquely determine which theory is true).

The core logical point is simple: for any finite set of observations, there are in principle infinitely many theories consistent with those observations. Geometry provides the classic illustration. Pre-Einsteinian physicists assumed Euclidean geometry and built mechanics accordingly. When astronomical anomalies appeared — like the perihelion precession of Mercury — they could have modified the mechanics (as Einstein eventually did), or they could have modified the geometry, or they could have modified some auxiliary assumption about how light travels. All three adjustments could be made consistent with the same observations. These are **empirically equivalent theories**: they make identical predictions for every possible observation yet describe metaphysically different worlds.

The most discussed historical case is Newtonian absolute space. Newton's mechanics with a preferred rest frame (absolute space) is empirically equivalent to Newton's mechanics with any uniformly moving frame — no mechanical experiment can distinguish them, because uniform boosts don't affect any measurable quantity. The two theories describe different objective realities (one posits absolute rest, the other doesn't), yet no observation can adjudicate between them. What should we do? Einstein resolved this by reformulating the theory so that the underdetermined choice (which frame is "really" at rest) vanishes entirely.

When theories are empirically equivalent, scientists inevitably appeal to **theoretical virtues**: simplicity, fruitfulness, internal coherence, breadth of scope, consistency with background knowledge. The underdetermination thesis raises the question of whether these virtues are *truth-tracking* or merely pragmatic. The **scientific realist** argues they are evidence: if one theory is simpler and more fruitful, that's reason to believe it's closer to the truth, not just more convenient for us. The **empiricist** or **instrumentalist** counters: theoretical virtues reflect our cognitive preferences, not the world's structure; they select for good tools, not true descriptions of unobservables. Underdetermination is thus a central pressure point in the realism debate — it's not merely a curiosity about theory choice but a fundamental challenge to the idea that science converges on a unique, true description of unobservable reality.
