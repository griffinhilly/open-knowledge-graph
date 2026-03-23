---
id: inclusive-fitness
title: Inclusive Fitness
domain: biology
course: evolutionary-biology
prerequisites:
- id: kin-selection-theory
  type: hard
builds-toward:
- hamilton-rule
- altruism-evolution
tags:
- fitness
- selection
- sociobiology
stage: advanced
status: validated
---

# Inclusive Fitness

## Core Idea
Inclusive fitness is an individual's total genetic contribution to the next generation through both direct reproduction and help given to relatives. An organism can increase its inclusive fitness by raising its own offspring, helping siblings, or supporting other kin, weighted by relatedness coefficient (r).

## Questions

```yaml
- question: "An organism produces 2 offspring of its own, and its help allows a full sibling (r = 0.5) to raise 3 additional offspring beyond what the sibling would have raised anyway. What is the organism's inclusive fitness?"
  type: multiple-choice
  options:
    - "1.5 — only the indirect component counts (3 × 0.5)"
    - "2 — only direct reproduction counts toward fitness"
    - "3.5 — direct fitness (2) plus indirect fitness (3 × 0.5 = 1.5)"
    - "5.5 — direct fitness (2) plus the sibling's total output (3 + 5 baseline) × 0.5"
  answer: 2
  explanation: "Inclusive fitness = direct fitness + indirect fitness. Direct fitness is 2 (own offspring). Indirect fitness is the *additional* offspring caused by the helper's assistance, discounted by relatedness: 3 × 0.5 = 1.5. Total = 3.5. Option D is the classic error — including the sibling's baseline reproduction (offspring she would have raised anyway) inflates indirect fitness by counting genes the actor had no causal role in propagating."

- question: "A worker bee in a haplodiploid colony (sisters share r = 0.75) produces no offspring but helps her mother raise hundreds of sisters. Which statement best describes her fitness?"
  type: multiple-choice
  options:
    - "Her fitness is zero because she has no direct reproductive output — she contributes nothing to the next generation"
    - "Her inclusive fitness can be very high, because indirect fitness through highly related sisters contributes to gene propagation"
    - "Her classical Darwinian fitness equals her inclusive fitness because both capture the same thing"
    - "Her fitness depends only on how many offspring her mother produces, regardless of her own contribution"
  answer: 1
  explanation: "Classical Darwinian fitness counts only direct offspring — which gives the worker zero. But inclusive fitness adds the indirect component: the sisters she helps raise, each sharing r = 0.75 of her genes. Helping raise 100 extra sisters contributes 100 × 0.75 = 75 units of indirect fitness. Natural selection can strongly favor the worker phenotype even with zero direct reproduction. This is why inclusive fitness — not classical fitness — is needed to explain eusociality."

- question: "A gene that causes an organism to sacrifice its own reproductive success could still spread by natural selection if it sufficiently boosts the reproduction of relatives carrying that gene."
  type: true-false
  answer: true
  explanation: "This is Hamilton's foundational insight formalized in inclusive fitness theory. Natural selection tracks gene frequencies, not individual survival. If an allele that causes costly helping behavior propagates enough copies of itself through relatives to offset the direct cost, it will increase in frequency. The 'altruistic' gene can spread even while the individual expressing it reproduces less — as long as relatives carrying the same gene reproduce more."

- question: "Inclusive fitness measures the total reproductive output of an organism and all its relatives combined."
  type: true-false
  answer: false
  explanation: "This is a common misreading. Inclusive fitness is measured strictly from the *actor's* perspective and counts only the additional reproduction in relatives that the actor caused, weighted by relatedness. If a sibling would have raised 5 offspring anyway but raises 7 with your help, your indirect fitness contribution is (7 − 5) × r = 2r, not 7r. Counting baseline reproduction the actor had no role in producing creates double-counting and breaks the accounting logic."

- question: "Why is it important to count only the *additional* offspring that an organism's help causes (rather than all of a relative's offspring) when calculating indirect fitness?"
  type: short-answer
  answer: "Because inclusive fitness is a causal measure of the actor's contribution to gene propagation. A relative's baseline offspring would exist regardless of the actor's behavior, so counting them attributes fitness gains to the wrong source. Only the increment caused by the actor's assistance represents genes entering the next generation *because of* that actor. Counting total offspring would inflate indirect fitness, making every organism appear to have massive fitness through relatives it had nothing to do with."
  explanation: "The counterfactual baseline ('what would the relative have produced without my help?') is essential to keeping the accounting honest. Inclusive fitness theory is designed to explain *why* helping behavior evolved — which means tracking what the helping behavior actually causes. This precision is also what makes Hamilton's rule mathematically coherent: rB > C compares the causal benefit to the causal cost, not inflated totals."
```

## Explainer

From kin selection theory, you already know that natural selection can favor behaviors that benefit relatives because relatives share genes. **Inclusive fitness** takes this insight and turns it into a precise accounting system. Instead of measuring an organism's fitness only by counting its own offspring, inclusive fitness adds a second column to the ledger: the extra offspring that relatives produce *because of the organism's help*, each discounted by the coefficient of relatedness (r) between helper and recipient.

Think of it like a financial portfolio. **Direct fitness** is income you earn yourself — your own surviving offspring. **Indirect fitness** is income earned through investments in others — the additional offspring your relatives produce thanks to your assistance, weighted by how much genetic stock you share with them. A full sibling shares r = 0.5, so helping a sibling raise two extra offspring contributes 2 × 0.5 = 1.0 units of indirect fitness, equivalent to raising one offspring yourself. Inclusive fitness is the sum of both components.

This framework explains behaviors that look selfless from a classical fitness perspective. A worker bee that never reproduces but helps her mother queen raise thousands of sisters has zero direct fitness, yet her inclusive fitness can be enormous because she shares r = 0.75 with her sisters in a haplodiploid system. The key insight is that natural selection does not "care" whether genes reach the next generation through the organism's own body or through a relative's — what matters is the total number of copies of those genes that persist.

Crucially, inclusive fitness is measured from the *actor's* perspective. It counts only the fitness effects that the actor causes, not the total reproductive output of all its relatives. If your sibling would have raised five offspring anyway, and your help lets her raise seven, your indirect fitness contribution is (7 − 5) × r, not 7 × r. This distinction prevents double-counting and keeps the bookkeeping honest. Understanding this accounting principle is essential preparation for Hamilton's rule, which formalizes when helping behavior will be favored: when the indirect fitness gain (benefit × relatedness) exceeds the direct fitness cost to the helper.
