---
id: pipe-roughness-absolute-relative
title: 'Pipe Roughness: Absolute and Relative Effects on Friction'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: friction-factor-determination-methods
  type: hard
- id: moody-diagram-friction-factor
  type: soft
builds-toward:
- pipe-network-solutions-hardy-cross
tags:
- roughness
- friction-factor
- surface-texture
stage: advanced
status: draft
---

# Pipe Roughness: Absolute and Relative Effects on Friction

## Core Idea
Absolute roughness (ε, actual surface irregularity height) becomes significant only at high Reynolds numbers where the viscous sublayer shrinks below roughness projections. Relative roughness (ε/D) determines the friction factor in turbulent flow; smooth pipes and very rough pipes have asymptotic limits on the Moody chart. Pipe age and material cause roughness to increase, increasing friction factor and reducing system capacity over time.

## Questions

```yaml
- question: "Two pipes carry the same fluid at the same fully turbulent flow rate. Pipe A has diameter 50 mm and Pipe B has diameter 500 mm. Both are made of the same material with identical absolute roughness ε = 0.5 mm. Which pipe has the higher friction factor?"
  type: multiple-choice
  options:
    - "Pipe B (500 mm), since larger pipes have more total surface area in contact with the fluid"
    - "They have identical friction factors, since absolute roughness ε is the same for both"
    - "Pipe A (50 mm), since it has higher relative roughness (ε/D = 0.01 vs. 0.001)"
    - "Pipe A (50 mm), since smaller pipes inherently have higher flow resistance at any roughness"
  answer: 2
  explanation: "The friction factor in turbulent flow depends on relative roughness ε/D, not absolute roughness ε alone. Pipe A has ε/D = 0.5/50 = 0.01, while Pipe B has ε/D = 0.5/500 = 0.001 — a tenfold difference. On the Moody chart, Pipe A traces a much higher friction factor curve. Option B is the classic misconception: same material does not mean same friction factor unless the diameters match, because the roughness bumps loom much larger relative to the flow channel in the smaller pipe."

- question: "A pump engineer is designing a system for very low flow velocity (well within the laminar or smooth-turbulent regime). The pipe is made of a rough material. Which statement best describes the effect of pipe roughness in this regime?"
  type: multiple-choice
  options:
    - "High roughness always increases the friction factor, regardless of the flow regime"
    - "In the hydraulically smooth regime, roughness projections are submerged within the viscous sublayer and have little effect on friction"
    - "Relative roughness is irrelevant at low Reynolds numbers; only absolute roughness matters"
    - "The pipe behaves as fully rough once any roughness is present, so friction is independent of Re"
  answer: 1
  explanation: "The viscous sublayer — the thin laminar layer adjacent to the wall — thickens as Reynolds number decreases. When the sublayer is thicker than the roughness height ε, the bumps are fully submerged and do not disrupt turbulent flow. The pipe is hydraulically smooth, and friction depends only on Re (not ε). This is the left portion of the Moody chart. Roughness only matters once the sublayer shrinks below ε, which happens at higher Re. Option A confuses the fully rough regime behavior with all regimes."

- question: "In the fully rough turbulent regime of pipe flow, increasing the flow velocity (and thus Reynolds number) does not change the friction factor."
  type: true-false
  answer: true
  explanation: "This is a key result from the Moody chart. When Re is large enough that the viscous sublayer is negligibly thin compared to ε, the roughness elements protrude fully into the turbulent core and generate eddies whose magnitude is independent of viscosity. Friction losses are then proportional to velocity squared, meaning the friction factor — defined as the ratio of head loss to velocity head — becomes constant. On the Moody chart, the fully rough curves are horizontal at large Re. The friction factor depends only on ε/D in this regime."

- question: "A pipe with a larger absolute roughness value (ε) will always have a higher friction factor than a pipe with a smaller ε, regardless of pipe diameter."
  type: true-false
  answer: false
  explanation: "Friction factor in turbulent flow is governed by relative roughness ε/D, not absolute roughness ε. A large-diameter pipe with high absolute roughness can have a lower friction factor than a small-diameter pipe with low absolute roughness if its relative roughness is smaller. For example, a 1000-mm pipe with ε = 1 mm (ε/D = 0.001) will have a lower friction factor than a 20-mm pipe with ε = 0.1 mm (ε/D = 0.005). The physical reason is that what matters is how large the bumps are relative to the flow channel, not their absolute size."

- question: "Explain why engineers use relative roughness (ε/D) rather than absolute roughness (ε) alone when predicting friction losses in turbulent pipe flow."
  type: short-answer
  answer: "The friction losses in turbulent pipe flow depend on how large the roughness elements are relative to the flow channel diameter, not on their absolute size. A roughness height of 0.1 mm creates much more disruption in a 10-mm pipe (ε/D = 0.01) than in a 100-mm pipe (ε/D = 0.001), because in the small pipe the bumps occupy a much larger fraction of the cross-section and cause more severe disturbance to the velocity profile. Relative roughness captures this scaling; absolute roughness alone does not."
  explanation: "The physical mechanism reinforces this: in the fully rough regime, the friction factor depends only on the ratio of roughness height to pipe diameter because the eddies generated by roughness elements scale with ε, while the mean flow scales with D. When ε/D is small, roughness effects are minor; when ε/D is large, they dominate. This is why the Moody chart plots friction factor against both Re and ε/D — both parameters matter, and ε alone tells you nothing without knowing D."
```

## Explainer

You already know from the Moody diagram that the friction factor f depends on two parameters: Reynolds number Re and relative roughness ε/D. But why does relative roughness — rather than absolute roughness ε alone — determine friction losses? The answer lies in how turbulent flow actually interacts with a rough surface, and understanding it gives you physical intuition for what the Moody chart is showing.

Even in turbulent flow, there is a thin layer of fluid immediately adjacent to the pipe wall — the **viscous sublayer** — where viscosity dominates and flow is essentially laminar. This sublayer has a thickness that scales inversely with Reynolds number: the faster and more turbulent the flow, the thinner the sublayer. **Absolute roughness** ε describes the physical height of the surface irregularities (sand grains, machining marks, corrosion bumps). The critical comparison is between ε and the sublayer thickness. When the sublayer is thicker than ε, the roughness is buried beneath it; the pipe behaves as hydraulically smooth, and friction depends only on Re (the smooth-pipe region of the Moody chart). When Re is high enough that the sublayer shrinks below ε, roughness elements protrude into the turbulent core, generate additional eddies, and dramatically increase friction losses.

**Relative roughness** ε/D enters because what matters for a fluid parcel traveling through a pipe is not the absolute size of the bumps but how large they are relative to the flow channel. A roughness height of 0.1 mm in a 10-mm pipe (ε/D = 0.01) creates ten times more disruption per diameter of travel than the same roughness in a 100-mm pipe (ε/D = 0.001). At very high Reynolds numbers — the fully rough regime — the viscous sublayer effectively disappears and friction losses become independent of Re entirely, depending only on ε/D. On the Moody chart this appears as horizontal lines at large Re: once fully rough, increasing flow speed no longer changes the friction factor because viscosity has stopped being relevant.

The engineering implication is significant for long-lived piping systems. A new commercial steel pipe has ε ≈ 0.046 mm; after years of service, corrosion and biological fouling can increase ε by an order of magnitude. For a 200-mm pipe (ε/D going from 0.00023 to 0.002), this shifts the friction factor from roughly 0.015 to 0.024 in fully turbulent flow — a 60% increase. Pipeline operators use this to project how pump station requirements will grow over the service life of a pipeline, and to plan cleaning or relining schedules. When you encounter a field pipe with an unexpectedly high head loss, ε/D degradation from aging is often the first thing to check.
