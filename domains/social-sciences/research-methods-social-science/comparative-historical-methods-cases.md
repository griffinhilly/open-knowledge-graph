---
id: comparative-historical-methods-cases
title: 'Comparative Historical Methods: Case Selection and Process Tracing'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-from-questions-to-methods
  type: hard
- id: conditional-probability
  type: soft
tags:
- comparative-historical
- case-selection
- process-tracing
stage: advanced
status: draft
---

# Comparative Historical Methods: Case Selection and Process Tracing

## Core Idea
Comparative historical research examines processes across time and cases to identify causal mechanisms. Case selection strategies isolate drivers of variation. Process tracing examines evidence about how causes produce outcomes. This approach suits questions about historical trajectories and institutional change.

## Explainer

You already know from research design that the method must match the question. Comparative historical methods answer a distinctive kind of question: not "what is the average effect of X?" but "how did this particular configuration of factors produce this outcome, and does that explanation hold across other cases?" These are questions about causal mechanisms operating across time — why did welfare states emerge in some countries but not others, why do some revolutions succeed while others fail? Survey methods cannot answer them because the outcomes are rare, historically embedded, and shaped by sequences that average out in aggregation.

**Case selection** is the first critical choice. The goal is to select cases that maximize your inferential leverage. The **most-similar systems design** (MSSD) holds many factors constant across cases while varying the factor you suspect is causal — if two otherwise-identical countries diverged on the outcome, the variable that differs between them is a strong candidate for the cause. Conversely, the **most-different systems design** (MDSD) selects cases that differ on nearly everything except the outcome and one shared factor — if very different cases share the outcome and one common condition, that condition is implicated. Both strategies operationalize the logic of controlled comparison without a randomized experiment. A critical mistake is selecting cases *on the dependent variable* alone — comparing only successful revolutions tells you nothing about what distinguishes them from failed ones.

**Process tracing** is the second core tool, and it operates differently from cross-case comparison. Rather than comparing outcomes across cases, process tracing traces the causal chain *within* a single case, examining the step-by-step sequence of events and mechanisms connecting cause to outcome. Think of it as building a case — literally. You derive observable implications from your causal theory: if the mechanism is operating as you claim, what evidence should you find at each step? **Hoop tests** are necessary but not sufficient (failing eliminates the hypothesis, passing is expected); **smoking-gun tests** are sufficient but not necessary (passing confirms the hypothesis, but failing doesn't eliminate it). The strongest evidence satisfies both — a finding that only your theory predicts and that you actually observe. Your prerequisite in conditional probability helps formalize this: each piece of evidence updates the probability that your theory is correct (this is sometimes called **Bayesian process tracing**).

The power of comparative historical methods comes from combining both tools: cross-case comparison identifies which factors vary with the outcome; process tracing confirms that the mechanism actually operates within cases as the theory predicts. Neither alone is fully convincing. Comparison without process tracing risks spurious correlation; process tracing without comparison risks overfitting to a single case. Together, they produce the kind of mechanistic, historically grounded causal explanations that distinguish this approach from both statistical work (which identifies correlations at scale) and pure case-study narrative (which describes but often struggles to generalize).
