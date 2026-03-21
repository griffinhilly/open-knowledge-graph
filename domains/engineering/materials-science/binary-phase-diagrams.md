---
id: binary-phase-diagrams
title: Reading and Interpreting Binary Phase Diagrams
domain: engineering
course: materials-science
prerequisites:
- id: phase-diagrams-binary-mixtures
  type: hard
- id: lever-rule
  type: soft
builds-toward:
- phase-transformations-kinetics
- heat-treatment-steels
tags:
- phase-diagrams
- binary-systems
- alloys
- equilibrium
stage: advanced
status: draft
---

# Reading and Interpreting Binary Phase Diagrams

## Core Idea
Binary phase diagrams map the stable phases present at equilibrium for different temperatures and compositions in two-component systems. Key features include single-phase regions (where one phase is stable), two-phase regions (where two phases coexist in equilibrium), and invariant reactions (eutectic, peritectic, eutectoid) where three or more phases meet. Phase diagrams enable prediction of equilibrium microstructure and serve as a guide for heat treatment design.

## Questions

```yaml
- question: "An alloy of 40 wt% B in a two-phase (α + β) region has a tie line at its temperature showing the α-phase boundary at 20 wt% B and the β-phase boundary at 70 wt% B. What are the compositions of the α and β phases actually present in this alloy?"
  type: multiple-choice
  options:
    - "Both phases are 40 wt% B — the overall alloy composition determines each phase's composition"
    - "α is 20 wt% B and β is 70 wt% B — determined by the tie line endpoints, independent of the overall alloy composition"
    - "α is 40 wt% B and β is 70 wt% B — the overall composition equals one phase's composition in a two-phase region"
    - "α is 20 wt% B and β is 40 wt% B — the heavier component concentrates in the denser phase"
  answer: 1
  explanation: "In a two-phase region, the compositions of the coexisting phases are fixed by the tie line endpoints — the intersections of the tie line with the surrounding single-phase region boundaries. The overall alloy composition (40 wt% B here) determines only the RELATIVE AMOUNTS of each phase (via the lever rule), not their compositions. Both phases are always at the boundary compositions regardless of where the overall alloy sits within the two-phase region. This is the most commonly misunderstood feature of phase diagram reading."

- question: "An alloy at exactly the eutectic composition is slowly cooled through the eutectic temperature. What happens?"
  type: multiple-choice
  options:
    - "It solidifies gradually over a temperature range, like most off-eutectic alloys, because two phases form simultaneously"
    - "It solidifies at a single fixed temperature, simultaneously forming two solid phases from the liquid in a fine-scale lamellar microstructure"
    - "It transforms from one solid phase to another at the eutectic temperature without passing through a liquid state"
    - "It forms a single solid phase because the eutectic composition is where the two solid phases have identical compositions"
  answer: 1
  explanation: "At the eutectic point, three phases coexist simultaneously (liquid + two solids) — an invariant condition fixed at one specific temperature and composition. On cooling through this point, the liquid transforms entirely and simultaneously into two solid phases. Because the two solids nucleate and grow together from the liquid, they produce the characteristic fine-scale eutectic microstructure (lamellae or rods). This also explains why eutectic compositions are used in solders: they melt (and solidify) at a single sharp temperature — the lowest melting point in the system — rather than through a mushy two-phase region."

- question: "In a two-phase region, the overall alloy composition determines the compositions of each individual coexisting phase."
  type: true-false
  answer: false
  explanation: "The compositions of the coexisting phases are determined by the tie line endpoints — the phase boundaries at that temperature — not by the overall alloy composition. Moving the overall composition across a two-phase region at constant temperature changes the FRACTIONS of the two phases (lever rule) but not their compositions, which remain fixed at the boundary values. The overall composition determines 'how much of each phase,' while the tie line endpoints determine 'what each phase looks like.'"

- question: "A phase diagram describes equilibrium states, so an alloy processed by rapid quenching may not develop the microstructure predicted by the diagram at room temperature."
  type: true-false
  answer: true
  explanation: "Phase diagrams show what a system would look like given sufficient time to reach thermodynamic equilibrium. Real processing is kinetically constrained: if cooling is fast enough, high-temperature phases can be 'frozen in' at lower temperatures where they are thermodynamically unstable. This gap between equilibrium prediction and kinetically trapped reality is the basis of heat treatment in steels: austenite (stable at high temperature) can be retained or directed toward pearlite, bainite, or martensite depending on cooling rate. The phase diagram tells you the target state; the cooling rate determines whether you get there."

- question: "Explain how to use a tie line in a two-phase region to determine both the composition and the relative amount of each coexisting phase."
  type: short-answer
  answer: "Draw a horizontal (constant-temperature) tie line through the two-phase region. The endpoints where the tie line intersects the single-phase region boundaries give the compositions of the two phases. To find relative amounts (lever rule): the fraction of phase α equals the distance from the overall composition to the β boundary divided by the total tie line length (β boundary minus α boundary); vice versa for β. Intuitively, an alloy whose overall composition is close to the α boundary has mostly α phase; one close to the β boundary has mostly β phase."
  explanation: "The lever rule is named by analogy to a mechanical lever: the overall composition is the fulcrum, and the tie line endpoints are the ends of the lever. The fraction of a phase is proportional to the lever arm on the opposite side. Mathematically: f_α = (X_β − X_overall)/(X_β − X_α), where X denotes composition in wt% or mole fraction. This is derived directly from a mass balance: total mass of B = (mass of α)(composition of α) + (mass of β)(composition of β)."
```

## Explainer

Think of a binary phase diagram as a map. The horizontal axis is composition — the fraction of component B in a mixture of A and B, running from pure A on the left to pure B on the right. The vertical axis is temperature. Every point on this map corresponds to a specific alloy at a specific temperature, and the diagram tells you which phase or phases are thermodynamically stable at that condition. Reading the map correctly is the core skill.

The most important feature is the distinction between **single-phase regions** and **two-phase regions**. In a single-phase region, the alloy exists as one homogeneous phase throughout — all atoms are in the same arrangement. In a two-phase region, two distinct phases coexist simultaneously, each with its own composition and crystal structure. When you are inside a two-phase region, a horizontal tie line connects the boundaries of the surrounding single-phase regions. The endpoints of that tie line give you the compositions of each coexisting phase at that temperature. From your prerequisite knowledge of the **lever rule**, you can calculate the *fraction* of each phase: the fraction of a phase is proportional to how far the overall composition is from that phase's boundary, divided by the full width of the two-phase region.

**Invariant reactions** are the points where three phases coexist simultaneously — a condition so constrained that it occurs only at one specific temperature and composition. The most important is the **eutectic reaction**: on cooling through the eutectic point, a liquid of fixed composition simultaneously solidifies into two solid phases. This produces the characteristic fine-scale lamellar or rod microstructure visible in eutectic alloys. The eutectic temperature is the lowest melting point in the system, which is why eutectic compositions are used in solders — they melt sharply at a lower temperature than either pure component. Peritectic and eutectoid reactions follow similar logic but involve different phase combinations (solid + liquid → solid, and solid → two solids, respectively).

The phase diagram encodes equilibrium — what the system *would* reach given infinite time. Real processing is kinetically constrained: cooling rapidly can suppress equilibrium transformations, trapping high-temperature phases at room temperature. Heat treatment deliberately exploits this gap between equilibrium and kinetics. By reading the phase diagram, an engineer can identify the temperature range where a particular phase is stable, then use cooling rate to control whether that phase is retained or transformed. This is the foundation of steel heat treatment: the iron-carbon phase diagram tells you where austenite is stable; the cooling rate determines whether it transforms to pearlite, bainite, or martensite.
