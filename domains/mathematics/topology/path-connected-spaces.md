---
id: path-connected-spaces
title: Path Connected Spaces
domain: mathematics
course: topology
prerequisites:
- id: connected-spaces-definition
  type: hard
builds-toward:
- connected-components-decomposition
- homotopy-definition
tags:
- path-connected
- connectedness
stage: formal-systems
status: draft
---

# Path Connected Spaces

## Core Idea
A space is path-connected if for every two points x,y, there exists a continuous path γ: [0,1] → X with γ(0) = x and γ(1) = y. Path-connected implies connected, but not conversely (topologist's sine curve). Most natural 'nice' spaces that are connected are path-connected; path-connectivity is more intuitive and stronger.

## Questions

```yaml
- question: "Which statement correctly describes the relationship between connectedness and path-connectedness?"
  type: multiple-choice
  options:
    - "They are equivalent properties: a space is connected if and only if it is path-connected"
    - "Connected implies path-connected, but there exist path-connected spaces that are not connected"
    - "Path-connected implies connected, but there exist connected spaces that are not path-connected"
    - "Neither property implies the other; they are independent"
  answer: 2
  explanation: "Path-connected implies connected, but not conversely — this is the key asymmetry. The proof that path-connected ⟹ connected uses the fact that a continuous image of [0,1] is connected. The converse fails: the topologist's sine curve (closure of {(x, sin(1/x)) : x > 0}) is connected but not path-connected — there is no continuous path from any point on the oscillating graph to the segment {0} × [−1, 1]. Path-connectedness is the strictly stronger property."

- question: "A mathematician claims a certain space X is connected but presents no path between two specific points. A student argues: 'If X is connected, you must be able to draw a continuous path between any two points.' Who is correct?"
  type: multiple-choice
  options:
    - "The student — connectedness guarantees a path between any two points by definition"
    - "The mathematician — connectedness does not guarantee paths; the topologist's sine curve is connected but not path-connected"
    - "Both are wrong — neither property says anything about paths"
    - "The student, but only for subsets of ℝⁿ"
  answer: 1
  explanation: "The student conflates connectedness with path-connectedness. Connectedness is a purely topological property: a space cannot be split into two disjoint nonempty open sets. It makes no direct claim about paths. Path-connectedness is the separate (stronger) condition that any two points can be joined by a continuous path. The topologist's sine curve is the standard counterexample: connected by the topological definition, yet no continuous path can reach the accumulation segment at x = 0 from the oscillating part."

- question: "Every path-connected topological space is connected."
  type: true-false
  answer: true
  explanation: "This is the one-directional implication that does hold. If X is path-connected, then for any two points you can find a continuous path γ: [0,1] → X between them. Since [0,1] is connected and γ is continuous, its image is connected. Using this, one can show X cannot be partitioned into two disjoint nonempty open sets, which is the definition of connectedness. The implication is: path-connected ⟹ connected."

- question: "Every connected topological space is path-connected."
  type: true-false
  answer: false
  explanation: "False — the topologist's sine curve is the standard counterexample. It is the closure of {(x, sin(1/x)) : x > 0} in ℝ². This set cannot be split into two disjoint nonempty open sets (it is connected in the topological sense), but there is no continuous path from any point on the oscillating graph part to any point on the limiting segment {0} × [−1, 1]. The oscillation near x = 0 is too rapid for any continuous function to 'cross' it. This shows connectedness is strictly weaker than path-connectedness."

- question: "Describe the topologist's sine curve and explain why it is connected but not path-connected."
  type: short-answer
  answer: "The topologist's sine curve is the closure of the set {(x, sin(1/x)) : x > 0} in ℝ². It consists of the oscillating graph (which oscillates infinitely rapidly as x → 0⁺) together with the limiting segment {0} × [−1, 1] on the y-axis. It is connected because any open set separating the two pieces would have to be open in ℝ², but the oscillating part accumulates at every point of the segment, preventing any separation. It is not path-connected because no continuous function γ: [0,1] → X can travel from a point on the oscillating graph to a point on the segment: near t = 0, the path would have to cross the y-axis with a continuously oscillating value, which no continuous function can do."
  explanation: "This example is pedagogically important because it shows that the topological definition of connectedness captures something real but weaker than geometric intuition suggests. Informally, we think 'connected' means 'you can get from here to there,' but the topological definition doesn't guarantee that. Path-connectedness is the formal version of that intuition. For the spaces of analysis and geometry — open subsets of ℝⁿ, manifolds, convex sets — the two notions coincide, which is why the distinction rarely matters in those settings."
```

## Explainer

From your study of connected spaces, you know that a topological space X is **connected** if it cannot be written as a disjoint union of two nonempty open sets. Connectedness captures a kind of "oneness" — the space cannot be split apart. But connectedness is defined in purely set-theoretic and topological terms, and it admits some counterintuitive examples. **Path-connectedness** offers a more geometric, hands-on version of the same intuition: a space is path-connected if you can draw a continuous curve between any two of its points without leaving the space.

Formally, a **path** from x to y is a continuous function γ: [0, 1] → X with γ(0) = x and γ(1) = y. The interval [0, 1] serves as the parameter domain — think of it as "time." At time 0 you are at x; at time 1 you are at y; at each intermediate time t you are at γ(t), continuously varying. The space X is **path-connected** if such a path exists for every pair of points. All of ℝⁿ is path-connected: the straight-line path γ(t) = (1−t)x + ty works. Open balls, spheres, and all manifolds you encounter in calculus are path-connected.

The relationship to connectedness is one-directional: **path-connected implies connected**, but not vice versa. The proof of the implication uses the intermediate value theorem in disguise — a continuous image of the connected space [0, 1] is connected, and if you can path-connect every pair of points, you can show X cannot be split. The classic counterexample to the converse is the **topologist's sine curve**: the closure of the graph of sin(1/x) for x > 0. This set is connected — it cannot be split into two separated open pieces — but there is no path from a point on the oscillating part to any point on the segment {0} × [−1, 1], because no continuous function can "cross" the accumulation behavior at x = 0.

For the spaces that arise naturally in analysis and geometry — open subsets of ℝⁿ, smooth manifolds, convex sets — path-connectedness and connectedness agree. The distinction matters most in algebraic topology, where path-connectedness is the right notion for defining the **fundamental group** and **homotopy theory**: the next topic you will study. Two paths from x to y that can be continuously deformed into each other represent the same "shape of connection," and comparing these shapes is how homotopy captures the topological holes and loops in a space.
