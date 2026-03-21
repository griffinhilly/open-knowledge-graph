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
builds-toward: []
tags:
- transparency
- preregistration
- open-science
- research-integrity
stage: formal-systems
status: draft
---
# Preregistration and Research Transparency Planning

## Core Idea
Preregistration involves documenting research hypotheses, design decisions, and analytical plans before data collection, creating a public record that distinguishes confirmatory hypothesis testing from exploratory analysis. Preregistration reduces researcher degrees of freedom—the flexibility in decision-making that can inflate false positive rates and effect size estimates through p-hacking and HARKing (Hypothesizing After Results are Known). Open science practices including preregistration, open data, and open code enhance transparency and reproducibility. Preregistration is particularly valuable in exploratory research and when researchers have many possible analytical choices.

## How It's Best Learned
Write a detailed preregistration document for a hypothetical study, specifying all design, measurement, and analytical decisions before data collection.

## Common Misconceptions
Preregistration is only for confirmatory studies (actually, it is valuable for both exploratory and confirmatory research). Preregistration prevents all flexibility in analysis (actually, sensitivity analyses and robustness checks can still occur; preregistration just distinguishes them from primary analyses).

## Questions

```yaml
- question: "A researcher collects data, runs 15 variations of their analysis (different exclusion criteria, covariates, and outcome measures), finds that one combination yields p = 0.04, and publishes this as 'confirmatory evidence' for their hypothesis. What is the fundamental problem with this approach?"
  type: multiple-choice
  options:
    - "The sample size was too small; any result with only 15 analytical variants is unreliable"
    - "The nominal α = 0.05 no longer reflects the true false positive rate — selecting the significant analysis post-hoc inflates the actual probability of a false positive far above 5%"
    - "The p-value threshold should be 0.01 for studies with multiple analytical variants"
    - "Exploratory analyses cannot be published in peer-reviewed journals"
  answer: 1
  explanation: "Each undisclosed analytical choice is a fork that multiplies the chance of finding a spurious significant result. If enough variants are tested, significance is almost guaranteed even in pure noise. The p-value only means what it claims (5% false positive rate) when the analysis was specified before looking at the data. Selecting the significant variant and presenting it as confirmatory is p-hacking: the true false positive rate in this example is far higher than the reported p-value implies. Preregistration prevents this by binding the researcher to a single pre-specified analysis."

- question: "What does preregistration make impossible — or at minimum immediately detectable — in a published study?"
  type: multiple-choice
  options:
    - "Conducting any exploratory analyses not mentioned in the original plan"
    - "HARKing (Hypothesizing After Results are Known) — presenting a post-hoc hypothesis as if it were specified in advance"
    - "Collecting additional participants if the original sample was underpowered"
    - "Running sensitivity analyses or robustness checks on the primary findings"
  answer: 1
  explanation: "Preregistration timestamps your hypothesis before data collection. If the registered hypothesis differs from what was reported, readers can see the discrepancy. HARKing — finding an unexpected significant result and then writing the paper as though you predicted it — looks like a confirmatory test but is really exploratory. Preregistration makes the distinction transparent. Exploratory analyses, additional participants, and sensitivity analyses are still allowed; they just must be labeled as such rather than presented as confirmatory."

- question: "A preregistered study that reports p = 0.04 provides stronger evidence for its hypothesis than an unregistered study reporting the same p = 0.04."
  type: true-false
  answer: true
  explanation: "The p-value is only interpretable at face value when the hypothesis and analysis were specified before the data were collected. In a preregistered study, p = 0.04 means there is a 4% chance of this result under the null hypothesis — no more. In an unregistered study, the researcher may have examined many analyses; the reported p = 0.04 could reflect one significant result from dozens of attempts, making the actual false positive rate much higher. Same number, very different evidential meaning."

- question: "Preregistration prevents researchers from conducting any analyses beyond what was specified in the original plan."
  type: true-false
  answer: false
  explanation: "Preregistration does not prohibit exploratory analysis — it requires that any analysis not in the preregistered plan be clearly labeled as exploratory rather than confirmatory. Sensitivity analyses, robustness checks, and unexpected findings are still valuable and publishable; they just cannot be presented as tests of pre-specified hypotheses. The key move is transparency: label what was planned in advance and what emerged from the data. This distinction — not the prohibition of exploration — is what preregistration achieves."

- question: "Explain how researcher degrees of freedom can inflate the false positive rate even when no individual analytical decision is dishonest or intended to deceive."
  type: short-answer
  answer: "Each legitimate-seeming analytical choice — which participants to exclude, whether to transform a variable, which covariates to include, which of several measured outcomes to report — is a branch point. If a researcher (consciously or not) gravitates toward choices that produce significant results and away from those that don't, the final analysis is implicitly selected from many possible analyses. Even if each choice seems reasonable in isolation, the effective Type I error rate across all those choices far exceeds the nominal α. Simulations show that even a handful of unconstrained choices can push the real false positive rate above 60% while appearing to be 5%."
  explanation: "This is why the problem is structural, not moral. Researchers don't need to be dishonest — natural motivated reasoning, the preference for coherent narratives, and confirmation bias guide analytical choices in ways the researcher may not notice. Preregistration removes the degrees of freedom by specifying choices before the data can influence them, making the p-value mean what it claims."
```

## Explainer

From hypothesis formation, you know how to construct a testable, grounded, directional hypothesis. From open science and research ethics, you know that psychology has faced a replication crisis — many published findings fail when independent labs attempt to reproduce them. Preregistration addresses a root cause of that crisis: not deliberate fraud, but the quiet inflation of false positives that happens when researchers have too many undisclosed choices during analysis.

The key concept is **researcher degrees of freedom**: the range of legitimate-seeming analytical decisions available at each step — which participants to exclude as outliers, whether to log-transform a skewed variable, which covariates to control for, which of several collected dependent variables to report, whether to run one more participant after a near-significant result. No single choice is obviously wrong. The problem is what happens when a researcher (consciously or not) cycles through combinations until something reaches p < .05 and then reports only that analysis as if it were the only one tried. The nominal α = .05 threshold no longer means what it claims. Each additional analytical choice is a fork in the road; if you walk enough forks and report only the significant path, you will find significance even in noise. Simulations show that with just a handful of unconstrained analytical choices, the true false positive rate can exceed 60% while appearing to be 5%.

**Preregistration** is the prophylactic: by documenting your hypothesis, design, and analysis plan in a public registry *before* data collection, you bind yourself. The timestamp proves the hypothesis existed before the data. A preregistered analysis is **confirmatory**: the test was specified in advance, so the p-value is interpretable at face value — a false positive rate of 5% really means 5%. Any analysis not in the preregistration is **exploratory**: interesting, potentially hypothesis-generating, but not confirmatory. The critical move is not eliminating flexibility but making the distinction *transparent to readers*. You can still run exploratory analyses; you just label them honestly.

**HARKing** — Hypothesizing After Results are Known — is the specific abuse that preregistration prevents most directly. A researcher runs an exploratory analysis, finds an unexpected significant effect, then writes the paper as if that was the hypothesis all along. The finding looks like a confirmatory test but is really an exploratory one. The study's false positive rate is not the nominal α but something much higher, because the hypothesis was selected precisely because it was significant. Preregistration timestamps the hypothesis before the data exist, making HARKing impossible — or at minimum visible as a deviation from the registered plan. Preregistration doesn't change what you find; it changes what your findings *mean*. A p = .03 in a preregistered study is strong evidence; a p = .03 that emerged from twenty undisclosed analysis variants is considerably weaker, regardless of what the paper claims.
