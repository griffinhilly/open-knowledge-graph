---
id: control-and-raising-constructions
title: Control and Raising Constructions
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: minimalist-program-core-concepts
  type: hard
- id: argument-structure-thematic-roles
  type: hard
tags:
- syntax
- argument-structure
- control
stage: expert
status: validated
---

# Control and Raising Constructions

## Core Idea
Control and raising are distinct mechanisms for linking subject positions across clauses: raising involves NP movement to a higher clause, while control involves a null subject (PRO) in the lower clause obligatorily coreferent with a matrix argument.

## How It's Best Learned
Compare minimal pairs distinguishing control from raising (e.g., 'John tried to leave' vs. 'John seems to have left'), examining which tests (passivization, tough-movement) apply to each.

## Common Misconceptions
Both involve a coindexed subject relationship, but raising is movement (one argument), while control is composition of two separate predicates.

## Questions

```yaml
- question: "A student analyzes 'John appears to be happy' and says: 'John is the subject of both appears and be happy, so this must be a control construction like tried to leave.' What is wrong with this analysis?"
  type: multiple-choice
  options:
    - "The student is correct — appear and try are both control verbs that assign thematic roles to their matrix subjects"
    - "'Appear' is a raising predicate that assigns no thematic role to its subject position; John originates as the subject of the embedded clause and raises to matrix subject only to satisfy the EPP — there is only one argument, not two"
    - "'Appear' has no subject at all — it is an impersonal verb like 'rain'"
    - "The error is that 'happy' is an adjective, not a verb, so no movement is possible"
  answer: 1
  explanation: "The surface similarity of control and raising — both have a matrix NP followed by an infinitival complement — conceals a deep structural difference. In 'appear to be happy,' appear takes no external argument; it is semantically vacuous with respect to its subject. John is not the agent or experiencer of appearing — he is simply the subject of the embedded predicate (be happy) that has moved to the matrix subject position to satisfy the EPP. In 'try to leave,' John IS the agent of trying — try selects a thematic subject. The student's error is treating surface subject position as evidence of an argument relationship, when in raising the matrix subject position is just a structural host."

- question: "Which test most reliably distinguishes a raising predicate from a control predicate?"
  type: multiple-choice
  options:
    - "Raising predicates require the infinitival marker 'to'; control predicates use bare infinitives"
    - "Only control predicates can be passivized"
    - "Expletive substitution: replacing the matrix subject with 'it' or 'there' is grammatical with raising predicates (which assign no thematic role to the subject) but ungrammatical with control predicates (which require a referential agent)"
    - "Raising predicates occur only in subordinate clauses; control predicates occur only in matrix clauses"
  answer: 2
  explanation: "The expletive test works because raising predicates take no external argument — their subject position is a structural requirement (EPP), not a thematic slot. 'It seems that John left' is grammatical; 'There seem to be problems' is grammatical. But 'It tried that John left' and 'There tried to be problems' are ungrammatical because try requires a referential agent in its subject position — a non-referential expletive cannot satisfy a thematic requirement. This test is reliable across constructions and languages because it probes whether the matrix predicate genuinely selects a semantic argument in subject position."

- question: "In 'There seem to be many problems,' the expletive 'there' can appear as matrix subject because 'seem' is a raising predicate that assigns no thematic role to its subject position."
  type: true-false
  answer: true
  explanation: "This is a direct application of the raising predicate's defining property: it takes no external argument and assigns no thematic role to its subject. When the EPP (the requirement that TP have a specifier) must be satisfied but there is no NP to raise from the embedded clause in a convenient position, an expletive can fill the slot. 'There seem to be many problems' is grammatical for exactly this reason. The real argument (many problems) remains in the embedded clause. If you tried the same with a control verb — 'There tried to be many problems' — you get ungrammaticality because try demands an agentive referential subject."

- question: "In the control construction 'John tried to leave,' John bears only one thematic role — agent — because 'try' and 'leave' together form a single complex predicate with a single argument structure."
  type: true-false
  answer: false
  explanation: "Control constructions involve two separate predications, each with its own argument structure. John is the agent of trying (try selects an external argument with the agent role) AND the agent of leaving (leave selects an external argument with the agent role). The null pronoun PRO in the embedded clause's subject position is what the control relation targets — PRO must be coreferent with the matrix subject John. This is why control is analyzed as involving two predicates and two separate semantic role assignments, not a single complex predicate. The two-predicate analysis is confirmed by the fact that try and leave can each independently select different thematic properties."

- question: "Explain why idiom chunks can appear as the raised subject in raising constructions but not as the controlled subject in control constructions, and what this reveals about the structural difference between raising and control."
  type: short-answer
  answer: "Idioms like 'the shit hit the fan' or 'the cat is out of the bag' have their idiomatic meaning only when the entire idiomatic string is interpreted together — you cannot extract a piece and reassign its reference while preserving the idiom's meaning. In raising, the NP 'the shit' originates inside the embedded clause where the idiom is intact (the shit hit the fan) and merely moves to matrix subject position for structural reasons — the idiom is interpreted at its base position and the meaning is preserved. In control, the matrix predicate assigns a thematic role to its subject: 'the shit tried to hit the fan' requires 'the shit' to be an agent of trying — which an idiom chunk cannot be, since it has no independent referent. The grammaticality of idiom chunks as raised subjects but not controlled subjects is diagnostic evidence that raising subjects receive no thematic role from the matrix predicate."
  explanation: "The idiom chunk test is powerful because it probes thematic role assignment without requiring speakers to have theoretical knowledge of syntax. Idiom chunks are semantically inert as isolated NPs — they only have meaning as part of the idiom. If a predicate assigns a thematic role to its subject, the idiom chunk cannot satisfy that role, and the construction fails. If the predicate merely hosts a structural subject (raising), the idiom chunk passes through and the idiom is interpreted where it was formed. This asymmetry provides direct evidence for the raising/control distinction without appeal to abstract theoretical machinery."
```

## Explainer

From your work on the Minimalist Program you know that syntactic derivations involve movement operations (Merge, Move) and that argument structure maps thematic roles onto syntactic positions. Control and raising constructions are the key test cases for understanding how matrix and embedded clauses interact — specifically, how the subject of an infinitival complement gets its interpretation and its thematic role.

Consider two sentences: *John tried to leave* and *John seems to have left*. Both look superficially similar — a matrix subject, a main verb, and an infinitival complement. But they work differently at a deep level. In *John tried to leave*, John is the **agent** of both trying and leaving. The infinitival complement has its own subject position, occupied by **PRO** — a phonologically null pronoun whose reference is controlled by (bound to) a matrix argument. This is an **obligatory control** construction: PRO must refer to John, not some arbitrary person. John bears two thematic roles (agent of try, agent of leave), and the sentence involves two separate predications joined by the control relation.

In *John seems to have left*, John is **not** an argument of *seem* at all — *seem* is a raising predicate that takes no external argument. John originates as the subject of the embedded clause (agent of leaving), and raises to the matrix subject position to satisfy the EPP (the requirement that TP have a specifier). This is why raising predicates pass the **expletive test**: *It seems that John left* works perfectly, substituting the expletive *it* for the raised NP. But *It tried that John left* is ungrammatical — *try* is a control verb that requires a referential agent in its subject position. The same test distinguishes raising from control across constructions: if you can substitute *it* or a non-referential expression (*There seems to be a problem* but not *There tried to be a problem*), you have a raising predicate.

The practical diagnostic toolkit matters because the distinction has real consequences for semantic interpretation. **Idiom chunks** provide another diagnostic: *The shit seems to have hit the fan* is grammatical because *the shit* raises from the embedded clause where the idiom is intact. *The shit tried to hit the fan* — interpreted as an idiom — is blocked, because *try* assigns a thematic role to its subject, and *the shit* cannot be an agent. Similarly, the **tough-movement** construction (*John is easy to please*) appears superficially like raising but actually involves a gap in the embedded complement — an A-bar movement phenomenon distinct from both control and raising. Keeping these constructions distinct requires asking, each time, where each NP receives its thematic role, and whether the matrix predicate takes that position as an argument or merely as a structural host.
