---
id: two-sided-matching-deferred-acceptance
title: Two-Sided Matching and the Deferred Acceptance Algorithm
domain: economics
course: advanced-microeconomics
prerequisites:
- id: pareto-efficiency-and-optimality
  type: soft
- id: core-of-an-economy
  type: soft
- id: mechanism-design-basics
  type: soft
- id: incentive-compatibility
  type: soft
builds-toward: []
tags:
- market design
- matching
- stable matching
- deferred acceptance
- Gale-Shapley
- strategy-proofness
stage: advanced
status: validated
---

# Two-Sided Matching and the Deferred Acceptance Algorithm

## Core Idea
In two-sided matching markets, such as doctors and hospitals or students and schools, participants on each side have preferences over the other side and prices do not clear the market. A matching is stable if no pair of agents would both rather be matched to each other than to their assigned partners. David Gale and Lloyd Shapley showed in 1962 that a stable matching always exists in the basic model and that their deferred acceptance algorithm finds one. The matching it produces is the best stable matching for every member of the proposing side, and truthful reporting is a dominant strategy for that side.

## How It's Best Learned
Give students a three-by-three set of preference lists and have them run deferred acceptance by hand, round by round, recording tentative holds and rejections. Then have them check every possible blocking pair in the result and in an alternative matching. Finally, swap which side proposes and compare the outcomes, which shows that the choice of proposing side matters.

## Common Misconceptions
- A stable matching gives everyone their first choice. (Stability only rules out pairs who would both rather be together; many agents may get lower-ranked partners.)
- In deferred acceptance, a receiver who accepts an offer is bound to it. (Acceptances are tentative; a receiver keeps the best offer so far and drops it if a preferred proposer arrives later, which is why the algorithm is called deferred acceptance.)
- Deferred acceptance makes truthful reporting a dominant strategy for everyone. (It is strategy-proof for the proposing side only; no stable mechanism is strategy-proof for both sides in general.)

## Questions

```yaml
- question: "Proposers P1, P2, P3 and receivers R1, R2, R3 have these rankings. P1: R1, R2, R3. P2: R1, R3, R2. P3: R2, R1, R3. R1: P2, P1, P3. R2: P1, P3, P2. R3: P1, P2, P3. What matching does proposer-side deferred acceptance produce?"
  type: multiple-choice
  options: ["P1-R1, P2-R3, P3-R2", "P1-R2, P2-R1, P3-R3", "P1-R3, P2-R1, P3-R2", "P1-R2, P2-R3, P3-R1"]
  answer: 1
  explanation: "Round 1: P1 and P2 propose to R1, P3 to R2. R1 holds P2 and rejects P1; R2 holds P3. Round 2: P1 proposes to R2, which prefers P1 to P3, so it holds P1 and rejects P3. Round 3: P3 proposes to R1, which keeps P2 and rejects P3. Round 4: P3 proposes to R3, which holds P3. No one is rejected, so the result is P1-R2, P2-R1, P3-R3."
- question: "A matching is unstable if there is a proposer and a receiver who each prefer the other to their current partner."
  type: true-false
  answer: true
  explanation: "Such a pair is called a blocking pair. They would both gain by leaving their assigned partners and matching with each other, so the assignment would unravel."
- question: "Compared with every other stable matching, the proposer-proposing deferred acceptance outcome is:"
  type: multiple-choice
  options: ["Best for every receiver", "Best for every proposer and worst for every receiver among stable matchings", "The only stable matching", "Best for exactly half of each side"]
  answer: 1
  explanation: "Gale and Shapley showed the proposing side gets its best stable partner. A later result shows that, among stable matchings, the same outcome is the least preferred for each receiver."
- question: "Why have school districts and the U.S. medical residency match adopted deferred acceptance or close variants?"
  type: short-answer
  answer: "It produces stable assignments, so participants have no incentive to go around the system and make side deals, and it lets the proposing side, typically students or applicants, report their true preferences without fear of being penalized for ranking a popular option first."
  explanation: "Earlier mechanisms, such as ones that gave priority to first-choice rankings, rewarded strategic ranking and left matches unstable. Alvin Roth's work in market design helped bring deferred acceptance into practice."
```

## Explainer
Many markets match people rather than sell goods at a price. Medical graduates are matched to hospital residencies, students to public schools, and workers to some jobs. Each side has preferences over the other, and a match requires both. The design question is how to turn preference lists into an assignment that participants will accept.

The key requirement is **stability**. A matching is stable if there is no **blocking pair**: no proposer and receiver who both prefer each other to the partners they were assigned. If a blocking pair exists, its members have reason to break away and make a private deal, and the assignment can unravel.

David Gale and Lloyd Shapley, in their 1962 article "College Admissions and the Stability of Marriage," proved that a stable matching always exists in the basic model and gave a procedure that finds one, now called **deferred acceptance**. It runs in rounds. Each unmatched proposer applies to the most preferred receiver who has not yet rejected them. Each receiver looks at everyone who has applied, including the one held from the last round, keeps the best acceptable applicant, and rejects the rest. Rejected proposers move down their lists. The process ends when no one is rejected, and the tentative holds become final.

Why is the result stable? Suppose proposer P prefers receiver R to P's final partner. Then P applied to R earlier and was rejected, which happens only if R was holding someone R liked better. R's final partner is at least as good as that applicant, so R does not want P. No blocking pair can exist.

The algorithm has two further properties. The result is **proposer-optimal**: every proposer gets the best partner they could have in any stable matching, and every receiver gets the worst. And it is **strategy-proof for proposers**, as later shown by Lester Dubins and David Freedman and by Alvin Roth: no proposer can gain by misreporting preferences. Roth also showed that no stable mechanism is strategy-proof for both sides.

These ideas moved into practice. The National Resident Matching Program uses an applicant-proposing variant, and several large school districts, including New York City, adopted deferred acceptance for school choice. Roth and Shapley shared the 2012 Nobel Memorial Prize in Economic Sciences for the theory of stable allocations and the practice of market design.
