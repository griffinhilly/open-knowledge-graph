---
id: ellipsis-and-implicit-content
title: Ellipsis and Covert Structure
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: compositionality-principle
  type: soft
- id: anaphora-and-discourse-dynamics
  type: hard
builds-toward:
- semantic-underdetermination-context
tags:
- ellipsis
- implicit-meaning
- discourse
stage: formal-systems
status: validated
---

# Ellipsis and Covert Structure

## Core Idea
Ellipsis occurs when parts of a sentence are omitted but meaning is recovered from context. Elided material must satisfy strict structural and semantic constraints, and recovery is systematic rather than purely pragmatic.

## Questions

```yaml
- question: "In 'Mary thinks she's brilliant, and I do too,' what does the sloppy reading mean, and why does it matter theoretically?"
  type: multiple-choice
  options:
    - "I also think that Mary is brilliant — the elided VP copies the exact meaning of the antecedent"
    - "I think that I am brilliant — the syntactic structure is reused but the pronoun re-binds to a new referent, producing a different truth condition"
    - "The sentence is ambiguous in a way that only context can resolve pragmatically, with no grammatical explanation"
    - "The sentence is ungrammatical because the pronoun cannot bind across the ellipsis site"
  answer: 1
  explanation: "The sloppy reading (I think I'm brilliant) arises because the grammar reuses the VP structure with variable binding rather than copying the exact semantic content. The pronoun 'she' in the antecedent is interpreted relative to its binder (Mary) — in the elided copy, the parallel pronoun re-binds to the new subject (I). This proves that ellipsis recovery computes grammatical structure with binding, not just meaning-copying. A purely pragmatic account predicting free meaning inference could not explain why both readings are available and grammatically distinct."

- question: "What is the strongest evidence that ellipsis resolution is governed by grammatical constraints rather than unconstrained pragmatic inference?"
  type: multiple-choice
  options:
    - "Elliptical sentences are processed faster than full sentences, suggesting they are grammatically simpler"
    - "Ellipsis is cross-linguistically common, appearing in languages with very different grammars"
    - "Interpretations that are pragmatically reasonable and contextually supported are systematically blocked when they fail to satisfy structural identity or semantic licensing conditions"
    - "The antecedent for elided material must always appear in the immediately preceding sentence"
  answer: 2
  explanation: "If ellipsis were purely pragmatic, any contextually supported interpretation should be recoverable. But grammar blocks many pragmatically reasonable interpretations: the elided VP must match the antecedent in specific structural ways; the antecedent must be of the right syntactic type; certain mismatches (e.g., active/passive) are systematically blocked or produce strict/sloppy contrasts. These patterns follow from grammatical architecture, not conversational inference. Speed of processing and cross-linguistic frequency don't bear directly on this question."

- question: "In VP ellipsis, the elided material is grammatically present as covert structure — it has syntactic representation even though it is not phonologically realized."
  type: true-false
  answer: true
  explanation: "True. Linguists posit that the elided VP is present in the syntactic structure at an abstract level (sometimes called LF, logical form) even though it has no phonological realization. This covert structure is what enables variable binding (the sloppy reading) and what must satisfy the identity conditions for licensing. If the VP were simply absent with no structural trace, there would be no way to explain why only certain interpretations are recoverable and why the strict/sloppy distinction falls out from the grammar."

- question: "Ellipsis resolution is purely pragmatic: listeners infer missing content from world knowledge and conversational context, without any special grammatical machinery."
  type: true-false
  answer: false
  explanation: "False. If ellipsis were purely pragmatic, we would expect much greater flexibility in what interpretations are recoverable — anything that makes contextual sense should be available. Instead, ellipsis obeys strict structural constraints: VP ellipsis requires a VP antecedent; sluicing requires a matching existential in the antecedent; gapping follows locality and parallelism constraints. These restrictions are not explained by conversational principles but by grammatical architecture. Pure pragmatics cannot predict which interpretations are blocked, only which ones are contextually plausible."

- question: "Why do the strict and sloppy readings of VP ellipsis provide evidence for covert grammatical structure rather than purely pragmatic interpretation?"
  type: short-answer
  answer: "The two readings arise from different ways the grammar processes the elided VP. The strict reading copies semantic content directly (I think Mary is brilliant). The sloppy reading reuses the syntactic structure and re-applies variable binding (I think I am brilliant). A purely pragmatic account would simply recover whichever meaning is most contextually plausible — it has no mechanism to derive two grammatically distinct interpretations from a single syntactic context. The fact that both readings are systematically available and predictable from structural properties of the antecedent (whether the pronoun is bound or free) shows that the grammar is computing interpretations over covert structural representations, not inferring them from context."
  explanation: "The strict/sloppy distinction is a diagnostic for the presence of syntactic variable binding in the ellipsis site. It reveals that the grammar treats the elided VP as a structural object with binding relations intact, not as a semantic shorthand."
```

## Explainer

You already know **anaphora**: expressions like pronouns or definite descriptions that pick up their reference from a prior linguistic antecedent in the discourse. Anaphoric resolution is systematic — it follows strict constraints about which expressions can bind which antecedents. **Ellipsis** extends this idea into the domain of structure itself: whole phrases or clauses are omitted from the pronounced string, yet their meaning is recovered from context in an equally systematic way. The omitted material is not simply inferred freely from background knowledge; it must satisfy strict structural and semantic conditions that are properties of the grammar, not just of communication.

The clearest case is **VP ellipsis**. In "Mary ran, and John did too," the second clause is interpreted as "John ran too." The missing verb phrase (*ran*) is not spoken but is grammatically present — linguists call this **covert structure**, syntactic material with no phonological realization. Recovery depends on an antecedent VP that must match the elided position in specific ways. Crucially, there can be a mismatch in interpretation: "Mary thinks she's brilliant, and I do too" can mean either that I think *she's* brilliant or that I think *I'm* brilliant. These **strict** versus **sloppy** readings reveal that the grammar is computing meaning, not just copying words — the sloppy reading reuses the syntactic structure with variable binding, producing a new truth condition rather than a direct copy.

**Sluicing** is another type where an entire clause is deleted after a *wh*-word: "Someone left, but I don't know who [left]." The bracketed material is absent from pronunciation but present in interpretation. The constraints here combine structural requirements (the deleted clause must fit the syntactic context of the antecedent) and semantic requirements (there must be a matching existential claim in the antecedent). **Gapping** — "Mary ordered pasta and John [ordered] risotto" — omits a repeated verbal element while retaining two arguments, and follows its own constraints on locality and parallelism. Each construction has a distinct fingerprint of what it permits and what it blocks.

What makes ellipsis theoretically important is that you know from **compositionality** that sentence meaning is built from parts by grammatical rules. Ellipsis shows that meaning can be recovered even when parts are absent — but only within tight structural limits, not by unconstrained pragmatic inference. If ellipsis resolution were purely pragmatic, you would predict much wider flexibility in what counts as a recoverable interpretation. Instead, the strict identity and structural constraints reveal that recovery operates at the level of **grammatical representation**, not just conversational guesswork. Ellipsis is thus evidence that the grammar-discourse interface has a systematic architecture, and that much of what language communicates is present in structure even when absent from sound.
