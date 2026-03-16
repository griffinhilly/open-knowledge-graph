---
id: experimental-design-social
title: Experimental Design in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: hard
- id: probability-and-statistics
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- field-experiments-real-world
- lab-experiments-behavioral
tags:
- experimental
- causal
- design
- randomization
stage: advanced
status: draft
---

# Experimental Design in Social Science

## Core Idea
Experiments isolate causal effects by randomly assigning subjects to treatment and control conditions. Social science experiments range from laboratory settings (studying strategic behavior or bargaining) to field experiments in real communities (testing policy interventions). Random assignment eliminates confounding, but challenges include recruitment, compliance, external validity, and ethical constraints. Power analysis, heterogeneous treatment effects, and intention-to-treat estimation are central to rigorous experimental inference.

## Explainer

From your work in research design and probability, you know the fundamental problem of causal inference: we can never observe the same unit under both treatment and control simultaneously. The counterfactual — what would have happened to the treated person had they not been treated — is unobservable. **Random assignment** solves this problem not by recovering individual counterfactuals but by making treatment and control groups statistically equivalent in expectation. Because assignment is random, any pre-existing differences between groups are due to chance alone, and that chance is quantifiable. This is why a well-run randomized experiment lets you attribute the difference in outcomes directly to the treatment.

The logic extends cleanly from your probability background. Before randomization, each subject has some probability of receiving treatment. After randomization, treated and control groups have the same expected distribution of every variable — observed and unobserved. This is the key advantage over observational methods: you don't need to measure and control for all confounders because randomization has neutralized them as a group. The price you pay is that experiments are often expensive, slow, and sometimes ethically or practically impossible. You cannot randomly assign someone to a childhood in poverty to study its effects.

Social science experiments come in two main varieties. **Laboratory experiments** bring participants into a controlled setting — often a computer lab — to study decision-making, strategic interaction, or judgment under controlled conditions. They maximize internal validity (the causal claim is clean) but sacrifice external validity (do college students in a lab behave like everyone else?). **Field experiments** randomize real interventions in natural settings — assigning some neighborhoods to receive a job training program, some voters to receive a mobilization message. They sacrifice some control but gain external validity. The randomized controlled trial (RCT) used in development economics and public health is a field experiment.

Even a perfectly designed experiment faces implementation challenges. **Non-compliance** occurs when subjects assigned to treatment don't take it, or controls obtain it anyway. The solution is **intention-to-treat (ITT) estimation**: analyze outcomes based on assigned treatment, not received treatment. ITT is always unbiased; estimating the effect on compliers requires instrumental variables methods. **Attrition** — subjects dropping out — can reintroduce selection bias even after clean randomization, because attrition is often correlated with treatment. Researchers check for differential attrition and report bounds on estimates when it's present.

**Power analysis** is the statistical discipline of ensuring your experiment is large enough to detect effects that matter. Before running an experiment, you specify the smallest effect size you'd care about, an acceptable false-positive rate (typically 5%), and an acceptable false-negative rate (typically 20%), and the formula tells you the required sample size. Underpowered studies that fail to detect real effects are a major source of irreproducibility in social science. Running a power analysis is not a technicality — it is how you decide whether an experiment is worth running at all. **Heterogeneous treatment effects** analysis asks whether the average effect masks important variation: does the intervention work better for women than men, for high-income than low-income households? These subgroup analyses require larger samples and pre-registration to avoid spurious discoveries.
