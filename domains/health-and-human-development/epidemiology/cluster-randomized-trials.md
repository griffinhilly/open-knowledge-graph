---
id: cluster-randomized-trials
title: Cluster Randomized Trials
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: measures-of-association
  type: soft
tags:
- study-design
- randomization
- group-level
- intraclass-correlation
stage: expert
status: draft
---

# Cluster Randomized Trials

## Core Idea
Cluster randomized trials randomize groups rather than individuals, necessary when interventions naturally act at the group level or individual randomization is infeasible. Analysis must account for within-cluster correlations using appropriate statistical methods to avoid underestimating standard errors.

## Explainer

From your study of epidemiologic study designs, you know that the randomized controlled trial (RCT) achieves causal inference by randomly assigning individuals to treatment and control conditions, ensuring that confounders — both measured and unmeasured — are balanced by chance. **Cluster randomized trials (CRTs)** extend this logic to situations where the unit of randomization is not an individual but a group: a school, a village, a hospital ward, a workplace. The same fundamental goal applies — random assignment to achieve comparability — but the unit change introduces complications that require careful treatment.

Why randomize clusters rather than individuals? Two main reasons arise in practice. First, some interventions are **logistically impossible to deliver individually within a shared setting**. If you want to study the effect of a new teacher training program, you cannot randomize half the students in a classroom to have a trained teacher and half to have an untrained one — the teacher's behavior affects everyone. The classroom is the natural unit of delivery, so classrooms must be the unit of randomization. Second, **contamination** threatens internal validity when individuals in the same setting know each other's treatment status. In a community hygiene intervention, participants may share information about the intervention with neighbors, blurring the comparison. Randomizing entire communities prevents this cross-contamination.

The central statistical challenge of CRTs is **within-cluster correlation**. Individuals within the same cluster — students in the same school, patients of the same physician — tend to be more similar to each other than to individuals in different clusters. They share the same environment, the same norms, the same providers. This clustering of outcomes is measured by the **intraclass correlation coefficient (ICC)**: the proportion of total outcome variance that is attributable to between-cluster differences (rather than between-individual differences within clusters). An ICC near zero means clusters are internally heterogeneous and behave like a collection of independent individuals. An ICC near 1 means everyone in a cluster has nearly the same outcome.

The ICC matters because it deflates the effective sample size of the trial. If the ICC is 0.1 and each cluster contains 50 people, the **design effect** — the factor by which sample size must be inflated relative to an individually randomized trial — is approximately 1 + (50−1)×0.1 = 5.9. You need nearly six times as many participants as a comparable individual-level trial to achieve the same statistical power. Failing to account for this — treating each individual as independent when they are not — produces standard errors that are far too small, confidence intervals too narrow, and p-values that overstate the evidence for an effect. This is the most common analytical error in published CRTs.

Correct analysis requires methods that explicitly model the cluster-level correlation: **multilevel models** (also called mixed-effects or hierarchical models), **generalized estimating equations (GEE)**, or analysis that treats the cluster summary statistic as the unit of analysis. The choice depends on sample size and research question. Critically, the number of clusters — not the number of individuals — drives statistical power in a CRT. A CRT with 10 clusters per arm and 500 people per cluster has far less power than one with 50 clusters per arm and 100 people per cluster, even though the total sample size is identical. This design logic must be considered at the planning stage; no analysis can recover power lost by too few clusters.

## Questions

```yaml
- question: "A researcher wants to study the effect of a school-based mindfulness program on student anxiety. She randomizes schools, not students. What is the primary reason for this choice?"
  type: multiple-choice
  options:
    - "To increase statistical power by using a larger unit of randomization"
    - "Because the intervention is delivered at the school level and individual randomization within a school would cause contamination"
    - "Because students within a school are too heterogeneous for individual randomization to work"
    - "To avoid needing informed consent from individual participants"
  answer: 1
  explanation: "When an intervention is delivered by school staff and affects the entire school environment, randomizing individuals within the same school is not feasible — the treatment affects everyone in the school, not just those 'assigned' to it. Contamination (treated and control students interacting, or teachers behaving differently toward different students) would also undermine the comparison. School-level randomization is the natural choice."

- question: "In a cluster randomized trial, a high intraclass correlation coefficient (ICC) implies:"
  type: multiple-choice
  options:
    - "Individuals in different clusters are more similar to each other than individuals in the same cluster"
    - "Cluster size does not affect statistical power"
    - "A larger design effect, meaning you need more participants to achieve the same power as an individually randomized trial"
    - "The standard errors from individual-level analysis will be too large"
  answer: 2
  explanation: "A high ICC means individuals within clusters are similar (much of the variance is between clusters, not within), which reduces the amount of independent information each additional individual contributes. The design effect 1 + (m−1)×ICC increases with ICC, inflating required sample size. Standard errors from naive individual-level analysis will be too *small* (not too large), because the analysis wrongly assumes independence."
```
