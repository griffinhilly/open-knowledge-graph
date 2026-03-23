---
id: item-response-theory-assumptions
title: 'Item Response Theory: Assumptions and Fundamentals'
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: classical-test-theory
  type: hard
- id: probability-density-functions-theory
  type: soft
- id: normal-distribution
  type: soft
- id: probability-mass-functions
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
- ability-parameter-estimation-theta-estimation
- classical-vs-irt-item-analysis
tags:
- irt
- assumptions
- unidimensionality
- local-independence
stage: expert
status: validated
---

# Item Response Theory: Assumptions and Fundamentals

## Core Idea
IRT assumes unidimensionality (one latent ability drives responses), local independence (responses independent given ability), and monotonic item response functions. These assumptions are more restrictive than classical test theory but enable item-level precision and ability-independent item statistics. Testing assumptions is essential before IRT application.

## How It's Best Learned
Fit IRT models to real datasets and examine residuals and goodness-of-fit indices. Use dimensionality tests and compare unidimensional vs. multidimensional models.

## Common Misconceptions
- Assuming unidimensionality requires perfect homogeneity (acceptable even with small secondary factors)
- Local independence is violated when content is highly related (it means independence GIVEN ability, not necessarily in raw data)

## Questions

```yaml
- question: "Two test items share a reading passage about climate change. A researcher finds they are highly correlated in raw data. Does this necessarily violate local independence?"
  type: multiple-choice
  options:
    - "No — local independence only requires independence in raw data, and high correlation is acceptable"
    - "No — local independence allows raw correlations as long as the correlation is fully explained by the latent ability θ; but if a passage-specific factor drives additional correlation beyond θ, local independence IS violated"
    - "Yes — local independence requires all items to be uncorrelated in raw data, and high correlations always violate it"
    - "Yes — items sharing content always violate local independence regardless of θ"
  answer: 1
  explanation: "Local independence is a *conditional* statement: given θ, item responses must be independent. Raw (marginal) correlations between items are expected and acceptable — they arise because people with higher θ tend to get multiple items right. The violation occurs when knowing one item's response gives extra information about another *above and beyond* what θ already tells you. A shared reading passage creates a passage-specific skill component that adds correlation beyond θ, violating local independence. Option C is the most common misconception — it confuses unconditional correlation with conditional dependence."

- question: "What is the central practical payoff of IRT's stronger assumptions compared to classical test theory?"
  type: multiple-choice
  options:
    - "IRT produces higher reliability coefficients than CTT for the same test"
    - "IRT item difficulty and discrimination parameters are invariant across samples, and ability estimates are invariant across which items are used"
    - "IRT eliminates the need for large sample sizes when calibrating tests"
    - "IRT automatically detects and corrects for test bias without additional analysis"
  answer: 1
  explanation: "Parameter invariance is the key payoff that motivates IRT's stronger assumptions. In CTT, item statistics (difficulty, discrimination) change when you change the sample or the test. In IRT, item parameters estimated in one sample apply to another (assuming the assumptions hold), and a person's ability estimate is the same whether estimated from easy items, hard items, or a mix. This invariance is what enables computerized adaptive testing, item banking, and test equating — applications that CTT cannot support because its statistics are test- and sample-dependent."

- question: "Local independence in IRT means that item responses must be uncorrelated in the raw data — items measuring the same construct should show near-zero correlations."
  type: true-false
  answer: false
  explanation: "Local independence is a conditional independence assumption, not an unconditional one. It states that P(X_i, X_j | θ) = P(X_i | θ) × P(X_j | θ): given a person's ability level θ, knowing their answer to one item provides no additional information about their answer to another. Items measuring the same construct will naturally be correlated in raw data — people with higher ability tend to get more items right. That raw correlation is entirely expected. Local independence is violated only when correlation remains even after conditioning on θ, as when items share a stimulus (passage, figure) that creates a local ability cluster beyond the common trait."

- question: "Under IRT assumptions, an item's difficulty parameter estimated from one sample of test-takers can be applied to a different population without re-estimation."
  type: true-false
  answer: true
  explanation: "This is the principle of parameter invariance — the defining advantage of IRT over classical test theory. In CTT, item difficulty is defined as the proportion of the sample that answered correctly, which changes whenever the sample changes. In IRT, item difficulty is the value of θ at which a person has a 50% probability of a correct response (for the 1PL model), which is a property of the item itself, independent of who was tested. When IRT assumptions (unidimensionality, local independence, monotone IRF) hold, the same item parameters apply across groups, enabling applications like test equating and item banking."

- question: "Explain why unidimensionality is the most fundamental assumption of IRT, and what 'approximate' unidimensionality means in practice."
  type: short-answer
  answer: "Unidimensionality means all items measure a single underlying latent trait θ — one common factor accounts for all covariation among item responses. It is the most fundamental assumption because the IRT model is built around a single ability parameter; if responses are driven by multiple distinct abilities, the single-θ model is misspecified and parameter estimates lose their meaning. In practice, perfect unidimensionality is never achieved — most tests have a dominant factor with minor secondary ones (e.g., a math test may also require reading skill). 'Approximate' unidimensionality means the secondary factors are small enough that the dominant factor captures the bulk of variance; IRT is empirically robust to this. It breaks down when secondary factors are substantial, which is why confirmatory factor analysis is run before fitting IRT models."
  explanation: "The reason this matters practically is that violations of unidimensionality produce biased ability estimates and misleading item parameters. For example, if a science test has two equally strong factors (quantitative reasoning and verbal comprehension), lumping them into one θ produces estimates that conflate two real abilities. Students strong in one but not the other will have unstable estimates depending on item sampling. The practical standard is to check factor structure, confirm there is a clearly dominant first factor, and note the proportion of variance explained before proceeding with IRT."
```

## Explainer

Classical test theory (CTT), which you have already studied, treats a test as a whole — every statistic (reliability, item difficulty, item discrimination) is computed relative to the specific sample and the specific test. Swap the sample, and item statistics change. Shorten the test, and reliability estimates change. IRT was developed to escape this sample-and-test dependency, but doing so requires stronger assumptions about the structure of the data. Understanding those assumptions is not optional overhead — it is the key to understanding why IRT works when it works, and why it fails when it fails.

The first and most fundamental assumption is **unidimensionality**: all items in the test are measuring a single underlying latent ability or trait, denoted θ. This does not mean items must be identical — a math test can have geometry and algebra items that differ in content — but it does mean that one common factor accounts for all the covariation among responses. In practice, perfect unidimensionality is never achieved; most tests have dominant factors with minor secondary ones. The working standard is that IRT is robust to minor multidimensionality but breaks down when secondary factors are substantial. Confirmatory factor analysis and parallel analysis are the standard tools for evaluating this assumption before fitting IRT models.

The second assumption is **local independence**: given a person's true ability level θ, knowing their response to one item provides no additional information about their response to any other item. This is the conditional independence assumption from your probability prerequisites — mathematically, P(X_i, X_j | θ) = P(X_i | θ) × P(X_j | θ). Local independence is not the same as saying items are uncorrelated in raw data; highly correlated items can still satisfy local independence if the correlation is fully explained by the shared latent ability. Local independence is violated, for example, when two items share a reading passage, so that reading skill for that passage creates an item-cluster effect beyond general ability. Violations inflate item information and produce artificially high reliability estimates.

The third assumption is a **monotone item response function**: higher ability must always be associated with a higher (or equal) probability of correct response. No IRT model tolerates items where very high-ability people are *less* likely to answer correctly than moderate-ability people (which would indicate item flaws like implausible distractors that trap sophisticated test-takers). Together, these three assumptions define the measurement model that IRT requires. When they hold, IRT delivers **parameter invariance** — the great payoff that item difficulty parameters estimated in one sample apply to others, and ability parameters estimated from one set of items apply when different items are used. This invariance is what enables item banking, CAT, and test equating — applications that CTT cannot support.
