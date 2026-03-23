---
id: bayesian-confirmation-and-evidence
title: Bayesian Confirmation Theory
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: bayesian-epistemology
  type: hard
- id: probabilistic-reasoning
  type: soft
builds-toward:
- theoretical-virtues-in-theory-choice
tags:
- confirmation
- bayesian
- evidence
stage: expert
status: validated
---

# Bayesian Confirmation Theory

## Core Idea
Bayesian confirmation theory treats evidential support probabilistically: evidence confirms a hypothesis when observing it raises the hypothesis's probability. This formalizes the intuitive idea that evidence must be more likely given the theory than it would be otherwise, providing a quantitative measure of confirmation.

## How It's Best Learned
Learn Bayes' theorem and apply it to simple scientific examples. Study how it handles problems like old evidence and the ravens paradox that troubled earlier confirmation theories.

## Questions

```yaml
- question: "A geologist observes a rock formation consistent with Hypothesis A (continental drift) and Hypothesis B (fixed continents). The observation has probability 0.90 given A and 0.80 given B. Does this observation strongly confirm Hypothesis A over B?"
  type: multiple-choice
  options:
    - "Yes — the observation is more likely given A (0.90) than given B (0.80), confirming A substantially"
    - "No — the observation confirms A only if P(observation|A) = 1; anything less counts as weak evidence"
    - "No — the likelihood ratio is only 0.90/0.80 = 1.125, providing only weak relative confirmation for A over B"
    - "Whether the observation confirms A depends solely on whether P(A) > 0.5 before the observation"
  answer: 2
  explanation: "Bayesian confirmation is comparative: evidence confirms A over B to the extent that A predicts it better than B does, measured by the likelihood ratio P(E|A)/P(E|B) = 0.90/0.80 = 1.125. A ratio barely above 1 means A is only marginally a better predictor of this observation than B — both hypotheses predict it quite well. This is the subtlety of Bayesian evidence: it is not just 'does the hypothesis predict this?' but 'does it predict it substantially better than the alternative?' Option D confuses prior probability with the logic of evidential updating."

- question: "According to Bayesian confirmation theory, evidence E confirms hypothesis H when..."
  type: multiple-choice
  options:
    - "E is logically entailed by H (i.e., H → E is a valid implication)"
    - "Observing E raises the probability of H: P(H|E) > P(H)"
    - "E could not have occurred if H were false: P(E|¬H) = 0"
    - "The scientist predicted E before the observation was made"
  answer: 1
  explanation: "The Bayesian definition is probabilistic: E confirms H if and only if P(H|E) > P(H) — the posterior probability exceeds the prior. This is broader than logical entailment (option A) and different from conclusive evidence (option C, which requires P(E|¬H) = 0 — decisive disconfirmation of alternatives). The framework accommodates partial, graded confirmation: E can raise H's probability a little or a lot. Option D (prior prediction) has nothing to do with the formal definition — surprising evidence often confirms more strongly than expected evidence."

- question: "According to Bayesian confirmation theory, observing a green apple technically provides some confirmation for the hypothesis 'all ravens are black.'"
  type: true-false
  answer: true
  explanation: "This is the Bayesian resolution of Hempel's ravens paradox. 'All ravens are black' is logically equivalent to 'All non-black things are non-ravens.' A green apple is a non-black non-raven, consistent with this equivalent statement. Bayes' theorem confirms this technically: a green apple very slightly raises P(all ravens are black) because it eliminates one non-black object from the sample space without revealing a non-black raven. The Bayesian response is that this confirmation is real but negligible — the sample space of non-black things is enormous, so each instance provides only infinitesimal update."

- question: "Evidence confirms a hypothesis independently of competing hypotheses — the degree of confirmation depends only on the two-place relationship between E and H."
  type: true-false
  answer: false
  explanation: "Bayesian confirmation is inherently comparative. P(H|E) = P(E|H)P(H)/P(E), and P(E) = P(E|H)P(H) + P(E|¬H)P(¬H) — the denominator explicitly depends on how well alternatives to H also predict E. A hypothesis that uniquely predicts E gains massive confirmation when E is observed; a hypothesis that predicts E no better than its competitors gains almost none. Evidence is always evidence relative to alternatives: 'data confirms theory' is always implicitly a comparison."

- question: "Why does a single counterexample decisively refute a universal hypothesis ('all ravens are black'), while many confirming instances raise its probability only gradually?"
  type: short-answer
  answer: "A universal hypothesis assigns probability zero to any counterexample — 'all ravens are black' strictly rules out white ravens, so P(white raven observed | all ravens are black) = 0. When a white raven is observed, Bayes' theorem gives P(H|E) = 0 × P(H)/P(E) = 0, regardless of the prior. Confirming instances (black ravens), by contrast, are quite common even under alternative hypotheses, so the likelihood ratio P(E|H)/P(E|¬H) is only slightly above 1 for each black raven, producing tiny probability increments. The asymmetry is structural: a universal claim creates exactly one condition that destroys it completely, while confirmation requires ruling out every possible counterexample."
  explanation: "This asymmetry has deep implications for scientific methodology. Popper's falsificationism is the philosophical response: since confirmation accumulates slowly while falsification strikes decisively, focusing on bold predictions that could refute a theory is epistemically efficient. The Bayesian framework explains *why* this asymmetry exists — it follows directly from the mathematics of zero likelihood under a universal claim."
```

## Explainer

You already know Bayes' theorem from your study of Bayesian epistemology: P(H|E) = P(E|H) × P(H) / P(E). Bayesian confirmation theory applies this machinery to the philosophy of science. The central claim is simple: **evidence E confirms hypothesis H** if observing E raises the probability of H — formally, if P(H|E) > P(H). Evidence that leaves H's probability unchanged is irrelevant, and evidence that lowers H's probability disconfirms it. This gives us a quantitative framework for the qualitative intuition that data should update our confidence in theories.

The key ratio that drives confirmation is P(E|H) / P(E|¬H) — the **likelihood ratio**. Evidence confirms H strongly when it is much more likely if H is true than if H is false. If you observe a raven and it is black, this confirms the hypothesis "all ravens are black" — but only weakly, because black ravens are common anyway. If you observe a raven and it is *white*, this strongly disconfirms the hypothesis, because the hypothesis makes white ravens strictly impossible while the alternative does not. The asymmetry between confirmation and disconfirmation here reflects a real structural feature: a single counterexample defeats a universal claim decisively, while confirming instances raise the probability by only a small amount.

Bayesian confirmation handles several puzzles that troubled earlier theories. The **ravens paradox** (Hempel's paradox): "All ravens are black" is logically equivalent to "All non-black things are non-ravens," which seems to be confirmed by observing a green apple. Bayesian analysis shows this is technically correct — a green apple does raise the probability of "all ravens are black" — but only infinitesimally, because the sample space of non-black things is enormous. The Bayesian framework dissolves the paradox by showing the confirmation is real but negligible. The **problem of old evidence** is harder: if you already know E with certainty (P(E) = 1), then E cannot raise the probability of H because the math yields P(H|E) = P(H). Bayesians address this by imagining a counterfactual prior probability before learning E, though this remains contested.

The philosophical significance of Bayesian confirmation is that it grounds scientific rationality in the mathematics of probability. Scientific reasoning is not a mysterious faculty — it is Bayes' theorem applied to theories and evidence. Each observation updates your credences by a definite amount. Theories with high prior probability (from simplicity, coherence with known science, etc.) require less confirming evidence; theories that make bold predictions require that those predictions come true to earn high probability. The framework also clarifies what it means to have evidence *for* a theory at all: evidence is only evidence relative to alternatives. Data that confirms one hypothesis always implicitly compares it to competing hypotheses through the denominator P(E).
