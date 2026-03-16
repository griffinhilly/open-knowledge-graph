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

## Explainer

You know KVL and Ohm's law. In principle, you could write KVL equations for any loop in a circuit and solve them. But which loops should you choose? How do you avoid redundant equations? **Mesh analysis** answers both questions by providing a systematic recipe that always produces exactly the right number of independent equations — one per mesh, no more, no less.

A **mesh** is a loop that contains no smaller loops inside it — like the individual windows in a window frame. The key insight is to assign a fictitious **mesh current** flowing clockwise around each mesh. These aren't the currents through any single branch; they're circulating variables you use to express all branch currents. The actual current in any branch is the algebraic superposition of mesh currents passing through it. For a branch shared by mesh 1 (current I₁ clockwise) and mesh 2 (current I₂ clockwise), the branch current is I₁ − I₂ in the direction of mesh 1's flow.

Once mesh currents are assigned, you write one KVL equation per mesh and express each voltage drop using Ohm's law in terms of mesh currents. The pattern is mechanical: the **self-resistance** (sum of all resistors in the mesh) times the mesh's own current, minus each **mutual-resistance** (shared resistor with adjacent mesh) times the adjacent current, equals the net voltage source driving that mesh. For an n-mesh planar circuit, this produces n equations in n unknowns — solved by substitution or matrix inversion.

Two special cases arise in practice. A current source in a single mesh sets that mesh current directly, eliminating one unknown and one equation. A current source shared between two meshes creates a **supermesh**: you write KVL around the combined perimeter of both meshes (skipping the current source branch) and add the constraint that the two mesh currents differ by the source value. Handling these cases systematically makes mesh analysis a reliable, algorithm-like procedure — the same structured approach whether the circuit has 2 meshes or 20.
