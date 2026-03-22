---
id: open-sets-definition-examples
title: Open Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: topological-spaces-definition-examples
  type: hard
builds-toward:
- closed-sets-definition-examples
- neighborhoods-topology-definition
tags:
- open-sets
- fundamental
stage: formal-systems
status: draft
---

# Open Sets in Topological Spaces

## Core Idea
Open sets are the members of the topology τ and form the basic structure. A set U is open iff for every point x in U, there exists an open set V with x ∈ V ⊆ U. Open sets are the fundamental building blocks of topology; all other topological concepts (closure, continuity, compactness) are defined in terms of open sets.

## Questions

```yaml
- question: "Student A says the interval (0,1) ⊂ ℝ is open. Student B says it is not open. Can both be correct simultaneously?"
  type: multiple-choice
  options:
    - "No — a set either is or isn't open; there's no ambiguity"
    - "Yes — both can be correct if they are using different topologies on ℝ"
    - "Yes — openness is always a matter of interpretation near the boundary"
    - "No — (0,1) is always open because it contains no boundary points"
  answer: 1
  explanation: "Openness is not intrinsic to a set — it is relative to the chosen topology. In the standard topology on ℝ, (0,1) is open. In the trivial topology {∅, ℝ}, only ∅ and ℝ are open, so (0,1) is not open. Both students can be correct because they are implicitly using different topologies. This is the central insight: asking 'is this set open?' is meaningless without specifying which topology τ you are working in."

- question: "Which of the following must always be a member of any topology τ on a set X, by the axioms of a topological space?"
  type: multiple-choice
  options:
    - "Every singleton set {x} for x ∈ X"
    - "The empty set ∅ and the whole space X"
    - "All subsets of X"
    - "All complements of finite sets"
  answer: 1
  explanation: "The axioms of a topological space require that τ contains ∅ and X, is closed under arbitrary unions, and is closed under finite intersections. ∅ and X are always open in every topology. Singletons are open in the discrete topology but not in general (e.g., not in the trivial topology). The collection of all subsets is the discrete topology — one valid choice but not required. Option D describes co-finite sets, which define a specific topology, not a universal axiom."

- question: "In any topological space (X, τ), the set X itself and the empty set ∅ are both open and closed (clopen)."
  type: true-false
  answer: true
  explanation: "By the axioms, both ∅ and X are always in τ, so they are open. Their complements are X and ∅ respectively, which are also in τ — so they are closed too. Being both open and closed (clopen) is not a contradiction; it's a feature of the definition. This surprises students who carry Euclidean intuitions about 'open' and 'closed' being mutually exclusive, but the topological definitions simply do not require that."

- question: "A set that is not open in a given topology must be closed in that topology."
  type: true-false
  answer: false
  explanation: "Open and closed are not complementary categories in topology — a set can be neither. For example, in the standard topology on ℝ, the half-open interval [0,1) is neither open (it contains the boundary point 0 with no open neighborhood inside the set) nor closed (its complement (−∞,0) ∪ [1,∞) is not open). The misconception that 'not open means closed' is a carryover from everyday language, but the topological definition of closed is a separate condition: a set is closed if its complement is open."

- question: "Why is it meaningless to ask 'is this set open?' without first specifying a topology? What does the question actually depend on?"
  type: short-answer
  answer: "Openness is membership in τ, the topology. The same set can belong to one topology (making it open) and not belong to another (making it not open). The question 'is S open?' has no answer until you specify which collection τ you are using as the topology on X."
  explanation: "This is the foundational shift from analysis to topology. In real analysis, 'open' has a metric-based definition inherited from the standard topology. In abstract topology, there is no metric — open sets are primitive objects defined by their membership in τ. A topology is just a family of subsets satisfying three axioms. Different choices of τ on the same underlying set X yield entirely different topological spaces with different open sets, different notions of continuity, and different compactness properties."
```
