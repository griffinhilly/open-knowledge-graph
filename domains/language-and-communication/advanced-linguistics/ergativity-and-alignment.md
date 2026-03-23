---
id: ergativity-and-alignment
title: Ergativity and Grammatical Alignment
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: argument-structure-thematic-roles
  type: hard
- id: linguistic-typology
  type: hard
tags:
- typology
- alignment
- morphosyntax
stage: expert
status: validated
---

# Ergativity and Grammatical Alignment

## Core Idea
Languages vary in how they mark core arguments. Nominative-accusative languages group the subject of transitives with intransitive subjects, aligning against objects. Ergative-absolutive languages group intransitive subjects and transitive objects, aligning against agents. This fundamental typological parameter has profound consequences for syntax, case marking, and agreement patterns, revealing that subject-hood is defined differently across languages.

## Questions

```yaml
- question: "In an ergative-absolutive language, how would the noun phrases in 'The woman carried the basket' and 'The woman arrived' be case-marked?"
  type: multiple-choice
  options:
    - "Both instances of 'the woman' receive nominative case and 'the basket' receives accusative — identical to English"
    - "'The woman' in the first sentence receives ergative case (as transitive agent); 'the woman' in the second sentence and 'the basket' both receive absolutive case"
    - "'The woman' receives absolutive in both sentences; 'the basket' receives ergative case as the affected object"
    - "'The woman' receives ergative in both sentences because she is the most animate, agentive participant in both events"
  answer: 1
  explanation: "In ergative-absolutive alignment, the transitive agent ('the woman' who carried) receives ergative case — marking her as the initiator of an action affecting another argument. The intransitive subject ('the woman' who arrived) and the transitive object ('the basket') both receive absolutive case. The absolutive groups these two grammatically despite their semantic differences because both are the argument most directly involved in the event without causing a change in another participant. This grouping reflects affectedness, not agenthood — which is the core semantic distinction underlying ergative alignment."

- question: "Split ergativity in Hindi-Urdu is conditioned by which grammatical feature?"
  type: multiple-choice
  options:
    - "The animacy of the subject — animate subjects trigger ergative alignment, inanimate subjects trigger nominative-accusative"
    - "The verb's transitivity alone — all transitive verbs trigger ergative marking regardless of tense or aspect"
    - "The aspect of the verb — perfective aspect triggers ergative alignment while imperfective aspect triggers nominative-accusative"
    - "The tense — past tense triggers ergative alignment while present and future trigger nominative-accusative"
  answer: 2
  explanation: "Hindi-Urdu is the canonical case of aspect-conditioned split ergativity: perfective aspect (completed, bounded actions) triggers ergative-absolutive alignment, while imperfective aspect (ongoing or habitual actions) triggers nominative-accusative. This reflects a semantic connection between ergativity and completed events where an agent caused a definite change of state in a patient. In ongoing or habitual events, the agent-patient asymmetry is less clear-cut, and the language shifts accordingly. This connection to aspect and event structure is one reason split ergativity fascinates typologists."

- question: "In an ergative-absolutive language, the subject of an intransitive verb and the object of a transitive verb receive identical case marking (absolutive)."
  type: true-false
  answer: true
  explanation: "This is the defining feature of ergative-absolutive alignment: the absolutive case groups intransitive subjects (S) with transitive objects (O), while the ergative case marks only transitive agents (A). This is the mirror image of nominative-accusative, where nominative groups agents (A) with intransitive subjects (S) against accusative objects (O). The absolutive S/O grouping reflects the semantic principle of affectedness: both the intransitive subject and the transitive object are the argument most directly affected by or involved in the event, while the transitive agent is the external initiator."

- question: "Ergative languages are rare exceptions found mainly in isolated or endangered language communities; the vast majority of the world's languages use nominative-accusative alignment."
  type: true-false
  answer: false
  explanation: "While nominative-accusative is the more familiar pattern (common in Indo-European languages), ergative-absolutive alignment is neither rare nor exotic. Major languages including Basque, Georgian, Tibetan, and dozens of Mayan languages are at least partially ergative. A large proportion of Australian Aboriginal languages use ergative alignment. Roughly a quarter to a third of the world's languages display some form of ergativity. The perception that ergativity is rare reflects an Indo-European bias in traditional linguistics, not the actual cross-linguistic distribution."

- question: "What semantic principle underlies ergative-absolutive alignment, and how does studying ergativity challenge the assumption that 'subject' is a universal grammatical category?"
  type: short-answer
  answer: "Ergative-absolutive alignment tracks affectedness: the absolutive case marks the argument most directly affected by the event — whether it is an intransitive subject or a transitive object — while the ergative marks the transitive agent as the external causer. This is a coherent semantic grouping distinct from the agent-focused grouping of nominative-accusative. It challenges the universality of 'subject' because what counts as the privileged, unmarked grammatical argument differs across systems. In nominative-accusative languages, agenthood plus intransitive subjecthood define the subject category. In ergative-absolutive languages, this familiar 'subject' does not exist as a unified category — agents are ergative while intransitive subjects pattern with objects. Grammatical categories are language-specific design choices, not universal features of human grammar."
  explanation: "This is why linguistic typology is theoretically important, not just descriptively interesting. Ergativity reveals that concepts like 'subject' and 'object' that seem self-evident in European languages are actually one solution among multiple possible solutions to the problem of organizing clause arguments. It also connects to argument structure theory, case theory, and the semantics of events — a single phenomenon that illuminates how morphology, syntax, and semantics interact across languages."
```

## Explainer

To get ergativity, start with something you already know: in English, "the teacher praised the student" and "the student arrived" both use subject position the same way. "The teacher" is the **agent** — the one performing the action. "The student" in the first sentence is the **patient** — the one receiving it. "The student" in the second sentence is neither agent nor patient in the transitive sense; it is simply the sole participant in an intransitive event. English groups the transitive agent ("the teacher") with the intransitive subject ("the student arrived") — both appear before the verb with no special marking. The object "the student" in the transitive sentence gets a different treatment (accusative in case-marking languages). This is **nominative-accusative** alignment: it distinguishes subject-like arguments (nominative) from object-like arguments (accusative), and the defining principle is that agents and intransitive subjects are treated the same.

Now consider flipping the grouping. Instead of grouping transitive agents with intransitive subjects, imagine grouping **transitive objects with intransitive subjects** — and giving the transitive agent its own special marking. This is **ergative-absolutive** alignment. The transitive agent gets **ergative case**; the transitive object and intransitive subject both get **absolutive case**. If English worked this way, "the teacher" in "the teacher praised the student" would carry a special ergative marker, while "the student" in "the teacher praised the student" and "the student arrived" would look identical (absolutive). The ergative marks the argument that actively causes something to happen to another argument; the absolutive marks the argument most directly affected by the event — whether or not there is a causing agent.

This is not arbitrary linguistic variation. The ergative-absolutive system reflects a coherent semantic distinction: it tracks **affectedness** rather than agenthood. Ergative languages are neither rare nor exotic — Basque, many Australian Aboriginal languages, Tibetan, Georgian, Mayan languages, and dozens more use ergative-absolutive patterning in some or all of their grammar. What's linguistically important is that ergativity reveals "subject" to be a non-universal category. Your thematic roles work taught you to distinguish agent, patient, and theme as semantic roles. English grammatical subject collapses agents and intransitive experiencers into one syntactic slot. Ergative alignment makes a different cut, one that emphasizes affectedness over agency. Studying typology forces you to recognize that the grammatical categories familiar from European languages are local solutions to cross-linguistic problems, not universal features of human language.

A further complication is **split ergativity** — many languages are not uniformly ergative across all contexts but split along tense, aspect, or person lines. In Hindi-Urdu, perfective aspect triggers ergative alignment while imperfective triggers nominative-accusative. This is not inconsistency; it reflects a semantic connection between ergativity and completed events where an agent caused a change of state in a patient. In ongoing or habitual events, the agent-patient asymmetry is less sharp, and the language shifts accordingly. Studying ergativity thus integrates morphology (case marking), syntax (agreement patterns), typology (cross-linguistic comparison), and semantics (aspect, agency, affectedness) into a single phenomenon — a model for how linguists understand grammatical categories as solutions to communicative pressures rather than as arbitrary conventions inherited without reason.

