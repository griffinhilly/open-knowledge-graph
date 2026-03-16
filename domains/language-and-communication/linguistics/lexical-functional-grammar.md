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
stage: formal-systems
status: draft
---

# Lexical-Functional Grammar: Formal Framework

## Core Idea
Lexical-Functional Grammar (LFG) represents sentences using two parallel structures: c-structure (constituent trees) and f-structure (attribute-value matrices). This allows elegant treatment of long-distance dependencies and languages with flexible word order while maintaining linear constituency.

## Explainer

You have learned about **unification** — the mechanism by which two feature structures are merged into one, failing if their values conflict. And from constituent trees, you know how to represent the phrase-level structure of a sentence hierarchically. Lexical-Functional Grammar puts these tools to work in parallel: every sentence receives two simultaneous structural descriptions, and both must be well-formed. Understanding why linguists developed this two-level architecture requires seeing what a single-level description cannot handle.

The first level — **c-structure** (constituent structure) — is the constituent tree you already know: S branches into NP and VP, VP branches into V and NP, and so on. C-structure captures the linear, hierarchical arrangement of words as they appear in the string. But c-structure alone runs into trouble with **long-distance dependencies**: in "Who did you say Maria saw?", the word "who" appears at the front of the sentence but functions as the object of "saw" — a grammatical relationship spanning an arbitrarily long distance across the tree. C-structure also struggles with **word-order freedom**: in languages like Japanese or Turkish, the subject can appear after the verb without changing meaning, but forcing flexible order into a rigid phrase-structure tree adds unwanted complexity.

The second level — **f-structure** (functional structure) — is an **attribute-value matrix**: a set of grammatical function labels (SUBJ, OBJ, TENSE, PRED) paired with their values. A typical f-structure for a simple sentence might be: {SUBJ: [PRED: 'Maria'], PRED: 'see⟨SUBJ, OBJ⟩', OBJ: [PRED: 'book'], TENSE: PAST}. The f-structure says who is doing what to whom, regardless of where those participants appeared in the surface string. "Maria saw the book" and a Japanese equivalent with the object first map to the same f-structure. Unification links c-structure to f-structure: annotations on c-structure nodes specify equations that the f-structure must satisfy, and unification checks whether those equations can all be satisfied simultaneously without contradiction.

The elegance of the two-structure approach is that it cleanly separates two kinds of linguistic information. C-structure handles what is visible on the surface — the linear order of words and their phrase-level groupings. F-structure handles grammatical relations — who is the subject, who is the object, what the tense is. Long-distance dependencies are resolved because the displaced element in c-structure simply **shares its f-structure value** with the position it semantically occupies. If the equations cannot be unified — for instance, if a word is specified both as nominative and as accusative — the structure is ungrammatical by definition. LFG thus makes grammaticality a provable property of a formal system rather than a matter of native-speaker intuition alone.
