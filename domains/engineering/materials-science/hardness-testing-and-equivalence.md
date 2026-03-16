---
id: hardness-testing-and-equivalence
title: Hardness Testing Methods and Hardness Equivalence
domain: engineering
course: materials-science
prerequisites:
- id: mechanical-testing-methods
  type: hard
- id: elastic-constants-and-elasticity
  type: soft
tags:
- hardness
- testing
- indentation
- vickers
- rockwell
- brinell
stage: formal-systems
status: draft
---

# Hardness Testing Methods and Hardness Equivalence

## Core Idea
Hardness testing measures resistance to permanent indentation through multiple methods: Vickers (pyramidal indenter, load-independent), Rockwell (conical indenter, multiple scales), and Brinell (spherical indenter). Hardness correlates with yield strength and wear resistance. Conversion tables enable approximation between scales, though perfect conversion is impossible due to different stress states.

## Explainer

From mechanical testing methods you know that a tensile test measures stress versus strain over the full elastic and plastic range, yielding Young's modulus, yield strength, and ultimate tensile strength. That test is thorough but destructive — you consume an entire specimen. **Hardness testing** offers a quick, nearly nondestructive alternative: press a hard indenter into the material surface, remove it, and measure either the size of the residual impression or the depth of penetration. The resistance to that permanent indentation is the hardness.

The three dominant methods differ in indenter geometry and what they measure. The **Vickers** test uses a square pyramidal diamond indenter and measures the diagonal length of the residual impression under a specified load. Because the pyramid maintains the same shape at all scales, the Vickers Hardness Number (HV) is approximately load-independent — you can use a microhardness load to measure individual phases in a microstructure or a macrohardness load to characterize a bulk part, and you get comparable numbers. This makes Vickers the most versatile method and the international standard for research and precision work. The **Brinell** test uses a hardened steel or carbide sphere and measures impression diameter; it averages over a larger area and is preferred for coarse-grained materials like cast iron where local variation would make a small indentation unrepresentative. The **Rockwell** test measures penetration depth under a minor preload then a major load, reading hardness directly off a dial — fast, operator-friendly, and widely used in manufacturing quality control. Different Rockwell scales (HRC for hard steels, HRB for softer metals) accommodate the range of materials encountered.

The physical basis for hardness is the **plastic zone** beneath the indenter. When the indenter is pressed in, the material directly below yields plastically while a surrounding elastic "halo" constrains it, creating a complex triaxial stress state. This is why hardness correlates empirically with yield strength — both reflect resistance to plastic deformation — but the relationship is approximate (tensile strength ≈ HV × 3.3 in MPa for steels) because the stress state during indentation differs from uniaxial tension. The conversion also breaks down for anisotropic or work-hardened materials where surface condition diverges from bulk properties.

Converting between Vickers, Rockwell, and Brinell scales is inherently approximate because each method interrogates a different volume at a different strain rate under a different stress state. Standard conversion tables (ASTM E140) are empirically derived from parallel measurements on a large set of steel specimens — they work well for steels near the tested range but should not be applied to aluminum, titanium, or ceramics without caution. The practical lesson is to specify hardness in the scale actually measured, use conversions only for rough cross-checking, and recognize that a Rockwell C hardness of 60 and its nominal Vickers equivalent are measuring fundamentally different things that happen to correlate.
