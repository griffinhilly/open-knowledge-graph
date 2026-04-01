---
id: multiple-testing-corrections
title: Multiple Testing Corrections
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: power-and-sample-size
  type: soft
- id: probability-axioms
  type: soft
builds-toward:
- meta-analysis-biostatistics
- group-sequential-methods
tags:
- multiple-comparisons
- Bonferroni
- FDR
- family-wise-error-rate
- Benjamini-Hochberg
stage: advanced
status: validated
---

# Multiple Testing Corrections

## Core Idea
When multiple statistical tests are performed simultaneously, the probability that at least one test produces a false positive increases rapidly — with 20 independent tests at alpha = 0.05, the probability of at least one false positive is approximately 64%. Multiple testing corrections adjust significance thresholds or p-values to control this inflated error rate. The two main frameworks are family-wise error rate (FWER) control, which limits the probability of any false positive (e.g., Bonferroni correction), and false discovery rate (FDR) control, which limits the expected proportion of false positives among rejected hypotheses (e.g., Benjamini-Hochberg procedure). FWER methods are conservative and appropriate for confirmatory studies; FDR methods are less conservative and better suited to exploratory, high-dimensional settings like genomics.

## Questions

```yaml
- question: "A researcher tests 20 dietary supplements for association with cancer risk, each at alpha = 0.05, and finds one significant result (p = 0.03). She reports this supplement as a confirmed risk factor. What is the fundamental problem?"
  type: multiple-choice
  options:
    - "The p-value of 0.03 is too close to 0.05 to be reliable"
    - "With 20 tests at alpha = 0.05, the probability of at least one false positive is about 64%, so the single significant result is likely a chance finding"
    - "She should have used alpha = 0.01 instead of 0.05 from the start"
    - "The problem is that she tested supplements rather than drugs, which have weaker effects"
  answer: 1
  explanation: "The probability of at least one false positive across k independent tests is 1 - (1 - alpha)^k. With k = 20 and alpha = 0.05, this is 1 - 0.95^20 ≈ 0.64. One significant result out of 20 is exactly what you would expect by chance alone. Without correction (e.g., Bonferroni threshold of 0.05/20 = 0.0025), the p = 0.03 result does not survive adjustment and should not be treated as confirmatory evidence."

- question: "The Bonferroni correction divides the significance threshold by the number of tests (alpha/m). A study performs 1,000 genome-wide tests and applies Bonferroni. Why might this be problematic in practice?"
  type: multiple-choice
  options:
    - "Bonferroni only works for fewer than 100 tests"
    - "The adjusted threshold (0.05/1000 = 0.00005) is so stringent that the study has very low power to detect real but moderate effects"
    - "Bonferroni assumes tests are perfectly correlated, which is rarely true"
    - "Bonferroni increases the Type I error rate with more tests"
  answer: 1
  explanation: "Bonferroni controls the family-wise error rate — the probability of even one false positive — by dividing alpha by m. When m is large, the per-test threshold becomes extremely small, and the power to detect real effects plummets. This is why FDR-controlling procedures like Benjamini-Hochberg are preferred in high-dimensional settings: they accept some false positives in exchange for much better power to detect true effects. Bonferroni is also conservative (not anti-conservative) because it assumes worst-case independence; correlated tests make it even more conservative."

- question: "The Benjamini-Hochberg procedure controls the false discovery rate rather than the family-wise error rate, making it identical to having no correction at all but with a different label."
  type: true-false
  answer: false
  explanation: "The Benjamini-Hochberg procedure is a genuine correction — it ranks p-values and compares each to a threshold that depends on its rank and the total number of tests. It is less conservative than Bonferroni because it controls a different quantity: the expected proportion of false discoveries among rejected hypotheses, rather than the probability of any false discovery. With FDR at 5%, you expect that 5% of your significant results are false positives — this is much more permissive than Bonferroni but still provides meaningful error control, which is why it dominates in genomics and other high-dimensional fields."

- question: "Explain the conceptual difference between controlling the family-wise error rate (FWER) and controlling the false discovery rate (FDR), and when each is appropriate."
  type: short-answer
  answer: "FWER controls the probability of making even one false positive across all tests — it answers 'what is the chance I report anything false?' FDR controls the expected proportion of false positives among the results declared significant — it answers 'among my discoveries, what fraction are likely wrong?' FWER is appropriate for confirmatory settings where any false positive has serious consequences (e.g., approving an ineffective drug). FDR is appropriate for exploratory settings where finding most true effects matters more than avoiding all false leads (e.g., identifying candidate genes for follow-up validation)."
  explanation: "The distinction reflects different research goals. In a confirmatory clinical trial testing one primary endpoint, a single false positive could lead to approving a harmful or useless treatment — FWER control (even Bonferroni) is justified. In a microarray experiment testing 20,000 genes, Bonferroni would require p < 2.5 × 10⁻⁶, missing nearly all real signals. FDR at 5% accepts that 1 in 20 flagged genes may be a false lead, but recovers far more true associations for downstream validation."
```

## Explainer

The multiple testing problem is one of the most important concepts in applied biostatistics because it arises in nearly every real study — any time you test more than one hypothesis, compare more than two groups, or examine more than one outcome. The underlying mathematics is straightforward: if each test has an independent 5% false-positive rate, the probability of at least one false positive across m tests is 1 - (1 - 0.05)^m. At m = 20, this reaches 64%. At m = 100, it exceeds 99%. Without correction, a study that tests many hypotheses is almost guaranteed to find something significant by chance.

The **Bonferroni correction** is the simplest and most conservative approach: divide the per-test significance level by the number of tests (alpha/m). If you perform 20 tests and want an overall alpha of 0.05, each individual test must reach p < 0.0025. This guarantees that the probability of any false positive across all tests remains at or below 5%. The cost is severe: each test now requires much stronger evidence, reducing the power to detect real effects. Bonferroni is appropriate when the number of tests is small and every false positive carries serious consequences — for example, testing a few pre-specified secondary endpoints in a clinical trial.

The **false discovery rate** framework, introduced by Benjamini and Hochberg in 1995, controls a fundamentally different quantity. Instead of asking "what is the probability of any false positive?", it asks "among the results I call significant, what proportion are false?" The Benjamini-Hochberg procedure ranks all p-values from smallest to largest and compares each to a threshold that increases with rank: the k-th smallest p-value is compared to (k/m) × q, where q is the desired FDR level. This allows more discoveries while maintaining a controlled rate of false findings among them. An FDR of 5% means that if you flag 100 genes as significant, you expect about 5 to be false discoveries — an acceptable tradeoff in exploratory research where flagged candidates will be validated independently.

Choosing between FWER and FDR depends on the research context. Confirmatory trials with regulatory consequences demand FWER control — approving an ineffective drug based on a false positive has real costs. Exploratory studies in genomics, proteomics, or epidemiological screening benefit from FDR control because the goal is to generate candidates for follow-up, and missing true signals is more costly than including a few false ones. Many studies use a hybrid approach: FDR for initial screening, followed by FWER-controlled confirmatory analysis on the reduced candidate set.
