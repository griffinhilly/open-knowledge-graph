---
id: empty-names-fictional
title: Empty Names and Fictional Discourse
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: russell-definite-descriptions
  type: hard
- id: reference-determination
  type: hard
tags:
- empty-names
- fiction
- reference
stage: formal-systems
status: validated
---

# Empty Names and Fictional Discourse

## Core Idea
Statements about fictional characters and empty names pose semantic challenges: how are they meaningful without referents? Solutions include treating them as quantified descriptions, denying truth values, or positing abstract objects. Different theories accommodate fictional discourse differently.

## Questions

```yaml
- question: "A philosopher argues that 'Sherlock Holmes is a detective' is true — not just pretend-true. Which theory best supports this claim while avoiding commitment to nonexistent concrete objects?"
  type: multiple-choice
  options:
    - "The Russellian description theory — the sentence is a true existential claim about actual detectives"
    - "The abstract object theory — Holmes is a real abstract entity created by authorship, which genuinely has the property of being a detective"
    - "Pretense theory — the sentence is literally true because fiction-internal claims count as literal assertions"
    - "Direct reference theory — 'Sherlock Holmes' refers successfully because names always refer"
  answer: 1
  explanation: "The abstract object theory holds that Conan Doyle created a real abstract entity called Sherlock Holmes, which genuinely (though abstractly) has the property of being-a-detective-according-to-the-stories. This makes the sentence true without requiring a nonexistent concrete person. Option A is wrong — the Russellian view makes the sentence false (no actual person satisfies the descriptions). Option C mischaracterizes pretense theory: pretense theorists say the sentence is fictionally true (true in the pretense), not literally true. Option D fails because direct reference theory cannot handle empty names — without a referent, meaning breaks down."

- question: "What is the fundamental tension that empty names create for direct reference theories of meaning?"
  type: multiple-choice
  options:
    - "Direct reference theories cannot explain why different names can refer to the same object"
    - "Direct reference theories equate a name's meaning with its referent, so a name without a referent appears to have no meaning — yet sentences with empty names are still understood"
    - "Direct reference theories rely on descriptions, which break down for proper names"
    - "Direct reference theories predict that fictional names refer to the authors who invented them"
  answer: 1
  explanation: "Direct reference theories (like Millian theories) hold that the semantic content of a name just is its referent. If 'Sherlock Holmes' has no referent, the theory predicts the name is semantically empty — contributing nothing to the proposition. Yet 'Sherlock Holmes was a detective' is clearly understood, apparently meaningful, and seems true in some sense. This is the core puzzle: we need a theory that accounts for the apparent meaningfulness and even truth-aptness of fictional discourse without a real referent. Options A and C describe different problems (co-reference and description theories, respectively). Option D is not a prediction of direct reference theory."

- question: "According to Russell's theory applied to fictional discourse, 'Sherlock Holmes lived at 221B Baker Street' is literally false."
  type: true-false
  answer: true
  explanation: "On Russell's approach, apparent names like 'Sherlock Holmes' are disguised definite descriptions or existential claims. 'Sherlock Holmes lived at 221B Baker Street' becomes something like 'There exists exactly one person satisfying the Holmes-descriptions, and that person lived at 221B Baker Street.' Since no actual person satisfies the Holmes-descriptions, the sentence is false — not meaningless (it has a truth value), but false. Many philosophers find this counterintuitive because we don't normally treat fiction-internal claims the same way as false empirical claims, but on strict Russellian grounds, that is the result."

- question: "Causal-historical theories of reference straightforwardly handle fictional names, because the author's act of naming a character counts as the original 'baptism' that grounds the name's reference."
  type: true-false
  answer: false
  explanation: "Causal-historical theories require that a name be connected by a causal chain to an actual object that was 'baptized' at the original naming event. For fictional names, there is no actual object — Conan Doyle did not dub a real person 'Sherlock Holmes.' The act of writing fiction is a deliberate act of reference-failure, not a baptism that connects language to reality. This means causal-historical theories need significant supplementation (or revision) to handle fictional names: either a special category of 'pretend baptism,' appeal to abstract objects as the baptized entity, or some other move. The theory does not straightforwardly apply as-is."

- question: "Pretense theory elegantly handles most fictional discourse, but struggles with cross-context statements like 'Sherlock Holmes is more famous than any real detective.' Why?"
  type: short-answer
  answer: "Cross-context statements mix entities from the pretense (Sherlock Holmes) with real-world entities (actual detectives), making it unclear how the pretense framework applies. Within a fiction, 'Holmes is a detective' can be understood as a move in a game of make-believe. But comparing Holmes's fame to that of real people seems to require Holmes to exist in the same domain as those real people — so the statement cannot be merely a move in a pretense governed by the fiction. Pretense theory handles intra-fiction claims well but lacks a clear account of these cross-domain comparisons."
  explanation: "Walton's pretense theory is powerful for fiction-internal claims and for explaining why we can engage emotionally with fiction without being irrational. But the cross-context problem reveals a genuine gap: we talk about fictional characters as if they have properties that can be compared with real things (fame, cultural influence, aesthetic complexity). This pushes toward either the abstract object view (Holmes is a real abstract entity that can genuinely be famous) or a hybrid approach. Most philosophers now acknowledge that no single theory captures all of fictional discourse without remainder."
```

## Explainer

An **empty name** is a name that appears grammatically well-formed but lacks a real-world referent. "Sherlock Holmes," "Zeus," "Vulcan" (the hypothetical planet) — these terms look just like "London" or "Einstein" syntactically, but nothing in reality corresponds to them. This creates a serious problem for a direct reference theory of meaning, which holds that the meaning of a name just is its referent. If "Sherlock Holmes" has no referent, the theory seems to predict that sentences containing it are meaningless or semantically defective. Yet "Sherlock Holmes lived at 221B Baker Street" seems perfectly understandable — and even true in some sense.

You've already studied Russell's theory of definite descriptions, which provides one classical response. Russell's move was to show that apparent names like "the present King of France" are not genuine names but disguised descriptions — logical abbreviations for existentially quantified claims. The same strategy can be applied to fictional names: "Sherlock Holmes is a detective" is parsed as something like "There exists exactly one entity satisfying the Holmes descriptions, and it is a detective." This gives the sentence a truth value (false, since no actual person satisfies the description) without requiring a real referent for the name. The Russellian approach preserves classical two-valued logic but treats fictional discourse as systematically false — which many find counterintuitive, since we don't normally say fiction-internal claims are false in the same way as empirical falsehoods.

An alternative is **Meinongianism** — the view that there are objects that do not exist but still have properties. On this account, Sherlock Holmes has being in a thin sense; he is a nonexistent object with the property of being a detective. Most analytic philosophers find this ontology extravagant, but it does preserve the intuition that "Sherlock Holmes is a detective" is straightforwardly true. A more palatable middle ground is the **abstract object** view: fictional characters are real abstract entities created by acts of authorship. On this view, Conan Doyle brought into existence an abstract object called Sherlock Holmes, which genuinely has the property of being-a-detective-according-to-the-stories. This preserves truth while avoiding nonexistent concrete objects.

A third approach, influential through Kendall Walton's work, is **pretense theory**: fictional discourse is a sophisticated kind of make-believe. When we say "Sherlock Holmes lived at 221B Baker Street," we are not asserting something about reality — we are performing a move in a collective game of pretense governed by the fiction. The statement is fictionally true, meaning true in the pretense, not literally true. This approach elegantly handles the range of fictional talk — internal claims about what happens in the story, comparative claims across fictions, and critical assessments — without positing mysterious abstract objects or nonexistent concreta. The challenge is accounting for cross-context statements: "Sherlock Holmes is more famous than any real detective" seems to compare a fictional entity to real ones, which is hard to capture as mere pretense.

The reference-determination theory you've already studied raises an additional dimension. Causal-historical theories of reference say names refer by virtue of causal chains connecting current uses to an original baptism. For real names, this works smoothly. For fictional names, there was no baptism event that connected the name to an actual referent — the author invented the character. This suggests fictional names may have a different semantic mechanism from ordinary proper names, or that the causal theory needs supplementation to handle cases of deliberate fiction, myth, and reference failure.

