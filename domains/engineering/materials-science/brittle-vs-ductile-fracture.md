---
id: brittle-vs-ductile-fracture
title: Brittle vs Ductile Fracture
domain: engineering
course: materials-science
prerequisites:
- id: fracture-mechanics
  type: hard
- id: stress-strain-behavior
  type: hard
builds-toward:
- impact-testing-toughness
tags:
- fracture-modes
- ductile-brittle-transition
- cup-and-cone
- cleavage-fracture
- temperature-effects
stage: formal-systems
status: draft
---

# Brittle vs Ductile Fracture

## Core Idea
Materials fail by fundamentally different fracture mechanisms depending on their ability to undergo plastic deformation before breaking. Ductile fracture involves substantial plastic deformation and energy absorption: microvoids nucleate at inclusions or second-phase particles, grow under triaxial stress, and coalesce to form a crack that propagates slowly and with warning. The classic macroscopic signature in a tensile specimen is the cup-and-cone fracture surface — a fibrous central region (from void coalescence) surrounded by a shear lip at 45 degrees. Brittle fracture, by contrast, involves rapid crack propagation along specific crystallographic planes (cleavage) or along grain boundaries (intergranular fracture) with minimal plastic deformation and little energy absorption. The fracture surface appears flat, faceted, and granular. Many BCC metals (steel, tungsten) and some HCP metals exhibit a ductile-to-brittle transition temperature (DBTT): above it, they fracture in a ductile mode with high energy absorption; below it, they fail by brittle cleavage. FCC metals (aluminum, copper, austenitic stainless steels) generally do not show a sharp DBTT and remain ductile to very low temperatures. The DBTT is critically important for structural design — the Liberty ship failures and Titanic fractures were partly attributed to steels operating below their DBTT.

## How It's Best Learned
Compare SEM fractographs of ductile (dimpled) versus brittle (cleavage facets or intergranular) fracture surfaces side by side. Plot absorbed energy from Charpy impact tests versus temperature to identify the DBTT for a BCC steel and compare it to an FCC alloy that shows no transition. Analyze the Titanic or Liberty ship case studies to connect materials science to real engineering failure.

## Common Misconceptions
- Brittle fracture does not mean the material is inherently weak — it means the material cannot absorb energy through plastic deformation, so failure is sudden regardless of the material's ultimate strength.
- The ductile-to-brittle transition is not a universal phenomenon — FCC metals like copper and aluminum do not exhibit a sharp transition and remain ductile at cryogenic temperatures.
- A material is not either ductile or brittle in an absolute sense — the same steel can fracture in a ductile mode at room temperature and a brittle mode at minus 40 degrees C.

## Explainer

Your stress-strain background gives you the foundation here. In a ductile material, the stress-strain curve shows a long plastic plateau — energy is continuously absorbed as dislocations move, slip planes shear, and the material necks before finally separating. In a brittle material, the curve has no such plateau: the material behaves elastically all the way to fracture, and the sudden crack releases stored elastic energy almost instantaneously. The difference is not about which material is "stronger" — a brittle ceramic or glass can have very high ultimate strength — but about how much energy is absorbed and how much warning the fracture gives before it occurs.

**Ductile fracture** begins microscopically: under triaxial tension (especially at a notch or stress concentration), small voids nucleate at inclusions, second-phase particles, or grain boundary precipitates. Each void grows as the material around it deforms plastically, and neighboring voids eventually connect — a process called **void coalescence** — to form a crack that propagates slowly across the cross section. In a tensile specimen this produces the classic **cup-and-cone** fracture: the central region shows a fibrous, dimpled texture (from void coalescence) and the periphery shows a 45-degree shear lip (from shear failure under the maximum shear stress, which acts at 45° to the tensile axis). The dimpled texture is the SEM signature of ductile fracture.

**Brittle fracture** involves crack propagation along specific crystallographic planes — **cleavage** — or along grain boundaries — **intergranular fracture**. In cleavage, the crack follows the lowest-energy crystallographic plane (e.g., {100} planes in BCC iron), splitting atomic bonds directly rather than shearing them. The fracture surface looks flat, faceted, and granular, with characteristic **river markings** showing the direction of crack propagation. No significant plastic deformation occurs, so the energy absorbed is tiny compared to ductile fracture. The crack can propagate at speeds approaching the speed of sound — which is why brittle fractures are sudden and catastrophic.

The **ductile-to-brittle transition temperature** (DBTT) is a critical property of BCC metals like structural steel. Above the DBTT, dislocation mobility is high enough that plastic deformation precedes fracture. Below it, dislocations are pinned, and cleavage becomes energetically competitive with the stress required for plastic flow — so the material switches to brittle behavior. The DBTT can be measured with a Charpy impact test: plot absorbed energy versus temperature, and you see a sigmoidal curve dropping from high values (ductile) to low values (brittle) over a transition range. FCC metals (aluminum, copper, gold, austenitic steels) have enough slip systems and sufficient dislocation mobility at all temperatures that they never exhibit a sharp DBTT — they remain ductile down to cryogenic temperatures.

The engineering stakes are enormous. The Liberty ships of World War II used notch-sensitive steels with a DBTT near 0°C; welds created stress concentrations that acted as crack initiators, and ships operating in the cold North Atlantic failed by brittle fracture — a whole ship could split in two. The Titanic's hull plates have been shown by modern analysis to have had a DBTT well above the −2°C water temperature on the night of the collision. These are not just historical curiosities: any design specifying a BCC structural steel for service below 0°C requires impact testing to verify the DBTT is safely below the operating temperature, with a design margin for uncertainty and dynamic loading.
