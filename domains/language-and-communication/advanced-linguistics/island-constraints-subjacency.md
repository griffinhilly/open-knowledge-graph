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
stage: advanced
status: draft
---

# Island Constraints and Subjacency

## Core Idea
Island constraints prohibit extraction from certain syntactic domains (relative clauses, coordinate structures, adjuncts), limiting where wh-constituents can originate. Subjacency formalizes this by requiring moved elements to cross no more than one bounding node per derivational step.

## How It's Best Learned
Test each major island type systematically with grammaticality judgments; compare with free extraction contexts to identify the domains that block movement.

## Common Misconceptions
Islands are not absolute barriers; pragmatic context, processing cost, and language variation affect island sensitivity, suggesting the constraints are syntactic violability principles rather than hard rules.

## Explainer

Your prerequisites in movement and transformations, and in X-bar theory, give you the tools to understand island constraints. From movement, you know that syntactic derivations can displace constituents from their base positions — a wh-word like "what" can originate as the object of a verb deep in the structure and move to the front of the sentence: *What did she buy?* (from the underlying *She did buy what*). From X-bar theory, you know that phrases are built hierarchically, with specifiers, heads, and complements. **Island constraints** are restrictions on where that movement can begin — or more precisely, they identify certain syntactic domains from which extraction is impossible or severely degraded.

Consider three classic island types. First, the **relative clause island**: *What did she meet the man who bought?* — ungrammatical. The object of "bought" is trapped inside the relative clause "who bought ___". You cannot extract it. Compare: *What did she meet the man who bought yesterday?* — still ungrammatical, no matter how the sentence is arranged. Second, the **coordinate structure island**: *What did she buy a book and read?* — trying to extract the object of only one conjunct of a coordination is impossible. The "Coordinate Structure Constraint" requires that you extract from both conjuncts equally or neither. Third, the **adjunct island**: *What did she leave before she bought?* — extraction from the subordinate adjunct clause is blocked.

Ross (1967) identified these patterns empirically; Chomsky's **Subjacency Condition** (1973) attempted to provide a unified formal explanation. Subjacency states that a moved element cannot cross more than one **bounding node** in a single derivational step. Bounding nodes are typically specified as NP and S (or IP in later frameworks) — the main clause nodes that create structural barriers. A relative clause is embedded inside an NP, which is inside another S, so extracting from a relative clause would require the moved element to cross two bounding nodes in one step — a subjacency violation. The elegance of subjacency was that a single formal principle could explain multiple empirically distinct island effects.

However, subjacency immediately faced problems. First, **which nodes count as bounding nodes varies across languages** — in Italian and Spanish, extraction from relative clauses is somewhat more acceptable than in English, which is difficult to explain if islands are purely syntactic. Second, **not all island effects are equally strong**: extracting from a Complex NP ("What did you believe the claim that she bought?") feels worse than extracting from a simple adjunct, and these gradations are hard to capture in an all-or-nothing syntactic constraint. Third, **processing accounts** have argued that "island violations" partly reflect working memory costs of maintaining long-distance dependencies through complex structures, not a categorical grammatical prohibition.

These complications have led to several successor theories: the **Phase Impenetrability Condition** in Minimalism treats phases (vP and CP) as the relevant barriers; **Optimality-theoretic** approaches treat islands as violable ranked constraints; experimental linguists have shown that acceptability judgments are gradient and context-sensitive, not binary. What survives across all these approaches is the core empirical observation: human languages systematically restrict movement from certain syntactic domains, and these restrictions are not arbitrary but fall into identifiable categories. Island constraints are thus a window into the nature of syntactic computation — evidence that grammar has internal architecture that limits what operations can reach what positions, making syntax not just a combinatorial system but one with structural memory of its own derivational history.

