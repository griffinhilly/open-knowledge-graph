---
id: counterfactual-causation
title: Counterfactual Theory of Causation
domain: philosophy
course: metaphysics
prerequisites:
- id: causation-and-causal-relations
  type: hard
- id: possible-worlds-semantics
  type: soft
- id: modal-logic-intro
  type: soft
- id: regularity-theory-of-causation
  type: soft
tags:
- counterfactuals
- David Lewis
- causation
- possible worlds
- dependence
stage: advanced
status: validated
---
# Counterfactual Theory of Causation

## Core Idea
Lewis's counterfactual theory analyzes causation in terms of counterfactual dependence: C causes E if, had C not occurred, E would not have occurred. This is evaluated using possible-worlds semantics — E counterfactually depends on C if in the closest possible worlds where C doesn't happen, E also doesn't happen. The theory handles many cases that defeat regularity theories. However, it faces serious problems with preemption (backup causes that would have produced E anyway), overdetermination (two independent sufficient causes), and late preemption, which Lewis and successors have worked to resolve through transitivity and influence accounts.

## How It's Best Learned
Read Lewis's 'Causation' (1973) and then immediately work through the preemption and overdetermination counterexamples. Track how each variant of the theory (his 1986 update, influence account) attempts to handle these cases.

## Common Misconceptions
- Counterfactual dependence and causation are not the same: E can counterfactually depend on C without C causing E (e.g., common cause cases).
- The theory doesn't require determinism — Lewis extended it to probabilistic causation.

## Explainer

You already understand **causation as a metaphysical relation** and the **regularity theory**, which analyzes causes as events that are regularly followed by their effects (Hume's constant conjunction). The counterfactual theory takes a different approach: instead of looking at patterns across many events, it analyzes what would have happened in a single case if things had gone differently. The core claim is that C causes E if and only if, had C not occurred, E would not have occurred — a condition of **counterfactual dependence**.

The possible-worlds framework you've studied makes this precise. To evaluate "Had C not occurred, E would not have occurred," you ask: consider the closest possible worlds where C doesn't happen — worlds that differ minimally from the actual world except that C is absent. Do those worlds also lack E? If yes, E counterfactually depends on C, and this dependence constitutes causation (or at least is evidence of it). The elegance of this approach is that it captures our ordinary causal intuitions: the spark caused the fire because, had there been no spark, there would have been no fire (in the nearest possible world where the spark is absent, everything else being equal, the fire also doesn't happen).

The theory handles cases that defeat regularity theories. **Regularity theories** struggle with singular causation — unique events that have never happened before and will never happen again can't appeal to patterns. They also struggle with overdetermination and preemption. The counterfactual theory initially seems better placed. But it generates its own notorious counterexamples. In **preemption**, C1 and C2 are both headed toward causing E, but C1 gets there first and C2 never fires. E depends counterfactually on C1 (if C1 hadn't happened, C2 would have fired and E would still have occurred) — so the dependence fails, even though we want to say C1 caused E. Lewis's response involved **chains of counterfactual dependence** and eventually the **influence account** (1986), which requires that E's fine-grained properties counterfactually depend on C's fine-grained properties, not merely whether E occurs.

**Overdetermination** is even trickier: two fires independently and simultaneously reach a barn, each sufficient to burn it. Neither fire is a counterfactual cause by Lewis's original analysis because removing either still leaves the other to do the work. This reveals a general tension: the counterfactual analysis works best for simple, isolated cases and strains under complex causal structure. Contemporary causation theory has branched into **interventionist accounts** (Woodward), **mechanistic accounts**, and sophisticated variants of the counterfactual approach — but Lewis's original theory remains the indispensable starting point, and the preemption/overdetermination problems it generated have shaped the entire subsequent discussion.

## Questions

```yaml
- question: "Event C caused event E on Lewis's original counterfactual analysis. What does this mean?"
  type: multiple-choice
  options:
    - "C and E are regularly conjoined across similar situations"
    - "In the closest possible world where C does not occur, E also does not occur"
    - "There exists some possible world where C occurs and E does not occur"
    - "C is a necessary condition for E in all possible worlds"
  answer: 1
  explanation: "Lewis's analysis requires counterfactual dependence in the *closest* possible worlds — those that differ from actuality only minimally in the absence of C. Option C is too weak (just any possible world); option D is too strong (necessity across all worlds); option A describes the regularity theory, not Lewis's account. The key move is using proximity among possible worlds (similarity to actuality) to evaluate what *would* have happened."

- question: "Why does the case of early preemption pose a problem for Lewis's original counterfactual theory?"
  type: short-answer
  answer: "In early preemption, two potential causes C1 and C2 are both headed toward E, but C1 fires first and produces E before C2 can act. The problem: in the closest possible world where C1 is absent, C2 would have taken over and produced E anyway. So E does *not* counterfactually depend on C1 — remove C1 and E still occurs (via C2). But intuitively, C1 caused E. The theory thus fails to identify the actual cause in such cases, returning a false negative."
  explanation: "Lewis attempted to handle this through chains of counterfactual dependence and later through his 'influence' account. The deeper lesson is that counterfactual dependence (if C hadn't happened, E wouldn't have happened) is neither necessary nor sufficient for causation in complex cases — it is a good indicator in simple, isolated cases, but the metaphysics of causation is harder to capture in a single clean analysis."
```
