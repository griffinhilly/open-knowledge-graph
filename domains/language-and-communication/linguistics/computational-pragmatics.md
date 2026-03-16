---
id: computational-pragmatics
title: Computational Models of Pragmatic Reasoning
domain: language-and-communication
course: linguistics
prerequisites:
- id: linguistic-pragmatics
  type: hard
- id: conversational-implicature
  type: hard
builds-toward:
- syntax-semantics-interface-formal
tags:
- pragmatics
- implicature
- reasoning
- computation
stage: formal-systems
status: draft
---

# Computational Models of Pragmatic Reasoning

## Core Idea
Computational pragmatics formalizes how context modifies meaning. Implicatures are derived through algorithms reasoning about conversational maxims and mutual knowledge. Speakers navigate trade-offs between clarity and efficiency; listeners infer intended meanings beyond literal truth conditions. Formal models represent belief states and use fixed-point reasoning to derive speaker meanings.

## Explainer

You already know, from your study of pragmatics and conversational implicature, that speakers routinely communicate more than they say. When someone asks "Can you pass the salt?" and you hand over the salt shaker, you have correctly derived a request from a grammatical question about capability. Grice's maxims explain *why* this inference is licensed — cooperative speakers say what they mean efficiently and relevantly — but describing the inference in narrative terms is not the same as formally specifying the algorithm that produces it. Computational pragmatics asks: can we write down the exact mechanism?

The most influential formal framework is the **Rational Speech Act (RSA) model**, which treats communication as a recursive reasoning problem. A pragmatic listener reasons about what a rational speaker would say in order to convey a given meaning, and a pragmatic speaker reasons about what a rational listener would infer from a given utterance. The reasoning iterates: literal listener → pragmatic speaker → pragmatic listener → … This **fixed-point reasoning** produces implicatures as emergent properties of the recursion rather than hard-coded rules. For example, the scalar implicature from "some" to "not all" arises because a cooperative speaker who knew "all" would have said "all" — so "some" pragmatically implies the stronger alternative was unavailable.

The formal machinery requires representing **belief states** — probability distributions over possible worlds — and updating them via Bayesian inference. A listener hears an utterance and updates their beliefs about what the speaker intended; a speaker selects utterances to maximize the probability that the listener will arrive at the intended interpretation. This framework makes explicit the trade-off between **informativeness** (say things that rule out alternatives) and **efficiency** (avoid unnecessary length and complexity). Speakers who choose less informative expressions when more informative ones are available are interpreted as implicating that the stronger claim doesn't hold.

The payoff of formalization is that the same machinery generalizes across phenomena. Scalar implicatures ("some" → "not all"), reference resolution (choosing between "the dog" and "it"), and M-implicatures (the marked form implies a marked situation) all reduce to the same underlying inference mechanism: rational agents reasoning about each other's reasoning. This unified account is both an empirical claim — that human pragmatic inference has this recursive structure — and a practical tool, since the RSA model and its descendants are now widely used in natural language processing to build systems that interpret utterances in context rather than just parsing their literal content.
