---
id: argument-structure-thematic-roles
title: Argument Structure and Thematic Roles
domain: language-and-communication
course: linguistics
prerequisites:
- id: syntactic-structure
  type: hard
- id: compositional-semantics
  type: hard
tags:
- thematic roles
- theta theory
- agent
- patient
- valency
- argument structure
stage: formal-systems
status: draft
---

# Argument Structure and Thematic Roles

## Core Idea
Argument structure describes how many and what kinds of participants a verb requires — its valency — while thematic roles (theta roles) classify the semantic relationship each participant bears to the event. Core roles include Agent (the intentional doer), Patient (the entity undergoing change), Theme (the entity being moved or located), Experiencer (the entity perceiving or feeling), Goal, Source, and Instrument. Theta theory, within the Principles and Parameters framework, constrains the mapping between thematic roles and syntactic positions through the Theta Criterion: each argument must receive exactly one theta role, and each theta role must be assigned to exactly one argument. Alternations like the dative shift ("gave the book to Mary" / "gave Mary the book") and the causative-inchoative alternation ("broke the vase" / "the vase broke") reveal how argument structure can be reorganized while preserving underlying thematic relations.

## How It's Best Learned
Assign thematic roles to every noun phrase in a set of sentences, then test your assignments by paraphrasing — the Agent should still feel like the doer, the Patient like the affected entity. Compare the argument structures of verbs with different valencies (rain = 0, sleep = 1, hit = 2, give = 3) to see how verb meaning constrains participant number. Analyze causative alternations across languages to see which verbs allow them and which resist them.

## Common Misconceptions
- The grammatical subject is not always the Agent — in passive sentences, experiencer constructions ("The noise frightened me"), and unaccusative verbs ("The ice melted"), the subject bears a non-Agent role.
- Thematic role lists are not universally agreed upon; the exact inventory and boundaries between roles (Theme vs. Patient, Goal vs. Beneficiary) remain actively debated.
- Valency is not fixed for a verb — many verbs participate in alternations that add, remove, or rearrange arguments (causativization, passivization, applicative constructions).

## Questions

```yaml
- question: "In the sentence 'The ice melted,' what thematic role does 'the ice' bear, and why is this theoretically significant?"
  type: multiple-choice
  options:
    - "Agent — because it is the grammatical subject and subjects are always Agents"
    - "Patient/Theme — the ice undergoes the change of state without intentionally causing it, demonstrating that grammatical subjects need not be Agents"
    - "Instrument — because ice is a physical substance involved in a process"
    - "Experiencer — because the ice 'experiences' a temperature change"
  answer: 1
  explanation: "Unaccusative verbs like 'melt' and 'arrive' take a Patient/Theme as their surface subject. The subject position is syntactically defined (it controls agreement, determines word order), but it does not fix thematic role. This is exactly what the Theta Criterion captures: each argument gets one theta role, but the mapping between syntactic positions and thematic roles is not one-to-one — it is mediated by the verb's argument structure."

- question: "The Theta Criterion states that a single theta role can be assigned to multiple arguments in one clause, as long as each argument receives at least one role."
  type: true-false
  answer: false
  explanation: "The Theta Criterion is a biconditional constraint: each argument must receive exactly one theta role AND each theta role must be assigned to exactly one argument. The 'multiple arguments sharing a role' reading is precisely what the criterion prohibits. This bidirectionality ensures a one-to-one correspondence between semantic participants and syntactic arguments within a clause."

- question: "What does 'valency' describe, and how does the causative-inchoative alternation ('The vase broke' / 'She broke the vase') illustrate that valency can change?"
  type: short-answer
  answer: "Valency describes how many arguments a verb requires: intransitive verbs have valency 1, transitive verbs valency 2, ditransitive verbs valency 3. In 'The vase broke,' 'break' is intransitive (valency 1) with only the Theme argument. In 'She broke the vase,' it is transitive (valency 2) with an Agent added. The same verb participates in both frames, showing valency is not a fixed lexical property but can be altered by argument-structure operations that add or remove participants while preserving the core semantic relation."
  explanation: "The causative alternation is cross-linguistically common and reveals that verbs encode not just an event type but a range of possible participant configurations. Understanding valency as flexible rather than fixed is essential for analyzing passives, applicatives, and other constructions that systematically manipulate argument structure."
```

## Explainer

You have already studied syntactic structure — how sentences are built from phrases according to hierarchical rules — and compositional semantics — how sentence meanings are assembled from word meanings. Argument structure and thematic roles sit at the interface: they describe how the semantic participants in an event are packaged into the syntactic positions that sentences provide.

Start with an observation about verbs: they differ in how many participants they require. "Rain" needs none (it's an event with no participants); "sleep" needs one (the sleeper); "hit" needs two (the hitter and the thing hit); "give" needs three (the giver, the recipient, and the thing given). This is a verb's valency. But valency alone is not fine-grained enough — we also need to know what kind of participant each argument is. This is where thematic roles come in. The doer in "hit" is an Agent (intentional, causing the action); the thing done to is a Patient (undergoing change). "Frighten" also has two arguments, but here the roles differ: "The noise frightened John" has a non-agentive cause (the noise) and an Experiencer who feels the effect (John). Valency tells you how many; thematic roles tell you what kind.

The Theta Criterion, from Chomsky's Principles and Parameters framework, formalizes the constraint that the mapping between roles and arguments must be one-to-one within a clause: each argument gets exactly one role, and each role goes to exactly one argument. This constraint rules out sentences like *"John hit" where the Patient is absent, or hypothetical constructions where two arguments share a single role. The Theta Criterion is why verbs with different argument structures cannot be freely swapped into the same syntactic frame — the frame must match the verb's thematic requirements.

One of the most important results of studying argument structure is discovering that the same verb can appear in multiple frames with different valencies. "The vase broke" (intransitive, Theme only) and "She broke the vase" (transitive, Agent + Theme) use the same verb root but different argument structures. This causative-inchoative alternation, found across hundreds of verbs in many languages, shows that verbs do not have a single fixed argument structure — they have a range of possible structures related by systematic operations. The underlying thematic relation (a Theme undergoing a change of state) is preserved; what varies is whether an Agent is introduced as a cause.

The most persistent misconception to overcome is the equation of "subject" with "Agent." The subject position is defined syntactically (it controls verb agreement, appears before the verb in English declaratives, etc.), but what thematic role it receives depends on the verb. Passive sentences ("The window was broken"), unaccusative verbs ("The ship arrived"), and Experiencer predicates ("The news surprised Maria") all have subjects that are not Agents. Keeping syntactic role (subject, object) and semantic role (Agent, Patient, Experiencer) conceptually separate is the core skill this topic develops.
