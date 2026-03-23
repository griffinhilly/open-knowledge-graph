---
id: airfoil-aerodynamics
title: Airfoil Aerodynamics
domain: engineering
course: fluid-mechanics
prerequisites:
- id: lift-and-circulation-theory
  type: hard
- id: boundary-layer-theory
  type: soft
tags:
- airfoil
- angle of attack
- stall
- lift coefficient
- NACA profiles
- pressure distribution
stage: formal-systems
status: validated
---
# Airfoil Aerodynamics

## Core Idea
An airfoil generates lift through the pressure distribution created by its curved shape and angle of attack (α). Thin airfoil theory predicts C_L = 2π(α − α_L=0) for small angles, where α_L=0 is the zero-lift angle determined by camber. As α increases, the adverse pressure gradient on the upper surface strengthens until the boundary layer separates — this is stall, marked by a sudden loss of lift and increase in drag. NACA airfoil families (e.g., NACA 2412: 2% camber at 40% chord, 12% thickness) provide standardized shapes with tabulated lift, drag, and moment coefficients. The pressure distribution over an airfoil — suction peak near the leading edge on the upper surface, higher pressure on the lower surface — is the fundamental source of both lift and the pitching moment about the aerodynamic center.

## How It's Best Learned
Plot the pressure coefficient C_p distribution over a NACA 0012 airfoil at several angles of attack using panel method software or published data. Observe how the suction peak on the upper surface grows with α and how the area between upper and lower C_p curves corresponds to the lift coefficient. Then examine experimental C_L vs. α curves to identify the linear region, C_L,max, and the stall angle. Compare symmetric (NACA 0012) and cambered (NACA 4412) airfoils to see how camber shifts the zero-lift angle and increases C_L,max.

## Common Misconceptions
- Stall does not mean the airplane falls or the wing stops producing all lift — it means the lift coefficient decreases past C_L,max as flow separation spreads from the trailing edge forward. The wing still produces some lift.
- Thicker airfoils are not inherently worse. Moderate thickness delays leading-edge stall, provides structural depth, and can yield higher C_L,max. Very thin airfoils stall abruptly via leading-edge separation bubbles.
- The aerodynamic center (where the pitching moment coefficient is constant with α) is not the same as the center of pressure (where the resultant force acts). For thin airfoils, the aerodynamic center is at the quarter-chord regardless of camber.

## Questions

```yaml
- question: "A pilot increases angle of attack past the stall angle. Which of the following best describes what happens to the airfoil's aerodynamic performance?"
  type: multiple-choice
  options:
    - "Lift drops to zero immediately and the aircraft falls at the rate determined by gravity alone"
    - "Lift continues to increase as the angle of attack increases, but drag increases faster"
    - "The lift coefficient drops below its maximum value and drag increases sharply, but the wing still produces some lift"
    - "The pressure on the upper and lower surfaces equalizes, eliminating both lift and drag"
  answer: 2
  explanation: "Stall does not mean zero lift — it means the lift coefficient has passed C_L,max and is now decreasing as angle of attack increases further. The boundary layer separates from the upper surface (beginning at the trailing edge), disrupting the low-pressure suction distribution that generates most of the lift. Separation spreads forward with increasing alpha, progressively destroying lift and dramatically increasing form drag. The wing still produces some lift throughout — recovery from stall by reducing alpha is possible precisely because the flow reattaches when the adverse pressure gradient is relaxed. Option A is the most common misconception."

- question: "A NACA 2412 airfoil and a NACA 0012 airfoil are both at an angle of attack of 4°. Which generates more lift, and why?"
  type: multiple-choice
  options:
    - "NACA 0012, because its symmetric shape distributes pressure more evenly and efficiently"
    - "NACA 2412, because its 2% camber shifts the zero-lift angle to a negative value, increasing C_L at every angle of attack"
    - "They generate the same lift because both have the same thickness (12%) and are at the same angle of attack"
    - "NACA 2412, because its higher thickness provides a larger surface area for pressure to act on"
  answer: 1
  explanation: "Camber shifts the zero-lift angle α_L=0 to a negative value. Thin airfoil theory gives C_L = 2π(α − α_L=0). For a symmetric NACA 0012, α_L=0 = 0°, so C_L = 2π(4°) ≈ 0.44. For the cambered NACA 2412, α_L=0 is approximately −2°, so C_L = 2π(4° − (−2°)) = 2π(6°) ≈ 0.66. The cambered airfoil generates lift even at zero geometric angle of attack; at 4° it generates significantly more. Thickness affects stall characteristics and structural depth, not the lift curve slope or zero-lift angle."

- question: "For a subsonic airfoil, the aerodynamic center (where the pitching moment coefficient is constant regardless of angle of attack) is located at the quarter-chord point."
  type: true-false
  answer: true
  explanation: "True, and this is a fundamental result of thin airfoil theory that holds approximately for most practical subsonic airfoil shapes regardless of camber. The aerodynamic center's fixed location (independent of alpha) makes it the natural reference point for stability analysis — if you know C_m at the aerodynamic center at one angle of attack, you know it at all angles of attack. This is why aircraft wing spars are often placed near the quarter-chord and why tail sizing calculations are referenced to the aerodynamic center. The center of pressure (where the resultant force acts) is a different point that moves as alpha changes."

- question: "An airfoil with greater thickness will always stall at a lower angle of attack than a thinner airfoil of the same camber."
  type: true-false
  answer: false
  explanation: "False — the relationship between thickness and stall angle is not monotonically negative. Very thin airfoils actually tend to stall more abruptly via leading-edge separation bubbles, often at relatively low angles of attack, with little warning. Moderate thickness delays this leading-edge stall mechanism and often yields a higher C_L,max and a more gradual trailing-edge stall that pilots can detect (through buffeting) before full separation. Very thick airfoils eventually have worse characteristics from increased form drag, but 'thicker = lower stall angle' is a misconception — the Common Misconceptions section explicitly notes this."

- question: "Why does increasing angle of attack increase lift up to a maximum, but further increases cause lift to decrease? Explain the role of the boundary layer."
  type: short-answer
  answer: "Increasing angle of attack sharpens the suction peak near the leading edge on the upper surface, strengthening the low-pressure region and thus increasing lift. However, this also steepens the adverse pressure gradient — the flow must decelerate from the suction peak back to the trailing edge against an increasingly unfavorable pressure rise. The boundary layer on the upper surface, which has been losing momentum due to viscosity, eventually cannot overcome this adverse gradient and separates from the surface, beginning at the trailing edge. Separated flow cannot maintain the organized low-pressure distribution that generates lift, so C_L stops increasing and then decreases. When separation spreads to the leading edge region, the wing stalls: C_L drops sharply, drag rises, and the pitching moment changes abruptly."
  explanation: "The boundary layer is the link between inviscid lift theory (which predicts C_L rising indefinitely with alpha) and the real-world stall. Without viscosity and its associated boundary layer, an airfoil would not stall. The boundary layer accumulates adverse effects along the upper surface until it can no longer follow the surface contour — a fundamentally viscous phenomenon that inviscid potential flow theory cannot capture."
```

## Explainer

From your study of lift and circulation theory, you know that lift is generated by circulation Γ around the airfoil, with the Kutta-Joukowski theorem giving L = ρV∞Γ per unit span. What circulation theory does not tell you on its own is *how* a particular airfoil shape creates a particular circulation — that requires understanding the pressure distribution. The airfoil's curved upper surface accelerates flow, lowering pressure (Bernoulli), while the flatter lower surface maintains higher pressure. This pressure difference is not uniform: the suction peak concentrates near the **leading edge** on the upper surface, contributing the majority of the total lift. The net upward pressure force integrated over the chord is what thin airfoil theory predicts as C_L = 2π(α − α_L=0), where the zero-lift angle α_L=0 is set by camber — a cambered airfoil generates lift even at zero geometric angle of attack.

As **angle of attack** α increases, the suction peak grows sharper and shifts further forward on the upper surface. This creates an increasingly steep **adverse pressure gradient** — the flow must decelerate from the suction peak back toward the trailing edge. Here your boundary layer prerequisite becomes essential: the boundary layer, already thickened by viscosity along the upper surface, now must push against a rising pressure. When the adverse gradient becomes too steep, the boundary layer cannot follow the surface and **separates**, beginning at the trailing edge and spreading forward as α increases. This separation destroys the organized pressure distribution that generated lift. When separation reaches the leading edge region, the wing **stalls** — C_L drops sharply and drag rises. Stall does not mean zero lift; it means the lift-producing mechanism has partially broken down.

**NACA airfoil families** encode geometry systematically. The NACA four-digit designation — say, 2412 — specifies 2% maximum camber located at 40% chord, with 12% maximum thickness. Camber shifts α_L=0 to negative values, increasing C_L at every angle of attack relative to a symmetric airfoil. Thickness affects stall behavior: thicker airfoils produce a more gradual trailing-edge stall, giving pilots warning before full separation, while very thin airfoils stall abruptly via **leading-edge separation bubbles** with little warning. The design tradeoff is between thin airfoils' low drag at cruise and thicker airfoils' more forgiving stall behavior.

The **pitching moment** about an airfoil also deserves careful attention. The pressure distribution creates not only a net lift force but a torque tending to pitch the nose. The **aerodynamic center** is the special point about which this pitching moment coefficient C_m remains constant regardless of α — for thin airfoils and most subsonic profiles, this falls at the quarter-chord. The **center of pressure** is a different concept: it is the point where the resultant force acts, so there is no moment about it. As α changes, the center of pressure shifts, while the aerodynamic center remains fixed. Aircraft stability analysis uses the aerodynamic center because its fixed location simplifies the pitching moment equations; the quarter-chord location is why wing spars are often placed there.
