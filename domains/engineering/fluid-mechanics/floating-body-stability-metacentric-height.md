---
id: floating-body-stability-metacentric-height
title: Floating Body Stability and Metacentric Height
domain: engineering
course: fluid-mechanics
prerequisites:
- id: buoyancy-and-archimedes
  type: hard
- id: hydrostatic-force-vertical-surfaces
  type: soft
- id: floating-body-stability-equilibrium
  type: soft
builds-toward:
- open-channel-flow
tags:
- buoyancy
- stability
- naval-architecture
stage: formal-systems
status: validated
---
# Floating Body Stability and Metacentric Height

## Core Idea
A floating body is stable if the metacenter (intersection of buoyant force line with centerline) lies above the center of gravity. Metacentric height quantifies stability; larger values provide greater resistance to tipping. Ships, barges, and other floating structures must be designed to maintain positive metacentric height across all operating conditions to prevent capsizing.

## Questions

```yaml
- question: "A container ship loads cargo into stacks high above the deck. How does this affect the vessel's stability, and why?"
  type: multiple-choice
  options:
    - "Stability improves because the added mass increases the displaced volume and raises the center of buoyancy"
    - "Stability decreases because high cargo raises the center of gravity G toward or above the metacenter M, reducing metacentric height GM"
    - "Stability is unchanged because metacentric height depends only on the hull geometry, not the cargo position"
    - "Stability improves because the weight of high cargo increases the waterline draft, lowering the center of buoyancy and increasing GM"
  answer: 1
  explanation: "Metacentric height GM = height of metacenter M minus height of center of gravity G. The metacenter M is determined primarily by the hull geometry and waterplane area — it changes relatively little with loading. But G rises when cargo is loaded high above the waterline. As G approaches M, GM decreases. If G rises above M, GM becomes negative and the vessel is unstable — any heel will be amplified rather than corrected. This is why cargo ships have strict loading plans specifying maximum heights and require ballast calculations."

- question: "A vessel heels 8° to starboard. For the ship to self-right (generate a righting moment), where must the metacenter M lie relative to the center of gravity G?"
  type: multiple-choice
  options:
    - "M must lie above the center of buoyancy B, which always ensures stability"
    - "M must lie above G so that the offset buoyant force acts to windward of G, creating a restoring torque"
    - "M must lie at the same height as G so that gravity and buoyancy are balanced"
    - "M must lie below G to create a downward pull that rights the vessel"
  answer: 1
  explanation: "When the vessel heels, the center of buoyancy B shifts toward the submerged side. The buoyant force acts vertically upward through the displaced B. The righting moment is the couple formed by this upward buoyant force and the downward weight through G. If M (where the new buoyant force line intersects the original centerline) is above G, the buoyant force has a moment arm that generates a restoring torque. If M is below G, the geometry reverses and the torque amplifies the heel — the vessel capsizes. The condition GM > 0 (M above G) is the stability criterion."

- question: "A ship with a very large metacentric height (GM much greater than zero) is always preferable to one with a moderate GM because maximum stability minimizes capsizing risk."
  type: true-false
  answer: false
  explanation: "Excessive GM causes rapid, violent rolling — the righting moment is so strong that the ship snaps back too quickly after each wave, producing short-period rolling that causes discomfort, can injure crew, damage cargo, and stress structural joints. Well-designed vessels target an appropriate GM range: enough for safety under all loading conditions but not so large as to create operationally problematic stiffness. Naval architects balance stability and seakeeping comfort by specifying a target GM range, not simply maximizing it."

- question: "When a floating body heels by a small angle, the center of buoyancy shifts laterally toward the submerged (lower) side because more of the hull volume is submerged on that side."
  type: true-false
  answer: true
  explanation: "This shift of B is the fundamental mechanism of floating body stability. At rest, B is at the centroid of the displaced volume. When the vessel heels, the wedge of hull volume on the descending side enters the water while a corresponding wedge on the rising side emerges. The net effect shifts the centroid of the entire submerged volume toward the newly submerged side. The buoyant force — always vertical — now acts through this displaced B location, creating the righting or overturning moment depending on whether M lies above or below G."

- question: "Why is metacentric height not a fixed property of a vessel, and what are the consequences for ship design and operation?"
  type: short-answer
  answer: "Metacentric height GM depends on both the position of the metacenter M and the center of gravity G, and both change with loading. M depends on the vessel's waterplane area and submerged volume geometry, which change as the ship sinks deeper with load. G changes dramatically depending on how much cargo is loaded and where it is placed — high cargo raises G; ballast water in keel tanks lowers G. A ship with moderate GM when fully loaded in a standard configuration may have dangerously low GM if top-heavy cargo replaces ballast, or uncomfortably high GM when sailing empty. Designers must calculate GM for all planned loading conditions — from empty to fully loaded, with and without ballast — ensuring positive GM throughout. Operators must follow loading plans and ballast procedures to maintain GM in the design range; taking on water in upper compartments during flooding can shift G above M within minutes, causing capsizing."
  explanation: "This is why maritime disasters sometimes occur even to seemingly seaworthy vessels: a loading or damage condition that was not analyzed can bring G above M even on a well-designed ship."
```

## Explainer

From Archimedes' principle, you know that a floating body displaces fluid equal in weight to its own weight. The buoyant force acts upward through the **center of buoyancy** (B) — the centroid of the displaced fluid volume. The body's weight acts downward through the **center of gravity** (G). At rest on calm water, B lies directly below G (or they coincide for a symmetric body at rest), and the system is in static equilibrium. So far, this is just Archimedes. The interesting question is what happens when something disturbs the vessel — a wave, a shifting load, a gust of wind — causing it to tilt.

When a ship heels by a small angle θ, the geometry of the submerged volume changes: more volume enters the water on the leaning side, less on the other. The **center of buoyancy** shifts laterally toward the submerged side, because the submerged volume's centroid moves in that direction. The buoyant force still acts vertically, but now through this displaced B location. If you trace that vertical line of action upward, it intersects the vessel's original vertical centerline at a point called the **metacenter** (M). The crucial fact: for small heeling angles, M is fixed regardless of the heel angle, because the shift of B is approximately proportional to θ.

Stability is determined entirely by the relative positions of M and G. If M lies above G (positive **metacentric height** GM = height of M minus height of G), then when the vessel tilts, the offset buoyant force creates a **righting moment** pulling the ship back upright — analogous to a pendulum returning to center. The restoring torque is approximately W · GM · sin(θ) ≈ W · GM · θ for small angles. Larger GM means a stronger righting moment: a stiffer, more stable vessel. If M falls below G, the buoyant force creates an **overturning moment** that amplifies the tilt — the vessel is inherently unstable and will capsize.

Metacentric height is not a fixed property — it changes with loading. A container ship with cargo stacked high on deck raises G and reduces GM. A ship taking on water in its upper decks can go from positive to negative GM in minutes. This is why vessels carry **ballast** water in tanks near the keel: lowering G to maintain adequate GM under all loading conditions. Naval architects calculate GM curves across all planned loading configurations — not just the designed operating condition. Too little GM risks capsizing; too much GM causes rapid, violent rolling (a stiff ship is uncomfortable and can stress cargo and structure). Designing for an appropriate GM range under all conditions, from empty to fully loaded, is the central stability calculation in naval architecture.

## How It's Best Learned
Sketch the tilted ship showing B shift and the metacentric triangle (BM, BG, GM). Compute metacentric height from first principles for a simple rectangular barge, then check how GM changes when you add top weight versus ballast.
