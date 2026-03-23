---
id: root-locus-construction-rules
title: Root Locus Construction Rules
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-method
  type: hard
- id: transfer-functions-control
  type: hard
tags:
- root-locus
- asymptotes
- breakaway-points
- departure-angles
- arrival-angles
- real-axis-segments
stage: expert
status: draft
---

# Root Locus Construction Rules

## Core Idea
The root locus construction rules provide a systematic procedure for sketching the paths of closed-loop poles as gain K varies from 0 to ∞ without solving the characteristic equation numerically. The key rules are: (1) the number of branches equals the number of open-loop poles n; (2) branches start at open-loop poles (K = 0) and terminate at open-loop zeros or at infinity (K → ∞); (3) the locus is symmetric about the real axis; (4) real-axis segments exist to the left of an odd total count of real-axis poles and zeros; (5) n − m branches go to infinity along asymptotes with angles θ = 180°(2k + 1)/(n − m) emanating from the centroid σ_a = (Σpoles − Σzeros)/(n − m); (6) breakaway and break-in points on the real axis satisfy dK/ds = 0, found by differentiating K = −1/G(s)H(s); (7) departure angles from complex poles and arrival angles at complex zeros are computed from the angle condition by summing contributions from all other poles and zeros. Together these rules allow accurate hand-sketching of the locus, revealing how gain selection affects stability, damping, and natural frequency.

## How It's Best Learned
Apply the full rule set to progressively more complex open-loop transfer functions: start with two-pole systems, then three poles and one zero, then systems with complex pole pairs. Sketch each locus by hand, computing asymptote angles, centroids, breakaway points, and departure angles step by step, then overlay your sketch on MATLAB's rlocus() output to identify where your approximation deviates and why.

## Common Misconceptions
- Breakaway points do not always lie midway between adjacent poles — they are determined by dK/ds = 0 and can be at non-obvious locations, especially when zeros are present.
- The centroid formula (Σpoles − Σzeros)/(n − m) only determines where the asymptotes radiate from, not where the locus branches themselves intersect; branches may curve significantly before approaching the asymptotes.
- Departure angles from complex poles are not optional refinements — without computing them, sketches of systems with complex open-loop poles will be qualitatively wrong, potentially missing whether branches initially move toward or away from the right half-plane.

## Questions

```yaml
- question: "An open-loop system has poles at s = 0, −3, and −6 with no finite zeros (n = 3, m = 0). As K increases from 0 to ∞, what are the asymptote angles and the centroid from which they radiate?"
  type: multiple-choice
  options:
    - "All three branches converge to the centroid at s = −3 as K → ∞"
    - "Three branches go to infinity at 60°, 180°, and −60° from the centroid σ_a = (0 − 3 − 6)/3 = −3"
    - "All three branches go to infinity at 45°, 135°, and 225° because the system has three poles"
    - "The branches cannot be determined without numerically solving the characteristic equation"
  answer: 1
  explanation: "With n = 3 poles and m = 0 zeros, all three branches go to infinity (n − m = 3 asymptotes). The centroid is σ_a = (Σpoles − Σzeros)/(n − m) = (0 − 3 − 6)/3 = −3. Asymptote angles are θ = 180°(2k + 1)/(n − m) for k = 0, 1, 2: yielding 60°, 180°, and 300° (= −60°). The branches radiate to infinity in these three directions from s = −3, regardless of the exact pole spacing (which only affects the curve shape before it approaches the asymptotes)."

- question: "A system has real-axis open-loop poles at s = 0, −2, −5 and a real-axis zero at s = −3. Which real-axis segments belong to the root locus?"
  type: multiple-choice
  options:
    - "The entire negative real axis, because poles always outnumber zeros"
    - "Between s = 0 and s = −2 (one real pole to the right), and between s = −3 and s = −5 (three real critical values to the right: pole at 0, pole at −2, zero at −3)"
    - "Between s = −2 and s = −3 (two poles to the right), and to the left of s = −5 (four critical values)"
    - "Only to the left of s = −5 because the zero at −3 cancels one pole contribution"
  answer: 1
  explanation: "The real-axis rule: a segment belongs to the root locus when the total count of real-axis poles AND zeros to its right is odd. (1) Between 0 and −2: one pole at 0 is to the right → count = 1 (odd) → on locus. (2) Between −2 and −3: poles at 0 and −2 → count = 2 (even) → not on locus. (3) Between −3 and −5: poles at 0, −2 and zero at −3 → count = 3 (odd) → on locus. (4) Left of −5: all four elements → count = 4 (even) → not on locus."

- question: "The centroid σ_a = (Σpoles − Σzeros)/(n − m) indicates where root-locus branches cross or intersect each other on the real axis."
  type: true-false
  answer: false
  explanation: "The centroid determines only where the asymptotes RADIATE FROM — it is the geometric origin of the n − m lines along which branches escape to infinity. The centroid is not a point where branches intersect, and root-locus branches do not necessarily pass through it. Actual breakaway and break-in points on the real axis are found by solving dK/ds = 0, which can yield answers far from the centroid — especially when zeros are present. This is one of the most common misapplications of the asymptote rules."

- question: "Departure angles from complex open-loop poles must be computed explicitly; without them, a hand-sketched root locus may be qualitatively wrong about whether branches initially move toward the right half-plane."
  type: true-false
  answer: true
  explanation: "Departure angles are computed by applying the angle condition at a point infinitesimally close to a complex pole. The contributions from all other poles and zeros determine the net phase, and the departure angle is whatever value satisfies the ±180° requirement. This angle determines whether the branch initially moves left (toward stability) or right (toward instability). For systems with complex open-loop poles — common in underdamped or resonant plants — omitting this computation can produce a qualitatively wrong sketch that gives incorrect stability predictions at low gain."

- question: "The real-axis rule states a segment belongs to the root locus only when there is an ODD count of real poles and zeros to its right. Why odd and not even?"
  type: short-answer
  answer: "The root locus is defined by the angle condition: ∠G(s)H(s) = ±180°(2k+1). On the real axis, conjugate complex poles and zeros contribute phase in pairs that cancel exactly. Only real-axis poles and zeros contribute net phase: each real pole or zero to the RIGHT of a test point contributes ±180°. For the total to equal an odd multiple of 180° (the angle condition), the number of such contributions must be odd — an even count sums to a multiple of 360°, which fails the condition. The real-axis rule is therefore not a separate memorized fact but a direct consequence of the angle condition evaluated on the real axis."
  explanation: "This derivation shows why construction rules are not arbitrary mnemonics. Every rule — real axis, asymptotes, breakaway points, departure angles — is the angle condition applied in a different geometric context. Understanding this derivation means you can reconstruct the rules from first principles if you forget them, and you can correctly apply the real-axis rule even in unusual configurations with multiple zeros."
```

## Explainer

The root locus you studied introduced the concept: as gain K increases from 0 to ∞, the closed-loop poles trace continuous paths in the complex plane. The construction rules make those paths sketchable by hand, deriving everything from a single condition — the **angle condition**: a point s lies on the root locus if and only if ∠G(s)H(s) = ±180°(2k+1) for some integer k. Every construction rule is a consequence of enforcing this condition in a different geometric setting.

Rules 1–4 build the skeleton. **Branches** equal the number of open-loop poles n, each starting at a pole (K=0, where the closed-loop pole coincides with the open-loop pole) and ending at a zero or at infinity (K→∞). Symmetry about the real axis follows from the fact that characteristic polynomial coefficients are real — complex roots come in conjugate pairs, so if s is on the locus, so is s*. The **real-axis rule** derives from the angle condition evaluated on the real axis: complex poles and zeros each contribute ±180° that cancel in conjugate pairs, leaving only real-axis elements to contribute phase. Each real pole or zero to the right of a test point contributes ±180°. The net angle is ±180°(odd) exactly when there is an odd number of real poles and zeros to the right — so those segments belong to the locus.

Rules 5–7 handle the harder geometry. The **asymptote rule** describes the n−m branches headed to infinity. Far from the origin, all finite poles and zeros merge into an equivalent system with n−m excess poles concentrated at the **centroid** σ_a = (Σpoles − Σzeros)/(n−m). The asymptote angles θ = 180°(2k+1)/(n−m) distribute these branches evenly around the centroid. A 3-pole, 1-zero system has two branches going to infinity at ±90° from the centroid — regardless of where the specific poles and zeros sit. **Breakaway and break-in points** are where the locus enters or leaves the real axis; multiple branches pass through the same point at the same gain, which requires dK/ds = 0. **Departure angles** from complex poles are computed by applying the angle condition at a point infinitesimally close to the pole: the contributions from all other poles and zeros are known, and the required total of ±180° determines which direction the branch must depart.

Together, the rules give a qualitative picture of how all closed-loop poles move across all gain values simultaneously — something no single root-finding computation can provide. The design payoff: if a set of open-loop poles places locus branches heading toward the right half-plane at moderate gain, you can add a compensator zero to bend them back. If the asymptotes project into the right half-plane, you can shift the centroid leftward by adding a pole-zero pair that adjusts Σpoles − Σzeros. The construction rules are the analytical vocabulary for reading and manipulating this picture systematically.
