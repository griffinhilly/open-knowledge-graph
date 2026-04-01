---
id: geostrophic-wind-and-balance
title: Geostrophic Wind and Pressure-Coriolis Balance
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: pressure-systems-and-winds
  type: hard
- id: coriolis-effect
  type: hard
- id: newtons-second-law
  type: soft
builds-toward:
  - thermal-wind-balance
  - upper-level-divergence-and-pressure
tags:
- wind
- pressure
- balance
- geostrophic
- dynamics
stage: formal-systems
status: validated
---
# Geostrophic Wind and Pressure-Coriolis Balance

## Core Idea
In the free atmosphere away from surface friction, wind direction is determined by balance between the pressure gradient force (pushing toward low pressure) and the Coriolis force (deflecting moving air). This geostrophic balance results in wind flowing parallel to pressure contours, with speed proportional to the pressure gradient. The geostrophic approximation is excellent for mid-latitude weather systems and explains why high-pressure systems have clockwise flow in the Northern Hemisphere.

## Questions

```yaml
- question: "In the Northern Hemisphere, air around a low-pressure system initially accelerates toward the center (down the pressure gradient). What causes the resulting wind to flow counterclockwise around the low instead of into it?"
  type: multiple-choice
  options: ["Surface friction deflects the air to the left", "The Coriolis force deflects moving air to the right until it is flowing parallel to the isobars", "The low-pressure center repels air like a magnetic pole", "Air rises so quickly that horizontal inflow stops"]
  answer: 1
  explanation: "As air accelerates toward low pressure, the Coriolis force deflects it to the right (in the Northern Hemisphere). The deflection continues until the Coriolis force exactly balances the pressure gradient force — at that point the air is moving parallel to the isobars, not toward the low. This steady state is geostrophic balance, producing the counterclockwise circulation observed around Northern Hemisphere lows."

- question: "Geostrophic wind speed increases as isobars are spaced farther apart on a weather map."
  type: true-false
  answer: false
  explanation: "Geostrophic wind speed is proportional to the pressure gradient — the rate of pressure change with distance. Isobars spaced farther apart indicate a weaker pressure gradient (pressure changes slowly with distance), which produces lighter winds. Tightly packed isobars indicate a strong gradient and faster geostrophic winds. This is why closely spaced contours on a weather map signal strong winds."

- question: "Why is the geostrophic approximation more accurate at mid-latitudes than near the equator?"
  type: short-answer
  answer: "The Coriolis force is proportional to the sine of latitude, so it approaches zero at the equator. Near the equator, the Coriolis force is too weak to balance the pressure gradient force, so air flows toward low pressure rather than parallel to isobars. Geostrophic balance requires a significant Coriolis force, which only exists at mid-to-high latitudes."
  explanation: "The Coriolis parameter f = 2Ω sin(φ), where φ is latitude. At the equator sin(0°) = 0, so f ≈ 0 and the Coriolis force vanishes. Tropical meteorology therefore requires different dynamical frameworks. The geostrophic approximation is most accurate at mid-latitudes (30°–60°) where f is large enough to dominate the force balance in synoptic-scale systems."
```

## Explainer

When you learned about the pressure gradient force, you saw that air accelerates from high to low pressure — the steeper the gradient, the stronger the push. If that were the whole story, wind would always blow straight into low-pressure centers and out of high-pressure ones. But upper-level winds observed on weather maps do something quite different: they flow *around* pressure systems, not into them. The missing piece is the Coriolis force.

As an air parcel begins moving down the pressure gradient, the Coriolis force deflects it — to the right in the Northern Hemisphere, to the left in the Southern. The deflection doesn't stop the parcel; it continuously turns it. As the parcel curves, the angle between its velocity and the pressure gradient changes, altering the balance of forces. Eventually the parcel reaches a direction where the Coriolis force (pointing 90° to the right of motion) exactly opposes the pressure gradient force (pointing toward low pressure). At this point, the two forces are equal and opposite, the net force is zero, and the parcel moves in a straight line — parallel to the isobars. This steady state is called **geostrophic balance**, and the resulting wind is the **geostrophic wind**.

The geostrophic wind speed follows directly from the force balance. Setting the pressure gradient force equal to the Coriolis force: (1/ρ)(ΔP/Δn) = f·V_g, where ρ is air density, ΔP/Δn is the pressure gradient perpendicular to the flow, f is the Coriolis parameter (2Ω sin φ), and V_g is the geostrophic wind speed. Solving for V_g shows that stronger pressure gradients produce faster winds, and that the same gradient produces stronger winds at lower latitudes (where f is smaller). On a synoptic weather map, tightly packed isobars mean strong winds; widely spaced isobars mean gentle winds.

The direction rule follows from the deflection direction. In the Northern Hemisphere, winds are deflected to the right, so geostrophic flow runs with low pressure to the left and high pressure to the right — counterclockwise around lows, clockwise around highs (Buys Ballot's Law). The Southern Hemisphere is the mirror image: deflection is to the left, so lows have clockwise circulation and highs are counterclockwise. This is not a coincidence or a convention — it is the direct geometric consequence of the Coriolis force opposing the pressure gradient in balance.

The geostrophic approximation is powerful but limited. It works well above the boundary layer (roughly above 1 km), away from the equator, and for large, slowly evolving weather systems. Near the surface, friction slows the wind below geostrophic speed and rotates the flow slightly across isobars toward low pressure — which is why surface winds spiral inward into lows rather than flowing purely parallel to isobars. Near the equator, f ≈ 0 and the Coriolis force cannot provide the balancing force at all, so tropical dynamics require different approximations. Understanding geostrophic balance is nonetheless the essential entry point to atmospheric dynamics: it explains the large-scale structure of mid-latitude weather and sets up the thermal wind relationship, which connects vertical wind shear to horizontal temperature gradients.
