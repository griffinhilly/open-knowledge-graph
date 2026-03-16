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
status: draft
---

# Inclusive Fitness

## Core Idea
Inclusive fitness is an individual's total genetic contribution to the next generation through both direct reproduction and help given to relatives. An organism can increase its inclusive fitness by raising its own offspring, helping siblings, or supporting other kin, weighted by relatedness coefficient (r).

## Explainer

From kin selection theory, you already know that natural selection can favor behaviors that benefit relatives because relatives share genes. **Inclusive fitness** takes this insight and turns it into a precise accounting system. Instead of measuring an organism's fitness only by counting its own offspring, inclusive fitness adds a second column to the ledger: the extra offspring that relatives produce *because of the organism's help*, each discounted by the coefficient of relatedness (r) between helper and recipient.

Think of it like a financial portfolio. **Direct fitness** is income you earn yourself — your own surviving offspring. **Indirect fitness** is income earned through investments in others — the additional offspring your relatives produce thanks to your assistance, weighted by how much genetic stock you share with them. A full sibling shares r = 0.5, so helping a sibling raise two extra offspring contributes 2 × 0.5 = 1.0 units of indirect fitness, equivalent to raising one offspring yourself. Inclusive fitness is the sum of both components.

This framework explains behaviors that look selfless from a classical fitness perspective. A worker bee that never reproduces but helps her mother queen raise thousands of sisters has zero direct fitness, yet her inclusive fitness can be enormous because she shares r = 0.75 with her sisters in a haplodiploid system. The key insight is that natural selection does not "care" whether genes reach the next generation through the organism's own body or through a relative's — what matters is the total number of copies of those genes that persist.

Crucially, inclusive fitness is measured from the *actor's* perspective. It counts only the fitness effects that the actor causes, not the total reproductive output of all its relatives. If your sibling would have raised five offspring anyway, and your help lets her raise seven, your indirect fitness contribution is (7 − 5) × r, not 7 × r. This distinction prevents double-counting and keeps the bookkeeping honest. Understanding this accounting principle is essential preparation for Hamilton's rule, which formalizes when helping behavior will be favored: when the indirect fitness gain (benefit × relatedness) exceeds the direct fitness cost to the helper.
