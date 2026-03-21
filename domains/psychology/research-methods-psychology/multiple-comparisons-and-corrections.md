---
id: multiple-comparisons-and-corrections
title: Multiple Comparisons Problem and Correction Methods
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: type-i-type-ii-error-tradeoffs
  type: soft
builds-toward:
- analysis-plan-preregistration-commitment
tags:
- statistics
- multiple-comparisons
- correction
stage: formal-systems
status: draft
---

# Multiple Comparisons Problem and Correction Methods

## Core Idea
When conducting multiple statistical tests (comparing many conditions, testing multiple outcomes, exploring subgroups), the probability of false positives accumulates. Corrections like Bonferroni, false discovery rate control, or planned contrasts manage error rates but reduce statistical power. The appropriate correction depends on whether comparisons were planned a priori or exploratory post-hoc.

## Questions

```yaml
- question: "A researcher runs an ANOVA with 4 groups, finds a significant omnibus F-test, then examines all 6 possible pairwise comparisons to locate the effect. What correction is most appropriate for these comparisons?"
  type: multiple-choice
  options:
    - "No correction — the overall F-test already controlled for familywise error across the six comparisons"
    - "Bonferroni correction dividing α by 6 — any post-hoc comparison requires this specific correction"
    - "A post-hoc correction designed for exhaustive pairwise comparisons, such as Tukey's HSD"
    - "FDR control — all post-hoc comparisons are exploratory, and FDR is the standard for exploration"
  answer: 2
  explanation: "The omnibus F-test tells you that *some* difference exists among the groups, but not which pairs differ — that requires further testing. These follow-up pairwise tests are post-hoc comparisons conducted after observing data, which capitalizes on chance and inflates false positive risk. Tukey's HSD is specifically designed for this situation: all pairwise comparisons after a significant ANOVA. Simple Bonferroni (option B) is valid but more conservative than necessary here. The F-test (option A) does not protect against the pairwise comparisons — it answers a different question."

- question: "A researcher conducts 100 statistical tests at α = .05. Assuming all null hypotheses are true (no real effects exist), approximately how many tests are expected to yield a 'significant' result?"
  type: multiple-choice
  options:
    - "0 — with proper alpha control, no false positives should occur under the null"
    - "5 — the expected number of Type I errors is α × number of tests = .05 × 100"
    - "1 — one test per family is the conventional allowance"
    - "0.05 — that is the probability of a false positive, not the expected count"
  answer: 1
  explanation: "Each test independently has a 5% false positive rate. With 100 tests and no true effects, the expected number of false positives is 0.05 × 100 = 5. This is the core of the multiple comparisons problem: the more tests you run, the more false positives you expect by chance alone, even when nothing is real. The familywise error rate — the probability of at least one false positive — approaches 1 − (0.95)^100 ≈ 99.4% with no correction."

- question: "The Bonferroni correction controls the familywise error rate by making each individual test harder to pass, but this comes at the cost of reduced statistical power to detect true effects."
  type: true-false
  answer: true
  explanation: "Bonferroni divides α by the number of tests k: each test uses α/k instead of α. For k = 20 tests, the per-test threshold drops from .05 to .0025. This dramatically reduces the probability of any false positive, but equally reduces power: true effects that would have been significant at α = .05 may no longer clear the stricter threshold. This power reduction is why Bonferroni is considered conservative, especially when tests are positively correlated — in that case, it over-corrects."

- question: "A researcher who specifies exactly two theoretically motivated comparisons before data collection needs to apply the same stringent correction as a researcher who conducts 100 post-hoc comparisons on the same dataset."
  type: true-false
  answer: false
  explanation: "The appropriate correction depends critically on whether comparisons were planned a priori or discovered post-hoc. Two pre-specified planned contrasts constitute a family of 2 tests with a coherent theoretical basis — the inflation of Type I error is modest and may not require correction beyond the two tests themselves. One hundred post-hoc comparisons represent a fundamentally different situation: the researcher is hunting for significance, and the probability of a false positive among the findings is high. The number of tests is only one factor; whether they were planned or exploratory determines the correct accounting."

- question: "Why does the multiple comparisons problem arise when conducting many statistical tests, and why can't it be fully fixed by applying corrections after data collection has occurred?"
  type: short-answer
  answer: "The multiple comparisons problem arises because each test has a nonzero false positive rate (α), so running many tests guarantees some false positives will occur by chance. With k independent tests at α = .05, the familywise error rate is 1 − (1 − .05)^k, which approaches 1 as k grows. Post-hoc corrections like Bonferroni or FDR can mathematically adjust thresholds to control error rates, but they cannot undo the deeper problem: when a researcher selects which comparisons to report after seeing the data (or runs many comparisons to find significance), the reported p-values no longer have their nominal meaning. The selection process itself introduces bias that no correction can fully repair — only pre-registration and honest reporting of all tests conducted can preserve the validity of the inference."
  explanation: "This is why the distinction between planned and post-hoc comparisons matters so much. A Bonferroni correction applied after exploring all possible subgroup analyses does reduce the nominal false positive rate, but the researcher's decision to report only significant findings, or to stop analyzing once significance was found, cannot be corrected statistically. The solution is procedural (preregistration, full reporting) not purely mathematical."
```

## Explainer

Your understanding of inferential statistics already tells you that a significance threshold of α = .05 means you accept a 5% chance of a false positive on any single test. The **multiple comparisons problem** follows directly from this: if you run 20 independent tests at α = .05 and there are truly no effects, you expect about one false positive by chance alone. The more tests you run, the more likely you are to find something that looks significant but isn't. This is the mathematical foundation of the **familywise error rate (FWER)** — the probability of making at least one Type I error across a family of tests.

The **Bonferroni correction** is the simplest solution: divide your alpha by the number of tests. If you run 20 tests, use α = .0025 per test instead of .05. This controls the FWER at .05 — the probability of any false positive across the whole family remains at most 5%. The logic is intuitive (you've made the threshold harder to clear), but the cost is real: Bonferroni is conservative when tests are correlated (as many tests of the same construct will be), and it reduces statistical power substantially. With 20 tests at α = .0025, you need a much larger effect to achieve significance, which means you'll miss more true effects (increased Type II error).

The **false discovery rate (FDR)** approach, developed by Benjamini and Hochberg, offers a different philosophical deal: instead of guaranteeing that no false positive slips through, it controls the *expected proportion* of your significant results that are false positives. An FDR of .05 means that among all findings you declare significant, about 5% are expected to be false positives. This is less stringent than FWER control, but for exploratory research generating hypotheses — rather than making confirmatory decisions — it captures the right trade-off. When exploring 200 brain regions for an effect, FDR control at .05 allows many comparisons while promising that most significant findings are probably real.

The most practically important distinction is between **planned contrasts** and **post-hoc comparisons**. If you specify, before collecting data, that you will compare exactly three conditions using two theoretically motivated contrasts, you have two tests and a coherent family — and you may not need aggressive correction. If you run an ANOVA, find overall significance, and then examine every possible pairwise comparison to find where the effect lives, you are conducting post-hoc exploration and must apply corrections (Tukey, Scheffé, or others designed for this case). The reason is not ceremonial — it is that post-hoc exploration capitalizes on chance in ways that planned contrasts do not. The honest accounting of your testing strategy, declared before data collection in a preregistration, is what determines the correct correction. The multiple comparisons problem cannot be fixed after the fact; it must be planned around.
