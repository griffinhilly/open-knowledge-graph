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

## Explainer

From stress-strain behavior, you know the key features of the stress-strain curve: the initial linear elastic region (slope = Young's modulus), the yield point where permanent deformation begins, the ultimate tensile strength (UTS) at the peak, and the fracture point. Mechanical tests are standardized procedures that extract specific numbers from those features in a reproducible, comparable way. Each test is engineered to isolate one aspect of behavior.

The **tensile test** is the most complete single test. A "dogbone" specimen — with a narrow gauge section to ensure predictable fracture location — is gripped at both ends and pulled at a controlled rate. A load cell and extensometer record force and elongation, which are converted to engineering stress (F/A₀) and engineering strain (ΔL/L₀). From the resulting curve you read directly: E from the elastic slope, yield strength from the 0.2% offset (the stress at which a line parallel to the elastic slope, offset by 0.2% strain, intersects the curve), UTS at the peak, and ductility as the percent elongation at fracture. This single test answers: how stiff is it, how strong is it, and how much can it deform before breaking?

**Hardness tests** trade completeness for speed and minimal specimen preparation. A standardized indenter is pressed into the surface under a defined load, and the size or depth of the resulting indent is measured. The Brinell test uses a 10-mm steel ball and a large load, producing a wide indent measured under a microscope — it's better for coarse-grained materials like cast iron. The Rockwell test measures depth directly and gives an immediate readout — faster and better for production floor use. The Vickers test uses a pyramidal diamond indenter and applies across all hardness levels. All three correlate approximately with tensile strength: for steels, UTS (MPa) ≈ 3.3 × Brinell Hardness Number. Hardness is fast, nearly non-destructive, and maps easily across a component — which is why production lines use it rather than tensile testing every part.

The **Charpy V-notch impact test** measures something neither of the above tests captures: energy absorption under rapid, dynamic loading with a stress concentration present. A notched specimen is struck by a swinging pendulum, and the difference in pendulum height before and after gives the energy absorbed in fracture. The key use is plotting absorbed energy against temperature. For many body-centered cubic metals (especially mild steels), there is a narrow temperature range — the **ductile-to-brittle transition temperature (DBTT)** — above which the steel absorbs a large amount of energy (ductile fracture, dimpled surface) and below which it absorbs very little (brittle cleavage, flat crystallographic surface). This transition caused catastrophic failures in World War II Liberty ships operating in cold North Atlantic water: their steel had a DBTT above the ocean temperature, making them behave like glass in service. Understanding the DBTT is now a design requirement for any structure exposed to low-temperature conditions.
