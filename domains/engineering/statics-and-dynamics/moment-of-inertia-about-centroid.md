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
builds-toward:
- principal-axes-and-rotation
- shear-force-bending-moment-diagrams
tags:
- centroidal-axes
- parallel-axis-theorem
- composite
stage: formal-systems
status: draft
---

# Moment of Inertia about Centroidal Axes

## Core Idea
The moment of inertia about centroidal axes is minimal and is used as a reference point. Using the parallel-axis theorem, the moment of inertia about any parallel axis is I = I_c + A d². For composite sections, calculate the centroid first, then sum the individual moments of inertia (corrected for distance) to find the total.

## Explainer

From your prerequisite work with the second moment of area and double integrals, you know that I = ∫ r² dA measures how area is distributed around an axis — and that it governs resistance to bending the same way mass governs resistance to acceleration. But raw second moments depend on which axis you choose. The **centroidal moment of inertia** I_c is special: it is the value about the axis passing through the centroid (the area's center of mass), and this is the minimum value among all parallel axes. Standard tables (for rectangles, circles, I-sections) tabulate I_c for this reason — it's the most compact, reference-independent description of a cross-section's geometry.

The **parallel-axis theorem** bridges I_c to any other parallel axis: I = I_c + A d², where d is the perpendicular distance between the centroidal axis and the new axis. The term A d² is always non-negative, confirming that I_c is the minimum. The physical intuition: every piece of area contributing to I_c is measured from the centroid, which minimizes the sum of squared distances by definition of the centroid. Moving to any other axis increases those distances for some area without decreasing them for any area on net. The extra term A d² captures the bulk translation of the entire cross-section through distance d.

For **composite sections** — L-sections, T-beams, built-up I-sections assembled from rectangles and circles — the procedure follows a strict three-step order. First, locate the **composite centroid** using area-weighted averaging of component centroids (from your centroid-areas-composite work). Second, for each component, compute the distance d_i from its own centroidal axis to the composite centroidal axis. Third, apply the parallel-axis theorem to transfer each component's tabulated I_c,i to the composite centroidal axis: I_i = I_c,i + A_i d_i². Sum these to get the total I. The critical error to avoid: d_i is measured from each component's *own* centroid to the *composite* centroid, not to some arbitrary reference.

The reason this matters for structural engineering is the bending stress formula σ = M y / I, where I is the moment of inertia about the neutral axis (which coincides with the centroidal axis for symmetric sections under pure bending). A larger I at the same moment M means lower stress and higher stiffness. An **I-beam** is optimally shaped precisely because the parallel-axis theorem makes flanges far from the neutral axis disproportionately effective: each flange contributes a small I_c (it's thin) plus a large A d² (it's far from the neutral axis). The parallel-axis theorem makes explicit the engineering principle: concentrate material as far from the bending axis as possible, and you get the most bending resistance per unit of material.

The **mass moment of inertia** you've studied (from mass-moment-of-inertia) follows the identical parallel-axis theorem, with mass replacing area: I = I_cm + M d². The centroidal axis becomes the axis through the center of mass, and the minimum inertia property holds there too. Both cases — area moments for stress analysis, mass moments for rotational dynamics — share the same mathematical structure, so intuition built in one domain transfers directly to the other.
