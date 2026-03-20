---
id: heat-treatment-steels
title: Heat Treatment Processes and Microstructure Control
domain: engineering
course: materials-science
prerequisites:
- id: phase-transformations-kinetics
  type: hard
- id: heat-treatment-of-steels
  type: soft
tags:
- heat-treatment
- annealing
- quenching
- tempering
stage: advanced
status: draft
---

# Heat Treatment Processes and Microstructure Control

## Core Idea
Heat treatment deliberately controls heating and cooling rates to produce desired microstructures and mechanical properties in metals and alloys. Key processes include annealing (heating followed by slow cooling to reduce hardness and increase ductility), quenching (rapid cooling to form hardened non-equilibrium structures), and tempering (reheating to increase toughness). The Fe-C phase diagram and TTT curves guide selection of heat treatment to achieve specific combinations of strength, ductility, and toughness.

## Explainer

From your study of phase transformation kinetics, you know that whether a transformation occurs depends on both *driving force* (how far from equilibrium) and *time* (whether atoms can diffuse to rearrange). The Fe-C system is the canonical case where these factors can be precisely manipulated by controlling cooling rate. The central idea is that the equilibrium microstructure — dictated by the phase diagram — is not the only possible microstructure. If you cool fast enough to outrun the diffusion-controlled transformations, you can trap the steel in metastable states with dramatically different properties. Heat treatment is the engineering of this kinetic competition.

**Annealing** restores the equilibrium microstructure. You heat the steel into the austenite (γ) phase field — where carbon is dissolved uniformly in the FCC iron lattice — hold long enough to homogenize, then cool slowly. Slow cooling gives sufficient time for the **eutectoid transformation**: austenite decomposes into alternating lamellae of ferrite (α-Fe, nearly pure iron, soft) and cementite (Fe₃C, iron carbide, hard). This lamellar mixture is **pearlite**, and its lamella spacing determines hardness — coarser spacing from slower cooling gives softer pearlite. The result is a steel that is soft, ductile, and easily machined. Annealing is the starting condition for further processing.

**Quenching** — rapid immersion in water, oil, or air — attempts to suppress the diffusive eutectoid transformation entirely by cooling through the critical temperature range too quickly for carbon atoms to segregate. When the cooling rate exceeds the "nose" of the TTT (Time-Temperature-Transformation) curve — the fastest path for pearlite or bainite formation — the austenite cannot transform diffusively. Instead, at temperatures below the **martensite start temperature** M_s, the FCC lattice transforms to the BCT (body-centered tetragonal) structure by a *diffusionless* shear mechanism: carbon atoms are trapped in interstitial sites within the iron lattice, distorting it. This trapped carbon makes **martensite** extremely hard and brittle — hardness scales steeply with carbon content — because the lattice distortion impedes dislocation motion. A 0.6% carbon steel can reach 60+ Rockwell C hardness after quenching, compared to ~15 HRC after annealing.

**Tempering** addresses martensite's brittleness. By reheating the quenched steel to an intermediate temperature (150–650°C), you allow limited diffusion: excess carbon begins to precipitate as fine carbide particles from the supersaturated martensite. The result — **tempered martensite** — is a fine mixture of ferrite and carbide that is substantially tougher than as-quenched martensite while retaining much of its hardness. The tempering temperature controls the tradeoff: low temperatures (150–250°C) relieve internal stresses with minimal hardness loss; higher temperatures (500–600°C) sacrifice more hardness for substantially greater toughness. The TTT diagram's companion, the **CCT (Continuous Cooling Transformation)** diagram, maps this directly onto realistic industrial cooling paths — austenitize, cool at a rate that crosses specific phase boundaries, and read off the resulting microstructure and estimated hardness at room temperature.
