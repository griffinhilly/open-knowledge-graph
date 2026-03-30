---
id: list-coloring
title: List Coloring and Choosability
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
- id: brooks-theorem
  type: soft
tags:
- graph-theory
- coloring
stage: advanced
status: validated
---
# List Coloring and Choosability

## Core Idea
List coloring (choosability) is a generalization where each vertex has a list of available colors, and the goal is to color vertices from their lists with no adjacent vertices sharing a color. The list chromatic number is always at least chromatic number and often larger, revealing finer structural properties.

## How It's Best Learned
Construct list-assignments and try to find valid colorings; observe how the structure of lists and graph connectivity interact.

## Common Misconceptions
List chromatic number can be much larger than standard chromatic number; having more total colors available doesn't guarantee good list colorability.

## Questions

```yaml
- question: "A bipartite graph K_{3,3} has chromatic number 2. Someone claims: 'We have 6 different colors available — one assigned to each vertex — so we can always list-color it.' The lists each have size 1. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "K_{3,3} actually requires 3 colors, so the chromatic number assumption is wrong"
    - "List coloring requires every vertex's list to have size k; with size-1 lists, adjacent vertices may receive the same color, making a valid coloring impossible"
    - "Having 6 distinct colors for 6 vertices guarantees a valid coloring regardless of adjacency"
    - "Bipartite graphs are not list-colorable because they contain no odd cycles"
  answer: 1
  explanation: "The error is confusing 'many total colors available' with 'lists large enough to guarantee a valid coloring.' In list coloring, each vertex must be colored from its own private list. If adjacent vertices are forced to share the same color because their size-1 lists happen to contain the same color, no valid coloring exists regardless of how many distinct colors are used globally. The adversary chooses the lists to maximize conflict — a carefully designed size-1 list assignment for K_{3,3} can make coloring impossible."

- question: "Which statement correctly describes the relationship between the chromatic number χ(G) and the list chromatic number χ_ℓ(G)?"
  type: multiple-choice
  options:
    - "χ(G) = χ_ℓ(G) always, because the adversary can never do worse than the uniform case"
    - "χ_ℓ(G) ≤ χ(G) always, because list coloring is strictly more flexible"
    - "χ(G) ≤ χ_ℓ(G) always, and the gap can be dramatic — for example, K_{n,n} has χ = 2 but χ_ℓ = Θ(log n)"
    - "χ_ℓ(G) < χ(G) for all graphs with at least one cycle"
  answer: 2
  explanation: "Because the uniform case (all lists identical) is a special case of list coloring, any graph that requires k colors in standard coloring will also require at least k colors in list coloring. So χ(G) ≤ χ_ℓ(G) always. The gap can be large: K_{n,n} has chromatic number 2 (it's bipartite) but list chromatic number Θ(log n), because an adversary can construct list assignments that defeat any fixed coloring strategy for small list sizes."

- question: "If a graph can be properly colored with k colors, it can usually be properly list-colored from any assignment of lists of size k."
  type: true-false
  answer: false
  explanation: "This is the central misconception list coloring is designed to expose. Standard k-colorability means there exists *one* assignment of k colors that works when all vertices draw from the same pool. List k-choosability (χ_ℓ ≤ k) means the graph can be colored *no matter what* specific k colors each vertex's list contains. These are very different guarantees. K_{n,n} is 2-colorable but not 2-choosable — a cleverly designed list assignment of size 2 can make it impossible to color."

- question: "The list chromatic number of a graph is always at least as large as its standard chromatic number."
  type: true-false
  answer: true
  explanation: "When all vertex lists are identical (each list = the same set of k colors), list coloring reduces exactly to standard k-coloring. So if the graph can be list-colored from any k-size lists, it can certainly be colored from k colors in the standard sense. Contraposing: if standard k-coloring fails, list k-coloring fails too. Therefore χ(G) ≤ χ_ℓ(G) always holds."

- question: "Why does having many total colors available across all vertex lists not guarantee that a graph can be list-colored from those lists?"
  type: short-answer
  answer: "In list coloring, the adversary chooses which specific colors go on each vertex's list, and they choose adversarially to make coloring as hard as possible. Even if the total pool of colors is vast, a clever adversary can assign lists so that every possible color assignment to one vertex conflicts with every neighbor's available colors. The guarantee in k-choosability is not about the number of colors globally — it's about being able to succeed against *any* assignment of size-k lists, including the worst-case adversarial one."
  explanation: "This is the core insight that separates list coloring from standard coloring. Standard coloring gives you full control over the color assignment; list coloring hands partial control to an adversary. The adversary exploits the graph's structure to design list assignments that force conflicts. This is why K_{n,n}'s list chromatic number grows with n even though its standard chromatic number is always 2."
```

## Explainer

Standard graph coloring asks: given k colors for the whole graph, can every vertex be assigned one of those k colors so no two adjacent vertices share a color? **List coloring** relaxes the uniformity: each vertex v gets its own private list L(v) of allowed colors, and you must color v from L(v) while still avoiding color conflicts with neighbors. The graph is **k-choosable** (or k-list-colorable) if it can be properly list-colored from *any* assignment of lists of size k — no matter what specific k colors each vertex gets on its list.

The **list chromatic number** χ_ℓ(G) is the smallest k for which G is k-choosable. Because the uniform case (all lists identical) is a special case of list coloring, we always have χ(G) ≤ χ_ℓ(G). But list chromatic number can be strictly larger — and sometimes dramatically so. The canonical example is the complete bipartite graph K_{n,n}: it has chromatic number 2 (it's bipartite, so 2-colorable), but its list chromatic number is Θ(log n). To see why, imagine a cleverly adversarial list assignment where the top and bottom vertices each get n different colors arranged to conflict pairwise — no consistent coloring survives.

The distinction matters because list coloring models scenarios where different vertices have incompatible constraints. In scheduling, employees might each be available only on certain days; the question is whether a valid schedule exists given those individual constraints, not whether a fixed set of days works universally. Brooks' Theorem gives χ(G) ≤ Δ for most graphs, but the analogous result for list coloring (the **Galvin-Vizing theorem** for bipartite graphs, the **Erdős–Rubin–Taylor theorem** generally) requires higher k. A bipartite graph is always Δ-edge-choosable (Galvin's theorem), which is a stronger statement than the equivalent for vertex coloring.

The deep subtlety is that the adversary choosing lists is working *against* you. Even if the total number of colors across all lists is vast, a carefully constructed list assignment can make coloring impossible at any smaller-than-χ_ℓ list size. This is why checking whether a graph is 2-choosable is already nontrivial — you must verify that no adversarial list assignment of size 2 defeats you. The **kernel method**, a key proof technique, converts list coloring problems into questions about orientations of the graph, connecting this topic to directed graph theory you've seen in your prerequisites on graph coloring.
