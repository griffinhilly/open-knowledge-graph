---
id: root-locus-asymptote-centroid-breakaway
title: 'Root Locus: Asymptotes, Centroid, and Breakaway Points'
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-angle-magnitude-equations
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- root-locus
- asymptotes
- centroid
- breakaway-points
stage: advanced
status: validated
---

# Root Locus: Asymptotes, Centroid, and Breakaway Points

## Core Idea
Asymptotes describe locus behavior at high frequency (σ = Σpoles - Σzeros)/(#poles - #zeros), angles = 180°(2k+1)/(n-m)). Centroid is their intersection point. Breakaway/break-in points occur where dK/ds = 0, indicating multiple roots. These features enable sketching the locus without computing every point.

## Questions

```yaml
- question: "A system has open-loop poles at s = 0, −1, −2, −3 and a single open-loop zero at s = −5. How many root locus asymptotes are there, and what are their angles?"
  type: multiple-choice
  options:
    - "4 asymptotes at 45°, 135°, 225°, 315°"
    - "3 asymptotes at 60°, 180°, 300°"
    - "5 asymptotes at 36°, 108°, 180°, 252°, 324°"
    - "3 asymptotes at 45°, 135°, 225°"
  answer: 1
  explanation: "The number of asymptotes equals n − m (poles minus zeros) = 4 − 1 = 3. The angles are 180°(2k+1)/(n−m) for k = 0, 1, 2: (180°×1)/3 = 60°; (180°×3)/3 = 180°; (180°×5)/3 = 300°. Answer A is the common error of using n (total poles) rather than n−m (excess poles). Answer D uses the wrong formula yielding 45° intervals. Only branches that cannot reach a finite zero escape to infinity along asymptotes."

- question: "A system's root locus centroid is computed as σ_a = (Σ real parts of poles − Σ real parts of zeros) / (n − m) = −0.5. What does this tell you about the system's behavior at high gain?"
  type: multiple-choice
  options:
    - "All branches will remain stable for all values of gain K, since the centroid is in the left half-plane"
    - "The asymptotes pass through s = −0.5, so branches escaping to infinity will cross the imaginary axis relatively quickly, suggesting the system becomes unstable at moderate-to-high gain"
    - "The system will be critically damped at the centroid location"
    - "Breakaway points will occur at s = −0.5 on the real axis"
  answer: 1
  explanation: "The centroid anchors the asymptotes on the real axis. With σ_a = −0.5, the asymptotes pass very close to the imaginary axis. For asymptotes at 60° and 300° (common for a 3-asymptote system), branches heading toward infinity will cross the imaginary axis not far from the centroid — meaning instability occurs at relatively modest gain. A centroid deep in the left half-plane (e.g., σ_a = −10) would indicate the system can tolerate much higher gain before going unstable. Answer A is wrong because stability depends on where the asymptotes go, not just whether the centroid is negative."

- question: "A breakaway point on the root locus is a location on the real axis where two closed-loop poles meet and then depart into the complex plane as conjugate pairs, corresponding to a repeated root of the characteristic equation."
  type: true-false
  answer: true
  explanation: "At a breakaway point, two root locus branches traveling along the real axis in opposite directions meet at a point of repeated roots. The characteristic equation has a double root there, and for infinitesimally larger gain, the two poles split into complex conjugate pairs leaving the real axis. Mathematically, breakaway points are found by dK/ds = 0 along the locus — the gain K reaches a local maximum or minimum as a function of s along the real axis."

- question: "The asymptote angles of a root locus depend on the exact numerical locations of the open-loop poles and zeros, not just on how many there are."
  type: true-false
  answer: false
  explanation: "Asymptote angles depend only on the *count* n − m (number of poles minus zeros), not on their specific locations. The formula 180°(2k+1)/(n−m) contains no information about where the poles and zeros are — just how many excess poles exist. In contrast, the *centroid* σ_a = (Σ real parts of poles − Σ real parts of zeros)/(n − m) does depend on the actual pole and zero locations. This is a critical distinction: you can determine asymptote angles from the system's order alone, but placing the asymptotes in the s-plane requires computing the centroid."

- question: "What information does the centroid of the root locus asymptotes provide to a control system designer, and how does it guide compensator design?"
  type: short-answer
  answer: "The centroid σ_a = (Σ real parts of poles − Σ real parts of zeros)/(n − m) is the point on the real axis through which all asymptotes pass. Its location tells the designer whether branches escaping to infinity will remain in the stable left half-plane (centroid far left) or cross the imaginary axis at relatively low gain (centroid near zero or positive). If the centroid is near the imaginary axis, the system will become unstable at moderate gain — making high-gain operation infeasible. A compensator designer can shift the centroid leftward by adding a zero (which decreases the numerator sum in the formula) or removing a pole, making the asymptotes pass through a more negative location and allowing higher gain before instability. The centroid thus provides the first quick check on whether a proposed plant can be stabilized by gain alone or requires zero placement."
  explanation: "The key is understanding that the centroid is not just a formula to memorize but a design guideline: it summarizes in a single number where the 'center of gravity' of the escaping branches is, and it's directly actionable through compensator zero placement."
```

## Explainer

From your work on the root locus angle and magnitude equations, you know that as gain K increases from 0 to ∞, the closed-loop poles travel continuously along paths in the s-plane that start at the open-loop poles (K = 0) and end at the open-loop zeros (K → ∞). If there are more poles than zeros — which is almost always true in physical systems — some branches cannot end at finite zeros. Instead, they travel outward toward infinity along **asymptotes**. Understanding where those asymptotes go is essential for predicting whether a high-gain system will be stable.

The **asymptote angles** are evenly spaced at 180°(2k+1)/(n−m) degrees, where n is the number of poles and m the number of zeros, and k = 0, 1, 2, … up to (n−m−1). For a system with 3 poles and 1 zero, there are 2 asymptotes at angles of 90° and 270° (straight up and straight down in the s-plane). For 3 poles and 0 zeros, the asymptotes are at 60°, 180°, and 300°. The **centroid** σ_a is where all asymptotes intersect the real axis: σ_a = (Σ real parts of poles − Σ real parts of zeros) / (n − m). This single point anchors all the asymptotes and tells you immediately whether the branches escaping to infinity are heading into the left half-plane (stable) or right half-plane (unstable). A centroid deep in the left half-plane is reassuring; a centroid near the imaginary axis warns that high-gain instability is possible.

**Breakaway and break-in points** occur where two or more branches of the locus coincide — that is, where the characteristic equation has repeated roots. On the real axis, branches that are traveling along the real axis in opposite directions will meet at some point and break away from the real axis into complex conjugate pairs (a **breakaway point**). Conversely, complex conjugate branches can meet on the real axis and re-enter it (a **break-in point**). These points occur where dK/ds = 0, since K is an implicit function of s along the locus. Differentiating the characteristic equation 1 + KG(s)H(s) = 0 gives a polynomial whose real roots are the candidate breakaway and break-in points.

Together, these three features — asymptote angles, centroid, and breakaway points — let you sketch the qualitative shape of the entire root locus with only arithmetic. You can immediately identify how many branches go unstable at high gain, roughly where they cross the imaginary axis, and whether the closed-loop poles pass through any real breakaway geometry. The sketch won't give you exact crossover frequencies (use the Routh criterion or Bode plot for that), but it gives you the topological picture of how pole locations evolve with gain — which is exactly the information needed for initial compensator design.
