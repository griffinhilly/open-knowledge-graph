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
status: validated
---

# Computational Models of Pragmatic Reasoning

## Core Idea
Computational pragmatics formalizes how context modifies meaning. Implicatures are derived through algorithms reasoning about conversational maxims and mutual knowledge. Speakers navigate trade-offs between clarity and efficiency; listeners infer intended meanings beyond literal truth conditions. Formal models represent belief states and use fixed-point reasoning to derive speaker meanings.

## Questions

```yaml
- question: "A speaker says 'Some students passed the exam.' A listener derives the implicature 'Not all students passed.' Under the RSA model, how does this implicature arise?"
  type: multiple-choice
  options:
    - "The word 'some' is defined to mean 'some but not all' in the lexicon, so the implicature is semantic, not pragmatic"
    - "The listener applies a maxim requiring speakers to say what they mean, ruling out 'some' as a synonym for 'all'"
    - "A cooperative speaker who knew 'all' passed would have said 'all'; since they said 'some,' the listener infers 'all' was unavailable — i.e., not all passed"
    - "The listener uses prior knowledge about typical exam outcomes to update their beliefs"
  answer: 2
  explanation: "In RSA, the pragmatic listener reasons about speaker behavior: a rational, cooperative speaker always chooses the most informative utterance consistent with what they know. 'All' is stronger and more informative than 'some.' If the speaker knew 'all' was true, they would have said 'all.' Since they said 'some,' the listener infers the stronger alternative was unavailable — not all passed. This scalar implicature is not a lexical rule (option A) but an emergent property of reasoning about what a rational speaker would do. Gricean maxims (option B) explain the inference narratively but don't formalize the mechanism RSA provides."

- question: "What is the most important difference between explaining implicature via Grice's conversational maxims versus the Rational Speech Act (RSA) model?"
  type: multiple-choice
  options:
    - "The RSA model only applies to scalar implicatures; Grice's maxims apply to all pragmatic phenomena"
    - "Grice's maxims describe the inference narratively; RSA specifies a formal recursive algorithm that derives implicatures as outputs of a computable process"
    - "Grice's maxims have been empirically validated; RSA is purely theoretical with no empirical applications"
    - "RSA requires speakers to be perfectly rational at all times; Grice's maxims allow for irrational speakers"
  answer: 1
  explanation: "Grice's maxims (be informative, be truthful, be relevant, be clear) provide a narrative explanation: listeners derive implicatures by reasoning about why a cooperative speaker would say what they said. This is descriptively accurate but not formally specified — it doesn't define an algorithm you could implement or make quantitative predictions with. RSA formalizes Gricean intuitions as recursive probabilistic reasoning: literal listener → pragmatic speaker → pragmatic listener, iterated. Implicatures emerge as outputs. The key upgrade is computability and precision: RSA makes testable quantitative predictions and is used in NLP systems. Option A is wrong — RSA generalizes beyond scalar implicatures."

- question: "In the RSA model, a pragmatic listener does not just interpret an utterance literally — they reason about what a rational speaker would have said in order to infer the speaker's intended meaning."
  type: true-false
  answer: true
  explanation: "This is the defining feature of the RSA framework. A literal listener simply evaluates whether an utterance is true in the current state. A pragmatic listener does something more complex: they model speaker behavior — 'what would a rational, cooperative speaker say if they intended to communicate X?' — and invert that reasoning to infer X from what the speaker actually said. This recursive structure, where the listener models the speaker who models the listener, generates pragmatic inferences beyond literal meaning."

- question: "The Rational Speech Act model and Grice's conversational maxims are equivalent explanations of implicature — they make the same predictions and differ only in degree of formalism."
  type: true-false
  answer: false
  explanation: "While RSA is inspired by Gricean intuitions, the two frameworks are not equivalent. RSA makes quantitative, graded predictions about the probability of different interpretations; Gricean accounts give categorical judgments. RSA can be implemented computationally and makes predictions that Gricean accounts leave underspecified. RSA also handles phenomena like M-implicatures and reference resolution through the same unified mechanism, whereas Gricean accounts often require separate auxiliary principles for each phenomenon. The two converge on many basic cases but diverge in predictive structure and explanatory power."

- question: "What does it mean to say that scalar implicatures 'emerge' from recursive reasoning in the RSA model, rather than being hard-coded pragmatic rules?"
  type: short-answer
  answer: "Hard-coded rules would say: 'when you hear some, infer not all' — a lookup in a fixed list. Emergence means no such rule exists in the model; the 'not all' inference falls out of the recursive reasoning structure itself. A literal listener knows 'some' is compatible with 'all.' A pragmatic speaker choosing between 'some' and 'all' would pick 'all' if they knew it was true, because it is more informative. A pragmatic listener, reasoning about this speaker behavior, infers that if the speaker said 'some,' 'all' must not have been available. The implicature is the output of this reasoning chain, not a stored rule."
  explanation: "This emergence property matters because the same recursive mechanism — reasoning about rational speaker behavior — generates multiple different pragmatic inferences without needing separate rules for each. Scalar implicatures, reference disambiguation, M-implicatures, and others all reduce to the same underlying computation. This unification is both theoretically elegant and practically powerful: a system implementing RSA gets a broad range of pragmatic inference, not just isolated hard-coded cases, which is why RSA descendants are now used in natural language processing systems."
```

## Explainer

You already know, from your study of pragmatics and conversational implicature, that speakers routinely communicate more than they say. When someone asks "Can you pass the salt?" and you hand over the salt shaker, you have correctly derived a request from a grammatical question about capability. Grice's maxims explain *why* this inference is licensed — cooperative speakers say what they mean efficiently and relevantly — but describing the inference in narrative terms is not the same as formally specifying the algorithm that produces it. Computational pragmatics asks: can we write down the exact mechanism?

The most influential formal framework is the **Rational Speech Act (RSA) model**, which treats communication as a recursive reasoning problem. A pragmatic listener reasons about what a rational speaker would say in order to convey a given meaning, and a pragmatic speaker reasons about what a rational listener would infer from a given utterance. The reasoning iterates: literal listener → pragmatic speaker → pragmatic listener → … This **fixed-point reasoning** produces implicatures as emergent properties of the recursion rather than hard-coded rules. For example, the scalar implicature from "some" to "not all" arises because a cooperative speaker who knew "all" would have said "all" — so "some" pragmatically implies the stronger alternative was unavailable.

The formal machinery requires representing **belief states** — probability distributions over possible worlds — and updating them via Bayesian inference. A listener hears an utterance and updates their beliefs about what the speaker intended; a speaker selects utterances to maximize the probability that the listener will arrive at the intended interpretation. This framework makes explicit the trade-off between **informativeness** (say things that rule out alternatives) and **efficiency** (avoid unnecessary length and complexity). Speakers who choose less informative expressions when more informative ones are available are interpreted as implicating that the stronger claim doesn't hold.

The payoff of formalization is that the same machinery generalizes across phenomena. Scalar implicatures ("some" → "not all"), reference resolution (choosing between "the dog" and "it"), and M-implicatures (the marked form implies a marked situation) all reduce to the same underlying inference mechanism: rational agents reasoning about each other's reasoning. This unified account is both an empirical claim — that human pragmatic inference has this recursive structure — and a practical tool, since the RSA model and its descendants are now widely used in natural language processing to build systems that interpret utterances in context rather than just parsing their literal content.
