---
id: applicative-voice-operations
title: Applicative Voice Operations
domain: language-and-communication
course: linguistics
prerequisites:
- id: valency-changing-operations
  type: hard
- id: argument-structure-thematic-roles
  type: hard
- id: case-systems-typology
  type: soft
tags:
- syntax
- voice
- valency
- morphology
stage: advanced
status: validated
---

# Applicative Voice Operations

## Core Idea
Applicative voice is a valency-increasing operation that promotes a peripheral thematic role (benefactive, locative, instrumental, malefactive) to object status. Applicative morphemes, frequent in Bantu languages, allow constructions like 'build-APPL a house for him' (benefactive applicative) to function as syntactically transitive or ditransitive structures.

## Questions

```yaml
- question: "In a language with a productive applicative morpheme, compare: 'She cooked food' (transitive, 2 core arguments) vs. 'She cook-APPL him food' (where 'him' is a beneficiary). Which statement best describes what happened to 'him' in the second sentence?"
  type: multiple-choice
  options:
    - "'Him' was added as an optional adjunct prepositional phrase meaning 'for him,' leaving valency unchanged"
    - "'Him' was promoted from a peripheral/optional role to a core direct object argument, increasing the verb's valency"
    - "The verb became intransitive to accommodate the additional semantic participant"
    - "'Him' retains adjunct status and receives a special dative case marker rather than becoming a core object"
  answer: 1
  explanation: "Applicative voice is a valency-increasing operation: it takes a participant that would normally be expressed as an adjunct (an optional prepositional phrase like 'for him') and promotes it to a core argument position — a direct object of the verb. The applicative morpheme on the verb absorbs the function of the preposition; the beneficiary is now syntactically required (part of the verb's core argument structure) rather than optional. The result is a ditransitive structure with three core arguments: Agent, Applied Object (the promoted beneficiary), and Patient."

- question: "Why are applicative morphemes more common in languages with limited case morphology than in languages with rich case systems?"
  type: multiple-choice
  options:
    - "Languages with rich case morphology have more complex verbal morphology that blocks applicative affixation"
    - "Rich case systems allow peripheral thematic roles like beneficiaries to be expressed directly with distinctive case markers, without needing to promote them to object status"
    - "Applicative morphemes are genetically restricted to Bantu languages and do not develop elsewhere"
    - "Languages with limited case morphology have simpler syntactic structures that cannot express beneficiaries any other way"
  answer: 1
  explanation: "This is a key typological insight. In a language like Russian (rich case system), a beneficiary can simply appear in the dative case — the case marker itself signals the beneficiary role without changing the verb's core argument structure. In a language with little or no case morphology, there is no such direct flagging option; the language instead recruits verbal morphology (applicatives) to promote the beneficiary to object status where it can be unambiguously identified and tracked. The two strategies solve the same expressive problem through different grammatical means."

- question: "An applicative construction increases a verb's valency by promoting an adjunct thematic role (such as a beneficiary or instrument) to the status of a core argument."
  type: true-false
  answer: true
  explanation: "This is the defining property of applicative voice. The operation takes a participant that would normally be expressed as an optional, peripheral prepositional phrase (an adjunct) and incorporates it into the verb's core argument structure as a new object. Valency increases — a transitive verb becomes ditransitive; an intransitive verb becomes transitive — and the morpheme on the verb signals this restructuring."

- question: "In a language with applicative morphology, the applied object (e.g., a promoted beneficiary) retains its adjunct status and can seldom become the subject of a passive construction."
  type: true-false
  answer: false
  explanation: "One of the key diagnostics for whether the applied object has genuinely become a core argument (rather than remaining an adjunct) is whether it can be passivized — promoted to subject position in a passive construction. In well-documented applicative languages like Chichewa and Swahili, the applied object can become the subject of a passive, and it controls verb agreement morphology. These are signature properties of core argument status. If the applied object still behaved like an adjunct, passivization would not be available to it."

- question: "What does applicative voice reveal about the nature of grammatical relations like 'object'? Use a concrete example to illustrate your answer."
  type: short-answer
  answer: "Applicative voice shows that grammatical relations like 'object' are syntactic positions that can be assigned to different thematic roles through morphological operations — they are not fixed to one semantic role. For example, in 'She build-APPL him a house,' the Beneficiary ('him') occupies the object position even though 'object' in the base verb 'build' corresponds to the Patient ('a house'). The applicative morpheme reassigns object status from the Patient to the Beneficiary. This demonstrates that 'object' is a structural slot in clause structure, not a semantic label."
  explanation: "This has major implications for syntactic theory: it means argument structure is not rigidly determined by semantics. A morphological operation can restructure which roles occupy which grammatical positions, showing that the mapping between thematic roles and grammatical relations is manipulable. Applicatives are thus evidence for the independence of semantic and syntactic levels of representation."
```

## Explainer

You've studied valency-changing operations — processes that add or remove arguments from a verb's argument structure. You've also worked with thematic roles: the semantic labels (Agent, Patient, Beneficiary, Goal, Instrument, Location) that describe how participants relate to an event. Applicative voice is where those two frameworks intersect: it is a valency-increasing operation that takes a role that is normally expressed as an **adjunct** (a peripheral, optional phrase) and pulls it into the **core argument** position of the verb.

To see the contrast, start with a simple transitive clause: "She built a house." The verb *build* has two core arguments — an Agent (she) and a Patient (a house). If you want to add a Beneficiary, you do so with a prepositional phrase: "She built a house **for him**." That for-phrase is an adjunct — syntactically optional, not required by the verb's valency. In a language with a productive **applicative morpheme**, the verb itself can be marked to incorporate that Beneficiary directly: "She build-APPL him a house," where *him* is now a direct object, a core argument. The preposition disappears; the morpheme on the verb absorbs it. The result is a ditransitive structure with three core arguments: Agent, Applied Object (the new one), and Patient.

Different thematic roles produce different applicative types. A **benefactive applicative** promotes a Beneficiary ("she cooked-APPL him food" = she cooked food for him). A **locative applicative** promotes a Location ("she slept-APPL the mat" = she slept on the mat). An **instrumental applicative** promotes an Instrument ("she hit-APPL the stick him" = she hit him with the stick). A **malefactive applicative** promotes someone adversely affected ("she cooked-APPL him food" in a context meaning she cooked his food without permission). Bantu languages like Swahili and Chichewa are the canonical examples because their applicative morphemes are highly productive and their argument-structure effects have been extensively documented.

Why does this matter for typology and syntactic theory? The applied object behaves like a core argument in several ways: it can become the subject of a passive, it controls agreement morphology on the verb, and it has the word-order properties of a direct object. This is evidence that grammatical relations like "object" are not just semantic notions but syntactic positions that can be assigned to different thematic roles by morphological means. Applicatives thus reveal a crucial design feature of clause structure: the number of semantic roles present in an event can exceed the verb's default valency, and morphological operations exist to restructure which roles occupy which grammatical slots. From your earlier work on case systems, you can also see that languages with rich case morphology often don't need applicative morphemes — they can simply case-mark a Beneficiary differently — which is one reason applicatives are more developed in languages with less robust case systems.
