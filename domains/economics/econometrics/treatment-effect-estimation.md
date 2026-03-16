---
id: treatment-effect-estimation
title: 'Treatment Effects: ATE, CATE, and Heterogeneous Effects'
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- matching-estimators-causal-inference
tags:
- causal-inference
- treatment-effects
- heterogeneous
stage: formal-systems
status: draft
---

# Treatment Effects: ATE, CATE, and Heterogeneous Effects

## Core Idea
The Average Treatment Effect (ATE) measures mean causal impact across the population; Conditional Average Treatment Effect (CATE) varies by subgroups; Local Average Treatment Effect (LATE) applies to compliers in instrumental variable settings. Identifying these requires assumptions about confounding and selection mechanisms.

## How It's Best Learned
Contrast ATE, CATE, and LATE with examples; understand which assumptions identify each and when each is relevant.

## Common Misconceptions
ATE and CATE are conceptually different; ATE averages over the population while CATE allows effects to differ by observable characteristics.

## Explainer

From your potential outcomes prerequisite, you know the fundamental setup: every unit i has two potential outcomes — Y(1) if treated and Y(0) if not treated. The individual causal effect is τᵢ = Y(1)ᵢ − Y(0)ᵢ, but you observe only one potential outcome per person. Since individual effects are never identified, empirical work targets averages — and which average matters depends on the policy question being asked.

The **Average Treatment Effect (ATE)** is E[Y(1) − Y(0)] averaged over the full population, treated and untreated alike. This is the right quantity for a universal policy question: if we were to randomly select someone from the population and treat them, what would happen on average? The **Average Treatment Effect on the Treated (ATT)** narrows focus to those who actually received treatment: ATT = E[Y(1) − Y(0) | D = 1]. For a voluntary job training program, ATT tells you the benefit to participants — people who chose to enroll. ATE would additionally include the counterfactual effect on people who didn't enroll, which may be different if selection into treatment was based on expected benefit.

The **Conditional Average Treatment Effect (CATE)** takes heterogeneity seriously. Rather than a single number, CATE maps each covariate vector X to a local treatment effect: τ(x) = E[Y(1) − Y(0) | X = x]. This is the right framework when effects are expected to vary across subgroups — a drug may work better for older patients, a training program may benefit low-educated workers more. In practice, estimating CATE requires data-rich methods: causal forests and other machine learning approaches partition the covariate space to estimate local effects, but they need large samples to be precise. The fundamental tradeoff is between aggregation (ATE is precise but hides heterogeneity) and granularity (CATE reveals heterogeneity but demands more data and stronger assumptions).

The **Local Average Treatment Effect (LATE)** arises in instrumental variables settings. When you use an instrument Z to address selection into treatment, the IV estimator does not recover ATE or ATT — it recovers the effect only for **compliers**: people who take treatment when Z assigns them to treatment and decline when Z does not. Always-takers (who take treatment regardless) and never-takers (who never take it) contribute no identifying variation. LATE can differ substantially from ATE if compliers are unusual. In a military draft lottery study, LATE measures the earnings effect for men who served because they were drafted but would not have enlisted voluntarily — this may not generalize to those who chose to serve.

The practical lesson is to specify the target parameter before analyzing data. "The effect of X on Y" is incomplete. "The ATE if the policy is universally applied" differs from "the ATT — the effect on current participants" which differs from "which subgroups benefit most (CATE)" which differs from "what does this particular instrument identify (LATE)." Most empirical papers report ATT or LATE rather than ATE, because their identification strategy only credibly identifies effects for a specific subpopulation. Being explicit about which estimand you are targeting — and why it matches your policy question — is the hallmark of careful causal inference.
