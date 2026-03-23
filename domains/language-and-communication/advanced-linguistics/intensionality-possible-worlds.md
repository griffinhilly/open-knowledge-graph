---
id: intensionality-possible-worlds
title: Intensionality and Possible Worlds Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: montague-semantics
  type: hard
- id: modal-semantics-necessity-possibility
  type: hard
builds-toward: []
tags:
- intensionality
- possible-worlds
- modality
stage: expert
status: validated
---
# Intensionality and Possible Worlds Semantics

## Core Idea
Intensional expressions like modals, belief verbs, and conditionals cannot be evaluated purely in the actual world; their truth conditions depend on possible worlds. The meaning of an intensional expression is an intension—a function from possible worlds to extensions. 'It is possible that it rains' is true if there exists a possible world where it rains, even if it is not raining in the actual world.

## How It's Best Learned
Represent modal and intensional statements using possible-worlds models, assigning truth values relative to different world states. Examine how the truth of intensional statements depends on accessibility relations between worlds.

## Common Misconceptions
- Intensional operators do not merely express uncertainty; they quantify over possible worlds with specific accessibility properties.
- Not all apparent intensionality requires possible-worlds analysis; some may be pragmatic or epistemically grounded.

## Questions

```yaml
- question: "John believes that Superman can fly. It is a fact that Superman is Clark Kent. Does it follow that John believes Clark Kent can fly?"
  type: multiple-choice
  options:
    - "Yes — 'Superman' and 'Clark Kent' denote the same individual, so they can be substituted in any sentence without changing its truth value"
    - "No — belief contexts are intensional; 'Superman' and 'Clark Kent' have the same extension but different intensions, and John may not know they refer to the same person"
    - "Yes — belief is about facts in the actual world, and it is a fact that Superman = Clark Kent, so any belief about one applies to the other"
    - "No — 'Clark Kent' does not have the same extension as 'Superman' because one is a public identity and one is private"
  answer: 1
  explanation: "This is the classic intensionality puzzle. In purely extensional semantics, co-referring terms can always be substituted salva veritate. But in intensional contexts — especially propositional attitude reports like 'John believes...' — substitution can fail. 'Superman' and 'Clark Kent' have the same extension (they pick out the same individual in the actual world) but different intensions (they pick him out via different descriptions, and could pick out different individuals in other possible worlds). John's belief is indexed to his mental states, which track descriptions and modes of presentation, not just individuals. Option A is the classic mistake; option C explicitly commits it."

- question: "What is an intension, as distinguished from an extension, in possible worlds semantics?"
  type: multiple-choice
  options:
    - "An intension is the emotional or connotative meaning of a word; an extension is its literal, denotative meaning"
    - "An intension is a function from possible worlds to extensions; an extension is the set of individuals (or truth value) a term denotes in the actual world"
    - "An intension is the full set of properties associated with a concept; an extension is just the concept's referent"
    - "An intension applies only to modal operators like 'necessarily'; extensions apply to all non-modal expressions"
  answer: 1
  explanation: "In possible worlds semantics, an extension is a term's denotation at a particular world — for a noun phrase, the set of individuals it picks out; for a sentence, its truth value. An intension is the rule that assigns extensions across all possible worlds — a function from worlds to extensions. 'The morning star' and 'the evening star' have the same extension in the actual world (both denote Venus) but different intensions, because in a world where Venus didn't exist or the two objects were distinct, they would pick out different things. The intension is what distinguishes genuinely co-referential terms from terms that merely happen to co-refer."

- question: "Because 'the morning star' and 'the evening star' both refer to Venus in the actual world, the sentence 'The morning star is the evening star' is necessarily true — true in all possible worlds."
  type: true-false
  answer: false
  explanation: "This is a contingent identity, not a necessary one. The statement is true in the actual world as an a posteriori astronomical discovery — it was not known until observation revealed it. In possible worlds where Venus doesn't exist, or where two distinct objects occupy those orbital positions, the sentence would be false. Necessary truth ('true in all possible worlds') is a much stronger claim. The morning star/evening star example is precisely Kripke's argument that some identity statements are contingent even though co-referential expressions are involved."

- question: "In possible worlds semantics, 'Possibly P' is true at world w if and only if there is at least one world accessible from w in which P is true."
  type: true-false
  answer: true
  explanation: "This is the standard Kripkean semantics for the possibility operator. The accessibility relation ◇ between worlds determines what counts as 'possible' relative to a given world — different kinds of modality (epistemic, deontic, metaphysical) correspond to different accessibility relations. For epistemic modality ('It might be raining'), accessible worlds are those compatible with what the agent knows. For metaphysical possibility, accessible worlds are those where the laws of nature or logic could obtain. 'Necessarily P' is then the dual: P is true in all accessible worlds."

- question: "Why can't co-referring expressions like 'the morning star' and 'the evening star' always be substituted for each other in intensional contexts like belief reports? What does this reveal about the difference between extensions and intensions?"
  type: short-answer
  answer: "Co-referring expressions have the same extension (they pick out the same individual in the actual world) but different intensions (they are associated with different descriptions or modes of presentation, and could pick out different things in other possible worlds). In intensional contexts like belief reports, truth does not depend only on what is actually true — it depends on the possible worlds compatible with the agent's mental states. John's belief worlds may include 'the morning star is a planet' without including 'the evening star is a planet' if John has never connected the two descriptions. Substituting one for the other in a belief report changes which set of possible worlds is being quantified over, potentially changing the truth value. This shows that extensions alone are insufficient for intensional semantics: we need intensions — functions from possible worlds to extensions — to capture meaning in opacity-creating contexts."
  explanation: "The substitution failure is the core diagnostic of intensionality. An extensional context is one where substituting co-referring terms preserves truth; an intensional context is one where it may not. Possible worlds semantics explains this by distinguishing what a term denotes now (extension) from how it picks out things across all possible circumstances (intension). Belief verbs, modals, and conditionals all create intensional contexts for the same underlying reason: their truth depends on quantification over possible worlds, not just evaluation at the actual world."
```

## Explainer

From your work with Montague semantics, you know that meanings can be treated compositionally as functions: a sentence's meaning is built from the meanings of its parts, with each part denoting something in a model. In standard extensional semantics, a noun phrase denotes a set of individuals, a verb phrase denotes a property, and a sentence denotes a truth value — true or false relative to the actual world. This works well for "The cat is on the mat." But it breaks down for "It is possible that the cat is on the mat" or "Alice believes the cat is on the mat." These are **intensional contexts**, where the truth of the whole does not depend only on what is actually true.

The problem becomes vivid with substitution. In purely extensional semantics, if "the morning star" and "the evening star" both denote the planet Venus, then replacing one with the other in any sentence should preserve truth. But "John believes the morning star is a planet" can be true while "John believes the evening star is a planet" is false — if John doesn't know they're the same object. The two expressions have the same **extension** (they pick out the same individual in the actual world) but different **intensions** (they pick it out via different descriptions, and may pick out different things in other possible worlds). Intensional semantics distinguishes between the two by making meanings functions from possible worlds to extensions: an **intension** is a function from possible worlds to an extension, not just an extension.

A **possible world** is a complete way the world could have been — a maximally consistent description of a state of affairs. Modal operators quantify over them: "Necessarily P" means P is true in all accessible possible worlds; "Possibly P" means P is true in at least one. The **accessibility relation** between worlds determines which worlds count as "possible" relative to a given world — and different kinds of modality (epistemic, deontic, metaphysical) correspond to different accessibility relations. From your prerequisite work on modal semantics, you know this framework; intensionality extends it from modals to the full range of operators that create opaque contexts.

**Propositional attitude verbs** like *believe*, *want*, *hope*, and *fear* are then analyzed as quantifying over worlds compatible with the subject's mental states. "Alice believes P" is true if P is true in all worlds compatible with what Alice believes — which may exclude some actual facts and include some counterfactual ones. This explains the morning star/evening star asymmetry: Alice's belief worlds may include the morning star being a planet without including the evening star being a planet if she hasn't connected the two. Intensionality is thus not a quirk of a few special constructions — it is pervasive in natural language, appearing in modals, belief verbs, conditionals, and desire predicates, all receiving a unified treatment through possible-worlds semantics.
