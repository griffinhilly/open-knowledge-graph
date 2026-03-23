---
id: union-and-intersection-intro
title: Union and Intersection
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: set-notation-basics
    type: hard
  - id: subsets-and-supersets-intro
    type: hard
  - id: venn-diagrams-intro
    type: soft
builds-toward:
  - complement-of-a-set-intro
  - set-operations-and-venn-diagrams
  - set-operations-union-intersection-complement
tags: [union, intersection, set-operations, logic]
stage: abstract-reasoning
status: draft
---

# Union and Intersection

## Core Idea
The union of two sets A and B (written A ∪ B) is the set of all elements that belong to A or B (or both). The intersection of two sets A and B (written A ∩ B) is the set of all elements that belong to both A and B. Union corresponds to the logical OR (include if in either set), and intersection corresponds to the logical AND (include only if in both sets). Two sets with no elements in common have an empty intersection and are called disjoint.

## How It's Best Learned
Start with concrete examples. A = {1, 2, 3, 4}, B = {3, 4, 5, 6}. Union: {1, 2, 3, 4, 5, 6} (everything from either set, no duplicates). Intersection: {3, 4} (only the elements in both). Use Venn diagrams to visualize: union is the entire shaded region, intersection is only the overlap. Connect to logical connectives: ∪ is like OR, ∩ is like AND. Practice with word-based sets: "students who play basketball" ∪ "students who play soccer" = "students who play at least one sport."

## Common Misconceptions
- Thinking union means adding the sizes: |A ∪ B| = |A| + |B|. This overcounts elements in the intersection. The correct formula is |A ∪ B| = |A| + |B| - |A ∩ B|.
- Confusing union with intersection. Union includes everything from both sets (OR); intersection includes only what is in both (AND). The symbols help: ∪ looks like a cup that holds everything, ∩ looks like a cap that only covers the overlap.
- Forgetting that union uses the "inclusive or": elements in both A and B are included in A ∪ B.

## Questions

```yaml
- question: "If A = {1, 2, 3} and B = {2, 3, 4, 5}, what is A ∩ B?"
  type: multiple-choice
  options:
    - "{1, 2, 3, 4, 5}"
    - "{2, 3}"
    - "{1, 4, 5}"
    - "{}"
  answer: 1
  explanation: "A ∩ B contains elements that are in BOTH A and B. Checking each element: 1 is in A but not B (excluded). 2 is in both (included). 3 is in both (included). 4 is in B but not A (excluded). 5 is in B but not A (excluded). So A ∩ B = {2, 3}. Option A is the union, not intersection. Option C contains elements in exactly one set (the symmetric difference)."

- question: "If A and B are disjoint sets, then A ∪ B = ∅."
  type: true-false
  answer: false
  explanation: "Disjoint means A ∩ B = ∅ (they share no elements), not that their union is empty. A = {1, 2} and B = {3, 4} are disjoint, but A ∪ B = {1, 2, 3, 4}. The union of disjoint sets combines all elements from both sets. Only if both A and B are themselves empty would A ∪ B be empty."

- question: "A class has 30 students. 18 play basketball, 14 play soccer, and 7 play both. How many play at least one sport? Explain using union and intersection."
  type: short-answer
  answer: "Let B = basketball players, S = soccer players. |B ∪ S| = |B| + |S| - |B ∩ S| = 18 + 14 - 7 = 25. So 25 students play at least one sport."
  explanation: "The union B ∪ S represents students who play basketball OR soccer (or both). Simply adding 18 + 14 = 32 overcounts the 7 students who play both, because they are counted once in |B| and once in |S|. Subtracting the intersection corrects the overcount. This is the inclusion-exclusion principle."
```

## Explainer

Union and intersection are the two most fundamental operations on sets. They combine sets to create new sets, just as addition and multiplication combine numbers to create new numbers. And just as understanding addition and multiplication is essential for arithmetic, understanding union and intersection is essential for all set-based reasoning.

The union A ∪ B collects everything from both sets. If A = {1, 2, 3} and B = {3, 4, 5}, then A ∪ B = {1, 2, 3, 4, 5}. Notice that 3 appears in both A and B, but it appears only once in the union — sets do not have duplicates. The union answers the question "what belongs to at least one of these sets?" It corresponds to the logical OR: an element is in A ∪ B if it is in A or in B or in both.

The intersection A ∩ B keeps only what is shared. With the same sets, A ∩ B = {3} — the only element in both. The intersection answers "what belongs to both of these sets?" It corresponds to the logical AND: an element is in A ∩ B if it is in A and in B.

When two sets share no elements at all, their intersection is the empty set: A ∩ B = ∅. Such sets are called disjoint. The sets {1, 2} and {3, 4} are disjoint — they have nothing in common. Disjointness is important because when sets are disjoint, counting becomes simpler: |A ∪ B| = |A| + |B| exactly, with no overlap to worry about.

When the sets do overlap, you need the inclusion-exclusion principle: |A ∪ B| = |A| + |B| - |A ∩ B|. Adding the sizes of A and B double-counts the elements in the intersection (they get counted once in |A| and again in |B|), so you subtract |A ∩ B| to compensate. If 18 students play basketball and 14 play soccer but 7 play both, the total playing at least one sport is 18 + 14 - 7 = 25, not 32. This principle extends to three or more sets, though the formula becomes more involved.

The connection between set operations and logical connectives is deep and worth internalizing. Union (∪) corresponds to OR (∨). Intersection (∩) corresponds to AND (∧). This parallel will strengthen as you learn about complements (which correspond to NOT) and study De Morgan's Laws for sets. The language of sets and the language of logic describe the same structures from different angles.
