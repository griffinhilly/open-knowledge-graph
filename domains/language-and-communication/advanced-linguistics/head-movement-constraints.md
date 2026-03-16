---
id: head-movement-constraints
title: Head Movement and Locality Constraints
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: movement-and-transformations
  type: hard
- id: x-bar-theory
  type: hard
tags:
- syntax
- movement
- constraints
stage: advanced
status: draft
---

# Head Movement and Locality Constraints

## Core Idea
Head movement (single-word displacement) obeys the Head Movement Constraint: a head can only move to the head of its immediately dominating phrase. This explains why auxiliary verbs move to sentence-initial C in English ('Does he leave?'), but full verbs cannot (*'Leaves he?'). The constraint reveals that syntactic operations respect locality boundaries, with profound crosslinguistic consequences.

## Explainer

From X-bar theory, you know that every phrase has a **head** — the word that projects the phrase's category. A verb projects a VP; a noun projects a NP; a tense morpheme or auxiliary projects a TP; the complementizer position (the slot for *that*, *if*, *whether*, or the empty position at the top of a clause) projects a CP. These projections nest hierarchically: a CP dominates TP dominates VP. From your study of movement and transformations, you know that syntactic elements can be displaced from their base-generated positions, leaving a trace. **Head movement** is displacement that targets a head specifically — a single word, not a phrase — and moves it upward in the tree.

The **Head Movement Constraint (HMC)**, proposed by Travis (1984), states that a head X can only move to Y if Y is the head of the phrase that immediately dominates XP. In plain terms: heads can only move one step at a time, and they must land in the head position directly above them in the structure. They cannot skip levels. This is why English auxiliary inversion works as it does. In *He does leave*, the auxiliary *does* is in T (Tense head); in the question *Does he leave?*, *does* has moved from T up to C (Complementizer head), one step up the tree. This is licit under the HMC: T is immediately dominated by CP, so T's head can move to C.

Why can't the main verb do the same in English? In *He leaves*, the verb *leaves* is in V. To reach C, it would need to skip TP entirely — moving from V to C without stopping at T. The HMC blocks this: V is not immediately dominated by CP. In contrast, in French, main verbs *do* appear to move higher in the tree — *Jean aime Marie* has the verb appearing before adverbs in positions that indicate movement. This cross-linguistic contrast (English auxiliary movement vs. French full-verb movement) is explained by whether the language's V-to-T movement is overt or covert: English moves only auxiliaries overtly; French moves all finite verbs. The HMC permits movement at each step, so long as each individual step is local.

The deeper implication is that **syntactic locality** is a fundamental design feature of language. Movement is not unconstrained displacement — it respects structural boundaries at every level. This locality principle extends beyond head movement: the same basic insight (movement must be local; operations cannot see inside opaque boundaries) underlies constraints on wh-movement, raising, and control. Head movement gives you a clean, concrete test case for observing locality in action, because the landing sites and departure sites are discrete heads in a hierarchy you can diagram. Cross-linguistically, the variation in where verbs and auxiliaries surface is one of the best diagnostics for how a language's functional structure is organized — which heads are present, and which trigger overt movement versus covert displacement.

