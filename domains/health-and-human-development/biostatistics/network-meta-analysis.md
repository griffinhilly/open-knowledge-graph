---
id: network-meta-analysis
title: Network Meta-Analysis
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: meta-analysis-biostatistics
  type: hard
- id: bayesian-biostatistics
  type: soft
builds-toward: []
tags:
- network-meta-analysis
- indirect-comparison
- consistency
- treatment-ranking
- mixed-treatment-comparison
stage: expert
status: validated
---

# Network Meta-Analysis

## Core Idea
Network meta-analysis (NMA) extends standard pairwise meta-analysis to simultaneously compare multiple treatments by combining direct evidence (from head-to-head trials) with indirect evidence (inferred through common comparators). If Treatment A has been compared to placebo and Treatment B has been compared to the same placebo, NMA estimates the A-vs-B difference indirectly through the shared comparator — even without a direct A-vs-B trial. The network of all available comparisons is modeled simultaneously, producing a coherent set of relative treatment effects and enabling ranking of all treatments. The critical assumption is **consistency** (also called coherence): direct and indirect evidence for a given comparison agree. Inconsistency suggests that the treatment effects depend on which comparator was used, potentially indicating effect modification, heterogeneity across study populations, or violation of the transitivity assumption.

## Questions

```yaml
- question: "Five antidepressants have been studied: A vs. placebo (3 trials), B vs. placebo (2 trials), A vs. B (1 trial), C vs. A (1 trial), and D vs. B (1 trial). No trial directly compared C to D. Can NMA estimate the C vs. D effect, and what is the evidence pathway?"
  type: multiple-choice
  options:
    - "No — NMA requires at least one direct comparison between all treatment pairs"
    - "Yes — the indirect pathway runs through the network: C → A → placebo → B → D, using the transitive chain of comparisons"
    - "Yes — but only if a Bayesian framework is used"
    - "No — indirect comparisons are never valid for treatments not directly compared"
  answer: 1
  explanation: "The power of NMA is that it can estimate any pairwise comparison that is connected through the network, regardless of whether a direct trial exists. C was compared to A, A to placebo, placebo to B, and B to D — the network is connected, so C vs. D can be estimated indirectly. The estimate combines all available evidence and is less precise than a direct comparison would be (it inherits uncertainty from each link in the chain), but it provides information that would otherwise be unavailable. The transitivity assumption requires that the relative effects are consistent across the indirect pathway."

- question: "A network meta-analysis finds that the direct estimate of A vs. B from head-to-head trials is OR = 1.5, but the indirect estimate (through a common comparator C) is OR = 0.8. This inconsistency threatens the validity of the pooled NMA estimate."
  type: true-false
  answer: true
  explanation: "Inconsistency between direct and indirect evidence indicates that the treatment effects may depend on the study populations, co-interventions, or other factors that differ between the trial networks — violating the transitivity assumption. The pooled NMA estimate for A vs. B would blend the direct (1.5) and indirect (0.8) evidence, producing a result that may not represent either the direct or indirect truth accurately. Inconsistency should be investigated: are the trials comparing A-B directly conducted in different populations than those forming the indirect comparison? Are there effect modifiers that explain the discrepancy?"

- question: "NMA produces treatment rankings (e.g., 'Treatment B has a 73% probability of being the best'). Explain why these rankings should be interpreted cautiously."
  type: short-answer
  answer: "Rankings are highly sensitive to the precision and number of comparisons available for each treatment. A treatment with only one small trial may rank highly due to an imprecisely estimated large effect — wide confidence intervals create high ranking probabilities without strong evidence. Rankings also ignore clinically important differences in magnitude: being ranked #1 versus #2 may correspond to a trivially small difference. Furthermore, rankings can be unstable across modeling choices (fixed vs. random effects, prior distributions). Treatment effect estimates with confidence intervals are more informative than rankings for clinical decision-making."
  explanation: "The Surface Under the Cumulative Ranking curve (SUCRA) is often reported alongside rankings, summarizing each treatment's probability of being among the best. But SUCRA values are vulnerable to the same problems as raw rankings. A treatment with SUCRA = 0.85 could be slightly better than all alternatives with high confidence, or dramatically better with very low confidence. The effect estimate and its precision are always more informative than the ranking statistic."
```

## Explainer

Clinical practice requires choosing among multiple treatments, but most trials compare only two at a time — typically a new treatment against placebo or against one active comparator. Clinicians wanting to choose among five antidepressants, three blood pressure drugs, or six surgical techniques face a fragmented evidence base with many missing head-to-head comparisons. **Network meta-analysis** synthesizes this fragmented evidence into a coherent framework that estimates all pairwise treatment effects simultaneously.

The key insight is that **indirect evidence** can supplement direct evidence. If Trial 1 shows that Drug A beats placebo with OR = 2.0, and Trial 2 shows that Drug B beats placebo with OR = 1.5, the indirect comparison suggests Drug A beats Drug B with OR ≈ 2.0/1.5 = 1.33. This inference requires the **transitivity assumption**: the relative effects would be the same regardless of which comparator was used, which means the trials must be sufficiently similar in population, design, and conduct. NMA combines all direct and indirect evidence, weighting each by its precision, to produce a complete matrix of pairwise comparisons.

The analysis is typically conducted in a **Bayesian framework** (using MCMC methods in software like WinBUGS, OpenBUGS, or R's gemtc package), though frequentist approaches exist. Bayesian NMA naturally produces posterior distributions for all treatment effects, enabling probabilistic statements like "there is a 73% probability that Treatment B is the most effective." These treatment rankings — while appealing for clinical communication — must be interpreted cautiously, as they are sensitive to the precision and number of available comparisons.

The most important threat to NMA validity is **inconsistency**: disagreement between direct and indirect evidence for the same comparison. If the A-vs-B estimate from direct trials conflicts with the A-vs-B estimate inferred through the network, the transitivity assumption may be violated — perhaps the trials contributing indirect evidence enrolled different populations, used different outcome definitions, or involved different versions of the comparator treatment. Consistency can be assessed globally (does the model fit improve when inconsistency parameters are added?) and locally (do specific loops in the network show discrepant direct and indirect estimates?). When inconsistency is detected, the NMA results for those comparisons should be viewed skeptically, and the sources of inconsistency should be investigated through subgroup or meta-regression analyses.
