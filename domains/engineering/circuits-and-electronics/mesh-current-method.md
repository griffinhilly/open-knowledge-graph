---
id: mesh-current-method
title: Mesh Current Method (Mesh Analysis)
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: kirchhoffs-rules
  type: hard
- id: dc-circuits-series-parallel
  type: soft
- id: gaussian-elimination
  type: soft
- id: systems-elimination
  type: soft
- id: node-voltage-method
  type: soft
builds-toward:
- superposition-theorem-circuits
- thevenin-norton-equivalents
- ac-circuit-analysis-methods
tags:
- mesh-analysis
- KVL
- loop-currents
- planar-circuits
stage: formal-systems
status: validated
---
# Mesh Current Method (Mesh Analysis)

## Core Idea
The mesh current method assigns a circulating current variable to each independent mesh in a planar circuit and applies KVL around each mesh. Mesh currents are fictitious variables; actual branch currents are found as algebraic sums of the mesh currents sharing that branch. When a current source lies on the boundary between two meshes, a supermesh is formed by combining those meshes and writing one KVL equation around the supermesh periphery plus a constraint from the current source. The method is dual to nodal analysis and is efficient when the circuit has fewer meshes than nodes.

## How It's Best Learned
Start with simple planar circuits and identify all independent meshes. Assign all mesh currents in the same direction (e.g., clockwise). Compare results with nodal analysis on the same circuit to build intuition for which method is more efficient in a given topology.

## Common Misconceptions
- Applying mesh analysis directly to non-planar circuits — the method requires a planar graph.
- Forgetting that a branch shared by two meshes carries a current equal to the algebraic difference of the two mesh currents.
- Omitting the constraint equation when forming a supermesh around a current source.

## Questions

```yaml
- question: "A circuit has two clockwise mesh currents I₁ and I₂ sharing a resistor R. What is the actual current flowing through R from the perspective of mesh 1?"
  type: multiple-choice
  options:
    - "I₁ + I₂, because both mesh currents pass through the shared resistor"
    - "I₁ − I₂, because the two mesh currents flow in opposite directions through the shared branch"
    - "I₁ alone, because I₂ is a fictitious variable that doesn't affect the branch"
    - "The average (I₁ + I₂)/2, since the resistor is shared equally"
  answer: 1
  explanation: "When two clockwise mesh currents share a branch, they flow in opposite directions through it — I₁ flows one way, I₂ flows the other. The actual branch current is the algebraic difference I₁ − I₂ (or I₂ − I₁, depending on the reference direction). This is a key consequence of how mesh currents work: they are not physical currents but mathematical variables. The actual current in any branch is found by summing — with appropriate signs — all mesh currents that pass through it."

- question: "A 3 A current source lies on the boundary between mesh 1 and mesh 2. How should mesh analysis handle this?"
  type: multiple-choice
  options:
    - "Assign the voltage across the current source as an unknown and include it in the KVL equation for each mesh"
    - "Ignore the current source — ideal current sources have zero resistance and don't appear in KVL"
    - "Write KVL around the outer perimeter of both meshes combined (skipping the current source branch), then add the constraint I₁ − I₂ = 3 A"
    - "Set I₁ = 3 A and I₂ = 0, since the source fixes the current in one mesh"
  answer: 2
  explanation: "An ideal current source has an unknown voltage across it, so you cannot write KVL around a loop that includes it without introducing another unknown. The supermesh technique avoids this: merge the two meshes into one by going around the outer perimeter (skipping the branch with the current source) to write one KVL equation. Then add the constraint equation I₁ − I₂ = 3 A (or its negative), which the current source directly specifies. Together these give the same number of equations as unknowns."

- question: "Mesh currents are fictitious variables — they are not directly measured anywhere in the physical circuit."
  type: true-false
  answer: true
  explanation: "True. Mesh currents (I₁, I₂, ...) are mathematical abstractions assigned to the enclosed loops of a planar circuit. They have no single physical wire where you could place an ammeter and read off I₁. The physically measurable quantity — actual branch current — is obtained by algebraically summing all mesh currents sharing that branch. Their value as a technique lies in producing a systematic, minimal set of equations, not in having direct physical meaning."

- question: "Mesh analysis can be applied to any circuit, including those whose wires is expected to cross when drawn on a flat surface."
  type: true-false
  answer: false
  explanation: "False. Mesh analysis requires the circuit to be planar — drawable on a flat surface without any wires crossing. In a non-planar circuit, the concept of an 'enclosed mesh region' breaks down because the topology does not admit a consistent set of independent loops in the plane. For non-planar circuits, nodal analysis (which works on any circuit) is the correct systematic method."

- question: "Explain why a current source between two meshes prevents writing a standard KVL equation around either mesh, and describe how the supermesh technique resolves this problem."
  type: short-answer
  answer: "KVL requires summing known or expressible voltage drops around a loop. An ideal current source fixes the current through a branch but leaves the voltage across it as unknown and unconstrained — it adjusts to whatever the circuit requires. Including this unknown voltage in a KVL equation adds a variable without adding a useful equation. The supermesh resolves this by forming a larger loop that goes around the outside of both meshes, bypassing the current source branch entirely. This produces one KVL equation free of the unknown voltage. The missing equation is replaced by the current source's own constraint: I₁ − I₂ = I_source, which directly relates the two mesh currents."
  explanation: "The supermesh is not a workaround — it is the correct application of KVL to a loop that avoids the problematic branch. The number of independent equations is preserved: two meshes normally give two equations; a supermesh gives one combined KVL equation plus one constraint equation, still totaling two equations for two unknowns."
```

## Explainer

You already know Kirchhoff's Voltage Law: the sum of voltage drops around any closed loop equals zero. KVL is always true — the mesh current method is simply a disciplined procedure for applying KVL to every independent loop in a circuit simultaneously, then solving the resulting system of equations. The key invention is the **mesh current**: a fictitious circulating current assigned to each enclosed region (mesh) of the circuit diagram. These currents are not physically measured anywhere; they are variables introduced to make the algebra tractable.

Here is why mesh currents are powerful: in a planar circuit (one you can draw on paper without crossing wires), every branch belongs to at most two meshes. If a branch is shared between meshes i and j, the actual branch current is the algebraic difference of the two mesh currents (I_i − I_j, where the sign depends on their relative directions). Branches on the boundary of only one mesh carry exactly that mesh current. This means once you solve for the mesh currents, you can immediately compute every branch current by inspection — no further equations needed. The method is efficient when the circuit has fewer independent meshes than nodes, which is the complement of the node-voltage method you may already know.

To apply the method: (1) assign a mesh current to each independent mesh, all in the same direction (clockwise is conventional); (2) write a KVL equation around each mesh by summing voltage drops. The self-resistance of mesh i contributes +I_i times the sum of all resistors in that mesh. Shared resistors contribute −I_j times their resistance (the other mesh current flowing in the opposing direction). Voltage sources are treated as fixed voltage drops with the sign determined by polarity. This produces a symmetric system of equations — the coefficient matrix is positive-definite for resistive circuits — which you then solve by Gaussian elimination or matrix methods.

**Supermeshes** arise when a current source sits on the boundary between two meshes. You cannot write a KVL equation directly around a mesh containing a current source because the voltage across an ideal current source is unknown. Instead, you merge the two meshes into a supermesh: write one KVL equation around the combined outer perimeter (skipping the current source branch), then add a second equation from the current source constraint: I_i − I_j = I_source. This gives you the same number of equations as unknowns. Think of the supermesh as treating the current source branch as an internal branch — its voltage adjusts to whatever is needed, and you learn it after solving. The method's elegance is that the systematic procedure never requires you to guess or inspect; the algebra carries you directly to the solution.
