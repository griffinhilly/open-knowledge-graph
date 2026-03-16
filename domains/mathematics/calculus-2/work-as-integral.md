---
id: work-as-integral
title: Work as an Integral
domain: mathematics
course: calculus-2
prerequisites:
- id: fundamental-theorem-of-calculus-part-2
  type: hard
- id: u-substitution
  type: soft
- id: optimization-problems
  type: soft
- id: dot-product
  type: soft
builds-toward: []
tags:
- integration
- applications
- physics
- work
stage: formal-systems
status: validated
---
# Work as an Integral

## Core Idea
When a variable force F(x) acts over a displacement from x = a to x = b, the work done is W = integral from a to b of F(x) dx. This generalizes the constant-force formula W = F*d. Applications include Hooke's law (spring stretching), pumping water out of a tank, and lifting a chain. Each problem requires identifying the force function and the variable of integration.

## How It's Best Learned
Start with Hooke's law (F = kx) as the simplest variable-force example. Then tackle pumping problems by computing the work to lift a thin slice of fluid to the top. Emphasize setting up the integral from the physics, not just plugging into a formula.

## Common Misconceptions
- Using the constant-force formula when force varies.
- Incorrect setup of pumping problems (wrong distance or wrong slice volume).
- Forgetting unit conversions (force in Newtons, distance in meters for SI).

## Explainer

From physics, you know that work equals force times distance — but only when force is constant. When force varies along the path, that formula breaks down. The fix is the same strategy behind every definite integral you've computed: slice the problem into tiny pieces where the quantity you care about is approximately constant, set up the contribution from one slice, and sum over all slices via the Fundamental Theorem of Calculus.

**Hooke's Law** provides the cleanest introduction. A spring resists extension with force F = kx, where x is the displacement from equilibrium and k is the spring constant. Stretching the spring a tiny amount dx from position x requires work dW ≈ F(x)·dx = kx·dx. The total work to stretch from x = a to x = b is W = ∫ₐᵇ kx dx = k·[x²/2]ₐᵇ. For a spring with k = 10 N/m stretched from 0 to 0.5 m: W = ∫₀^{0.5} 10x dx = 10·(0.25/2) = 1.25 J. The varying force is automatically handled by the integral.

**Pumping problems** are the classic application that challenges students most. Imagine a cylindrical tank of radius r and height H, filled with water, and you want to pump all the water to the top. The key move is to consider a thin horizontal slice of water at height y with thickness dy. Its volume is πr²dy, its weight (force due to gravity) is ρg·πr²dy (where ρ ≈ 1000 kg/m³ and g ≈ 9.8 m/s²), and it must travel a distance (H − y) to reach the top. Work for that one slice: dW = ρg·πr²(H − y)dy. Integrate from 0 to H for the total. The distance factor (H − y) is the piece that changes with position — slices near the top travel nearly zero distance, while slices at the bottom travel almost the full height H.

The general principle unifying these problems is dimensional. Work has units of force × distance. Your integral must produce those units: the integrand F(x)dx has units (force)(length), and integrating over length gives force × length = work. Setting up the slice correctly — identifying the variable force and the corresponding infinitesimal displacement — is the entire skill. Once the integral is written correctly, the calculus is usually straightforward.
