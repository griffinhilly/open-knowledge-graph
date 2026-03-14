---
id: hardness-testing-methods
title: Hardness Testing Methods
domain: engineering
course: materials-science
prerequisites:
- id: mechanical-testing-methods
  type: hard
- id: strengthening-mechanisms
  type: soft
builds-toward:
- materials-selection-design
tags:
- brinell
- rockwell
- vickers
- knoop
- microhardness
- hardness-strength-correlation
stage: formal-systems
status: draft
---

# Hardness Testing Methods

## Core Idea
Hardness testing measures a material's resistance to localized plastic deformation by pressing an indenter into the surface under a controlled load and measuring the resulting impression. Different test methods suit different applications. Brinell hardness (HB) uses a large hardened steel or tungsten carbide ball, producing a wide indent well-suited for averaging over coarse microstructures like cast irons. Rockwell hardness (HR) uses either a diamond cone (C scale, for hard materials) or a steel ball (B scale, for softer materials) and reads hardness directly from the depth of penetration, making it the fastest production method. Vickers hardness (HV) uses a diamond pyramid that produces geometrically similar indentations at any load, allowing a single continuous scale from soft lead to hard ceramics. Knoop hardness (HK) uses an elongated diamond pyramid producing a shallow indent, ideal for thin coatings, brittle materials, and anisotropy measurements. Microhardness testing (Vickers or Knoop at loads below 1 kgf) can measure hardness of individual phases, heat-affected zones, or thin surface layers. A key practical relationship links hardness to tensile strength: for many steels, UTS (in MPa) is approximately 3.45 times the Brinell hardness number, providing a quick non-destructive estimate of strength.

## How It's Best Learned
Perform or observe all four major hardness tests on the same material to compare indent sizes, measurement procedures, and resulting numbers. Convert between scales using standard conversion tables and verify that the conversions are approximate, not exact. Measure microhardness across a case-hardened or welded cross-section to see how hardness varies with position and microstructure.

## Common Misconceptions
- Hardness numbers from different scales (e.g., HRC 60 vs HV 700) cannot be directly compared — they must be converted using empirical tables, and conversions are approximate.
- Hardness is not a fundamental material property like elastic modulus — it depends on the test method, load, and indenter geometry, which is why the test conditions must always be specified.
- The hardness-strength correlation (UTS = 3.45 x HB) is reliable for carbon and low-alloy steels but breaks down for work-hardened non-ferrous metals, ceramics, and polymers.
