---
id: coulomb-stress-transfer
title: Coulomb Stress Transfer and Earthquake Triggering
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: focal-mechanisms-and-stress-tensors
  type: hard
- id: earthquakes-and-seismology
  type: hard
tags:
- coulomb-stress
- triggering
- earthquakes
stage: advanced
status: draft
---

# Coulomb Stress Transfer and Earthquake Triggering

## Core Idea
Earthquake ruptures change regional stress, increasing or decreasing Coulomb failure stress on nearby faults. Stress transfer can trigger aftershocks and migrate seismicity; this mechanism explains earthquake clustering and fault-to-fault interactions.

## Questions

```yaml
- question: "After a major strike-slip earthquake, where are aftershocks most likely to concentrate?"
  type: multiple-choice
  options:
    - "Directly on top of the ruptured fault segment, where stress was highest"
    - "In the stress shadow zones adjacent to the rupture, where faults were unclamped"
    - "In the positive ΔCFS lobes off the ends of the rupture and on the far side of the fault"
    - "Randomly distributed within 50 km, because stress transfer is too diffuse to predict"
  answer: 2
  explanation: "For a strike-slip earthquake, positive Coulomb stress change (ΔCFS > 0) concentrates in lobes off the ends of the rupture and on the side of the fault opposite to the slip direction. Aftershocks cluster in these positive ΔCFS zones because nearby faults there have been brought closer to failure. The zones adjacent to the rupture on the near side are stress shadows (ΔCFS < 0) — faults there are pushed further from failure and seismicity is suppressed. The ruptured fault itself has largely released stress (it just slipped), not accumulated it."

- question: "A fault lies 20 km from a major earthquake rupture and has a ΔCFS of +0.05 bar. Seismologists should expect this fault to be at no increased risk of rupture, because 0.05 bar is far below typical fault stress drops of 30–100 bar."
  type: multiple-choice
  options:
    - "Correct — stress changes below 1 bar have no observable effect on fault behavior"
    - "Incorrect — stress changes as small as 0.1 bar have triggered seismicity; 0.05 bar is near this threshold"
    - "Incorrect — stress drops and Coulomb stress changes are the same quantity; 0.05 bar is significant"
    - "Correct — only faults within 5 km of the rupture are affected by stress transfer"
  answer: 1
  explanation: "This is the most counterintuitive result in Coulomb stress transfer research. Triggered seismicity has been reliably correlated with ΔCFS values as small as 0.1 bar — orders of magnitude smaller than the stress drops of typical earthquakes (30–300 bar). This works because faults near failure are already critically stressed and need only a tiny nudge. The 0.05 bar change in the question is close to but below this empirical threshold, so some caution is warranted, but the stress drop comparison (option A's implicit logic) is the wrong benchmark. Even small positive ΔCFS deserves assessment."

- question: "Coulomb stress transfer predicts that seismicity is always suppressed in the region directly surrounding the ruptured fault segment."
  type: true-false
  answer: false
  explanation: "The spatial pattern of ΔCFS for a strike-slip earthquake creates four lobes: two positive (off the ends of the rupture) and two negative or stress shadows (adjacent to the rupture on the near side). The region 'surrounding' the rupture includes both positive and negative lobes depending on direction — off the tips, seismicity is enhanced; alongside the middle of the rupture, it is suppressed. The pattern depends strongly on fault geometry and mechanism (strike-slip, thrust, normal faults all produce different lobe configurations)."

- question: "Postseismic Coulomb stress transfer from viscoelastic relaxation operates on timescales of years to decades, meaning the hazard implications of a large earthquake extend far beyond its immediate aftershock sequence."
  type: true-false
  answer: true
  explanation: "After a large earthquake, the lithosphere doesn't simply 'reset.' The lower crust and upper mantle are viscoelastic — they respond elastically on short timescales but flow over years to decades. As the viscoelastic material relaxes and redistributes stress, it can progressively load distant faults well after the initial aftershock sequence has quieted. The 20th-century sequence of large earthquakes along the North Anatolian Fault in Turkey is a canonical example: each rupture appears to have loaded the next segment, with the sequence taking decades to propagate westward. This is why seismic hazard assessment must incorporate time-dependent stress modeling."

- question: "Explain why the ΔCFS formula (ΔCFS = Δτ + μ′Δσₙ) combines shear stress change and normal stress change, and why the sign of each term matters for fault stability."
  type: short-answer
  answer: "A fault slips when shear stress (Δτ) driving slip exceeds frictional resistance. Normal stress (σₙ) clamping the fault shut contributes to that resistance. A positive Δτ (increased shear in the slip direction) pushes the fault toward failure. A positive Δσₙ means unclamping (reduced normal stress), which reduces friction and also promotes failure. Both promote rupture when positive, so they add in the failure criterion. The effective friction μ′ weights how much the normal stress change matters relative to shear. A fault can be triggered by increased shear alone, by unclamping alone, or by both acting together."
  explanation: "The combined formula captures that earthquake triggering depends on the balance between driving shear and resisting friction. Pure normal stress changes (σₙ) matter because Coulomb friction is μσₙ — reduce the clamping force and you reduce the friction that prevents slip. This is why faults can be triggered by fluid injection (pore pressure reduces effective normal stress, equivalent to unclamping) even without any change in shear stress. The Coulomb criterion unifies all these mechanisms into a single quantity that can be mapped spatially from any source rupture."
```

## Explainer

From your study of focal mechanisms and stress tensors, you know that faults slip when the shear stress resolved on the fault plane exceeds the frictional resistance holding it locked. What Coulomb stress transfer adds is the recognition that when one fault ruptures, it does not simply release stress — it *redistributes* it, changing the stress state on every nearby fault. Some faults are pushed closer to failure; others are pushed farther from it. This is the mechanism behind the observation that earthquakes are not random in space and time but tend to cluster and cascade.

The key quantity is the **Coulomb failure stress change** (ΔCFS). It combines two effects: the change in shear stress resolved in the slip direction on a receiving fault, and the change in normal stress clamping the fault shut. The formula is straightforward: ΔCFS = Δτ + μ′Δσₙ, where Δτ is the shear stress change (positive encourages slip), Δσₙ is the normal stress change (positive means unclamping), and μ′ is the effective friction coefficient. A positive ΔCFS means the receiving fault has been brought closer to failure. Remarkably, stress changes as small as 0.1 bar (about one-tenth of atmospheric pressure) have been shown to correlate with triggered seismicity — faults near failure need only a tiny nudge.

Think of it with a physical analogy. Imagine a bookshelf full of books leaning at various angles. If you suddenly pull one book out (the mainshock), the books on either side shift — some lean more precariously and may topple (triggered earthquakes in positive ΔCFS zones), while others settle into more stable positions (stress shadows where seismicity is suppressed). The pattern is not random: it depends on the geometry of the shelf and the orientation of each book, just as Coulomb stress transfer depends on the geometry of the source rupture and the orientation of each receiving fault.

The spatial pattern of ΔCFS creates characteristic **stress lobes**. For a simple strike-slip earthquake, positive lobes extend off the ends of the rupture and on the opposite side of the fault from the slip direction, while negative lobes (called **stress shadows**) form adjacent to the rupture on the near side. Aftershock locations consistently concentrate in positive ΔCFS lobes and are suppressed in stress shadows. This framework has been applied to explain sequential fault ruptures along plate boundaries — for example, the progressive westward migration of large earthquakes along the North Anatolian Fault in Turkey during the twentieth century, where each rupture loaded the next segment closer to failure.

Coulomb stress transfer also operates on longer timescales. After a major earthquake, viscoelastic relaxation in the lower crust and upper mantle continues to redistribute stress over years to decades, a process called **postseismic stress transfer**. This means that the hazard implications of a large earthquake extend well beyond its immediate aftershock sequence. Understanding these stress interactions is now central to seismic hazard assessment, because it shifts the question from "where are faults?" to "which faults have been brought closer to failure by recent earthquakes?"
