---
id: confirmation-theory-science
title: Confirmation and Evidence
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: problem-of-induction
  type: hard
- id: inductive-reasoning
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- bayesian-confirmation-science
- logical-positivism
tags:
- confirmation
- evidence
- support
- hypothesis
stage: expert
status: validated
---

# Confirmation and Evidence

## Core Idea
Confirmation theory asks: When does evidence support or confirm a hypothesis? What makes one piece of evidence more confirmatory than another? Scientists intuitively assess evidence quality, but formalizing these judgments is philosophically challenging. Logical positivists sought deductive models, while modern approaches use probability theory and Bayesian inference to quantify how observation updates belief in hypotheses.

## Questions

```yaml
- question: "You observe a green apple. According to Bayesian confirmation theory, what is the relationship between this observation and the hypothesis 'All ravens are black'?"
  type: multiple-choice
  options:
    - "It does not confirm the hypothesis at all — only observations of ravens can confirm claims about ravens"
    - "It disconfirms the hypothesis, because the apple is irrelevant evidence"
    - "It confirms the hypothesis, but only infinitesimally, because almost all objects are non-black non-ravens"
    - "It confirms the hypothesis as strongly as observing a black raven, because they are logically equivalent"
  answer: 2
  explanation: "On the Bayesian account, E confirms H if P(H|E) > P(H). The green apple is a non-black non-raven, which satisfies the logically equivalent form of the hypothesis. So formally it does raise our credence in H — but only infinitesimally. The key Bayesian insight is that the degree of confirmation depends on how informative the evidence is: there are vastly more non-black things than ravens, so seeing one more non-black non-raven barely moves the needle. Observing a black raven, by contrast, is much more confirmatory because ravens are rare and the observation was therefore much more probable given H than given ¬H."

- question: "A scientist is testing whether a new drug reduces inflammation. Which observation provides stronger Bayesian confirmation for the hypothesis 'This drug reduces inflammation'?"
  type: multiple-choice
  options:
    - "A patient who did not take the drug and showed no change — this is consistent with the hypothesis"
    - "A patient who took the drug and showed reduced inflammation — this was more likely to occur if the hypothesis is true"
    - "Both observations confirm the hypothesis equally, since both are consistent with it"
    - "Neither observation confirms anything because consistency with a hypothesis is not evidence for it"
  answer: 1
  explanation: "Bayesian confirmation is not about consistency but about the likelihood ratio P(E|H)/P(E|¬H). A patient who took the drug and improved is highly likely given H and less likely given ¬H (where improvement is just random), so the likelihood ratio is large — strong confirmation. A patient who did not take the drug and showed no change is equally probable whether or not the drug works, so the likelihood ratio is near 1 — negligible confirmation. The Bayesian framework explains why 'consistent with the hypothesis' is not the same as 'confirms the hypothesis.'"

- question: "According to Bayesian confirmation theory, confirmation is a matter of degree rather than an all-or-nothing relation between an observation and a hypothesis."
  type: true-false
  answer: true
  explanation: "This is one of the most important conceptual contributions of Bayesian confirmation theory. Rather than asking 'does E confirm H?' (binary), Bayesian theory asks 'by how much does E raise the probability of H?' The answer depends on the prior probability of H and the likelihood ratio P(E|H)/P(E|¬H). The same observation can strongly confirm one hypothesis and weakly confirm another. This graduated picture resolves many apparent paradoxes — like why the green apple 'confirms' all ravens are black but in such a negligible way that it feels like no confirmation at all."

- question: "Hempel resolved the ravens paradox by arguing that the green apple definitely does not confirm 'All ravens are black,' because only objects in the relevant reference class (ravens) can confirm claims about that class."
  type: true-false
  answer: false
  explanation: "Hempel's actual response was the opposite: he accepted that the green apple does (weakly) confirm 'All ravens are black,' because it satisfies the logically equivalent formulation 'All non-black things are non-ravens.' Hempel argued that our intuition that the apple is irrelevant reflects a pragmatic point about where we expect evidence to come from, not a logical error. It was Hempel's acceptance of the paradoxical conclusion — not its rejection — that motivated philosophers to search for better accounts. The Bayesian approach, which came later, explains why the apple confirmation feels trivial without denying it."

- question: "Explain why the Bayesian account of confirmation handles the ravens paradox more satisfyingly than simply accepting that the green apple fully confirms 'All ravens are black.'"
  type: short-answer
  answer: "The Bayesian account distinguishes between whether something confirms a hypothesis and how much it does so. The green apple does technically confirm 'All ravens are black' — P(H|green apple) > P(H) — but only infinitesimally. This is because confirmation depends on the likelihood ratio P(E|H)/P(E|¬H), and since there are vastly more non-black non-raven objects than there are ravens, seeing one more green apple barely changes our credence in the hypothesis. Observing a black raven, by contrast, is far more informative because ravens are rare. The Bayesian framework explains why the apple confirmation is negligible without denying that it exists, which is more satisfying than simply saying 'it doesn't confirm at all.'"
  explanation: "The key move is making confirmation gradational. Hempel was stuck with a binary notion (confirms or doesn't confirm), which forced him to either accept the absurd-seeming conclusion that the apple fully confirms or reject it and lose logical consistency. Bayesian theory dissolves the dilemma: both the raven and the apple confirm, but to vastly different degrees, and the difference in degree corresponds exactly to our intuition that the raven observation is the relevant evidence."
```

## Explainer

From your study of Hume's problem of induction, you know that no finite set of observations logically entails a universal generalization. No number of observed black ravens proves "all ravens are black." But science clearly works by gathering evidence, and some evidence genuinely supports hypotheses more than others. Confirmation theory is the attempt to make this intuition precise: to give a formal account of when and how much an observation supports a hypothesis. The difficulty is that our intuitions about evidential support, when pressed, generate genuine paradoxes.

The most famous is Carl Hempel's **ravens paradox**. Consider the hypothesis H: "All ravens are black." Observing a black raven seems to confirm it. Now consider the logically equivalent statement H': "All non-black things are non-ravens." A green apple is a non-black non-raven — it satisfies H'. Since H and H' say exactly the same thing (they are logically equivalent), and the green apple confirms H', it must also confirm H. But this seems absurd: you can sit in your living room collecting green apples and thereby (trivially) confirm the hypothesis about ravens. Hempel's response was to bite the bullet and accept that the apple does weakly confirm H — the counterintuitiveness reflects a pragmatic point about where we expect evidence to come from, not a logical error. But this answer is unsatisfying.

The Bayesian approach offers a cleaner resolution. **Bayesian confirmation** defines "E confirms H" as: the probability of H given E is higher than the prior probability of H. Formally, E confirms H if P(H|E) > P(H), which is equivalent to saying that E is more probable given H than given ¬H: P(E|H) > P(E|¬H). On this account, the green apple does confirm "all ravens are black" — but only infinitesimally. Before seeing the apple, almost all physical objects were non-black non-ravens; seeing one more doesn't update H much at all. Observing a black raven, by contrast, provides significantly more confirmation because ravens are much rarer than non-black things, making the raven observation more informative. The Bayesian framework explains why the apple confirmation feels trivial without denying it.

What the Bayesian approach reveals is that **confirmation is gradational and context-sensitive** — it is not a binary on/off relation but a matter of degree, governed by prior probabilities and the likelihood ratio P(E|H)/P(E|¬H). Evidence is more confirmatory when it was more likely to occur if the hypothesis is true and less likely if the hypothesis is false. This connects directly to your understanding of inductive reasoning: induction is not a single monolithic rule but a probabilistic updating process, and its strength depends on the specific evidential situation. The apparent paradoxes of confirmation largely dissolve once we shift from seeking a simple logical relation between statement and evidence to thinking in terms of probability updating — which is why Bayesian confirmation theory is the foundation of the more advanced framework you'll study next.
