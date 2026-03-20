---
id: longitudinal-design-methods
title: 'Longitudinal Designs: Methods for Studying Change'
domain: psychology
course: research-methods-psychology
prerequisites:
- id: between-subjects-design-implementation
  type: soft
- id: within-subjects-design-implementation
  type: soft
builds-toward:
- internal-validity-and-threats
- measurement-error-and-attenuation
tags:
- design
- longitudinal
- change
- development
stage: formal-systems
status: draft
---

# Longitudinal Designs: Methods for Studying Change

## Core Idea
Longitudinal studies strengthen causal inference by establishing temporal precedence and can reveal nonlinear trajectories, critical periods, and individual differences in change. However, they incur substantial costs in time, money, and participant retention, and patterns of missingness can bias results.

## How It's Best Learned
Design a 3-wave longitudinal study, specifying assessment intervals, expected attrition rates, and analysis approach (mixed models, latent growth curve). Examine published longitudinal studies and identify how authors handled attrition, practice effects, and missing data.

## Common Misconceptions
- Longitudinal designs automatically imply causality; without experimental manipulation or strong temporal and theoretical evidence, causality cannot be inferred.
- Equal spacing of assessments is necessary; unequal spacing can accommodate practical constraints and still support valid analysis.
- Attrition is random and ignorable; selective attrition based on outcomes introduces bias that must be addressed through sensitivity analyses.

## Explainer

From your work on between-subjects and within-subjects designs, you know the core tradeoff: between-subjects designs compare different people, while within-subjects designs compare the same people under different conditions. A **longitudinal design** extends the within-subjects logic into time itself — the same participants are measured repeatedly over weeks, months, or years, allowing you to observe how each individual changes. This temporal tracking is what distinguishes longitudinal studies from the alternatives. A **cross-sectional study** takes a snapshot of different age groups at the same moment; it can reveal age differences but cannot separate aging effects from cohort effects (the possibility that 60-year-olds today simply grew up in a different era than 30-year-olds). Only longitudinal data can directly track change within individuals.

The central methodological strength of longitudinal designs is **temporal precedence** — one of the three conditions for causal inference. If you measure Variable A and then Variable B months later, and A predicts change in B over that interval, you have eliminated the possibility that B caused A (the effect preceded the putative cause). This makes longitudinal designs far stronger than cross-sectional correlational studies for establishing directionality. Longitudinal data can also reveal phenomena invisible in cross-sectional snapshots: **non-linear trajectories** (ability may rise steeply in childhood, plateau in adulthood, and decline in late life), **critical periods** (certain experiences may only affect development during a specific window), and **individual differences in rates of change** (not everyone follows the same trajectory, and understanding who changes faster or slower is often the scientific question of interest).

The costs of this strength are substantial. Longitudinal studies are expensive in time, funding, and administrative complexity. The most serious methodological threat is **selective attrition** — the systematic dropout of participants who differ from those who remain. If healthier, higher-functioning, or more motivated participants are more likely to stay in the study, the surviving sample becomes increasingly unrepresentative over time. Longitudinal studies of aging, for example, often suffer from a "healthy survivor" bias: those who remain at later waves are those who have aged most successfully, making decline look less steep than it actually is in the population. Researchers address this through sensitivity analyses, careful comparison of completers versus dropouts at baseline, and modern missing-data methods like **multiple imputation** or **full information maximum likelihood**, which use all available information rather than deleting participants with missing observations.

**Practice effects** add another wrinkle specific to longitudinal designs: participants who are tested on the same instrument multiple times may improve simply from familiarity, not from genuine development. This is especially problematic in cognitive testing, where the tasks themselves teach the skills being measured. Researchers manage this by spacing assessments far enough apart, using parallel forms at different waves, or modeling the expected practice-effect trajectory and removing it from estimates of true change. The design decision about how many waves to include and how far apart to space them is not arbitrary — it should be driven by the expected shape of the trajectory and the minimum interval over which meaningful change can occur. Three waves are generally required to distinguish linear from non-linear change; more waves provide richer information but increase attrition risk.
