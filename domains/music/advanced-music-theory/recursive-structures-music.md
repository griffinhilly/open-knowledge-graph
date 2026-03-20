---
id: recursive-structures-music
title: Recursive and Self-Similar Structures in Composition
domain: music
course: advanced-music-theory
prerequisites:
- id: rotational-form-analysis
  type: soft
- id: isorhythmic-structures-modern
  type: soft
- id: recurrence-relations
  type: soft
- id: recurrence-relations-definition
  type: soft
- id: recursion
  type: soft
- id: sequences-convergence
  type: soft
builds-toward:
- mathematical-structure-analysis
tags:
- recursion
- self-similarity
- form
- structure
stage: advanced
status: draft
---

# Recursive and Self-Similar Structures in Composition

## Core Idea
Recursive processes create structures where the whole mirrors parts at different scales. In music, this may manifest as nested phrase structures, fractal-like melodic unfolding, or self-embedding forms. Composers like George Lewis and David Cope use algorithmic recursion to generate complex forms from simple rules.

## Explainer

From your study of recursion in computing and recurrence relations in mathematics, you know the defining property: a recursive process is one that is defined in terms of itself at a smaller scale. In programming, a function calls itself on a simpler input until it reaches a base case. In mathematics, a recurrence relation expresses each term as a function of previous terms. **Recursive structures in music** apply the same logic to musical material: a compositional rule operates on a motive or phrase to produce a larger structure, and then that same rule applies again to the result, and again, nesting inward or outward across multiple timescales.

The simplest musical manifestation is **nested phrase structure**. A period consists of two phrases; each phrase consists of two sub-phrases; each sub-phrase consists of two gestures. The grouping hierarchy is self-similar — the relationship between parts at each level mirrors the relationship between levels above and below. This is not merely metaphorical; Lerdahl and Jackendoff's generative theory of tonal music formalizes exactly this recursion in a grammar analogous to Chomsky's linguistic phrase-structure rules. Sentences embed clauses, which embed phrases; musical periods embed phrases, which embed motives. The analogy is structural, not superficial.

At the compositional level, **self-similar processes** generate melodic or rhythmic patterns whose large-scale shape replicates their small-scale shape. A well-known example is the rhythmic pattern in Ligeti's études, where a single rhythmic figure recurs at multiple speeds simultaneously, producing a texture that looks the same when you zoom in or out. Fractal curves like the Cantor set — which you may have encountered in analysis — are the mathematical archetype: remove the middle third of a line segment, remove the middle third of each remaining segment, and continue infinitely. The result is a set that looks the same at every scale. Musical recursion does not usually carry the mathematical rigor of fractals, but it shares the structural logic: a rule iterated at multiple scales.

Algorithmically generated music pushes this further. David Cope's EMI system analyzed thousands of pieces to extract compositional rules, then applied those rules recursively to generate new pieces in the same style. George Lewis's Voyager uses real-time recursive decision trees to respond to improvising musicians. The computer's ability to apply the same rule indefinitely — with exact precision and at any scale — makes musical recursion a natural fit for algorithmic composition. Your background in recurrence relations gives you the mathematical lens: the base case is the seed motive, the recursive step is the transformation rule, and the resulting sequence of transformations is the unfolding composition. Understanding the rule is understanding the piece.
