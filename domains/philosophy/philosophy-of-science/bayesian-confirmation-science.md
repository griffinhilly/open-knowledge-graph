---
id: bayesian-confirmation-science
title: "Bayesian Approaches to Confirmation"
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: bayesian-epistemology
  type: hard
- id: confirmation-theory-science
  type: hard
- id: probabilistic-reasoning
  type: hard
- id: probabilistic-computation
  type: soft
- id: bayesian-confirmation-and-evidence
  type: soft
builds-toward:
- scientific-realism
- causal-explanation-science
tags:
- bayesian
- probability
- likelihood
- posterior
stage: expert
status: validated
---

# Bayesian Approaches to Confirmation

## Core Idea
Bayesian confirmation theory applies Bayes' theorem to understand how evidence confirms or disconfirms hypotheses. Your degree of belief in a hypothesis should be updated by evidence using P(H|E) = P(E|H) × P(H) / P(E). Evidence confirms H if it is more likely given H than given its negation. Bayesian approaches provide a mathematically rigorous account of rational belief revision and offer responses to problems of induction and underdetermination.

## Questions

```yaml
- question: "A researcher designs an experiment whose result E is almost equally likely whether hypothesis H is true or false — P(E|H) ≈ P(E|¬H) ≈ 0.9. She observes E. What happens to her credence in H by Bayesian lights?"
  type: multiple-choice
  options:
    - "Her credence rises substantially — she observed evidence that the hypothesis predicts"
    - "Her credence barely changes — the Bayes factor P(E|H)/P(E|¬H) ≈ 1 means E is nearly neutral"
    - "Her credence drops — if ¬H also predicts E, that undermines H"
    - "She must assign H a credence of exactly 0.9 to match the likelihood"
  answer: 1
  explanation: "The strength of evidence is determined by the Bayes factor P(E|H)/P(E|¬H), not by P(E|H) alone. When both the hypothesis and its negation predict E nearly equally well, observing E tells you almost nothing about which is true — the ratio is close to 1 and the posterior barely shifts from the prior. This is why the common intuition 'the experiment confirmed the hypothesis because the prediction came true' can be misleading: what matters is whether the hypothesis predicted E *better than the alternatives*, not just whether it predicted E at all. Trivially predictable results are weak evidence."

- question: "You observe a green apple. According to Bayesian confirmation theory, does this observation confirm the hypothesis 'All ravens are black'?"
  type: multiple-choice
  options:
    - "No — observations of non-ravens are logically irrelevant to hypotheses about ravens"
    - "Yes, but only infinitesimally — the Bayes factor is barely above 1 because a green apple is almost equally likely whether or not all ravens are black"
    - "Yes, and as strongly as observing a black raven — both are positive instances of the logically equivalent contrapositive"
    - "No — confirmation only counts when you observe a direct instance of the subject class"
  answer: 1
  explanation: "Bayesianism dissolves the raven paradox by treating confirmation as a matter of degree, not a binary yes/no. Logically, 'All ravens are black' is equivalent to 'All non-black things are non-ravens,' so a green apple (non-black, non-raven) is a positive instance. Does it confirm? Technically yes, but the Bayes factor is barely above 1 — knowing you've seen a green apple is almost equally likely whether all ravens are black or not, because the world contains overwhelmingly more non-ravens than ravens. The paradox arose from a binary notion of confirmation; the quantitative Bayesian approach shows the green apple confirms only negligibly while a black raven confirms substantially."

- question: "According to Bayesian confirmation theory, evidence E confirms hypothesis H if and only if observing E raises your credence in H above its prior value."
  type: true-false
  answer: true
  explanation: "This is the Bayesian definition of confirmation: E confirms H iff P(H|E) > P(H). It is elegant because it is both mathematically precise and intuitively appealing — learning E is good news for H if and only if E makes H more likely than it was before. The definition also has a natural companion: E disconfirms H iff P(H|E) < P(H), and E is neutral iff P(H|E) = P(H). The quantitative framework then lets us ask how much confirmation E provides, answering with the Bayes factor rather than just yes/no."

- question: "If two scientists begin with very different prior probabilities for the same hypothesis, Bayesian updating cannot bring their posteriors into agreement regardless of how much evidence accumulates."
  type: true-false
  answer: false
  explanation: "Under mild conditions (both scientists assign non-zero prior probability to the true hypothesis and share the same evidence), Bayesian agents will converge to the same posterior as evidence accumulates, regardless of their starting priors. This is the 'washing out of priors' result. The evidence eventually overwhelms any finite prior — only a prior of exactly 0 (assigning zero probability to a hypothesis) prevents convergence, because updating a zero prior produces a zero posterior no matter what. This convergence property is one of Bayesianism's strongest responses to the worry about subjective priors in science."

- question: "Why are trivially predictable experimental results weak evidence for a hypothesis, from a Bayesian perspective? Use the concept of the Bayes factor in your explanation."
  type: short-answer
  answer: "The strength of evidence E for hypothesis H is measured by the Bayes factor: P(E|H)/P(E|¬H) — the ratio of how likely E is if H is true to how likely E is if H is false. If E is trivially predictable, both H and ¬H (and every other competitor) assign it high probability, so P(E|H) ≈ P(E|¬H), and the Bayes factor ≈ 1. A factor of 1 means E does not shift the odds between H and its competitors at all. Evidence confirms H strongly only when H predicts E substantially better than its competitors — when P(E|H) is much larger than P(E|¬H). The discriminating power of evidence comes not from whether H predicts E, but from whether H predicts E *specifically*, in a way that other hypotheses do not."
  explanation: "A classic example: every hypothesis predicts that 'the sun will rise tomorrow,' so observing the sunrise is not evidence for or against any particular hypothesis. By contrast, a specific quantitative prediction that comes true — and that a competing hypothesis would not have made — has a high Bayes factor and genuinely discriminates between theories."
```

## Explainer

From your study of **Bayesian epistemology**, you know that beliefs can be represented as degrees of credence — real numbers between 0 and 1 — and that rational agents update them by conditionalization: when you learn E, your new credence in H becomes P(H|E), your prior conditional probability. Bayesian confirmation theory applies this framework specifically to the scientific context, asking: when does evidence *confirm* a hypothesis, and by how much? The answer is elegantly simple: evidence E **confirms** hypothesis H if and only if P(H|E) > P(H) — that is, learning E raises your credence in H above where it started.

Expanding via Bayes' theorem — P(H|E) = P(E|H) × P(H) / P(E) — makes the structure visible. The key term is **P(E|H)**, the **likelihood**: how probable would the evidence be if H were true? A high likelihood means the hypothesis predicts the evidence well, so observing it strongly supports H. Compare this to **P(E|¬H)**, the probability of the evidence if H is false. The ratio P(E|H)/P(E|¬H) is the **Bayes factor**, measuring the evidence's force. If a hypothesis predicts the evidence far better than its competitors, the evidence is strong confirmation. If both H and ¬H predict E equally, E is neutral — this is why trivially predictable results are weak evidence.

This framework handles several problems that troubled earlier confirmation theories. The **raven paradox** (from your confirmation theory study) noted that classical accounts made it mysterious why observing a green apple could confirm "all ravens are black." Bayesianism dissolves this: observing a non-black non-raven does confirm the hypothesis, but only infinitesimally — because such observations are almost equally likely whether the hypothesis is true or false. The Bayes factor is barely above 1. The paradox arose from treating confirmation as binary; Bayesianism restores the quantitative difference between weak and strong confirmation.

The most contested element is the **prior**: P(H) before any evidence. Bayesians are divided between **objectivists**, who think there are uniquely rational priors determined by logic or symmetry, and **subjectivists**, who accept that priors vary among agents and is acceptable so long as updating is rational. The subjectivist position raises a worry: if two scientists begin with very different priors, will they ever converge on the same hypothesis? The good news is that, under mild conditions, Bayesian agents who share evidence will eventually converge regardless of starting priors — evidence eventually overwhelms the prior. This makes Bayesianism a strong response to **underdetermination**: even if data alone cannot force a unique theory, iterative Bayesian updating across a scientific community tends toward agreement.

The framework also illuminates **old evidence** problems. If E was observed before H was proposed, then P(E) ≈ 1, making the update trivial — E cannot raise P(H) because E is already certain. Yet intuitively, explaining long-known phenomena is genuine confirmation (Einstein's general relativity explaining Mercury's perihelion advance). Addressing this requires treating confirmation as what P(E|H) tells us relative to the theoretical alternatives available, not just the raw update. These subtleties show that while Bayesianism gives the most mathematically precise theory of confirmation in science, applying it to real scientific practice requires careful handling of priors, likelihoods, and the background context in which evidence is acquired.
