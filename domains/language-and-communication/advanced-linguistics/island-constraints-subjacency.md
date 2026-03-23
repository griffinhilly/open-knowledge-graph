---
id: island-constraints-subjacency
title: Island Constraints and Subjacency
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
status: validated
---

# Island Constraints and Subjacency

## Core Idea
Island constraints prohibit extraction from certain syntactic domains (relative clauses, coordinate structures, adjuncts), limiting where wh-constituents can originate. Subjacency formalizes this by requiring moved elements to cross no more than one bounding node per derivational step.

## How It's Best Learned
Test each major island type systematically with grammaticality judgments; compare with free extraction contexts to identify the domains that block movement.

## Common Misconceptions
Islands are not absolute barriers; pragmatic context, processing cost, and language variation affect island sensitivity, suggesting the constraints are syntactic violability principles rather than hard rules.

## Questions

```yaml
- question: "The sentence 'What did you believe the claim that she bought?' is ungrammatical. According to subjacency, why?"
  type: multiple-choice
  options:
    - "The verb 'believe' cannot take a wh-complement under any syntactic conditions"
    - "Wh-movement is never permitted when the gap is located more than one clause away from the landing site"
    - "Extracting 'what' requires crossing two bounding nodes—the NP containing the relative clause and the higher S—in a single derivational step, violating subjacency"
    - "The object position of 'bought' is not a valid extraction site because relative clauses have no specifier position"
  answer: 2
  explanation: "Subjacency prohibits any single movement step from crossing more than one bounding node (typically NP and S/IP). 'The claim that she bought ___' is a complex NP—the relative clause is embedded inside an NP, itself inside a higher clause. Extracting 'what' from the object position of 'bought' would require crossing both the NP boundary and the S boundary in one step: a subjacency violation. Compare the grammatical 'What did you believe she bought?' where there is no complex NP and movement can proceed via successive-cyclic steps through intermediate positions."

- question: "Which statement best characterizes island constraints across human languages?"
  type: multiple-choice
  options:
    - "Island constraints are categorical and equally strong in all languages, confirming that they are a universal syntactic primitive"
    - "Island constraints apply only in languages that front wh-words to sentence-initial position"
    - "Island sensitivity varies cross-linguistically and shows gradient acceptability within languages, suggesting the constraints may be violable principles rather than absolute rules"
    - "All languages obey the coordinate structure constraint but differ only in whether they observe complex NP islands"
  answer: 2
  explanation: "Cross-linguistic variation is one of the central challenges for purely syntactic accounts of islands. Italian and Spanish permit some extractions from relative clauses that are blocked in English. Within languages, experimental work shows that acceptability judgments are gradient—not binary—and vary with context and processing load. These gradations are hard to reconcile with islands as inviolable syntactic prohibitions. They have motivated Optimality-theoretic accounts (violable ranked constraints) and processing-based explanations (island effects as working-memory costs), neither of which treat islands as universal categorical rules."

- question: "According to subjacency, extraction from a relative clause is blocked because the moved element would need to cross two bounding nodes—the NP containing the relative clause and the higher S—in a single derivational step."
  type: true-false
  answer: true
  explanation: "This is correct and is the core of the subjacency account of relative clause islands. A relative clause is embedded inside an NP (as in 'the man [NP who bought ___]'), and that NP is inside a higher sentence (S/IP). Movement out of the relative clause in one step crosses both the NP boundary and the S boundary simultaneously. Subjacency allows crossing at most one bounding node per step. Successive-cyclic movement can avoid violations in other contexts but cannot rescue movement from inside an embedded NP—there is no intermediate landing site within the NP that would allow incremental escape."

- question: "Ross's (1967) empirical island generalizations are fully and adequately explained by Chomsky's Subjacency Condition, leaving no residual counterexamples or competing theoretical accounts."
  type: true-false
  answer: false
  explanation: "False. Subjacency provided an elegant unified account of several island types but faced immediate empirical problems: cross-linguistic variation in island sensitivity (Italian allows extractions that English blocks); gradient rather than categorical acceptability within languages; and difficulty specifying which nodes count as bounding nodes across languages. These failures motivated successor theories: the Phase Impenetrability Condition in Minimalism, violable-constraint accounts in Optimality Theory, and processing-based explanations that attribute island effects partly to working memory costs rather than syntactic prohibition. The empirical landscape remains actively theorized."

- question: "What is the core empirical phenomenon that island constraints describe, and what evidence challenges the view that island sensitivity is purely a syntactic phenomenon?"
  type: short-answer
  answer: "Island constraints describe the observation that syntactic movement (wh-movement, topicalization, etc.) is systematically blocked from certain structural domains—relative clauses, coordinate structures, adjuncts—even when the same type of movement is grammatical elsewhere. Evidence against a purely syntactic account includes: (1) cross-linguistic variation (Italian allows relative clause extractions that English blocks); (2) gradient acceptability judgments within languages (island violations are not uniformly impossible but vary in severity); (3) processing accounts showing that many 'island effects' correlate with working memory demands of maintaining long-distance dependencies through complex structures."
  explanation: "The key insight is that subjacency sought to derive multiple distinct island types from one formal principle—an elegant explanatory strategy. But the empirical departures from categorical ungrammaticality across languages and contexts reveal that 'island sensitivity' is not a single, purely syntactic phenomenon. Modern theories treat it as a cluster of effects with both syntactic and non-syntactic contributors, making islands a revealing window into how grammar and processing interact."
```

## Explainer

Your prerequisites in movement and transformations, and in X-bar theory, give you the tools to understand island constraints. From movement, you know that syntactic derivations can displace constituents from their base positions — a wh-word like "what" can originate as the object of a verb deep in the structure and move to the front of the sentence: *What did she buy?* (from the underlying *She did buy what*). From X-bar theory, you know that phrases are built hierarchically, with specifiers, heads, and complements. **Island constraints** are restrictions on where that movement can begin — or more precisely, they identify certain syntactic domains from which extraction is impossible or severely degraded.

Consider three classic island types. First, the **relative clause island**: *What did she meet the man who bought?* — ungrammatical. The object of "bought" is trapped inside the relative clause "who bought ___". You cannot extract it. Compare: *What did she meet the man who bought yesterday?* — still ungrammatical, no matter how the sentence is arranged. Second, the **coordinate structure island**: *What did she buy a book and read?* — trying to extract the object of only one conjunct of a coordination is impossible. The "Coordinate Structure Constraint" requires that you extract from both conjuncts equally or neither. Third, the **adjunct island**: *What did she leave before she bought?* — extraction from the subordinate adjunct clause is blocked.

Ross (1967) identified these patterns empirically; Chomsky's **Subjacency Condition** (1973) attempted to provide a unified formal explanation. Subjacency states that a moved element cannot cross more than one **bounding node** in a single derivational step. Bounding nodes are typically specified as NP and S (or IP in later frameworks) — the main clause nodes that create structural barriers. A relative clause is embedded inside an NP, which is inside another S, so extracting from a relative clause would require the moved element to cross two bounding nodes in one step — a subjacency violation. The elegance of subjacency was that a single formal principle could explain multiple empirically distinct island effects.

However, subjacency immediately faced problems. First, **which nodes count as bounding nodes varies across languages** — in Italian and Spanish, extraction from relative clauses is somewhat more acceptable than in English, which is difficult to explain if islands are purely syntactic. Second, **not all island effects are equally strong**: extracting from a Complex NP ("What did you believe the claim that she bought?") feels worse than extracting from a simple adjunct, and these gradations are hard to capture in an all-or-nothing syntactic constraint. Third, **processing accounts** have argued that "island violations" partly reflect working memory costs of maintaining long-distance dependencies through complex structures, not a categorical grammatical prohibition.

These complications have led to several successor theories: the **Phase Impenetrability Condition** in Minimalism treats phases (vP and CP) as the relevant barriers; **Optimality-theoretic** approaches treat islands as violable ranked constraints; experimental linguists have shown that acceptability judgments are gradient and context-sensitive, not binary. What survives across all these approaches is the core empirical observation: human languages systematically restrict movement from certain syntactic domains, and these restrictions are not arbitrary but fall into identifiable categories. Island constraints are thus a window into the nature of syntactic computation — evidence that grammar has internal architecture that limits what operations can reach what positions, making syntax not just a combinatorial system but one with structural memory of its own derivational history.

