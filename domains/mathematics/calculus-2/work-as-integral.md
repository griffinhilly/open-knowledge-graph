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

## Questions

```yaml
- question: "A spring with k = 200 N/m is already stretched 0.1 m from its natural length. How much work is required to stretch it an additional 0.2 m (to 0.3 m total displacement)?"
  type: multiple-choice
  options:
    - "W = 200 × 0.2 = 40 J (constant-force formula using spring constant × extra distance)"
    - "W = ∫₀.₁^{0.3} 200x dx = [100x²]₀.₁^{0.3} = 9 − 1 = 8 J"
    - "W = ½ × 200 × 0.3² = 9 J (using only the final displacement)"
    - "W = 200 × 0.3 = 60 J (maximum force times total displacement)"
  answer: 1
  explanation: "The spring force F = 200x varies with displacement, so the constant-force formula fails. Work is W = ∫_{0.1}^{0.3} 200x dx = [100x²]_{0.1}^{0.3} = 100(0.09) − 100(0.01) = 9 − 1 = 8 J. Option C uses only the final position and ignores where the stretching started. Option D applies the maximum force over the entire interval, overestimating. Only the definite integral correctly accounts for the force varying throughout the displacement."

- question: "In a pumping problem, why does the work integral for a thin horizontal slice of water at height y include a factor of (H − y), where H is the height of the tank's outlet?"
  type: multiple-choice
  options:
    - "It represents the weight of all the water above that slice pressing down on it"
    - "It represents the distance that particular slice must travel to reach the outlet at the top"
    - "It is a pressure correction factor for the depth of the slice"
    - "It converts the slice's volume into a force value"
  answer: 1
  explanation: "(H − y) is the distance a slice at height y must travel to reach the top. Work = force × distance, and the distance is not constant across slices: a slice near the bottom (small y) must travel almost H, while one near the top travels nearly zero. The integral automatically sums these varying contributions. The weight of the slice provides the force; (H − y) provides the displacement for that specific slice."

- question: "In a pumping problem, a slice of water located near the top of a full tank requires less work to pump out than a slice of equal volume located near the bottom."
  type: true-false
  answer: true
  explanation: "Work = force × distance. Both slices have the same weight (same volume, same density), so the force component is equal. The difference is entirely in the distance: a near-top slice travels nearly zero to reach the outlet, while a near-bottom slice must travel almost the full tank height. This is why the factor (H − y) in the integral is small for upper slices and large for lower ones."

- question: "For a spring being stretched from rest (x = 0) to position x = d, the exact work done equals W = kd × d = kd², where kd is the spring force at the final position."
  type: true-false
  answer: false
  explanation: "Using the final force kd as if it acted over the entire displacement overestimates the work, because the spring force starts at zero and increases linearly. The correct answer is W = ∫₀ᵈ kx dx = ½kd² — exactly half of kd². The constant-force formula with the maximum force treats the spring as if it always exerted its peak resistance, which it only reaches at the very end of the stretch."

- question: "Explain why the constant-force formula W = F·d fails when force varies, and describe the key step in the integral approach that handles varying force correctly."
  type: short-answer
  answer: "W = F·d assumes force is the same at every point along the path. When force varies, applying a single value to the whole displacement mixes different force magnitudes and gives the wrong answer. The integral approach slices the displacement into infinitesimal pieces dx, approximates force as constant within each tiny slice (dW ≈ F(x)·dx), and sums all contributions via the definite integral. This makes the calculation exact rather than approximate."
  explanation: "The key move is the universal integral strategy: slice into pieces where the approximation is valid in the limit, then integrate to get the exact total. The constant-force formula W = F·d is just the special case where the integral collapses to F·(b − a) because F is truly constant."
```

## Explainer

From physics, you know that work equals force times distance — but only when force is constant. When force varies along the path, that formula breaks down. The fix is the same strategy behind every definite integral you've computed: slice the problem into tiny pieces where the quantity you care about is approximately constant, set up the contribution from one slice, and sum over all slices via the Fundamental Theorem of Calculus.

**Hooke's Law** provides the cleanest introduction. A spring resists extension with force F = kx, where x is the displacement from equilibrium and k is the spring constant. Stretching the spring a tiny amount dx from position x requires work dW ≈ F(x)·dx = kx·dx. The total work to stretch from x = a to x = b is W = ∫ₐᵇ kx dx = k·[x²/2]ₐᵇ. For a spring with k = 10 N/m stretched from 0 to 0.5 m: W = ∫₀^{0.5} 10x dx = 10·(0.25/2) = 1.25 J. The varying force is automatically handled by the integral.

**Pumping problems** are the classic application that challenges students most. Imagine a cylindrical tank of radius r and height H, filled with water, and you want to pump all the water to the top. The key move is to consider a thin horizontal slice of water at height y with thickness dy. Its volume is πr²dy, its weight (force due to gravity) is ρg·πr²dy (where ρ ≈ 1000 kg/m³ and g ≈ 9.8 m/s²), and it must travel a distance (H − y) to reach the top. Work for that one slice: dW = ρg·πr²(H − y)dy. Integrate from 0 to H for the total. The distance factor (H − y) is the piece that changes with position — slices near the top travel nearly zero distance, while slices at the bottom travel almost the full height H.

The general principle unifying these problems is dimensional. Work has units of force × distance. Your integral must produce those units: the integrand F(x)dx has units (force)(length), and integrating over length gives force × length = work. Setting up the slice correctly — identifying the variable force and the corresponding infinitesimal displacement — is the entire skill. Once the integral is written correctly, the calculus is usually straightforward.
