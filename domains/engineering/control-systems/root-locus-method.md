---
id: root-locus-method
title: Root Locus Method
domain: engineering
course: control-systems
prerequisites:
- id: routh-hurwitz-criterion
  type: hard
- id: complex-numbers-intro
  type: hard
- id: transfer-functions-control
  type: hard
- id: complex-plane
  type: hard
builds-toward:
- root-locus-controller-design
- state-feedback-pole-placement
tags:
- root-locus
- pole-migration
- asymptotes
- breakaway-points
- angle-condition
stage: advanced
status: validated
---

# Root Locus Method

## Core Idea
The root locus is a graphical method showing how closed-loop poles migrate in the complex s-plane as the gain parameter K varies from 0 to ∞. Starting at the open-loop poles (K=0) and terminating at the open-loop zeros or infinity (K→∞), the locus is symmetric about the real axis and satisfies the angle condition ∠G(s)H(s) = ±180°(2k+1). Key construction rules include: number of branches equals number of open-loop poles; asymptote angles are 180°(2k+1)/(n−m); the centroid of asymptotes is (Σpoles − Σzeros)/(n−m); real-axis locus exists to the left of an odd count of open-loop poles and zeros. The root locus provides immediate visual insight into how gain affects stability and dominant transient behavior.

## How It's Best Learned
Sketch loci by hand using the construction rules before verifying with MATLAB's rlocus() or Python's control.root_locus(). Focus on understanding why the angle condition governs locus membership rather than memorizing rules in isolation.

## Common Misconceptions
- The locus exists on the real axis to the left of an odd number of open-loop poles and zeros combined, not just between adjacent poles.
- Breakaway points are found from dK/ds = 0 (or equivalently d/ds[1/G(s)H(s)] = 0), not from the angle condition alone.
- The root locus only shows the effect of scalar gain K; adding poles or zeros to the compensator reshapes the entire locus, which is the basis of compensator design.

## Questions

```yaml
- question: "A closed-loop system has open-loop poles at s = 0, s = –2, and s = –5, and no finite zeros. As the gain K increases from 0 to ∞, where do the three root locus branches start and terminate?"
  type: multiple-choice
  options:
    - "Start at the closed-loop poles and terminate at open-loop poles as K→∞"
    - "Start at the open-loop zeros and terminate at the open-loop poles as K→∞"
    - "Start at the open-loop poles (s = 0, –2, –5) at K=0 and travel to infinity along asymptotes as K→∞"
    - "Start at the open-loop poles at K=0 and converge to the centroid of all poles as K→∞"
  answer: 2
  explanation: "Root locus branches always start at the open-loop poles (K=0) and terminate at open-loop zeros or at infinity (K→∞). Since this system has no finite zeros (n=3, m=0), all three branches escape to infinity along asymptotes. The asymptote angles are 180°(2k+1)/(n−m) = 60°, 180°, and 300°. The starting condition (branches begin at open-loop poles) follows from the fact that at K=0, the loop is barely closed and closed-loop poles approach the open-loop poles."

- question: "A system has open-loop poles at s = 0, –1, –3, –4 and open-loop zeros at s = –2. A student claims the root locus exists on the real-axis segment between s = –1 and s = –2, because this segment lies between adjacent poles. Is this correct, and why?"
  type: multiple-choice
  options:
    - "Yes — locus always exists between adjacent poles on the real axis"
    - "No — the locus rule counts all poles AND zeros combined to the right of the test point; the segment –1 to –2 has exactly 2 real singularities to its right (pole at 0 and... depends on count)"
    - "No — the real-axis locus exists to the LEFT of an odd count of all open-loop poles and zeros combined; test each segment by counting poles+zeros to its right"
    - "Yes — any segment between a pole and an adjacent zero is automatically on the locus"
  answer: 2
  explanation: "The real-axis rule: a point on the real axis is on the locus if and only if the total count of open-loop poles PLUS zeros to its RIGHT is odd. For the segment –1 to –2: to the right lie only the pole at s=0, giving a count of 1 (odd) → this segment IS on the locus. The key misconception is thinking the rule only applies to poles, or that it counts from the nearest singularity. You must count ALL poles and zeros to the right of the test point."

- question: "A root locus branch crossing the imaginary axis at a particular gain value means the closed-loop system becomes marginally stable at that gain."
  type: true-false
  answer: true
  explanation: "Stability requires all closed-loop poles to be in the left half of the s-plane (negative real parts). When a locus branch crosses the imaginary axis, the corresponding closed-loop pole(s) have zero real part — the system is marginally stable (sustained oscillations with no decay or growth). Below that gain, those poles are in the left half-plane (stable); above it, they are in the right half-plane (unstable). The crossing gain can be found from Routh-Hurwitz, connecting the two methods."

- question: "Adding a compensator pole or zero to the open-loop system shifts the root locus branches slightly but preserves the overall shape of the original locus."
  type: true-false
  answer: false
  explanation: "Adding a pole or zero to the open-loop transfer function changes the angle condition for every point in the s-plane and fundamentally reshapes the entire locus — it does not merely shift existing branches. A new zero attracts locus branches toward it; a new pole repels them. The entire topology of the locus changes: the number of branches, the asymptote angles and centroid, the real-axis segments, and the breakaway points all change. This is precisely why compensator design (lead/lag) is so powerful — you can pull the locus into entirely new regions of the s-plane."

- question: "Explain why the angle condition ∠G(s) = ±180°(2k+1) is the fundamental test for whether a point s₀ lies on the root locus."
  type: short-answer
  answer: "A closed-loop pole must satisfy 1 + KG(s) = 0, or G(s) = –1/K. For real positive K, this requires G(s) to be a negative real number, which means its phase angle must equal an odd multiple of 180°. So the angle condition ∠G(s₀) = ±180°(2k+1) is simply the requirement that K is positive and real at that point. If a point satisfies the angle condition, you can always find a positive K (namely K = 1/|G(s₀)|) that places a closed-loop pole there."
  explanation: "This is why the construction rules (real-axis rule, asymptotes, breakaway points) are all consequences of the angle condition: they are specialized forms of ∠G(s) = 180° applied to particular geometries. Understanding the angle condition as the definition means you can test any point in the s-plane directly, without memorizing rules. The magnitude condition |G(s₀)| = 1/K then gives you the specific gain value."
```

## Explainer

From the Routh-Hurwitz criterion, you can determine whether a closed-loop system is stable for a given gain. But Routh-Hurwitz gives you a yes/no answer about stability — it doesn't show you *how* the poles are moving or whether increasing gain makes the system faster, slower, or more oscillatory. The **root locus** provides the full picture: it traces every closed-loop pole position simultaneously as gain K varies from zero to infinity.

The starting logic is straightforward. For a unity-feedback loop with forward gain K·G(s), the closed-loop poles satisfy 1 + K·G(s) = 0, or equivalently G(s) = −1/K. As K → 0, the closed-loop poles approach the open-loop poles of G(s) (because small K means weak feedback and the loop barely closes). As K → ∞, the closed-loop poles must approach the open-loop zeros or escape to infinity along asymptotes (because infinite gain would force G(s) = 0 at some finite s, which occurs at zeros). Between these extremes, the poles trace continuous paths in the s-plane — one path per open-loop pole, starting at each pole and ending at each zero or at infinity. The **angle condition** ∠G(s) = ±180° is the membership test: a point s₀ is on the locus if and only if the product of angles from all open-loop zeros to s₀ minus the sum of angles from all poles to s₀ equals an odd multiple of 180°. This geometric condition is the locus's definition.

The construction rules make sketching tractable without solving high-degree polynomials. The real-axis rule — locus exists to the left of an odd count of real poles and zeros — follows directly from the angle condition on the real axis, where all angles are 0° or 180°. The asymptote angles (180°(2k+1)/(n−m) for k = 0, 1, ...) and centroid ((Σpoles − Σzeros)/(n−m)) tell you where locus branches escaping to infinity are headed, which reveals whether high gain drives the system unstable. A locus branch crossing the imaginary axis means a pair of poles is becoming purely imaginary — marginally stable. You can find the crossing gain from Routh-Hurwitz, connecting the two tools you know.

The power of the root locus for design lies in its visual directness. A glance at the locus tells you whether increasing gain stabilizes or destabilizes the system, where the dominant poles (closest to the imaginary axis) sit and therefore what the transient response looks like, and at what gain the system becomes unstable. More importantly, when a simple gain adjustment cannot place the poles where you need them, the locus reveals *why* — and adding a compensator pole or zero reshapes the entire locus, physically pulling branches toward better regions of the s-plane. The **lead compensator** (zero to the left of the dominant poles, pole further left) rotates the locus toward the left half-plane, improving speed and damping. The **lag compensator** improves steady-state error without significantly altering dynamic response. The root locus is not just an analysis tool — it is the geometric language of classical compensator design.
