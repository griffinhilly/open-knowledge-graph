---
id: lexical-functional-grammar
title: 'Lexical-Functional Grammar: Formal Framework'
domain: language-and-communication
course: linguistics
prerequisites:
- id: unification-mechanism
  type: hard
- id: constituent-trees-and-notation
  type: soft
tags:
- syntax
- framework
- formalism
stage: advanced
status: validated
---

# Lexical-Functional Grammar: Formal Framework

## Core Idea
Lexical-Functional Grammar (LFG) represents sentences using two parallel structures: c-structure (constituent trees) and f-structure (attribute-value matrices). This allows elegant treatment of long-distance dependencies and languages with flexible word order while maintaining linear constituency.

## Questions

```yaml
- question: "In LFG, the sentence 'Who did you say Maria saw?' poses a challenge because 'who' appears at the beginning but semantically functions as the object of 'saw.' How does LFG resolve this without moving 'who' in the tree?"
  type: multiple-choice
  options:
    - "LFG generates a second c-structure where 'who' appears in object position, and unification selects the correct one"
    - "'Who' in c-structure shares its f-structure value with the OBJ position in the embedded clause's f-structure"
    - "LFG uses a movement trace in c-structure, annotated with a coindex linking back to 'who'"
    - "F-structure ignores linear order, so the displacement is irrelevant — 'who' is simply assigned OBJ in f-structure without further mechanism"
  answer: 1
  explanation: "LFG's insight is that long-distance dependencies are resolved through f-structure sharing: the displaced element at the front of the sentence and the semantic position it occupies (object of 'saw') are linked to the same f-structure value. The c-structure correctly shows 'who' at the top, but unification propagates its f-structure specification down through the embedded clause until it fills the OBJ slot. No movement, no traces — the two levels work in parallel and the shared value bridges the gap."

- question: "Why did linguists develop LFG's two-level c-structure/f-structure architecture rather than enriching the c-structure alone?"
  type: multiple-choice
  options:
    - "C-structure is insufficient to represent tense and agreement features, which require a separate level"
    - "C-structure captures visible linear order but cannot elegantly represent grammatical relations that can surface in different positions across languages"
    - "F-structure was developed to represent semantic meaning, which c-structure cannot encode"
    - "LFG separates the levels because unification requires a feature matrix format that trees cannot provide"
  answer: 1
  explanation: "The core motivation is that grammatical relations (subject, object) are relatively stable across a language's paraphrases and cross-linguistic equivalents, while surface word order varies. In English 'Maria saw the book' and in an SOV language with object-first order, the subject and object relations are the same — but the c-structure positions differ. Encoding grammatical relations directly in c-structure (via fixed positions) cannot handle this variation without cumbersome additional mechanisms. F-structure captures what is functionally constant; c-structure captures what varies on the surface."

- question: "In LFG, the f-structure for 'Maria saw the book' and its Japanese equivalent (with different word order) would be different, because word order is part of what f-structure represents."
  type: true-false
  answer: false
  explanation: "This is the key misconception the two-level architecture is designed to avoid. F-structure represents grammatical functions (SUBJ, OBJ, TENSE, PRED) and their values — not word order. The f-structure for 'Maria saw the book' and a Japanese equivalent with object-first order would be identical: {SUBJ: [PRED: 'Maria'], OBJ: [PRED: 'book'], TENSE: PAST, PRED: 'see⟨SUBJ, OBJ⟩'}. C-structure captures the differing surface word orders; f-structure captures the shared grammatical relations. That is precisely the point of the separation."

- question: "Unification-based constraint satisfaction in LFG means that a sentence is grammatical if and only if its f-structure equations can all be satisfied simultaneously."
  type: true-false
  answer: true
  explanation: "This is LFG's formal definition of grammaticality. Annotations on c-structure nodes specify equations that the f-structure must satisfy. Unification then checks whether all those equations can be merged into a coherent attribute-value matrix without contradiction. If they can — the sentence is grammatical. If any two equations conflict (e.g., a word is specified as both nominative and accusative), unification fails and the sentence is ungrammatical. Grammaticality becomes a provable property of a formal system rather than relying solely on native-speaker intuition."

- question: "What work does f-structure do that c-structure cannot, and why does LFG need both levels rather than just enriching c-structure with more features?"
  type: short-answer
  answer: "C-structure captures what is visible on the surface: linear word order and phrase-level constituency. F-structure captures grammatical relations (SUBJ, OBJ, TENSE) independently of where they appear in the surface string. C-structure cannot elegantly handle two problems: long-distance dependencies (where a constituent's surface position differs from its grammatical role position) and cross-linguistic word-order freedom (where the same grammatical relations surface in different positions in different languages or constructions). Enriching c-structure to handle these cases requires adding complex movement rules or position-based feature proliferation. F-structure provides a clean, position-independent level where these relations are stated directly, with unification linking the two levels."
  explanation: "The two-level separation is a design choice: keep the surface representation simple (c-structure handles only what is observable), and let f-structure handle the invariant grammatical relations. This modularity is what allows LFG to cover typologically diverse languages without language-specific c-structure hacks."
```

## Explainer

You have learned about **unification** — the mechanism by which two feature structures are merged into one, failing if their values conflict. And from constituent trees, you know how to represent the phrase-level structure of a sentence hierarchically. Lexical-Functional Grammar puts these tools to work in parallel: every sentence receives two simultaneous structural descriptions, and both must be well-formed. Understanding why linguists developed this two-level architecture requires seeing what a single-level description cannot handle.

The first level — **c-structure** (constituent structure) — is the constituent tree you already know: S branches into NP and VP, VP branches into V and NP, and so on. C-structure captures the linear, hierarchical arrangement of words as they appear in the string. But c-structure alone runs into trouble with **long-distance dependencies**: in "Who did you say Maria saw?", the word "who" appears at the front of the sentence but functions as the object of "saw" — a grammatical relationship spanning an arbitrarily long distance across the tree. C-structure also struggles with **word-order freedom**: in languages like Japanese or Turkish, the subject can appear after the verb without changing meaning, but forcing flexible order into a rigid phrase-structure tree adds unwanted complexity.

The second level — **f-structure** (functional structure) — is an **attribute-value matrix**: a set of grammatical function labels (SUBJ, OBJ, TENSE, PRED) paired with their values. A typical f-structure for a simple sentence might be: {SUBJ: [PRED: 'Maria'], PRED: 'see⟨SUBJ, OBJ⟩', OBJ: [PRED: 'book'], TENSE: PAST}. The f-structure says who is doing what to whom, regardless of where those participants appeared in the surface string. "Maria saw the book" and a Japanese equivalent with the object first map to the same f-structure. Unification links c-structure to f-structure: annotations on c-structure nodes specify equations that the f-structure must satisfy, and unification checks whether those equations can all be satisfied simultaneously without contradiction.

The elegance of the two-structure approach is that it cleanly separates two kinds of linguistic information. C-structure handles what is visible on the surface — the linear order of words and their phrase-level groupings. F-structure handles grammatical relations — who is the subject, who is the object, what the tense is. Long-distance dependencies are resolved because the displaced element in c-structure simply **shares its f-structure value** with the position it semantically occupies. If the equations cannot be unified — for instance, if a word is specified both as nominative and as accusative — the structure is ungrammatical by definition. LFG thus makes grammaticality a provable property of a formal system rather than a matter of native-speaker intuition alone.
