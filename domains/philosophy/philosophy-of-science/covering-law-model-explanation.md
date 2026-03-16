---
id: covering-law-model-explanation
title: The Covering Law Model
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: deductive-nomological-explanation
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: propositional-logic-introduction
  type: soft
builds-toward:
- causal-explanation-science
- explanatory-power-and-unification
tags:
- covering-law
- inductive-statistical
- explanation
- laws
stage: advanced
status: draft
---

# The Covering Law Model

## Core Idea
The covering law model extends the D-N model to include inductive-statistical explanations where the explanans makes the explanandum probable by subsuming it under statistical laws. This captures explanations in quantum mechanics, genetics, and social science using probabilistic laws rather than strict universals. However, high statistical correlation provides a covering law but intuitively fails to explain: a barometer's rise doesn't explain incoming storms even though both are covered by meteorological laws.

## Explainer

You already understand the **deductive-nomological (D-N) model**: an explanation is a valid deductive argument whose premises include at least one natural law, and whose conclusion is the phenomenon to be explained. The covering law model is the generalization of that framework. It says that all scientific explanation has a common logical structure: the phenomenon is *covered* — subsumed — by one or more laws, and citing those laws is what makes something an explanation rather than a mere description. The D-N model is the deductive special case; the covering law model also includes the **inductive-statistical (I-S) model**, which handles probabilistic laws.

The I-S extension matters because much real science is irreducibly statistical. In quantum mechanics, a law might say that a radioactive atom has a 50% chance of decaying in a given interval — not that it *will* decay. In epidemiology, smoking raises the probability of lung cancer without guaranteeing it. In Mendelian genetics, a heterozygous parent passes a dominant allele to each offspring with probability 1/2. The I-S model says these probabilistic laws still explain outcomes by raising their probability. The key requirement is **high probability**: the law-plus-conditions must make the event very likely. An explanation of why this patient recovered from strep throat by citing that penicillin cures strep infections in 90% of cases is a genuine explanation precisely because the probability is high — you've been covered by a strong statistical law.

This generates an immediate problem: **the reference class problem**. Whether an event has high probability depends entirely on how you describe it. The same patient might also belong to a subclass — say, patients with a particular allergy — where the recovery rate is much lower. There is no principled way to choose the "right" reference class without already knowing what the explanation should look like. This threatened to make I-S explanations circular or indeterminate, and prompted Hempel to introduce the **requirement of maximal specificity**: use the most specific reference class for which you have relevant information.

The deeper challenge is **the asymmetry and irrelevance problems**. Suppose a law says that the height of a flagpole's shadow correlates perfectly with the pole's height plus the sun's angle. You can deduce the pole's height from the shadow length and the angle — but that doesn't *explain* the pole's height; it's the other way around. The covering law model permits explanations to run in logically valid but causally backward directions. Similarly, the barometer case: rising barometric pressure and approaching storms are both covered by the same meteorological laws, but the barometer's reading does not explain the storm. These cases suggest that explanation requires something the covering law model omits: **asymmetric causal structure**. This failure motivates rival accounts — causal-mechanical explanation and unificationist explanation — which build causation or explanatory power directly into the analysis.
