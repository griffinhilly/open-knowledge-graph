---
id: differential-equations-intro-separable
title: Separable Equations (Intro)
domain: mathematics
course: calculus-2
prerequisites:
- id: u-substitution
  type: hard
- id: derivatives-of-exponential-functions
  type: hard
- id: basic-integration-rules
  type: hard
- id: solving-trigonometric-equations
  type: soft
builds-toward: []
tags:
- differential-equations
- separable
- applications
stage: formal-systems
status: validated
---
# Separable Equations (Intro)

## Core Idea
A differential equation is an equation involving a function and its derivatives. A separable equation has the form dy/dx = f(x)g(y), which can be solved by separating variables: (1/g(y)) dy = f(x) dx, then integrating both sides. This technique solves many fundamental models: exponential growth/decay (dy/dx = ky), Newton's cooling law, logistic growth, and mixing problems. It is the first and most natural solution technique.

## How It's Best Learned
Start with exponential growth dy/dx = ky (solution: y = Ce^(kx)) as the motivating example. Practice the separation procedure: rearrange, integrate both sides, solve for y, apply initial conditions to find C. Work through applications: population growth, radioactive decay, cooling.

## Common Misconceptions
- Forgetting the constant of integration (or absolute value signs from integrating 1/y).
- Not checking that division by g(y) is valid (g(y) = 0 may give equilibrium solutions).
- Treating dy/dx as a fraction without understanding that separation of variables is justified by the chain rule.

## Questions

```yaml
- question: "After solving dy/dx = 3y by separation of variables, you get y = Ce^(3x). What does the constant C represent?"
  type: multiple-choice
  options: ["The rate of growth of y with respect to x", "An arbitrary constant determined by initial conditions", "The value of y when x = 0, always equal to 1", "A constant that cancels when you differentiate to verify the solution"]
  answer: 1
  explanation: "C arises from the constant of integration and is determined by an initial condition. If you know y(0) = 5, then 5 = Ce^0 = C, so C = 5. C does not cancel when differentiating — d/dx(Ce^(3x)) = 3Ce^(3x) = 3y, which confirms the solution. The constant encodes the starting value of the system."

- question: "When solving a separable equation dy/dx = f(x)g(y), you can always safely divide both sides by g(y) before integrating."
  type: true-false
  answer: false
  explanation: "Division by g(y) is only valid when g(y) ≠ 0. If g(y) = 0 for some constant value y = c, then y = c is an equilibrium solution that the separation-of-variables process will miss entirely. Always check whether g(y) = 0 has solutions and handle them separately."

- question: "Why does integrating 1/y with respect to y produce ln|y| rather than ln(y), and when is it valid to drop the absolute value?"
  type: short-answer
  answer: "The integral of 1/y is ln|y| because the natural log is only defined for positive arguments, and y could be negative depending on the problem. The absolute value can be dropped when the context guarantees y > 0 — for example, when y represents a population size or a physical quantity that cannot be negative — or when applying an initial condition confirms the sign."
  explanation: "Skipping the absolute value introduces subtle errors: for instance, writing ln(y) = x + C and then exponentiating gives y = e^(x+C) = Ae^x, which only captures positive solutions. The correct form ln|y| = x + C gives y = ±e^(x+C) = Ae^x where A can be any nonzero constant, including negative. The absolute value keeps track of sign information."
```

## Explainer

A differential equation is an equation that describes a relationship between a function and its rate of change. Rather than asking "what is y?" directly, it asks "how does y change?" — and your job is to find the function y(x) that satisfies the constraint. The simplest and most important family of differential equations are the **separable** ones: equations of the form dy/dx = f(x)g(y), where the right-hand side factors cleanly into a piece that depends only on x and a piece that depends only on y.

The solution strategy is elegant. If g(y) ≠ 0, you can rearrange to put all the y-dependent terms on one side and all the x-dependent terms on the other: (1/g(y)) dy = f(x) dx. Then integrate both sides. This works because the chain rule justifies treating dy/dx as if the dx can be "moved" — formally, you are using the substitution theorem for integrals. The result is an equation in y and x (possibly implicit) that you solve for y. The constant of integration that appears when integrating both sides is the free parameter that initial conditions pin down.

The canonical example is exponential growth: dy/dx = ky. Separating gives (1/y) dy = k dx. Integrating: ln|y| = kx + C. Exponentiating: |y| = e^(kx+C) = Ae^(kx) where A = e^C > 0. Dropping the absolute value and allowing A to be any nonzero real number gives y = Ae^(kx). If y(0) = y₀, then A = y₀. This models population growth, radioactive decay (with k < 0), and compound interest. The same separation technique solves Newton's cooling law, mixing problems, and the logistic growth equation.

Two pitfalls deserve emphasis. First, **never forget the absolute value** when integrating 1/y. Writing ln(y) instead of ln|y| loses sign information and implicitly restricts your solution to y > 0 only. The absolute value can be dropped once you know the sign of y from context or initial conditions, but not before. Second, **check for equilibrium solutions** before dividing by g(y). If g(c) = 0 for some constant c, then y = c is a constant solution (dy/dx = 0) that the separation procedure will miss because you divided by zero. For dy/dx = y(y − 2), both y = 0 and y = 2 are equilibrium solutions that must be noted separately.

Once you can solve separable equations fluently — rearrange, integrate, apply initial conditions — you have a genuine modeling tool. The derivative is a description of a physical or biological process; the solution is the trajectory. Differential equations are where calculus stops being about computing rates and starts being about *predicting behavior over time*.

## Notes

Separable equations are a special case of first-order ODEs. The next techniques — integrating factors (for linear first-order equations) and exact equations — generalize beyond the separable case. Numerical methods (Euler's method, Runge-Kutta) handle equations that cannot be solved analytically.
