---
id: hardness-of-approximation
title: Hardness of Approximation
domain: computer-science
course: theory-of-computation
prerequisites:
- id: approximation-algorithms-design
  type: hard
- id: np-completeness
  type: hard
tags:
- hardness
- inapproximability
- lower-bounds
stage: advanced
status: validated
---

# Hardness of Approximation

## Core Idea
Hardness of approximation studies which optimization problems resist good approximations unless P=NP. Using the PCP (probabilistically checkable proofs) theorem, one proves problems cannot be approximated better than specific thresholds: vertex cover cannot be approximated better than 1.36, max clique not better than n^ε for any ε > 0. This shows approximation hardness is orthogonal to decision hardness—some NP-hard problems have arbitrary approximations, others have tight inapproximability barriers.

## Questions

```yaml
- question: "The Knapsack problem is NP-hard, but it has a fully polynomial-time approximation scheme (FPTAS). Maximum Clique is also NP-hard. What does hardness of approximation theory tell us about Maximum Clique?"
  type: multiple-choice
  options:
    - "Maximum Clique must also have an FPTAS since both problems are NP-hard"
    - "Maximum Clique cannot be approximated within a factor of n^(1-ε) for any ε > 0, unless P = NP — making it essentially inapproximable"
    - "Maximum Clique has a constant-factor approximation, similar to Vertex Cover's 2-approximation"
    - "Maximum Clique is easier to approximate than Knapsack because cliques are simpler structures"
  answer: 1
  explanation: "This is the central lesson of hardness of approximation: NP-hardness of the decision problem tells you almost nothing about approximability of the optimization version. Knapsack has an FPTAS — you can get within (1+ε) of optimal for any ε. Maximum Clique is at the opposite extreme: no polynomial-time algorithm can find a clique within a factor n^(1-ε) of the largest, for any ε > 0, unless P = NP. Two problems can be equally hard to solve exactly but live in completely different approximability classes. This is why the classification into tiers (FPTAS, constant-factor, logarithmic, inapproximable) is so important."

- question: "The PCP theorem enables inapproximability proofs by showing that certain gap problems are NP-hard. What is a 'gap problem' in this context?"
  type: multiple-choice
  options:
    - "A problem where the optimal solution has a gap between its upper and lower bounds"
    - "Distinguishing between instances where the optimum is above one threshold versus below another threshold"
    - "A problem that is easy in the average case but hard in the worst case"
    - "A problem where approximation algorithms leave a gap between the achieved ratio and the optimal ratio"
  answer: 1
  explanation: "A gap problem asks: given an instance, is the optimum ≥ α (the 'yes' case) or ≤ β (the 'no' case), where α > β? If this distinction is NP-hard, then no polynomial-time algorithm can achieve an approximation ratio better than α/β (otherwise it could solve the gap problem). The PCP theorem transforms NP membership proofs into a form where a random subset of bits can certify correctness, enabling reductions that create these gaps. The magic is that these gap reductions come from the structure of probabilistically checkable proofs, not from ad hoc constructions."

- question: "All NP-hard optimization problems are equally difficult to approximate — if one has no constant-factor approximation, none of them do."
  type: true-false
  answer: false
  explanation: "This is the key misconception that hardness of approximation corrects. NP-hard problems span a wide spectrum of approximability. Some have FPTAS (Knapsack), some have constant-factor approximations (Vertex Cover: 2, TSP with triangle inequality: 1.5), some have only logarithmic approximations (Set Cover: O(log n)), and some are essentially inapproximable (Maximum Clique). The NP-hardness of the decision problem and the approximability of the optimization problem are largely orthogonal questions — the latter requires its own theory."

- question: "If a polynomial-time algorithm cannot solve an NP-hard decision problem exactly, it cannot achieve any useful approximation guarantee for the corresponding optimization problem either."
  type: true-false
  answer: false
  explanation: "Many NP-hard optimization problems admit excellent polynomial-time approximations despite having intractable exact decision versions. The Knapsack problem has an FPTAS producing solutions within (1+ε) of optimal for any ε. Christofides' algorithm gives a 1.5-approximation for metric TSP. These algorithms are polynomial-time and achieve strong guarantees — they just don't find the exact optimum. The inability to solve the decision version exactly says nothing about how close a polynomial algorithm can get to the optimum value."

- question: "Why is the classification of NP-hard problems into approximability tiers (FPTAS, constant-factor, logarithmic, inapproximable) more practically useful than simply knowing a problem is NP-hard?"
  type: short-answer
  answer: "NP-hardness only tells you that exact polynomial-time solution is unlikely. Approximability tiers tell you what quality of solution is achievable efficiently, which directly determines algorithm design strategy. If a problem has an FPTAS, you can get arbitrarily close to optimal — near-exact solutions are practical. A constant-factor approximation means you can guarantee quality within a fixed multiple of optimal. An inapproximability result tells you no polynomial algorithm will ever give a meaningful guarantee — you should use heuristics, restrict to special cases, or reformulate the problem. This prevents wasted effort chasing approximation guarantees that provably cannot exist."
  explanation: "The tiers matter because they set realistic expectations. A practitioner facing an NP-hard problem must decide: should I invest in approximation algorithm research, or switch to heuristics? If the problem is in the 'inapproximable' tier (like Max Clique), investing in approximation theory is futile — provably no good approximation can exist. If it has a PTAS, investing in tightening the approximation ratio is worthwhile. The classification guides resource allocation and sets the ceiling for what algorithms can achieve."
```

## Explainer

From your study of approximation algorithms, you know that when an NP-hard optimization problem can't be solved exactly in polynomial time, the next best thing is an efficient algorithm that gets *close* to optimal — say, within a factor of 2 or 1.5 of the best possible answer. And from NP-completeness, you know that certain problems are computationally intractable unless P = NP. Hardness of approximation asks the natural follow-up: for a given NP-hard problem, *how close* can a polynomial-time algorithm get? The answer, surprisingly, is that many problems have provable limits on how well they can be approximated.

The landscape of approximability is strikingly varied. Some NP-hard problems are easy to approximate: the **traveling salesman problem** with triangle inequality has a 1.5-approximation (Christofides' algorithm), meaning you can always find a tour within 50% of optimal. The **knapsack problem** has a fully polynomial-time approximation scheme (FPTAS) — you can get within any desired factor (1 + ε) of optimal. But other problems resist approximation stubbornly. **Maximum Clique** is so hard to approximate that no polynomial-time algorithm can find a clique within a factor of n^(1-ε) of the largest one, for any ε > 0, unless P = NP. That means even finding a clique that is, say, the square root of the optimal size is intractable. The decision version ("is there a clique of size k?") and the optimization version live in completely different approximability classes.

The key tool for proving these limits is the **PCP theorem** (Probabilistically Checkable Proofs). In its simplest form, the PCP theorem says that every NP proof can be reformulated so that a verifier needs to read only a constant number of randomly chosen bits to be convinced of its correctness, with high probability. This seemingly abstract statement has a stunning consequence: it transforms gap problems — distinguishing between instances where the optimal value is above one threshold versus below another — into NP-hard problems. If you can show that distinguishing "optimum ≥ k" from "optimum ≤ αk" is NP-hard, then no polynomial-time algorithm can achieve an approximation ratio better than α, unless P = NP. This is how inapproximability results for Max-3SAT, Vertex Cover, Set Cover, and many others are established.

The practical takeaway is a classification of NP-hard problems into tiers: those with constant-factor approximations, those with logarithmic-factor approximations, those with PTAS/FPTAS (arbitrarily good approximations), and those that are essentially inapproximable. Knowing which tier your problem falls into tells you what to expect from any algorithm and prevents wasted effort chasing an approximation guarantee that provably cannot exist. This classification is one of the most important contributions of computational complexity theory to practical algorithm design.
