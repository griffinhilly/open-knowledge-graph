---
id: thermodynamic-systems-engineering
title: Thermodynamic Systems and System Boundaries
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
builds-toward:
- thermodynamic-properties-and-equations-of-state
- first-law-closed-systems
tags:
- systems
- boundaries
- classification
stage: advanced
status: draft
---

# Thermodynamic Systems and System Boundaries

## Core Idea
A thermodynamic system is a defined region of matter or space whose properties are analyzed. Engineering thermodynamics classifies systems as closed (fixed mass) or open (mass flows across boundary), with boundaries that exchange heat and work with surroundings. Understanding system types and their boundary conditions is fundamental to setting up energy balance equations for engineering devices.

## How It's Best Learned
Draw system boundaries around devices (turbines, pumps, heat exchangers) and identify what crosses the boundary (mass, heat, work). Practice distinguishing closed systems (piston-cylinder) from open systems (pipe flow) and recognize how boundary choice affects analysis complexity.

## Common Misconceptions
- A closed system cannot exchange heat or work with surroundings.
- Work only occurs at moving boundaries; shaft work and electrical work are different phenomena.
- System boundaries must align with physical device walls; they can be drawn anywhere for analysis convenience.

## Explainer

The First Law of Thermodynamics — which you already know — states that energy is conserved: ΔU = Q − W. But this statement implicitly assumes you have defined *what* is gaining or losing energy. That definition is the **system boundary**: an imaginary or real surface that separates the "system" (what you analyze) from the "surroundings" (everything else). The system boundary is not a physical fact of nature — it is an analytical choice you make, and a well-chosen boundary can dramatically simplify a problem. The art of engineering thermodynamics is largely the art of drawing system boundaries wisely.

A **closed system** (also called a control mass) has a fixed set of molecules inside its boundary — no mass crosses the boundary. A piston-cylinder device is the classic example: the gas inside is the system, and the piston surface is a moving boundary that allows work transfer. The First Law for a closed system is Q − W = ΔU. Work occurs when the boundary moves (boundary work W = ∫P dV) or through other mechanisms like electrical work or shaft work through a sealed rotating shaft. Heat crosses the boundary whenever there is a temperature gradient across it. The key constraint is that mass does not cross. Many industrial vessels, sealed tanks, and batch reactors are analyzed as closed systems.

An **open system** (control volume) allows mass to cross the boundary. Turbines, compressors, pumps, heat exchangers, nozzles, and pipes are all open systems — mass enters and exits continuously. For open systems, the First Law must account for the energy carried in and out by the flowing mass. The critical new term is **flow work**: fluid flowing into the system does work PV to push itself through the inlet. This P₁V₁ term (per unit mass, P₁v₁ where v is specific volume) combines with the internal energy u₁ to give the **enthalpy** h = u + Pv. This is why enthalpy — not internal energy — appears in the steady-state energy balance for open systems: Q̇ − Ẇ_shaft = ṁ[(h₂ + V₂²/2 + gz₂) − (h₁ + V₁²/2 + gz₁)]. Enthalpy is the natural thermodynamic potential for open systems precisely because it already bundles in the flow work.

Choosing where to draw the boundary is a design decision. Drawing the boundary tightly around a turbine blade passage gives you the detailed local analysis; drawing it around the entire turbine casing gives you the overall energy balance in one equation. Both are valid — they give different information. The key questions to ask when choosing a boundary: What do I want to find? What crosses the boundary (heat, work, or mass)? Can I identify those crossing terms from known data? A systematic approach is to identify all heat interactions (Q terms), all work interactions (shaft work, boundary work, electrical), and all mass streams, then write the energy balance. This structured setup, more than any particular equation, is what First Law problem-solving in engineering practice looks like.
