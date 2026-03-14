---
id: mechanical-testing-methods
title: Mechanical Testing Methods
domain: engineering
course: materials-science
prerequisites:
- id: stress-strain-behavior
  type: hard
builds-toward:
- fracture-mechanics
- fatigue-in-materials
tags:
- tensile-test
- hardness
- impact-test
- charpy
- mechanical-testing
stage: formal-systems
status: validated
---

# Mechanical Testing Methods

## Core Idea
Standardized mechanical tests quantify material properties reproducibly. The tensile test measures Young's modulus, yield strength, UTS, and ductility. Hardness tests (Rockwell, Brinell, Vickers) use indentation to infer resistance to plastic deformation and correlate approximately with tensile strength. The Charpy V-notch impact test measures toughness and reveals the ductile-to-brittle transition temperature (DBTT) critical for structural steels used in cold environments. Each test probes a different facet of mechanical behavior and is standardized by ASTM or ISO.

## How It's Best Learned
Cross-reference test conditions with the property being measured. For the Charpy test, plot absorbed energy vs. temperature for a steel specimen to identify the DBTT and understand why it matters for engineering design.

## Common Misconceptions
- Hardness is not the same as strength, though they correlate. A hard material can still be brittle.
- Impact toughness and fracture toughness (KIc) are related but distinct measures; confusing them is a common design error.
