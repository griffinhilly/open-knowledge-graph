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

## Questions

```yaml
- question: "During alloy solidification, a tiny protrusion forms on the advancing solid-liquid interface and grows faster than the surrounding flat interface rather than being smoothed out. What drives this instability?"
  type: multiple-choice
  options:
    - "The protrusion extends into hotter liquid farther from the cold mold wall, increasing the thermal driving force for solidification"
    - "The protrusion tip has lower surface energy than the flat interface, making it thermodynamically favored to grow"
    - "The protrusion extends into constitutionally supercooled liquid — liquid whose melting point has been depressed by solute enrichment below the local temperature — promoting accelerated growth"
    - "The protrusion concentrates mechanical stress at the tip, forcing the solid to advance faster into the liquid"
  answer: 2
  explanation: "Constitutional supercooling is the key. Solute rejected during solidification accumulates in the liquid just ahead of the interface, depressing its liquidus temperature. If the actual temperature in this zone is below the depressed melting point, that liquid is simultaneously below its liquidus yet still liquid — it is constitutionally supercooled. When a protrusion pokes into this zone, it finds liquid that is below its melting point and solidifies rapidly. The protrusion's sides experience less supercooling (the protrusion locally relieves solute buildup laterally), so lateral growth is slower. This anisotropy amplifies the protrusion into a dendrite arm."

- question: "A casting engineer doubles the cooling rate for an aluminum alloy component. How does this change the final solidified microstructure?"
  type: multiple-choice
  options:
    - "Coarser secondary dendrite arm spacing (SDAS) and reduced microsegregation, because faster cooling allows more time for solid-state homogenization"
    - "Finer SDAS and reduced microsegregation, because faster cooling suppresses the constitutional supercooling that drives dendritic branching"
    - "Finer SDAS and increased microsegregation, because faster interface advance gives solute less time to diffuse away from dendrite boundaries"
    - "No change in SDAS; only grain density is affected by cooling rate"
  answer: 2
  explanation: "Faster cooling drives the interface forward more quickly, leaving less time for secondary dendrite arms to coarsen and merge — resulting in finer SDAS. Simultaneously, faster cooling gives solute less time to diffuse away from the solid-liquid interface and less time for solid-state homogenization after solidification, producing more pronounced microsegregation: solute is more concentrated at grain and dendrite boundaries relative to the dendrite core. These two effects together motivate post-casting homogenization annealing, which allows solid-state diffusion to smooth out composition gradients."

- question: "Constitutional supercooling occurs when the bulk temperature of the liquid drops below the nominal melting point of the pure base metal."
  type: true-false
  answer: false
  explanation: "Constitutional supercooling is not about the bulk temperature or the pure metal's melting point — it is about the local melting point being depressed by solute enrichment. The word 'constitutional' refers to composition (chemical constitution), not temperature. As solidification proceeds, rejected solute accumulates in the liquid ahead of the interface, lowering its liquidus temperature. If the actual temperature in that zone is below this solute-depressed liquidus, the liquid is constitutionally supercooled — even though the bulk liquid may be well above the pure metal's melting point."

- question: "Slower solidification cooling rates produce coarser secondary dendrite arm spacing (SDAS), because the interface advances more slowly, giving more time for competing dendrite arms to coarsen by Ostwald-type ripening processes."
  type: true-false
  answer: true
  explanation: "Secondary dendrite arm coarsening is diffusion-driven: smaller arms (with higher curvature and higher chemical potential) dissolve back into the liquid and redeposit on larger arms, reducing total surface energy. This requires time and diffusion — slower cooling provides both. The relationship is typically expressed as SDAS = C × t_f^(1/3), where t_f is the local solidification time (inversely related to cooling rate). Faster cooling yields shorter t_f and finer SDAS. Engineers exploit this: die-cast and rapidly solidified parts have fine microstructures with better mechanical properties than slow-cooled sand castings."

- question: "Explain why constitutional supercooling is called 'constitutional' — what does the word refer to, and why does solute enrichment in the liquid ahead of the solidification front cause that liquid to be supercooled?"
  type: short-answer
  answer: "'Constitutional' refers to composition — the chemical constitution of the alloy. During solidification, the solid phase rejects excess solute into the adjacent liquid (when partition coefficient k < 1). This rejected solute cannot rapidly diffuse away through the slow-diffusing solid, so it accumulates in a thin layer of liquid just ahead of the interface. According to the phase diagram, higher solute content means a lower liquidus temperature — it takes more undercooling to solidify a more concentrated liquid. If the actual temperature in this solute-enriched zone is below this depressed liquidus, that liquid is below its local melting point while still liquid — it is supercooled due to its composition, hence 'constitutional.'"
  explanation: "The mechanism can be visualized with the phase diagram: the liquidus temperature decreases with solute content. Rejected solute raises local solute concentration, sliding the local liquidus temperature downward. If the actual temperature gradient ahead of the interface is shallower than the liquidus temperature gradient — meaning the local temperature falls more slowly than the local liquidus temperature — there exists a region where T_actual < T_liquidus(C_local): the constitutionally supercooled zone. The width and depth of this zone determine how aggressively protrusions grow and therefore how branched the resulting dendrite structure becomes."
```

## Explainer

From the lever rule and phase composition concepts, you know that when an alloy solidifies, the solid and liquid phases have different compositions at a given temperature — the phase diagram tells you what those compositions must be at equilibrium. But the lever rule assumes that compositions can adjust instantly throughout both phases. In reality, diffusion in solids is extremely slow. When a solid crystal grows into the liquid, it rejects excess solute into the liquid immediately ahead of the advancing interface, and that rejected solute cannot easily redistribute back into the solid already formed. This kinetic constraint is the root cause of dendritic growth.

Consider a binary alloy with composition C₀ cooling through the two-phase region. The solid forming at the interface has a lower solute concentration than the adjacent liquid (for a typical alloy with a partition coefficient k < 1). As solidification proceeds, solute accumulates in a thin layer of liquid just ahead of the solid-liquid interface, building up a **solute-enriched boundary layer**. According to the phase diagram, higher solute concentration means a lower liquidus temperature — the liquid ahead of the interface has a depressed melting point. If the actual temperature in the liquid ahead of the interface is lower than this depressed melting point, that liquid is simultaneously below its liquidus temperature yet still liquid — it is **constitutionally supercooled**. The word "constitutional" refers to composition (constitution), not temperature: the supercooling is caused by the compositional enrichment, not by cooling the bulk liquid below its nominal melting point.

A constitutionally supercooled region is unstable to small protrusions. Imagine a tiny bump forming on the solid-liquid interface and poking into the supercooled liquid ahead. That bump finds itself surrounded by liquid that is below its local melting point — the bump grows faster than the flat interface around it. Meanwhile, the sides of the bump protrude into liquid with lower constitutional supercooling (the bump has locally relieved the solute buildup), so lateral growth is slower. The bump amplifies into a spike; secondary branches sprout from the spike, driven by the same instability; tertiary branches develop from those. The result is a **dendrite** — a tree-like crystal with a primary arm growing along a crystallographically preferred direction (⟨100⟩ in cubic metals) and secondary and tertiary arms branching at regular intervals. The pattern is familiar: snowflakes are ice dendrites, and the feathery structure visible in cast metals under a microscope is a forest of solidified dendrites.

**Cooling rate** is the dominant process variable controlling the resulting microstructure. Faster cooling means the solid-liquid interface advances more quickly, leaving less time for solute to diffuse away from the tips of growing arms. Constitutional supercooling extends further ahead of each arm, driving finer branching and a shorter **secondary dendrite arm spacing** (SDAS). Faster cooling also means less time for homogenization: solute rejected during solidification stays concentrated at the dendrite boundaries, creating a composition gradient within each arm called **microsegregation**. Slower cooling produces coarser SDAS, more homogeneous dendrite arms, and less microsegregation — but also larger grains. Engineers exploit this tradeoff directly: die casting and rapid solidification processes produce fine microstructures with better mechanical properties; after casting, **homogenization annealing** at elevated temperature allows solid-state diffusion to smooth out microsegregation at the cost of some grain coarsening. Understanding dendrite formation is therefore not just descriptive — it is the basis for process design in casting, welding, and additive manufacturing wherever a melt solidifies into a structural part.
