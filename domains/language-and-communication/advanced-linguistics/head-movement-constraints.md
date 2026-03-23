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
stage: expert
status: draft
---

# Head Movement and Locality Constraints

## Core Idea
Head movement (single-word displacement) obeys the Head Movement Constraint: a head can only move to the head of its immediately dominating phrase. This explains why auxiliary verbs move to sentence-initial C in English ('Does he leave?'), but full verbs cannot (*'Leaves he?'). The constraint reveals that syntactic operations respect locality boundaries, with profound crosslinguistic consequences.

## Questions

```yaml
- question: "In English, 'Does he leave?' is grammatical but '*Leaves he?' is not—even though both reorder subject and verb. Under the Head Movement Constraint, the BEST explanation is:"
  type: multiple-choice
  options:
    - "'Leaves' is semantically too heavy for movement; auxiliaries are lightweight and therefore movable"
    - "'Does' is in T (Tense head) and moves to C (Complementizer head)—one step up the tree; 'leaves' is in V and would need to skip T entirely to reach C, violating the locality requirement"
    - "English prohibits main verb movement for purely historical reasons unrelated to syntactic structure"
    - "'Does' moves because it lacks semantic content; movement is blocked for content words with full lexical meaning"
  answer: 1
  explanation: "The HMC requires that a head can only move to the head of its *immediately dominating* phrase—one step at a time. 'Does' sits in T; CP immediately dominates TP, so T's head can move to C—one local step. 'Leaves' sits in V; VP is dominated by TP, which is in turn dominated by CP. To reach C, 'leaves' would need to skip TP entirely, violating the HMC. The constraint is about locality in the syntactic tree, not about semantic weight or lexical content."

- question: "A head X must reach head position Y, which is three levels above it in the syntactic tree. According to the Head Movement Constraint, the movement must proceed:"
  type: multiple-choice
  options:
    - "X cannot move at all; any movement spanning more than one level is categorically blocked"
    - "X can move directly to Y if Y is a functional head rather than a lexical head"
    - "X must move through each intermediate head position in a series of local steps, landing at each intermediate head before continuing upward"
    - "X can move to Y in one step only if there are no phonologically overt heads occupying the intermediate positions"
  answer: 2
  explanation: "The HMC permits long-distance head movement through successive local steps—each individual movement must be from a head to the immediately dominating head. This is analogous to a series of one-step moves rather than a single long jump. French main verb movement to positions above adverbs (demonstrating V-to-T movement) is permitted because each step is local: V moves to T, and T can then move to C. What is blocked is skipping a level—not moving through multiple levels via successive local steps."

- question: "In French, finite main verbs appear to move to positions higher in the syntactic tree than they do in English, yet this is fully consistent with the Head Movement Constraint."
  type: true-false
  answer: true
  explanation: "True. The HMC requires that each *individual step* of head movement be local—a head can only land in the immediately dominating head position. French main verbs move from V to T overtly (as shown by their position relative to adverbs and negation), and from T they can proceed to C if needed. Each step is local, so the HMC is satisfied. The cross-linguistic variation is not about whether the HMC applies, but about whether V-to-T movement is overt (French) or covert/absent (English)."

- question: "The Head Movement Constraint allows a head to move freely to any higher head position in the tree, provided it lands in a head position rather than a specifier or adjunct position."
  type: true-false
  answer: false
  explanation: "False. The HMC requires not just that a head land in a head position, but specifically in the head of the *immediately dominating* phrase. A head cannot skip levels even if its destination is a head position rather than a specifier or adjunct. It is the locality of the landing site—not just its categorical type—that the HMC restricts. This is the crucial point: movement must be local at every step."

- question: "Why is the Head Movement Constraint considered evidence that syntactic locality is a fundamental design feature of language, rather than an arbitrary restriction on movement?"
  type: short-answer
  answer: "The HMC shows that syntactic operations respect structural boundaries at every level—they cannot 'see past' intermediate positions to reach a distant target. This locality isn't arbitrary because it generalizes: the same constraint on ignoring intervening structure appears in wh-movement (islands), raising, and other displacement phenomena. Heads must move through intermediate positions rather than skipping them, which reveals that syntax processes structure incrementally and cannot access non-adjacent positions directly. This makes locality a general architectural principle of the grammar, not a stipulation about verbs or auxiliaries specifically."
  explanation: "The power of the HMC as evidence is that it explains a cross-linguistic pattern (auxiliary movement vs. full-verb movement, verb positioning relative to adverbs) without stipulating language-specific rules. The explanation falls out from a general locality principle. When a theoretical principle predicts observed variation across many languages and constructions without being stipulated for each separately, it is evidence that the principle reflects something fundamental about the grammatical system."
```

## Explainer

From X-bar theory, you know that every phrase has a **head** — the word that projects the phrase's category. A verb projects a VP; a noun projects a NP; a tense morpheme or auxiliary projects a TP; the complementizer position (the slot for *that*, *if*, *whether*, or the empty position at the top of a clause) projects a CP. These projections nest hierarchically: a CP dominates TP dominates VP. From your study of movement and transformations, you know that syntactic elements can be displaced from their base-generated positions, leaving a trace. **Head movement** is displacement that targets a head specifically — a single word, not a phrase — and moves it upward in the tree.

The **Head Movement Constraint (HMC)**, proposed by Travis (1984), states that a head X can only move to Y if Y is the head of the phrase that immediately dominates XP. In plain terms: heads can only move one step at a time, and they must land in the head position directly above them in the structure. They cannot skip levels. This is why English auxiliary inversion works as it does. In *He does leave*, the auxiliary *does* is in T (Tense head); in the question *Does he leave?*, *does* has moved from T up to C (Complementizer head), one step up the tree. This is licit under the HMC: T is immediately dominated by CP, so T's head can move to C.

Why can't the main verb do the same in English? In *He leaves*, the verb *leaves* is in V. To reach C, it would need to skip TP entirely — moving from V to C without stopping at T. The HMC blocks this: V is not immediately dominated by CP. In contrast, in French, main verbs *do* appear to move higher in the tree — *Jean aime Marie* has the verb appearing before adverbs in positions that indicate movement. This cross-linguistic contrast (English auxiliary movement vs. French full-verb movement) is explained by whether the language's V-to-T movement is overt or covert: English moves only auxiliaries overtly; French moves all finite verbs. The HMC permits movement at each step, so long as each individual step is local.

The deeper implication is that **syntactic locality** is a fundamental design feature of language. Movement is not unconstrained displacement — it respects structural boundaries at every level. This locality principle extends beyond head movement: the same basic insight (movement must be local; operations cannot see inside opaque boundaries) underlies constraints on wh-movement, raising, and control. Head movement gives you a clean, concrete test case for observing locality in action, because the landing sites and departure sites are discrete heads in a hierarchy you can diagram. Cross-linguistically, the variation in where verbs and auxiliaries surface is one of the best diagnostics for how a language's functional structure is organized — which heads are present, and which trigger overt movement versus covert displacement.

