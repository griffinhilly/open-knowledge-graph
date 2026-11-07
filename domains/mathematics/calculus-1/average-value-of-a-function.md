---
id: average-value-of-a-function
title: Average Value of a Function
domain: mathematics
course: calculus-1
prerequisites:
  - id: definite-integral-definition
    type: hard
  - id: fundamental-theorem-of-calculus-part-2
    type: hard
  - id: riemann-sums
    type: soft
  - id: mean-value-theorem
    type: soft
builds-toward: []
tags: [calculus, integration, average-value, mean-value-theorem-for-integrals, applications]
stage: formal-systems
status: validated
---

# Average Value of a Function

## Core Idea
The average value of a function f on [a, b] is f_avg = (1/(b - a)) ∫ from a to b of f(x) dx. It extends the ordinary average of finitely many numbers to the infinitely many values a function takes on an interval. Geometrically, f_avg is the height of the rectangle on [a, b] with the same area as the region under f. The Mean Value Theorem for Integrals says that if f is continuous on [a, b], then f actually equals its average value at some point c in [a, b].

## How It's Best Learned
Start with a discrete average: sample f at n equally spaced points and average the samples. Rewrite that average as a Riemann sum divided by (b - a) and let n grow, so the formula appears as a limit rather than a rule to memorize. Then draw the equal-area rectangle and locate the point c where the graph crosses its top edge.

## Common Misconceptions
- The average value is (f(a) + f(b))/2. (That averages only the endpoint values; for f(x) = x² on [0, 3] it gives 4.5, while the true average value is 3.)
- The average value is the integral itself. (The integral must be divided by the length of the interval, b - a.)
- Average value of a function means average rate of change. (Average rate of change is (f(b) - f(a))/(b - a), which averages f', not f.)

## Questions

```yaml
- question: "What is the average value of f(x) = x² on [0, 3]?"
  type: multiple-choice
  options: ["3", "4.5", "9", "1.5"]
  answer: 0
  explanation: "f_avg = (1/3) ∫ from 0 to 3 of x² dx = (1/3)(27/3) = (1/3)(9) = 3. The value 4.5 is the average of the endpoint values 0 and 9, and 9 is the integral before dividing by the length 3."

- question: "For f(x) = x² on [0, 3], find a number c in [0, 3] with f(c) equal to the average value."
  type: short-answer
  answer: "c = √3 ≈ 1.732"
  explanation: "The average value is 3, so solve c² = 3 to get c = √3, which lies in [0, 3]. The Mean Value Theorem for Integrals guarantees such a c exists because x² is continuous."

- question: "The average value of f on [a, b] equals (f(a) + f(b))/2 for every continuous function f."
  type: true-false
  answer: false
  explanation: "That formula holds for linear functions but not in general. For x² on [0, 3] it gives 4.5, while the integral formula gives 3. The integral accounts for every value of f on the interval, not just the endpoints."

- question: "A car's velocity is v(t) = 6t meters per second for 0 ≤ t ≤ 4. What is its average velocity over this time?"
  type: multiple-choice
  options: ["12 m/s", "24 m/s", "48 m/s", "6 m/s"]
  answer: 0
  explanation: "Average velocity = (1/4) ∫ from 0 to 4 of 6t dt = (1/4)(3t² from 0 to 4) = (1/4)(48) = 12 m/s. The integral 48 is the total distance in meters, and dividing by 4 seconds gives the average."
```

## Explainer

To average a list of numbers, you add them and divide by how many there are. A function on an interval takes infinitely many values, so this recipe needs a new form. Calculus supplies it through the integral.

Suppose you want the average of f on [a, b]. A reasonable approximation is to sample f at n equally spaced points x₁, ..., xₙ and average them: (f(x₁) + ... + f(xₙ))/n. The spacing between points is Δx = (b - a)/n, so 1/n = Δx/(b - a). The sample average becomes (1/(b - a))(f(x₁)Δx + ... + f(xₙ)Δx). The expression in parentheses is a Riemann sum. As n grows, it approaches the definite integral, and the sample average approaches

f_avg = (1/(b - a)) ∫ from a to b of f(x) dx.

There is a clear picture behind this formula. Multiply both sides by (b - a) to get f_avg · (b - a) = ∫ f(x) dx. The left side is the area of a rectangle with base b - a and height f_avg. So the average value is the height of the one rectangle whose area equals the area under the curve. Parts of the graph above that height balance the parts below it.

Example: f(x) = x² on [0, 3]. The integral is 3³/3 = 9 and the interval has length 3, so f_avg = 3. Compare this with the endpoint average (0 + 9)/2 = 4.5. The endpoint average is too large because x² stays small for much of the interval and rises steeply near 3.

If f is continuous, the graph cannot jump over the rectangle's top edge. Since f takes values both at least and at most f_avg, the Intermediate Value Theorem gives a point c with f(c) = f_avg. This is the Mean Value Theorem for Integrals. For x² on [0, 3], solving c² = 3 gives c = √3.

The idea shows up whenever a quantity varies continuously. The average temperature over a day, the average velocity over a trip, and the average concentration of a drug over a dosing period are all computed by integrating and dividing by the length of the interval. For velocity, the integral is the displacement, so the formula agrees with "displacement divided by time."
