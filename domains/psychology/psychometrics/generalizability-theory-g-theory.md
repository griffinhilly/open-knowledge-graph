---
id: generalizability-theory-g-theory
title: Generalizability Theory and Multi-Faceted Reliability
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: anova-one-way-theory
  type: soft
- id: anova-one-way
  type: hard
builds-toward:
- computerized-adaptive-testing
tags:
- generalizability
- variance-components
- facets
stage: expert
status: validated
---

# Generalizability Theory and Multi-Faceted Reliability

## Core Idea
Generalizability theory extends classical reliability by examining how scores generalize across multiple measurement facets (items, raters, occasions, contexts). It decomposes variance into components from persons, each facet, and their interactions, providing nuanced reliability estimates for different testing conditions.

## How It's Best Learned
Design and conduct a simple G-study identifying facets and collecting data, then use results to conduct D-studies examining how test design decisions affect generalizability.

## Common Misconceptions
Generalizability theory replaces classical reliability entirely. Both frameworks are useful depending on context. Confusing G-coefficients with traditional reliability indices; g-coefficients address specific generalization questions.

## Questions

```yaml
- question: "A G-study examining essay scoring reveals the following variance components: 45% from persons, 10% from raters (main effect), 30% from the person×rater interaction, and 15% from items. Based on these results, which change to the test design would most improve the generalizability coefficient?"
  type: multiple-choice
  options:
    - "Adding more essay prompts, since item variance must be reduced to improve reliability"
    - "Increasing the number of raters, since rater-related variance (rater main effect + person×rater interaction) represents the largest source of error"
    - "Collecting scores on multiple occasions, since occasion variance is usually the biggest facet in performance assessments"
    - "Reducing the number of raters to one highly trained expert, eliminating the person×rater interaction entirely"
  answer: 1
  explanation: "The variance components tell you where error is coming from. Here, rater-related variance totals 40% (10% rater main effect + 30% person×rater interaction) — the dominant error source. Adding more raters averages across their idiosyncratic scoring tendencies, reducing this noise. A D-study would formalize this forecast by predicting the G-coefficient at different rater counts. Adding more items would help if item variance were the bottleneck, but the data show raters are. Using one 'expert' rater eliminates the person×rater variance from an ANOVA perspective only if that one rater scores all essays perfectly consistently."

- question: "How does a D-study (decision study) differ from a G-study (generalizability study)?"
  type: multiple-choice
  options:
    - "A D-study collects new data under the proposed design; a G-study applies those results to actual test decisions"
    - "A D-study uses the variance components estimated in the G-study to forecast how changing the number of conditions (raters, items, occasions) would affect the generalizability coefficient — without collecting new data"
    - "A D-study estimates variance due to person differences; a G-study estimates variance due to facets like raters and items"
    - "A D-study replaces CTT reliability calculations; a G-study supplements them"
  answer: 1
  explanation: "The G-study is the data-collection phase: participants are measured across multiple conditions of each facet, and the resulting data are analyzed to estimate how much variance each source (persons, raters, items, their interactions) contributes. The D-study then uses those variance component estimates to ask 'what-if' questions without collecting new data: if we used 4 raters instead of 2, how much would G improve? If we added 3 more items? This allows test designers to optimize the measurement design before committing to it, identifying the most cost-effective route to a target reliability level."

- question: "A G-coefficient computed for a two-rater, two-item performance test addresses a more precisely defined reliability question than Cronbach's alpha computed on the same data."
  type: true-false
  answer: true
  explanation: "Cronbach's alpha treats all non-person variance as undifferentiated error. A G-coefficient is specified for a particular universe of generalization — it answers 'how well do scores generalize across the specific facets included in this design?' If the design has two raters and two items, the G-coefficient tells you how reliably you can generalize to another pair of raters using another pair of items. A different G-study with different facets would yield a different G-coefficient. This specificity is both a strength (more actionable) and a limitation (not directly comparable across different designs)."

- question: "Generalizability theory renders classical test theory obsolete because it can answer all the questions CTT can, plus provide facet-specific variance information."
  type: true-false
  answer: false
  explanation: "G-theory and CTT are complementary, not competitive. CTT is simpler, requires less data, and is sufficient when the measurement involves a single dominant source of error (typically items). G-theory is indispensable when multiple facets are present — raters, occasions, testing sites — because only G-theory can identify which facet is the bottleneck and what redesigning the test around that bottleneck would yield. Choosing G-theory when CTT suffices adds unnecessary complexity; choosing CTT when multiple facets are present obscures the structure of error."

- question: "Why can't you improve a test's reliability simply by examining its overall Cronbach's alpha, and what additional information does G-theory provide?"
  type: short-answer
  answer: "Cronbach's alpha lumps all sources of error into one undifferentiated 'error variance' term, so you know reliability is low but not why. G-theory decomposes error into named facets (raters, items, occasions) and their interactions, revealing which specific source is the bottleneck. This allows targeted interventions — add more raters if rater variance dominates, add more items if item variance dominates — rather than guessing."
  explanation: "Imagine alpha = 0.68. Is the problem inconsistent items? Inconsistent raters? Performance that varies across occasions? Alpha cannot tell you. A G-study might reveal that person×rater interaction accounts for 35% of variance and items only 4%. Adding items would barely move reliability; adding raters would substantially improve it. The D-study then calculates exactly how many raters produce a target G of 0.85. Without G-theory, you can only observe that reliability is low; with it, you can diagnose why and prescribe a specific remedy."
```

## Explainer

Classical test theory (CTT) gives you one number for reliability: the ratio of true-score variance to observed-score variance. That number is powerful but opaque. It tells you how reproducible scores are, but not *why* they vary or *across what circumstances* they generalize. When a teacher rates students' essays, scores vary because students differ in writing ability — but they also vary because raters use the rubric differently, because some essay prompts are harder than others, and because all of these factors interact. CTT lumps all of this into a single "error" bucket. **Generalizability theory** (G-theory) opens that bucket.

The core move of G-theory is to treat the measurement situation as a **design** in the ANOVA sense, which you know from your work with one-way ANOVA. Just as ANOVA partitions total variance into between-groups variance and within-groups variance, G-theory partitions total score variance into components attributable to persons (the object of measurement), each **facet** of the measurement design, and their interactions. A facet is any systematic source of variation in the measurement conditions — raters, items, occasions, testing sites, and so on. Running a **G-study** (generalizability study) means collecting data across multiple conditions of each facet and estimating the variance each source contributes.

Suppose you run a G-study where 50 students each write two essays, and two raters score all essays. Your ANOVA-like decomposition might show: 40% of variance is attributable to persons (good — this is the signal), 15% to items (one prompt is harder than the other), 10% to raters (one rater scores more harshly), 20% to the person × item interaction (some students are relatively better on one prompt type), and 15% to the person × rater interaction (raters rank students inconsistently). Now you can ask targeted questions: which facet contributes most to measurement noise? How much can you reduce error by adding more raters vs. more items?

That targeted question is answered by the **D-study** (decision study). A D-study uses the variance components from the G-study to forecast how reliability — expressed as a **generalizability coefficient**, G — would change under different testing conditions. If you doubled the number of raters from 2 to 4, how much would G improve? If you added 3 more essay prompts? The D-study lets you optimize test design before actually running the test. The generalizability coefficient is analogous to Cronbach's alpha, but it is specific to the facets and number of conditions you are generalizing across — which is why G-coefficients answer specific generalization questions rather than providing a single context-free reliability number.

The practical takeaway is that CTT and G-theory are complementary tools. CTT is simpler and sufficient when you only care about overall score reproducibility and have a single source of error (items). G-theory becomes indispensable when your measurement involves multiple facets — any time raters, occasions, or varying contexts are part of the design — because only G-theory can tell you which facet is the bottleneck limiting reliability, and what redesigning the test around that bottleneck would cost or save.
