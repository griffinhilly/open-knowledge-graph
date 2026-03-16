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

## Explainer

You already know Kirchhoff's Voltage Law: the sum of voltage drops around any closed loop equals zero. KVL is always true — the mesh current method is simply a disciplined procedure for applying KVL to every independent loop in a circuit simultaneously, then solving the resulting system of equations. The key invention is the **mesh current**: a fictitious circulating current assigned to each enclosed region (mesh) of the circuit diagram. These currents are not physically measured anywhere; they are variables introduced to make the algebra tractable.

Here is why mesh currents are powerful: in a planar circuit (one you can draw on paper without crossing wires), every branch belongs to at most two meshes. If a branch is shared between meshes i and j, the actual branch current is the algebraic difference of the two mesh currents (I_i − I_j, where the sign depends on their relative directions). Branches on the boundary of only one mesh carry exactly that mesh current. This means once you solve for the mesh currents, you can immediately compute every branch current by inspection — no further equations needed. The method is efficient when the circuit has fewer independent meshes than nodes, which is the complement of the node-voltage method you may already know.

To apply the method: (1) assign a mesh current to each independent mesh, all in the same direction (clockwise is conventional); (2) write a KVL equation around each mesh by summing voltage drops. The self-resistance of mesh i contributes +I_i times the sum of all resistors in that mesh. Shared resistors contribute −I_j times their resistance (the other mesh current flowing in the opposing direction). Voltage sources are treated as fixed voltage drops with the sign determined by polarity. This produces a symmetric system of equations — the coefficient matrix is positive-definite for resistive circuits — which you then solve by Gaussian elimination or matrix methods.

**Supermeshes** arise when a current source sits on the boundary between two meshes. You cannot write a KVL equation directly around a mesh containing a current source because the voltage across an ideal current source is unknown. Instead, you merge the two meshes into a supermesh: write one KVL equation around the combined outer perimeter (skipping the current source branch), then add a second equation from the current source constraint: I_i − I_j = I_source. This gives you the same number of equations as unknowns. Think of the supermesh as treating the current source branch as an internal branch — its voltage adjusts to whatever is needed, and you learn it after solving. The method's elegance is that the systematic procedure never requires you to guess or inspect; the algebra carries you directly to the solution.
