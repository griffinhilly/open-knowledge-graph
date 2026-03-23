---
id: alignment-systems-typology
title: Alignment Systems and Grammatical Relations
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: linguistic-typology
  type: hard
- id: ergativity-and-alignment
  type: hard
tags:
- alignment
- typology
- grammatical-relations
stage: expert
status: validated
---

# Alignment Systems and Grammatical Relations

## Core Idea
Alignment systems classify how agents (A), patients (P), and single arguments (S) of intransitive verbs are marked (through agreement, case, word order, or voice). Nominative-accusative systems treat S and A alike; ergative-absolutive systems treat S and P alike. Other systems are tripartite, horizontal, or hierarchical. Alignment is not universal but varies; it determines how semantic roles map to grammatical relations.

## How It's Best Learned
Compare alignment patterns across languages, using data on agreement, case-marking, and word-order to identify the alignment type. Examine which semantic and pragmatic factors motivate different alignments.

## Common Misconceptions
- Alignment does not determine the semantic roles of arguments; it determines how semantic roles map to grammatical functions.
- A single language may exhibit different alignments in different constructions (split systems).

## Questions

```yaml
- question: "In Language X, the single argument of an intransitive verb ('she sleeps') takes the same case marking as the patient of a transitive verb ('the ball' in 'she kicked the ball'), while the agent takes a distinct case. What alignment does Language X exhibit?"
  type: multiple-choice
  options:
    - "Nominative-accusative, because the agent receives the special marked case"
    - "Ergative-absolutive, because S groups with P under absolutive marking while the agent takes the ergative case"
    - "Tripartite, because all three argument types — S, A, and P — receive different marking"
    - "Neutral, because all arguments share a common default case"
  answer: 1
  explanation: "The defining feature of ergative-absolutive alignment is that S (intransitive subject) groups with P (transitive patient) — both take the absolutive case — while A (transitive agent) is specially marked with the ergative case. This is the inverse of nominative-accusative, where S groups with A as the 'subject.' The question describes exactly the ergative-absolutive pattern: the agent is singled out with special marking while intransitive subjects and transitive patients share a form."

- question: "A student claims that Georgian 'is an ergative language' because it uses ergative case marking. A colleague notes that Georgian shows different alignment patterns depending on verb tense. Which statement best captures the theoretical implication?"
  type: multiple-choice
  options:
    - "If a language has ergative morphological case, it is ergative in all constructions — grammatical tense cannot affect alignment"
    - "Georgian's tense-based split shows that alignment is not a single unified property of a language; it can exhibit ergative-absolutive patterns in some contexts (e.g., perfective past) and nominative-accusative in others (e.g., present)"
    - "Tense variations in case marking are surface irregularities that don't affect a language's underlying alignment type"
    - "Split ergative systems represent languages in mid-transition from ergative to nominative-accusative alignment and have no stable type"
  answer: 1
  explanation: "Split systems are a central finding in alignment typology: a single language can show different alignment patterns in different grammatical subsystems. Georgian shows nominative-accusative in the present/imperfective and ergative-absolutive in the perfective past. Many languages show splits conditioned by person hierarchy, animacy, or aspect. The theoretical implication is that 'alignment' is not a single binary property of a language but a family of related phenomena that can partially decouple — which is why typologists analyze each grammatical subsystem separately."

- question: "In an ergative-absolutive language, the agent of a transitive clause receives the same grammatical marking as the subject of an intransitive clause."
  type: true-false
  answer: false
  explanation: "This describes the nominative-accusative pattern, not the ergative-absolutive pattern. In ergative-absolutive alignment, the intransitive subject (S) groups with the transitive patient (P) — both take absolutive marking. The transitive agent (A) takes the distinct ergative case and is therefore marked differently from S. Students who assume the 'subject' always groups the same way across alignment types are implicitly assuming nominative-accusative as the default — the classic confusion this topic corrects."

- question: "The S/A/P framework allows precise cross-linguistic comparison by treating the 'subject' of a transitive clause and the 'subject' of an intransitive clause as potentially different argument types that different languages may group differently."
  type: true-false
  answer: true
  explanation: "This is the analytical payoff of the S/A/P framework. In English-style (nominative-accusative) thinking, 'subject' means S and A together. But the framework separates them: S is the single argument of an intransitive verb; A is the agent of a transitive verb; P is the patient of a transitive verb. Different alignment systems group these differently. Without this framework, it would be impossible to state clearly that ergative languages 'treat S like P' rather than 'treat subjects differently' — the S/A/P terminology makes the cross-linguistic pattern visible."

- question: "Why does the distinction between alignment and semantic roles matter? Give an example showing that alignment cannot be read directly off who is performing the action."
  type: short-answer
  answer: "Semantic roles (agent, patient) describe who causes or is affected by an event — they are the same across all languages. Alignment describes how languages grammatically mark those roles, which varies. In English (nominative-accusative), 'she sleeps' (intransitive) and 'she kicked the ball' (agent) both use the nominative 'she' — S and A group together. In an ergative language like Basque, the same agent 'she' in 'she kicked the ball' takes the ergative case, while 'she sleeps' (intransitive subject) takes the absolutive — grouping with the patient 'the ball.' The person doing the kicking is the agent in both languages; only the grammatical coding differs. Alignment is a property of the morphosyntactic system, not of semantic roles themselves."
  explanation: "The misconception to avoid is thinking that ergative languages 'treat the subject differently' or 'demote the agent' semantically. The semantic roles are identical; what varies is which grammatical groupings the language uses to organize them. This is why cross-linguistic comparison requires the neutral S/A/P terminology rather than importing 'subject/object' from any one language type."
```

## Explainer

You've already worked through ergativity and the basic distinction between nominative-accusative and ergative-absolutive systems, and you've studied linguistic typology's broader project of mapping cross-linguistic variation. Alignment systems typology zooms out from those individual patterns to ask: across the world's languages, what are *all* the possible ways to group arguments, and what does that variation tell us about the relationship between grammar and meaning?

The core insight begins with three argument types. **S** is the single argument of an intransitive verb — the "she" in "she sleeps." **A** is the agent-like argument of a transitive verb — the "she" in "she kicked the ball." **P** is the patient-like argument of a transitive verb — the "ball" in "she kicked the ball." The logical question is: how many ways can these three types be grouped by grammatical marking? The options are mathematically constrained. If you treat S and A alike (and P differently), you get **nominative-accusative** alignment — the pattern familiar from English, Latin, and most European languages, where the subject of any verb (transitive or not) takes the same form. If you treat S and P alike (and A differently), you get **ergative-absolutive** alignment — found in Basque, many Australian languages, and numerous others, where the agent of a transitive clause is specially marked and the subject of an intransitive clause groups with the patient. If all three argument types are marked differently, you get a **tripartite** system. If they are all marked the same, you get a fully neutral system.

What makes alignment typology analytically powerful is that these patterns are not arbitrary: they reflect how different languages organize information about agency and affectedness. In a nominative-accusative language, the most "prominent" participant is the agent — S and A cluster together as the default grammatical role. In an ergative language, the absolutive (S and P) clusters as the default, decentering the agent. Different alignment choices encode different intuitions about which participant in an event is the most salient starting point for describing it. This is why typologists connect alignment to broader questions about event construal: languages differ not just in their morphology but in how they package events conceptually.

Real languages complicate the clean logical picture through **split systems** — the most important complication your prerequisite material introduced. A single language may show nominative-accusative alignment in some grammatical contexts and ergative-absolutive alignment in others. Georgian, for instance, shows nominative-accusative in the present tense and ergative-absolutive in the past. Many languages show ergative morphological case on nouns but nominative-accusative agreement on verbs. Splits often correlate with **person hierarchies** (first and second person arguments behaving differently from third person) or with **tense/aspect** distinctions (imperfective vs. perfective). These splits reveal that alignment is not a single, unified property of a language but a family of related phenomena that can partially decouple across grammatical subsystems — and understanding why splits occur where they do remains one of the productive open questions in typological linguistics.
