---
id: unit-step-function
title: Unit Step Function and Piecewise-Defined Forcing
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition-and-properties
  type: hard
- id: piecewise-functions
  type: soft
builds-toward:
- convolution-theorem
tags:
- laplace-transform
- piecewise
- step-function
stage: formal-systems
status: draft
---

# Unit Step Function and Piecewise-Defined Forcing

## Core Idea
The unit step function u(t - a) is 0 for t < a and 1 for t ≥ a. Its Laplace transform L{u(t - a)} = e^{-as}/s handles piecewise-defined forcing terms. The shifting property L{f(t - a)u(t - a)} = e^{-as}F(s) simplifies solving ODEs with discontinuous inputs.

## Explainer

You've learned the Laplace transform and its basic properties, and you know how to represent piecewise-defined functions by specifying different formulas on different intervals. The **unit step function** u(t − a) bridges these two ideas: it equals 0 for t < a and 1 for t ≥ a, acting like a switch that turns on at time t = a. By combining step functions, you can express any piecewise-defined forcing term as a single formula and take its Laplace transform in one calculation.

The key to writing piecewise functions cleanly is the following pattern: a function that equals g(t) for 0 ≤ t < a and h(t) for t ≥ a can be written as g(t) + [h(t) − g(t)] · u(t − a). Before the switch (t < a), the step function is 0, so you get g(t). After the switch (t ≥ a), the step function is 1, so you get g(t) + h(t) − g(t) = h(t). More complex piecewise functions, with multiple breakpoints, are assembled similarly by adding more step functions, one per switch. This turns a description with cases into a single algebraic expression that the Laplace transform can handle directly.

The Laplace transform of the unit step function is L{u(t − a)} = e^{−as}/s. The exponential factor e^{−as} is the signature of a time delay in the s-domain — it encodes "this feature arrives at time a." The **second shifting theorem** generalizes this: L{f(t − a) · u(t − a)} = e^{−as} · F(s), where F(s) = L{f(t)}. To apply it, you need the forcing term written as a function of (t − a) multiplied by u(t − a) — not f(t) · u(t − a), but f(t − a) · u(t − a), with the argument shifted to match the step function's activation time.

Inverting in the other direction: if you encounter e^{−as} · F(s) in the s-domain, the inverse transform is f(t − a) · u(t − a). Take the function whose transform is F(s), shift it right by a (replace t with t − a), and multiply by u(t − a) to indicate it only exists for t ≥ a. For example, e^{−2s}/(s + 1) inverts to e^{−(t−2)} · u(t − 2): an exponential decay that begins at t = 2. This combination — step functions for switching, time-shifting for delaying — makes the Laplace method directly applicable to discontinuous forcing, which arises constantly when modeling circuits being switched on, mechanical impulses starting at a fixed time, or any system responding to an input that begins at t = a rather than t = 0.
