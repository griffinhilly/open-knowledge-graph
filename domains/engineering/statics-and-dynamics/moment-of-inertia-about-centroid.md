---
id: moment-of-inertia-about-centroid
title: Moment of Inertia about Centroidal Axes
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: second-moment-of-area-calculation
  type: hard
- id: centroid-areas-composite
  type: hard
- id: applications-double-integrals
  type: hard
- id: mass-moment-of-inertia
  type: hard
- id: center-of-mass-vs-centroid
  type: soft
builds-toward:
- principal-axes-and-rotation
- shear-force-bending-moment-diagrams
tags:
- centroidal-axes
- parallel-axis-theorem
- composite
stage: formal-systems
status: validated
---

# Moment of Inertia about Centroidal Axes

## Core Idea
The moment of inertia about centroidal axes is minimal and is used as a reference point. Using the parallel-axis theorem, the moment of inertia about any parallel axis is I = I_c + A d². For composite sections, calculate the centroid first, then sum the individual moments of inertia (corrected for distance) to find the total.

## Questions

```yaml
- question: "A rectangular cross-section has centroidal moment of inertia I_c = 100 cm⁴ and area A = 20 cm². Its centroid is 6 cm from a parallel axis. What is the moment of inertia about that parallel axis?"
  type: multiple-choice
  options:
    - "100 cm⁴ — the parallel-axis theorem doesn't apply when moving away from the centroid"
    - "220 cm⁴ — using I = I_c + A·d = 100 + 20·6 = 220"
    - "820 cm⁴ — using I = I_c + A·d² = 100 + 20·36"
    - "620 cm⁴ — subtracting A·d² because the reference axis passes through the shape"
  answer: 2
  explanation: "The parallel-axis theorem states I = I_c + A·d², where d is the perpendicular distance between axes. Here: I = 100 + 20·(6²) = 100 + 720 = 820 cm⁴. The term A·d² is always added (never subtracted), confirming I_c is the minimum moment of inertia for any parallel axis. Option B is a common error: using d instead of d² (forgetting to square the distance). Always square the distance in the parallel-axis theorem."

- question: "When computing the moment of inertia of a composite L-section, a student applies the parallel-axis theorem to each component before locating the composite centroid. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Nothing — the parallel-axis theorem can be applied to each component independently at any stage"
    - "The parallel-axis theorem requires knowing the composite centroid to compute d_i for each component correctly"
    - "The parallel-axis theorem only applies to simple shapes, not composite sections"
    - "The student should use mass moment of inertia formulas for composite cross-sections"
  answer: 1
  explanation: "The distance d_i in I_i = I_c,i + A_i·d_i² must be measured from each component's own centroid to the *composite* centroidal axis. If the composite centroid hasn't been found yet, d_i is unknown. The composite centroid is found by area-weighted averaging of component centroids first — only then can d_i be computed for each component. Applying the parallel-axis theorem prematurely produces an incorrect total I because the reference axis is wrong."

- question: "Among all axes parallel to a given centroidal axis, the centroidal axis has the smallest moment of inertia."
  type: true-false
  answer: true
  explanation: "This follows directly from the parallel-axis theorem: I = I_c + A·d². Since A > 0 and d² ≥ 0, any non-centroidal parallel axis adds a positive term A·d² to I_c. The extra term is zero only when d = 0 — i.e., at the centroidal axis itself. This minimum property is why standard tables tabulate I_c: it is the most compact, reference-independent description of a cross-section's bending geometry."

- question: "The parallel-axis theorem can be applied in reverse — subtracting A·d² — to find a moment of inertia about an axis closer to the centroid than the given reference axis."
  type: true-false
  answer: false
  explanation: "The parallel-axis theorem is I = I_c + A·d², where I_c is *specifically the centroidal* moment of inertia. You can rearrange it to I_c = I − A·d² to find I_c from a known non-centroidal I — but you cannot chain this to transfer between two arbitrary non-centroidal axes directly. The correct procedure is always: go through the centroidal axis. Transfer from a known axis to the centroid (subtract A·d²), then from the centroid to the target axis (add A·d'²). Directly subtracting to jump between non-centroidal axes is incorrect."

- question: "For a composite cross-section, why must you locate the composite centroid *before* applying the parallel-axis theorem to each component?"
  type: short-answer
  answer: "The parallel-axis theorem transfers each component's I from its own centroidal axis to the composite centroidal axis. The distance d_i in I_i = I_c,i + A_i·d_i² is measured from the component's centroid to the composite centroid. Without knowing where the composite centroid is, d_i cannot be computed. The composite centroid is found first via area-weighted averaging of the component centroids, and only then can d_i be determined for each component."
  explanation: "The structural reason this matters: in bending, stresses are computed about the neutral axis of the full cross-section, which coincides with the composite centroidal axis (for symmetric sections under pure bending). A wrong d_i produces a wrong total I, which produces wrong bending stress predictions via σ = M·y/I. The three-step order — (1) find composite centroid, (2) compute d_i for each component, (3) sum I_c,i + A_i·d_i² — is rigid and cannot be reordered."
```

## Explainer

From your prerequisite work with the second moment of area and double integrals, you know that I = ∫ r² dA measures how area is distributed around an axis — and that it governs resistance to bending the same way mass governs resistance to acceleration. But raw second moments depend on which axis you choose. The **centroidal moment of inertia** I_c is special: it is the value about the axis passing through the centroid (the area's center of mass), and this is the minimum value among all parallel axes. Standard tables (for rectangles, circles, I-sections) tabulate I_c for this reason — it's the most compact, reference-independent description of a cross-section's geometry.

The **parallel-axis theorem** bridges I_c to any other parallel axis: I = I_c + A d², where d is the perpendicular distance between the centroidal axis and the new axis. The term A d² is always non-negative, confirming that I_c is the minimum. The physical intuition: every piece of area contributing to I_c is measured from the centroid, which minimizes the sum of squared distances by definition of the centroid. Moving to any other axis increases those distances for some area without decreasing them for any area on net. The extra term A d² captures the bulk translation of the entire cross-section through distance d.

For **composite sections** — L-sections, T-beams, built-up I-sections assembled from rectangles and circles — the procedure follows a strict three-step order. First, locate the **composite centroid** using area-weighted averaging of component centroids (from your centroid-areas-composite work). Second, for each component, compute the distance d_i from its own centroidal axis to the composite centroidal axis. Third, apply the parallel-axis theorem to transfer each component's tabulated I_c,i to the composite centroidal axis: I_i = I_c,i + A_i d_i². Sum these to get the total I. The critical error to avoid: d_i is measured from each component's *own* centroid to the *composite* centroid, not to some arbitrary reference.

The reason this matters for structural engineering is the bending stress formula σ = M y / I, where I is the moment of inertia about the neutral axis (which coincides with the centroidal axis for symmetric sections under pure bending). A larger I at the same moment M means lower stress and higher stiffness. An **I-beam** is optimally shaped precisely because the parallel-axis theorem makes flanges far from the neutral axis disproportionately effective: each flange contributes a small I_c (it's thin) plus a large A d² (it's far from the neutral axis). The parallel-axis theorem makes explicit the engineering principle: concentrate material as far from the bending axis as possible, and you get the most bending resistance per unit of material.

The **mass moment of inertia** you've studied (from mass-moment-of-inertia) follows the identical parallel-axis theorem, with mass replacing area: I = I_cm + M d². The centroidal axis becomes the axis through the center of mass, and the minimum inertia property holds there too. Both cases — area moments for stress analysis, mass moments for rotational dynamics — share the same mathematical structure, so intuition built in one domain transfers directly to the other.
