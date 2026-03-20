---
id: solidification-and-dendrite-formation
title: Solidification Microstructure and Dendrite Formation
domain: engineering
course: materials-science
prerequisites:
- id: lever-rule-and-phase-composition
  type: hard
- id: nucleation-and-growth-kinetics
  type: soft
builds-toward:
- grain-growth-and-recrystallization
tags:
- solidification
- dendrites
- microstructure
- cooling-rate
stage: advanced
status: draft
---

# Solidification Microstructure and Dendrite Formation

## Core Idea
During solidification, crystals grow dendrically due to constitutional supercooling at the solid-liquid interface; liquid ahead of the interface becomes enriched in rejected solute, depressing its melting point. Cooling rate controls dendrite arm spacing (secondary dendrite arm spacing SDAS) and microsegregation; slower cooling produces coarser structure with greater segregation.

## Explainer

From the lever rule and phase composition concepts, you know that when an alloy solidifies, the solid and liquid phases have different compositions at a given temperature — the phase diagram tells you what those compositions must be at equilibrium. But the lever rule assumes that compositions can adjust instantly throughout both phases. In reality, diffusion in solids is extremely slow. When a solid crystal grows into the liquid, it rejects excess solute into the liquid immediately ahead of the advancing interface, and that rejected solute cannot easily redistribute back into the solid already formed. This kinetic constraint is the root cause of dendritic growth.

Consider a binary alloy with composition C₀ cooling through the two-phase region. The solid forming at the interface has a lower solute concentration than the adjacent liquid (for a typical alloy with a partition coefficient k < 1). As solidification proceeds, solute accumulates in a thin layer of liquid just ahead of the solid-liquid interface, building up a **solute-enriched boundary layer**. According to the phase diagram, higher solute concentration means a lower liquidus temperature — the liquid ahead of the interface has a depressed melting point. If the actual temperature in the liquid ahead of the interface is lower than this depressed melting point, that liquid is simultaneously below its liquidus temperature yet still liquid — it is **constitutionally supercooled**. The word "constitutional" refers to composition (constitution), not temperature: the supercooling is caused by the compositional enrichment, not by cooling the bulk liquid below its nominal melting point.

A constitutionally supercooled region is unstable to small protrusions. Imagine a tiny bump forming on the solid-liquid interface and poking into the supercooled liquid ahead. That bump finds itself surrounded by liquid that is below its local melting point — the bump grows faster than the flat interface around it. Meanwhile, the sides of the bump protrude into liquid with lower constitutional supercooling (the bump has locally relieved the solute buildup), so lateral growth is slower. The bump amplifies into a spike; secondary branches sprout from the spike, driven by the same instability; tertiary branches develop from those. The result is a **dendrite** — a tree-like crystal with a primary arm growing along a crystallographically preferred direction (⟨100⟩ in cubic metals) and secondary and tertiary arms branching at regular intervals. The pattern is familiar: snowflakes are ice dendrites, and the feathery structure visible in cast metals under a microscope is a forest of solidified dendrites.

**Cooling rate** is the dominant process variable controlling the resulting microstructure. Faster cooling means the solid-liquid interface advances more quickly, leaving less time for solute to diffuse away from the tips of growing arms. Constitutional supercooling extends further ahead of each arm, driving finer branching and a shorter **secondary dendrite arm spacing** (SDAS). Faster cooling also means less time for homogenization: solute rejected during solidification stays concentrated at the dendrite boundaries, creating a composition gradient within each arm called **microsegregation**. Slower cooling produces coarser SDAS, more homogeneous dendrite arms, and less microsegregation — but also larger grains. Engineers exploit this tradeoff directly: die casting and rapid solidification processes produce fine microstructures with better mechanical properties; after casting, **homogenization annealing** at elevated temperature allows solid-state diffusion to smooth out microsegregation at the cost of some grain coarsening. Understanding dendrite formation is therefore not just descriptive — it is the basis for process design in casting, welding, and additive manufacturing wherever a melt solidifies into a structural part.
