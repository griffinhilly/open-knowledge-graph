---
id: root-locus-gain-design
title: Root Locus Gain Design
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-construction-rules
  type: hard
- id: time-domain-response-second-order
  type: soft
tags:
- root-locus
- gain-selection
- damping-ratio
- natural-frequency
- dominant-poles
- performance-specs
stage: expert
status: validated
---

# Root Locus Gain Design

## Core Idea
Root locus gain design selects the controller gain K so that the closed-loop poles lie at desired locations in the s-plane, meeting time-domain performance specifications such as percent overshoot, settling time, and rise time. The design procedure maps performance specs into s-plane regions: a damping ratio ζ requirement defines lines of constant angle θ = cos⁻¹(ζ) from the negative real axis, a natural frequency ωn requirement defines a circle of radius ωn centered at the origin, and a settling time requirement defines a vertical boundary at σ = −4/t_s (for 2% criterion). The designer identifies where the root locus crosses the desired damping line or enters the acceptable region, then computes the corresponding K using the magnitude condition |G(s)H(s)| = 1/K at that point. When the locus does not pass through the desired region, a compensator (adding poles or zeros) must reshape the locus before gain selection — pure gain adjustment alone cannot place poles arbitrarily. The dominant pole approximation assumes that the closed-loop response is primarily governed by the poles nearest the imaginary axis, provided other poles are at least five times farther to the left.

## How It's Best Learned
Given a plant transfer function with specified overshoot and settling time requirements, convert the specs to a target region in the s-plane, sketch the root locus, and graphically determine the gain K at the intersection point. Verify by computing the closed-loop step response and checking whether higher-order poles violate the dominant-pole assumption. Repeat for systems where the locus does not intersect the desired region to motivate compensator design.

## Common Misconceptions
- Meeting the damping ratio specification by placing dominant poles on the correct ζ line does not guarantee the predicted overshoot if there are nearby zeros or non-dominant poles that are not sufficiently far to the left — the dominant-pole approximation has limits.
- The gain K found from the root locus is the open-loop gain parameter, not the closed-loop DC gain — the steady-state value of the step response depends on the closed-loop transfer function and may require separate steady-state error analysis.
- Increasing K to speed up the response (higher ωn) eventually drives branches into the right half-plane for most systems, so there is a fundamental tradeoff between speed and stability that gain alone cannot resolve.

## Questions

```yaml
- question: "A root locus for a third-order plant shows two branches crossing the desired damping ratio line at gains K1=2 and K2=15. At K2=15, the third closed-loop pole is much closer to the imaginary axis than at K1=2. Which gain should the designer prefer, and why?"
  type: multiple-choice
  options:
    - "K2=15, because higher gain always means faster response and better transient performance"
    - "K1=2, because at K2=15 the third pole may be close enough to the imaginary axis to violate the dominant-pole assumption, causing actual overshoot and settling time to differ from predictions"
    - "Either gain, because both achieve the specified damping ratio and therefore produce identical step responses"
    - "K2=15, because the magnitude condition requires choosing the largest valid gain on the locus"
  answer: 1
  explanation: "Both gains satisfy the damping ratio requirement, but the dominant-pole approximation assumes all non-dominant closed-loop poles are at least five times farther left than the dominant pair. At K2=15, the third pole migrates toward the imaginary axis, potentially violating this assumption. When it does, the third pole contributes meaningfully to the step response, producing more overshoot or a slower tail than the second-order prediction. The designer must check the dominant-pole assumption at each candidate gain and prefer the one where it is satisfied — meeting the ζ line is necessary but not sufficient."

- question: "The root locus for a plant does not pass through the desired s-plane target region at any finite gain K. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "Increase K until the locus eventually reaches the target region — high enough gain can always extend the locus there"
    - "Pure gain adjustment cannot achieve the specifications; a compensator must be added to reshape the locus before gain selection"
    - "The specifications are physically impossible to achieve with any controller"
    - "Recheck the locus sketch — the root locus always passes through every point in the left half-plane at some gain"
  answer: 1
  explanation: "The root locus shows exactly which s-plane locations closed-loop poles can occupy as K varies from 0 to infinity, determined entirely by the open-loop poles and zeros. If the desired region is not on the locus, no value of K places a pole there — not a larger K, not an optimized K. The solution is compensator design: adding poles or zeros to the open-loop transfer function changes the shape of the locus entirely, potentially routing it through the desired region. Only then does gain selection become meaningful. Option A is wrong because increasing K moves poles along the existing locus, which already misses the target."

- question: "If the root locus passes through the desired damping ratio line at a given gain K, the resulting closed-loop system is expected to meet the specified percent overshoot."
  type: true-false
  answer: false
  explanation: "This is the central misconception about root locus gain design. Meeting the ζ specification by placing dominant poles on the correct line is necessary but not sufficient. The dominant-pole approximation assumes all other closed-loop poles are at least five times farther left. If nearby poles or zeros are present, they contribute to the response, producing more overshoot or a longer tail than the second-order prediction. The designer must always verify the dominant-pole assumption after computing K. Nearby zeros can also increase overshoot even when poles are correctly placed."

- question: "The gain K computed from the root locus magnitude condition equals the product of distances from the desired pole location to all open-loop poles, divided by the product of distances to all open-loop zeros."
  type: true-false
  answer: true
  explanation: "This is the geometric interpretation of the magnitude condition. At any point s* on the root locus, the condition |G(s*)H(s*)| = 1/K must hold. Expanding the open-loop transfer function as a product of first-order factors, the magnitude becomes the product of |s* - p_i| over the product of |s* - z_j|, which equals 1/K. Rearranging: K equals the product of distances to poles divided by the product of distances to zeros. This lets designers read off K graphically from a root locus plot using measured distances."

- question: "Why can't a designer achieve an arbitrary closed-loop pole location by choosing a large enough gain K? What fundamental constraint does the root locus impose?"
  type: short-answer
  answer: "The root locus traces the exact set of s-plane locations that closed-loop poles can occupy as K varies from 0 to infinity. These paths are determined entirely by the open-loop poles and zeros and are fixed regardless of how K is chosen. Gain K selects a point along these fixed paths — it cannot move poles off the locus or create new paths. Desired pole locations that do not lie on the locus are simply unreachable through gain adjustment alone, regardless of how large K becomes. Adding a compensator (poles or zeros) restructures the locus itself, potentially routing it through the desired region, at which point gain selection can work."
  explanation: "Recognizing that 'the locus does not pass through the desired region' is not a failure — it is critical diagnostic information indicating that the plant must be augmented before gain selection can achieve the specifications. This is the fundamental motivation for lead, lag, and lead-lag compensator design."
```

## Explainer

From your prerequisite work on root locus construction rules, you can draw the paths that closed-loop poles trace in the s-plane as the gain K varies from 0 to ∞. At K = 0, the closed-loop poles sit at the open-loop poles; as K → ∞, they migrate toward the open-loop zeros (or to infinity along asymptotes). The root locus tells you *where* the poles can go. Root locus gain design answers the follow-up question: where *should* they go, and what value of K puts them there?

The design procedure starts by translating **time-domain performance specifications** into geometric regions in the s-plane. A specified **percent overshoot** maps to a minimum **damping ratio** ζ via OS% = 100·e^(−πζ/√(1−ζ²)), which in turn defines a pair of lines radiating from the origin at angle θ = cos⁻¹(ζ) from the negative real axis. Poles on the left side of these lines are damped enough; poles to the right are not. A specified **settling time** t_s ≈ 4/σ (2% criterion) defines a vertical boundary: poles must be at least this far to the left of the imaginary axis. A specified **natural frequency** ωn defines a circle of radius ωn — poles inside meet the speed requirement. The intersection of all these regions is the **target zone** where the desired closed-loop poles should land.

Once you identify the target zone, you look at where the root locus passes through it. If the locus intersects the target zone, you apply the **magnitude condition** to find K: at the desired pole location s* on the locus, the condition |G(s*)H(s*)| = 1/K must hold. Rearranging: K = 1/|G(s*)H(s*)|. Geometrically, K equals the product of distances from s* to all open-loop poles divided by the product of distances to all open-loop zeros. This is the gain you program into the controller.

If the root locus does not pass through the target zone at any finite gain — a common situation — then gain alone cannot achieve the specifications. This is the fundamental limitation that motivates **compensator design**: adding poles or zeros to the open-loop transfer function reshapes the locus so it does pass through the desired region. The **dominant pole approximation** simplifies verification: if the closed-loop poles you placed are the leftmost ones and all others are at least five times farther left, the response is well-approximated by just those two poles, and the predicted overshoot and settling time are accurate. Checking this assumption is always the last step — a design that looks correct on the root locus can still produce incorrect behavior if non-dominant poles are not far enough away.
