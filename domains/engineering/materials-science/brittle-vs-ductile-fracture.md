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
