---
id: plastic-deformation-mechanisms
title: Plastic Deformation and Slip Systems
domain: engineering
course: materials-science
prerequisites:
- id: crystal-defects
  type: hard
- id: miller-indices
  type: hard
- id: stress-strain-behavior
  type: hard
builds-toward:
- strengthening-mechanisms
tags:
- slip
- dislocations
- plastic-deformation
- schmid-factor
stage: advanced
status: validated
---

# Plastic Deformation and Slip Systems

## Core Idea
Plastic deformation in crystalline metals occurs primarily by dislocation motion along specific slip systems — combinations of a close-packed plane and a close-packed direction. FCC metals (e.g., copper, aluminum) have 12 slip systems and are generally ductile; BCC metals have more systems but require higher stress to activate them; HCP metals have fewer systems and tend toward brittleness. The critical resolved shear stress (Schmid's law) determines when slip initiates on a given system. Deformation accumulates as dislocations glide, interact, and multiply.

## How It's Best Learned
Apply Schmid's law to predict which slip system activates first for a given loading direction. Compare dislocation density before and after cold working to connect microscopic mechanism to macroscopic strain hardening.

## Common Misconceptions
- Dislocations don't require all atoms in a plane to move simultaneously — it's sequential, like moving a rug wrinkle, which is why real yield stresses are orders of magnitude below the theoretical shear strength.

## Explainer

From your study of crystal defects, you know that dislocations are line defects — a boundary between a slipped and unslipped region of the crystal. From stress-strain behavior you know that plastic deformation is permanent, unlike elastic deformation. The connection between these two concepts is this: **plastic deformation in metals is almost entirely dislocation motion**. When enough shear stress acts on a slip plane, dislocations glide through the crystal, shifting one half of the crystal relative to the other by one atomic spacing at a time. The cumulative result of many dislocations traveling many atomic spacings is the macroscopic plastic strain you measure on a stress-strain curve.

The reason dislocations make plastic deformation so easy compared to a perfect crystal is the rug analogy. To slide a heavy rug across a floor, you could push the whole rug simultaneously — nearly impossible. Or you could create a wrinkle and push the wrinkle: trivially easy, and the net result after the wrinkle travels across is that the rug has moved one rug-length. A dislocation is that wrinkle. In a perfect crystal, the theoretical shear strength to slide one atomic plane over another is about G/30, where G is the shear modulus — roughly 3 GPa for copper. Real copper yields around 50 MPa — sixty times lower — precisely because dislocations make atomic-scale sequential motion available.

The **slip system** specifies which plane and direction this motion occurs on. From your Miller indices work, you know that the most densely packed planes have the largest interplanar spacing (lowest surface energy) and the most densely packed directions have the shortest Burgers vector (least lattice distortion per step). Nature selects the path of least resistance: slip concentrates on the closest-packed planes in the closest-packed directions. **FCC metals** (copper, aluminum, gold) have the {111} planes and ⟨110⟩ directions — 4 planes × 3 directions = 12 slip systems, so there is almost always a favorably oriented system no matter how the crystal is loaded. This is why FCC metals are so ductile. **HCP metals** (magnesium, zinc) have the (0001) basal plane and just three ⟨11̄20⟩ directions — only 3 slip systems, easily exhausted, which makes HCP metals brittle at room temperature unless deformation twins supplement slip.

**Schmid's law** gives the precise condition for slip initiation: slip starts on a given system when the resolved shear stress on that system reaches the **critical resolved shear stress** τ_crss. The resolved shear stress is τ = σ · cos(φ) · cos(λ), where φ is the angle between the tensile axis and the slip plane normal, and λ is the angle between the tensile axis and the slip direction. The product cos(φ)·cos(λ) is the **Schmid factor**, maximized at 45° (where both cosines equal 1/√2 and their product is 0.5). This is why polycrystalline metals yield at one-half the single-crystal theoretical shear strength under tension: the most favorably oriented grain has a Schmid factor of 0.5. Grains oriented with a ⟨100⟩ or ⟨111⟩ axis parallel to the tensile axis have low Schmid factors on all slip systems and require higher applied stress to yield, which is the foundation of texture strengthening.


