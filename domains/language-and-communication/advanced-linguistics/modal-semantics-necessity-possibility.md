---
id: modal-semantics-necessity-possibility
title: 'Modal Semantics: Necessity and Possibility'
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: modal-logic-intro
  type: hard
tags:
- semantics
- modality
- possible-worlds
stage: expert
status: validated
---

# Modal Semantics: Necessity and Possibility

## Core Idea
Modal expressions are analyzed using possible-worlds semantics: 'necessarily P' is true if P holds in all possible worlds; 'possibly P' if P holds in some possible world. This framework elegantly explains how modals interact with negation and quantifiers ('It's not necessary that everyone attends' differs in truth conditions from 'Everyone must not attend'), resolving ambiguities through formal structure.

## Questions

```yaml
- question: "A sentence is parsed as ¬□(∀x. attends(x)). Which English sentence does this represent?"
  type: multiple-choice
  options:
    - "Everyone must not attend"
    - "It's not necessary that everyone attends"
    - "It's not possible for anyone to attend"
    - "No one is required to attend"
  answer: 1
  explanation: "¬□(∀x. attends(x)) has negation taking wide scope over necessity, which scopes over the universal quantifier. This reads: it is not the case that (necessarily (everyone attends)) — i.e., 'It's not necessary that everyone attends.' Option A would be ∀x.□(¬attends(x)) — a very different truth condition where each person individually is forbidden to attend. Getting scope interactions right is the main payoff of doing modal semantics formally."

- question: "According to Kratzer's restrictor analysis, what is the role of the 'ordering source' in modal semantics?"
  type: multiple-choice
  options:
    - "It restricts which possible worlds are in the modal base"
    - "It ranks worlds within the modal base by a standard of normality or ideality"
    - "It determines which modal flavor (epistemic vs. deontic) the modal expresses"
    - "It specifies the worlds in which the embedded proposition must hold"
  answer: 1
  explanation: "In Kratzer's two-parameter analysis, the modal base restricts the relevant worlds (e.g., to what is known, or what the rules require), while the ordering source ranks those worlds by how closely they approximate some ideal. This two-parameter structure explains why modals can behave differently across contexts even when the modal base is the same — and why sentences like 'It might be that you must leave' are coherent (the two parameters can be set independently)."

- question: "The sentence 'She should be home — her lights are on' and 'You should report income over $50,000' both use 'is expected to' to express the same type of modal necessity."
  type: true-false
  answer: false
  explanation: "The first 'must' is epistemic — it expresses what is necessary given what the speaker knows (evidential commitment). The second is deontic — it expresses an obligation imposed by law or rule. In possible-worlds semantics, these differ in what the accessibility relation represents: epistemic necessity ranges over worlds compatible with the speaker's knowledge; deontic necessity ranges over worlds compatible with relevant norms. The same word can express different modal flavors depending on the contextual parameters."

- question: "In standard possible-worlds semantics, 'possibly P' is true at a world w if and primarily if P holds in nearly every world accessible from w."
  type: true-false
  answer: false
  explanation: "This is the definition of necessity (□P), not possibility (◇P). Possibility (◇P) is true at w if P holds in AT LEAST ONE world accessible from w. The two operators are duals: □P = ¬◇¬P, and ◇P = ¬□¬P. Confusing these is a fundamental error — necessity requires universal truth across all accessible worlds, while possibility only requires existence of one accessible world where the proposition holds."

- question: "Why does the possible-worlds framework handle natural language modals by varying the accessibility relation rather than by treating all modals uniformly?"
  type: short-answer
  answer: "Because different modal flavors quantify over different sets of worlds: epistemic modals range over worlds compatible with what is known, deontic modals over worlds where relevant norms are satisfied, and dynamic modals over worlds compatible with an agent's capacities. A single fixed accessibility relation couldn't distinguish these, and the same word (e.g., 'must') can express any flavor depending on context."
  explanation: "This flexibility is the major advantage of the possible-worlds framework over simpler accounts. By relativizing the accessibility relation to contextual parameters (what is known, what the rules say, what an agent can do), the framework explains both the diversity of modal flavors and why a single word like 'must' or 'can' can shift between them. Kratzer's restrictor analysis formalizes this further by decomposing the context into a modal base and ordering source, giving even finer control over truth conditions."
```

## Explainer

From Montague semantics, you know how to compute the truth conditions of sentences compositionally — building the meaning of a complex expression from the meanings of its parts using typed lambda calculus. From modal logic, you know the algebraic framework: a Kripke model with a set of possible worlds and an accessibility relation, where □P (necessity) means P is true in all accessible worlds and ◇P (possibility) means P is true in at least one. Modal semantics for natural language is the project of bringing these two frameworks together — applying possible-worlds reasoning to the modals that appear in ordinary speech, like *must*, *might*, *can*, *should*, *necessarily*, and *possibly*.

The first important move is recognizing that natural language modals are not uniform. **Epistemic modality** concerns what is possible or necessary given what is known: "She must be home — her lights are on" doesn't assert metaphysical necessity but the speaker's evidential commitment. **Deontic modality** concerns obligations and permissions: "You must report any income over $50,000" says nothing about what is physically necessary but what is required by law or rule. **Dynamic modality** concerns abilities and dispositions: "She can run a four-minute mile" reports a capacity. The same word (*must*, *can*) shifts meaning across these flavors; the possible-worlds framework handles this by varying what the accessibility relation represents — epistemic necessity ranges over worlds compatible with the speaker's knowledge; deontic necessity ranges over worlds compatible with the relevant rules or norms.

**Kratzer's restrictor analysis** (the dominant modern account) refines this further. Rather than treating a modal like *must* as simply "in all accessible worlds," Kratzer argues that modals operate on two contextual parameters: a **modal base** (a set of propositions restricting the relevant worlds — e.g., what is known, what the laws require) and an **ordering source** (a set of propositions ranking those worlds by some standard of normality or ideality). "You must leave" in a deontic context is evaluated against worlds where relevant rules are satisfied, ranked by how closely they approximate ideal compliance. This two-parameter structure explains why deontic and epistemic modals can differ in their projection behavior and why sentences like "It might be that you must leave" are coherent.

The power of the framework becomes clearest in **scope interactions with negation and quantifiers**. Consider: "It's not necessary that everyone attends" — here negation takes wide scope over necessity, yielding ¬□(∀x. attends(x)), which means it's not the case that all worlds have universal attendance. Contrast "Everyone must not attend" — parsed as ∀x.□(¬attends(x)), which says for each person, in all relevant worlds, they don't attend. These have very different truth conditions: the first is compatible with some worlds where everyone attends; the second prohibits attendance for each individual. Getting scope interactions right is one of the main motivations for doing modal semantics formally rather than informally — intuitions about these sentences are unreliable, but compositional derivation gives determinate answers.
