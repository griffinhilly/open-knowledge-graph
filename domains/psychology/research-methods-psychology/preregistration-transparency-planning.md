---
id: preregistration-transparency-planning
title: Preregistration and Research Transparency Planning
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-hypothesis-formation
  type: hard
- id: replication-and-open-science
  type: soft
- id: psychological-research-ethics
  type: soft
builds-toward:
- exploratory-vs-confirmatory-analysis-strategies
tags:
- transparency
- preregistration
- open-science
- research-integrity
stage: abstract-reasoning
status: draft
---

# Preregistration and Research Transparency Planning

## Core Idea
Preregistration involves documenting research hypotheses, design decisions, and analytical plans before data collection, creating a public record that distinguishes confirmatory hypothesis testing from exploratory analysis. Preregistration reduces researcher degrees of freedom—the flexibility in decision-making that can inflate false positive rates and effect size estimates through p-hacking and HARKing (Hypothesizing After Results are Known). Open science practices including preregistration, open data, and open code enhance transparency and reproducibility. Preregistration is particularly valuable in exploratory research and when researchers have many possible analytical choices.

## How It's Best Learned
Write a detailed preregistration document for a hypothetical study, specifying all design, measurement, and analytical decisions before data collection.

## Common Misconceptions
Preregistration is only for confirmatory studies (actually, it is valuable for both exploratory and confirmatory research). Preregistration prevents all flexibility in analysis (actually, sensitivity analyses and robustness checks can still occur; preregistration just distinguishes them from primary analyses).

## Explainer

From hypothesis formation, you know how to construct a testable, grounded, directional hypothesis. From open science and research ethics, you know that psychology has faced a replication crisis — many published findings fail when independent labs attempt to reproduce them. Preregistration addresses a root cause of that crisis: not deliberate fraud, but the quiet inflation of false positives that happens when researchers have too many undisclosed choices during analysis.

The key concept is **researcher degrees of freedom**: the range of legitimate-seeming analytical decisions available at each step — which participants to exclude as outliers, whether to log-transform a skewed variable, which covariates to control for, which of several collected dependent variables to report, whether to run one more participant after a near-significant result. No single choice is obviously wrong. The problem is what happens when a researcher (consciously or not) cycles through combinations until something reaches p < .05 and then reports only that analysis as if it were the only one tried. The nominal α = .05 threshold no longer means what it claims. Each additional analytical choice is a fork in the road; if you walk enough forks and report only the significant path, you will find significance even in noise. Simulations show that with just a handful of unconstrained analytical choices, the true false positive rate can exceed 60% while appearing to be 5%.

**Preregistration** is the prophylactic: by documenting your hypothesis, design, and analysis plan in a public registry *before* data collection, you bind yourself. The timestamp proves the hypothesis existed before the data. A preregistered analysis is **confirmatory**: the test was specified in advance, so the p-value is interpretable at face value — a false positive rate of 5% really means 5%. Any analysis not in the preregistration is **exploratory**: interesting, potentially hypothesis-generating, but not confirmatory. The critical move is not eliminating flexibility but making the distinction *transparent to readers*. You can still run exploratory analyses; you just label them honestly.

**HARKing** — Hypothesizing After Results are Known — is the specific abuse that preregistration prevents most directly. A researcher runs an exploratory analysis, finds an unexpected significant effect, then writes the paper as if that was the hypothesis all along. The finding looks like a confirmatory test but is really an exploratory one. The study's false positive rate is not the nominal α but something much higher, because the hypothesis was selected precisely because it was significant. Preregistration timestamps the hypothesis before the data exist, making HARKing impossible — or at minimum visible as a deviation from the registered plan. Preregistration doesn't change what you find; it changes what your findings *mean*. A p = .03 in a preregistered study is strong evidence; a p = .03 that emerged from twenty undisclosed analysis variants is considerably weaker, regardless of what the paper claims.
