---
id: case-hardening-surface-treatments
title: Case Hardening and Surface Treatments
domain: engineering
course: materials-science
prerequisites:
- id: heat-treatment-of-steels
  type: hard
- id: diffusion-in-solids
  type: hard
builds-toward:
- materials-selection-design
tags:
- carburizing
- nitriding
- induction-hardening
- surface-hardness
- case-depth
stage: formal-systems
status: draft
---

# Case Hardening and Surface Treatments

## Core Idea
Many engineering components — gears, bearings, camshafts — need a hard, wear-resistant surface combined with a tough, shock-absorbing core. Case hardening achieves this by selectively hardening only the outer layer (case) while leaving the interior (core) relatively soft and ductile. Carburizing diffuses carbon into the surface of a low-carbon steel (typically 0.1-0.25% C) at 850-950 degrees C in a carbon-rich atmosphere, raising the surface carbon content to 0.7-0.9% C. The part is then quenched to form martensite in the carbon-enriched case while the low-carbon core remains tough. Case depth is controlled by temperature, time, and the diffusion coefficient of carbon in austenite — following Fick's second law. Nitriding diffuses nitrogen into the surface at lower temperatures (500-575 degrees C), forming hard nitride compounds without requiring a subsequent quench, which minimizes distortion. Induction hardening uses electromagnetic induction to rapidly heat only the surface layer of a medium-carbon steel above the austenitizing temperature, followed by immediate quenching; the core never reaches transformation temperature. Each method involves trade-offs: carburizing produces deep cases but requires quenching and may distort; nitriding produces shallower, harder cases with minimal distortion; induction hardening is fast and localized but requires sufficient carbon already in the steel.

## How It's Best Learned
Calculate the carbon concentration profile during carburizing using Fick's second law with appropriate boundary conditions, and predict the case depth for a given time and temperature. Compare hardness profiles (hardness versus depth from surface) for carburized, nitrided, and induction-hardened components. Examine cross-sections of case-hardened gears to see the distinct case and core microstructures.

## Common Misconceptions
- Case hardening is not coating — it changes the chemistry or microstructure of the steel itself rather than depositing a separate material on top.
- Nitriding does not require quenching because the hard nitride phases form during the diffusion process itself, unlike carburizing where the high carbon must be "frozen" as martensite.
- Deeper case depth is not always better — an excessively deep case can make the component behave like a through-hardened (brittle) part, losing the tough core advantage.
