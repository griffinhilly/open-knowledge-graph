---
id: linguistic-typology-formal
title: Formal Linguistic Typology and Cross-Linguistic Variation
domain: language-and-communication
course: linguistics
prerequisites:
- id: linguistic-typology
  type: hard
builds-toward:
- principles-and-parameters-theory
tags:
- typology
- cross-linguistic
- variation
- universals
stage: formal-systems
status: validated
---

# Formal Linguistic Typology and Cross-Linguistic Variation

## Core Idea
Formal typology catalogs systematic cross-linguistic variation and explains it through formal constraints and parameters. Languages cluster by word order, case systems, and argument marking, yet all languages encode agency, tense, and aspect. Formal analysis reveals deep structural similarities beneath surface diversity: constraints permit only certain features to co-occur, limiting the space of possible human languages.

## Questions

```yaml
- question: "A linguist discovers a language with VSO word order (verb first, then subject, then object). Based on formal typological parameters, what other feature would you most expect to find?"
  type: multiple-choice
  options:
    - "Postpositions (e.g., 'the house from') rather than prepositions ('from the house')"
    - "Prepositions (e.g., 'from the house') rather than postpositions"
    - "SOV word order in subordinate clauses, since most languages use mixed orders across clause types"
    - "An absence of case morphology, since VSO languages express grammatical relations through word order alone"
  answer: 1
  explanation: "VSO order is head-initial: the verb (head of the clause) precedes its subject and object complements. The head-directionality parameter predicts that head-initial languages consistently place heads before complements across grammatical categories — including prepositional phrases, where the preposition (head) precedes the noun phrase it governs. Greenberg's universals confirm this: if a language has VSO order, it almost invariably has prepositions rather than postpositions. Option A (postpositions) is the head-final prediction — the opposite setting. Option C is wrong because the head-directionality parameter cascades consistently across all phrase types within a language, not just main clauses."

- question: "Why does formal typology claim that the actual space of human language variation is far smaller than the logically possible space?"
  type: multiple-choice
  options:
    - "Because the human vocal tract can only produce a limited range of sounds, constraining which phonological contrasts are possible"
    - "Because formal parameters link clusters of grammatical properties, so setting one parameter excludes combinations that would require inconsistent settings"
    - "Because all languages descend from a common ancestral proto-language that imposed its original structure on its descendants"
    - "Because language contact over millennia has gradually erased structural differences between geographically neighboring languages"
  answer: 1
  explanation: "The logical space of possible languages is vast — you can imagine any combination of word orders, case systems, and argument-marking strategies. But actual languages don't distribute randomly across this space; they cluster around parameter settings that make consistent predictions across many properties simultaneously. A language cannot easily be VSO (head-initial) for main clauses but use postpositions (head-final) for noun phrases, because both derive from the same head-directionality setting. Formal typology explains the gaps — the logically possible but unattested language types — as ruled out by formal constraints, not historical accident. Option A concerns phonology, not the syntactic/morphological variation that typological parameters address."

- question: "The head-directionality parameter predicts that a head-final language will tend to have postpositions rather than prepositions, because postpositions place the head after its complement."
  type: true-false
  answer: true
  explanation: "Head-final languages place grammatical heads after their complements across all phrase types. In a verb phrase, the verb follows its objects (SOV order). In an adpositional phrase, the adposition follows the noun phrase it governs — making it a postposition ('the house from') rather than a preposition ('from the house'). This is precisely the kind of cross-category prediction that makes the parameter concept powerful: a single binary setting cascades through the grammar, linking word order, adposition type, and other structural features. Japanese (head-final: SOV + postpositions) and English (head-initial: SVO + prepositions) illustrate the predicted correlation."

- question: "Typological implicational universals state that all human languages share every grammatical property, leaving no room for cross-linguistic variation."
  type: true-false
  answer: false
  explanation: "Implicational universals take the conditional form 'if a language has property X, then it also has property Y' — not 'all languages have property X.' They constrain variation without eliminating it. For example: 'if a language has VSO order, it has prepositions' doesn't say all languages are VSO or that all languages have prepositions. It says that the combination VSO + postpositions is ruled out. The universals mark which combinations don't occur in human languages, carving out the attested portion of the logically possible space. Languages still vary freely within the constraints — the universals describe the boundaries, not the content."

- question: "Explain what a typological implicational universal is, and how the existence of such universals supports the view that human language variation is constrained by formal grammatical principles rather than being arbitrary."
  type: short-answer
  answer: "A typological implicational universal is a cross-linguistic generalization of the form 'if a language has property X, it also has property Y,' where the relationship holds across virtually all known languages. For example, Greenberg's Universal 4: if a language has VSO order, it almost always has prepositions. These universals constrain the typological space — the set of logically possible language types — by ruling out certain property combinations. If language variation were arbitrary, we'd expect all logically possible combinations to appear roughly equally. Instead, we find systematic gaps (VSO + postpositions is vanishingly rare) and systematic correlations. This pattern is best explained by formal principles — parameters or constraints — that link grammatical properties, making some combinations coherent and others internally inconsistent."
  explanation: "The formal explanation is stronger than a frequency-based one: it's not just that VSO + postpositions is rare, it's that the head-directionality parameter predicts it should be absent because it would require inconsistent settings within the same grammar. The universals thus become evidence for an abstract grammatical architecture shared by all human languages — one that varies in parameter settings but not in the formal principles governing how those settings interact."
```

## Explainer

From your prerequisite work in linguistic typology, you already know that languages vary enormously on the surface — different word orders, different sounds, different ways of marking tense and possession — and yet these variations are not random. Certain patterns appear universally or near-universally; others are strongly correlated. **Formal linguistic typology** moves beyond cataloging these patterns to explaining them: why do languages cluster in the ways they do, and what principled constraints rule out the patterns that never appear?

The central concept is the **parameter** — a binary or small-scale formal choice in a language's grammar that, when set one way or another, predicts a cluster of downstream properties. The classic example is the **head-directionality parameter**: languages consistently place grammatical heads (verbs, prepositions, nouns) either before their complements (head-initial: English, French) or after them (head-final: Japanese, Turkish). This single setting cascades through the grammar: head-initial languages tend to have prepositions and SVO or VSO word order; head-final languages tend to have postpositions and SOV word order. You don't observe random mixtures of these properties because the parameter links them formally. The Principles and Parameters framework, which you'll study next, builds this insight into a generative theory of cross-linguistic variation.

The complementary concept is the **typological implicational universal** — a constraint of the form "if a language has property X, it also has property Y." Greenberg observed that if a language has VSO order, it almost invariably has prepositions rather than postpositions. If a language has both nominative-accusative and ergative-absolutive patterns, the ergative pattern applies to transitive perfectives while the nominative pattern applies elsewhere (split ergativity). These universals constrain the **typological space** — the set of logically possible language types. Formal typology is the project of explaining why the actual space of human languages is so much smaller than the logical space: what formal principles rule out the attested impossibilities?

The practical payoff is a more principled view of language acquisition and change. If grammars are governed by formal parameters, then acquiring a first language can be modeled as **parameter-setting** — a child hears enough input to fix the head-directionality parameter, and a cluster of other grammatical properties falls into place automatically. Language change, by this view, can occur when a parameter gradually shifts as speakers reanalyze input. This formal apparatus turns descriptive typology into a testable theory: the distribution of cross-linguistic variation becomes evidence for or against specific formal proposals about what the parameters actually are.

Formal typology also sharpens the distinction between **deep structure** and **surface form**. Two languages with radically different surface appearance — an SOV language with postpositions and an SVO language with prepositions — may share the same underlying formal architecture instantiated with different parameter settings. Conversely, two languages with similar-looking word orders may achieve them by entirely different formal mechanisms. This is the insight that makes formal typology more than an empirical catalog: it is a window into the abstract architecture that all human grammars share.
