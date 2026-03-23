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
stage: formal-systems
status: validated
---

# Plastic Deformation and Slip Systems

## Core Idea
Plastic deformation in crystalline metals occurs primarily by dislocation motion along specific slip systems — combinations of a close-packed plane and a close-packed direction. FCC metals (e.g., copper, aluminum) have 12 slip systems and are generally ductile; BCC metals have more systems but require higher stress to activate them; HCP metals have fewer systems and tend toward brittleness. The critical resolved shear stress (Schmid's law) determines when slip initiates on a given system. Deformation accumulates as dislocations glide, interact, and multiply.

## How It's Best Learned
Apply Schmid's law to predict which slip system activates first for a given loading direction. Compare dislocation density before and after cold working to connect microscopic mechanism to macroscopic strain hardening.

## Common Misconceptions
- Dislocations don't require all atoms in a plane to move simultaneously — it's sequential, like moving a rug wrinkle, which is why real yield stresses are orders of magnitude below the theoretical shear strength.

## Questions

```yaml
- question: "Copper's theoretical shear strength is approximately 3 GPa (about G/30), yet copper actually yields around 50 MPa. What accounts for this 60-fold discrepancy?"
  type: multiple-choice
  options:
    - "Copper is a soft metal with unusually weak metallic bonds compared to harder metals"
    - "Impurities in commercial copper lower its strength significantly below the theoretical pure-crystal value"
    - "Dislocations allow sequential atomic-scale slip — like pushing a wrinkle across a rug — which requires far less stress than sliding an entire plane simultaneously"
    - "The theoretical value assumes single-crystal copper; polycrystalline copper is weaker because grain boundaries act as stress concentrators"
  answer: 2
  explanation: "The rug analogy captures the key insight: sliding a whole rug simultaneously is nearly impossible, but pushing a wrinkle across it is trivial, and the net result is that the rug moved. Dislocations are that wrinkle — a line defect that allows one atomic spacing of slip to propagate sequentially through the crystal at a fraction of the theoretical stress for simultaneous sliding. This is why real metals yield at stresses far below G/30 and why controlling dislocation motion (through alloying, work hardening, grain refinement) is the central strategy of strengthening."

- question: "A single FCC crystal is loaded in tension with the tensile axis oriented 45° to a {111} slip plane normal and 45° to a ⟨110⟩ slip direction. According to Schmid's law, what is the Schmid factor and what does this imply?"
  type: multiple-choice
  options:
    - "Schmid factor = 1.0 — this orientation activates slip at the lowest possible applied stress"
    - "Schmid factor = 0.5 — this orientation maximizes the resolved shear stress on this slip system, so slip initiates at the lowest applied stress"
    - "Schmid factor = 0.5 — but this is the worst orientation for slip; ⟨100⟩ loading gives a factor of 1.0"
    - "Schmid factor = 0.25 — the factor is cos²(45°) because both angles are equivalent"
  answer: 1
  explanation: "Schmid factor = cos(φ)·cos(λ). Both angles are 45°, so the factor = (1/√2)(1/√2) = 0.5. This is the maximum possible Schmid factor — no orientation can exceed 0.5 — so this orientation initiates slip at the lowest applied tensile stress. Grains with ⟨100⟩ or ⟨111⟩ axes parallel to loading have low Schmid factors on all slip systems and require much higher applied stress to yield, which is exploited in texture strengthening."

- question: "Plastic deformation by dislocation motion requires all atoms in the slip plane to move simultaneously."
  type: true-false
  answer: false
  explanation: "The entire point of dislocation theory is that atoms move sequentially, not simultaneously. A dislocation is the boundary between a slipped and unslipped region; as it glides through the crystal, each successive row of atoms slips by one spacing while the rest remain stationary. This sequential mechanism is why real yield stresses are ~60× below theoretical values. Requiring simultaneous movement of an entire plane (as in the theoretical calculation) demands an enormous stress; moving a dislocation through the lattice requires only a tiny local distortion."

- question: "FCC metals have more active slip systems than HCP metals, which contributes to their greater ductility."
  type: true-false
  answer: true
  explanation: "True. FCC metals have 12 slip systems ({111}⟨110⟩ — 4 planes × 3 directions), so there is almost always a favorably oriented system available no matter how the crystal is loaded. HCP metals typically have only 3 easy slip systems on the basal (0001) plane, which are easily exhausted. When all available slip systems are blocked, the material cannot accommodate further deformation and fractures instead of deforming plastically. This is why magnesium and zinc (HCP) are brittle at room temperature without the additional slip and twinning mechanisms that activate at higher temperatures."

- question: "Why do FCC metals deform plastically much more easily than HCP metals under comparable stress conditions, even when their bond strengths are similar?"
  type: short-answer
  answer: "The key difference is the number of available slip systems. FCC metals have 12 slip systems (4 close-packed {111} planes × 3 ⟨110⟩ directions), so a favorably oriented slip system is almost always available for any loading direction — plastic deformation can proceed without exhausting all options. HCP metals have only 3 easy slip systems on the basal plane, and once these are loaded unfavorably or exhausted, no alternative system is available. The crystal cannot accommodate the imposed strain and fractures instead. More slip systems = more pathways for strain accommodation = greater ductility."
  explanation: "This tests whether students can connect the crystallography (number and orientation of slip systems) to macroscopic mechanical behavior. The insight is that ductility is not just about bond strength — it's about geometric flexibility in accommodating deformation."
```

## Explainer

From your study of crystal defects, you know that dislocations are line defects — a boundary between a slipped and unslipped region of the crystal. From stress-strain behavior you know that plastic deformation is permanent, unlike elastic deformation. The connection between these two concepts is this: **plastic deformation in metals is almost entirely dislocation motion**. When enough shear stress acts on a slip plane, dislocations glide through the crystal, shifting one half of the crystal relative to the other by one atomic spacing at a time. The cumulative result of many dislocations traveling many atomic spacings is the macroscopic plastic strain you measure on a stress-strain curve.

The reason dislocations make plastic deformation so easy compared to a perfect crystal is the rug analogy. To slide a heavy rug across a floor, you could push the whole rug simultaneously — nearly impossible. Or you could create a wrinkle and push the wrinkle: trivially easy, and the net result after the wrinkle travels across is that the rug has moved one rug-length. A dislocation is that wrinkle. In a perfect crystal, the theoretical shear strength to slide one atomic plane over another is about G/30, where G is the shear modulus — roughly 3 GPa for copper. Real copper yields around 50 MPa — sixty times lower — precisely because dislocations make atomic-scale sequential motion available.

The **slip system** specifies which plane and direction this motion occurs on. From your Miller indices work, you know that the most densely packed planes have the largest interplanar spacing (lowest surface energy) and the most densely packed directions have the shortest Burgers vector (least lattice distortion per step). Nature selects the path of least resistance: slip concentrates on the closest-packed planes in the closest-packed directions. **FCC metals** (copper, aluminum, gold) have the {111} planes and ⟨110⟩ directions — 4 planes × 3 directions = 12 slip systems, so there is almost always a favorably oriented system no matter how the crystal is loaded. This is why FCC metals are so ductile. **HCP metals** (magnesium, zinc) have the (0001) basal plane and just three ⟨11̄20⟩ directions — only 3 slip systems, easily exhausted, which makes HCP metals brittle at room temperature unless deformation twins supplement slip.

**Schmid's law** gives the precise condition for slip initiation: slip starts on a given system when the resolved shear stress on that system reaches the **critical resolved shear stress** τ_crss. The resolved shear stress is τ = σ · cos(φ) · cos(λ), where φ is the angle between the tensile axis and the slip plane normal, and λ is the angle between the tensile axis and the slip direction. The product cos(φ)·cos(λ) is the **Schmid factor**, maximized at 45° (where both cosines equal 1/√2 and their product is 0.5). This is why polycrystalline metals yield at one-half the single-crystal theoretical shear strength under tension: the most favorably oriented grain has a Schmid factor of 0.5. Grains oriented with a ⟨100⟩ or ⟨111⟩ axis parallel to the tensile axis have low Schmid factors on all slip systems and require higher applied stress to yield, which is the foundation of texture strengthening.


