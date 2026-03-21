---
id: mesh-current-systematic-solution
title: Mesh Analysis Method
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-laws-kvl-and-kcl
  type: hard
- id: ohms-law-and-conductance
  type: hard
builds-toward:
- circuit-theorems-linearity
tags:
- mesh-analysis
- loop-current
- systematic-method
stage: formal-systems
status: draft
---

# Mesh Analysis Method

## Core Idea
Mesh analysis solves circuits by assuming clockwise mesh currents and applying KVL around each independent loop. The resulting system of linear equations yields mesh currents; actual component currents are superpositions of mesh currents. This method is efficient for circuits with many current sources and applies to planar circuits only.

## Questions

```yaml
- question: "In a two-mesh circuit, mesh 1 has current I₁ (clockwise) and mesh 2 has current I₂ (clockwise). A resistor R is shared between the two meshes, with mesh 1's current flowing left-to-right through it and mesh 2's current flowing right-to-left. What is the actual current through R in the direction of I₁?"
  type: multiple-choice
  options:
    - "I₁ alone — shared resistors carry only the mesh current of the mesh that 'owns' them"
    - "I₁ + I₂ — both mesh currents add since they both pass through the resistor"
    - "I₁ − I₂ — the actual current is the superposition, with opposing currents subtracted"
    - "I₂ − I₁ — the larger mesh current dominates"
  answer: 2
  explanation: "Mesh currents are fictitious circulating variables, not real physical currents. Any branch shared by two meshes carries a current equal to the algebraic superposition of both mesh currents. When both mesh currents flow in the same direction through a branch, they add; when they oppose (as described here, with mesh 2 flowing opposite to mesh 1), the actual branch current is I₁ − I₂. This superposition principle is what makes mesh analysis work: you assign circulating currents and recover actual branch currents by adding up contributions with correct signs."

- question: "A circuit has a current source of value I_s sharing a branch between mesh 1 (current I₁) and mesh 2 (current I₂), with I₁ flowing into the positive terminal and I₂ flowing into the negative terminal of the source. How is this current source handled in mesh analysis?"
  type: multiple-choice
  options:
    - "The current source is replaced by a short circuit and the analysis continues normally"
    - "A supermesh is formed: KVL is written around the combined perimeter of both meshes, plus the constraint I₁ − I₂ = I_s"
    - "The mesh current of whichever mesh contains the source is set to I_s directly"
    - "The current source is replaced by its Norton equivalent before applying mesh analysis"
  answer: 1
  explanation: "A current source between two meshes creates a 'supermesh' — you cannot write KVL through a current source (you don't know its voltage without extra analysis). The solution is to write KVL around the outer perimeter of both meshes combined, skipping the branch containing the current source. This gives one equation. The second equation comes from the current source constraint: the difference between the two mesh currents equals the source value (I₁ − I₂ = I_s if I₁ flows into the positive terminal). Together, these two equations replace the two individual mesh equations."

- question: "A mesh current in mesh analysis represents the actual physical current flowing through each branch of that mesh."
  type: true-false
  answer: false
  explanation: "False. Mesh currents are fictitious circulating variables assigned to each mesh for computational convenience — they are not the actual currents in any specific branch. The actual current through a branch is the algebraic superposition (sum with appropriate signs) of all mesh currents that flow through that branch. For a branch belonging to only one mesh, the actual current equals the mesh current. For a shared branch, the actual current is the difference of the two mesh currents. This is the central conceptual point of mesh analysis."

- question: "For a planar circuit with n independent meshes, mesh analysis always yields exactly n independent equations in n unknown mesh currents."
  type: true-false
  answer: true
  explanation: "True. This is the key advantage of mesh analysis over ad hoc loop selection. Writing one KVL equation per mesh guarantees exactly n independent equations — no more, no less — because meshes (loops containing no smaller loops inside them) form a basis for all loops in a planar circuit. Any other loop in the circuit can be expressed as a combination of meshes. If you chose loops non-systematically, you might write redundant equations, producing an underdetermined system. Mesh analysis's systematic structure eliminates this problem."

- question: "What is a mesh current, and why are actual branch currents described as 'superpositions' of mesh currents rather than individual mesh currents?"
  type: short-answer
  answer: "A mesh current is a fictitious circulating current assigned to each mesh (a loop containing no smaller interior loops) for the purpose of setting up KVL equations. It is not a physical current through any single wire — it is a mathematical variable. The actual current through any branch is found by summing the contributions of every mesh current that flows through that branch, with signs determined by direction: if two mesh currents flow in the same direction through a shared branch, they add; if they oppose, they subtract. Branches belonging to only one mesh carry exactly that mesh's current."
  explanation: "The power of this abstraction is that it reduces circuit analysis to a mechanical procedure: assign clockwise currents to all meshes, write KVL around each (using Ohm's law in terms of mesh currents), and solve the resulting linear system. Once mesh currents are found, any branch current, voltage drop, or power is recoverable by superposition. The fictitious nature of mesh currents is not a problem — they are just well-chosen unknowns that make the equations simpler than they would be with physical branch currents as unknowns."
```

## Explainer

You know KVL and Ohm's law. In principle, you could write KVL equations for any loop in a circuit and solve them. But which loops should you choose? How do you avoid redundant equations? **Mesh analysis** answers both questions by providing a systematic recipe that always produces exactly the right number of independent equations — one per mesh, no more, no less.

A **mesh** is a loop that contains no smaller loops inside it — like the individual windows in a window frame. The key insight is to assign a fictitious **mesh current** flowing clockwise around each mesh. These aren't the currents through any single branch; they're circulating variables you use to express all branch currents. The actual current in any branch is the algebraic superposition of mesh currents passing through it. For a branch shared by mesh 1 (current I₁ clockwise) and mesh 2 (current I₂ clockwise), the branch current is I₁ − I₂ in the direction of mesh 1's flow.

Once mesh currents are assigned, you write one KVL equation per mesh and express each voltage drop using Ohm's law in terms of mesh currents. The pattern is mechanical: the **self-resistance** (sum of all resistors in the mesh) times the mesh's own current, minus each **mutual-resistance** (shared resistor with adjacent mesh) times the adjacent current, equals the net voltage source driving that mesh. For an n-mesh planar circuit, this produces n equations in n unknowns — solved by substitution or matrix inversion.

Two special cases arise in practice. A current source in a single mesh sets that mesh current directly, eliminating one unknown and one equation. A current source shared between two meshes creates a **supermesh**: you write KVL around the combined perimeter of both meshes (skipping the current source branch) and add the constraint that the two mesh currents differ by the source value. Handling these cases systematically makes mesh analysis a reliable, algorithm-like procedure — the same structured approach whether the circuit has 2 meshes or 20.
