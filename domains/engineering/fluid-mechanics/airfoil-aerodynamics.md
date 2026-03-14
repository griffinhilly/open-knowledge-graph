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
status: draft
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
