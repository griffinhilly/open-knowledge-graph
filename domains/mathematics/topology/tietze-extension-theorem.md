---
id: tietze-extension-theorem
title: Tietze Extension Theorem
domain: mathematics
course: topology
prerequisites:
- id: urysohns-lemma
  type: hard
builds-toward:
- metrization-theorems
tags:
- tietze
- extension
stage: formal-systems
status: validated
---

# Tietze Extension Theorem

## Core Idea
In a normal space, every continuous function f: A → ℝ from a closed subset A extends to a continuous function F: X → ℝ.

## Questions

```yaml
- question: "Let A be a closed subset of a normal space X, and let f: A → [−1, 1] be continuous. What does the Tietze extension theorem guarantee?"
  type: multiple-choice
  options:
    - "There exists a continuous F: X → ℝ such that F|_A = f, and F may take values outside [−1, 1] on X \\ A"
    - "There exists a continuous F: X → [−1, 1] such that F|_A = f"
    - "f extends continuously to X if and only if A is compact"
    - "There exists a continuous F: X → [−1, 1] such that F|_A = f only when A is also open"
  answer: 1
  explanation: "The Tietze theorem guarantees both existence of an extension and range control: F can be arranged to map all of X into [−1, 1], not just into ℝ. The correct answer (B) states the stronger bounded version. Option A is also valid (a weaker conclusion also follows), but option B is the most precise and useful statement. Options C and D introduce incorrect conditions: compactness of A is not required, and closedness of A (not openness) is the key hypothesis. Closedness matters because it ensures that boundary behavior of f on A can be matched continuously from outside."

- question: "Why does the proof of the Tietze extension theorem use Urysohn's lemma iteratively, rather than extending f directly?"
  type: multiple-choice
  options:
    - "Urysohn's lemma is needed to first verify that A is closed before the extension can proceed"
    - "Urysohn's lemma constructs functions that separate 0 and 1 on disjoint closed sets, and these are used as building blocks to approximate f with successively smaller error, assembling the extension as a uniformly convergent series"
    - "Urysohn's lemma replaces f with a simpler linear function that is then extended by linearity"
    - "The proof uses Urysohn's lemma only once, to separate A from the rest of X"
  answer: 1
  explanation: "The constructive proof proceeds by building a sequence of continuous functions, each defined on all of X, that approximate f on A with error shrinking by a factor of 2/3 at each step. Each approximation step calls Urysohn's lemma to construct a function that separates two closed sets (where f is large from where f is small). The sum of this series converges uniformly to the desired extension F. Urysohn's lemma is the 'atom' — it provides the simplest kind of separation function — and Tietze shows complex continuous functions are just infinite combinations of these atoms."

- question: "The Tietze extension theorem can be viewed as a generalization of Urysohn's lemma, since Urysohn's lemma constructs extensions of specific simple functions (the 0-on-A, 1-on-B indicator) while Tietze handles arbitrary continuous functions."
  type: true-false
  answer: true
  explanation: "Urysohn's lemma solves a special instance of the extension problem: it extends the function that is 0 on the closed set A and 1 on the closed set B to a continuous function on all of X. Tietze generalizes this: instead of the simple 0/1 target, any continuous f: A → ℝ can be extended. The proof of Tietze actually reduces to repeated applications of Urysohn's lemma, confirming the logical dependence. In this sense Urysohn is the atomic building block and Tietze is the general statement."

- question: "If A is an open (rather than closed) subset of a normal space X and f: A → ℝ is continuous, then the Tietze theorem still guarantees that f extends to a continuous function on most of X."
  type: true-false
  answer: false
  explanation: "Closedness of A is an essential hypothesis, not a convenience. When A is open, f need not extend continuously: consider X = ℝ, A = (0, 1), and f(x) = 1/x. This is continuous on A but cannot be extended continuously to 0, which is a limit point of A not in A. The open set provides no control over what f does as you approach the boundary from inside, so no continuous extension to the boundary (and hence to all of X) need exist. Closedness ensures that f's values on A constrain what F must do near A's boundary from both sides."

- question: "Why does the Tietze extension theorem require A to be closed in X, and what can go wrong if A is merely an arbitrary subset?"
  type: short-answer
  answer: "Closedness of A ensures that the boundary of A (the points in X that are limits of sequences in A but not in A) is contained in A. This means f is already defined and continuous at every boundary point of A, so there is no ambiguity about what F must do as it approaches A from outside — it must approach the values f takes on A's boundary. If A were not closed, its boundary points would lie outside A, and f would have no values there, creating a gap: F would need to pick values at those boundary points without guidance, and continuity of F on all of X would then be impossible to guarantee. Closedness is what allows the Urysohn-based approximation to 'stitch in' values outside A consistently."
  explanation: "A deeper way to see this: the extension theorem is really a statement about the ability to interpolate continuously from a subset to the whole space. Closed sets are 'complete' in the sense that they contain their own limit points, so the behavior of f on A already determines what F must do at every approach to A from outside. For open sets, you can approach the boundary from outside A without the set 'telling you' what value to take — there is no constraint, and the extension can fail."
```

## Explainer

Urysohn's lemma, your prerequisite, tells you that in a normal space, disjoint closed sets can be separated by a continuous real-valued function — there is a function g: X → [0,1] that equals 0 on one closed set and 1 on the other. The Tietze extension theorem is a natural generalization: instead of asking whether a particular simple function (the 0-on-A, 1-on-B separator) can be built, it asks whether an arbitrary continuous function defined on a closed subset can be extended to the whole space.

To see why normality matters, think about what could go wrong. Suppose A is a closed subset of X and f: A → ℝ is continuous. Extending f to X means finding F: X → ℝ continuous with F|_A = f — agreeing with f on A, behaving continuously on the rest of X. On the interior of A, the values of F are forced. On X \ A (which is open), F has freedom. The difficulty is on the boundary: as you approach A from outside, F must match what f is doing inside A. Normality provides exactly the separation power needed to build this extension: it ensures closed sets can be distinguished by continuous functions (via Urysohn), which can be assembled into an approximation of f and successively refined.

The constructive proof of Tietze uses Urysohn's lemma iteratively. You approximate f by a sequence of continuous functions defined on all of X, each reducing the approximation error by a factor of 2/3 on A. The series converges uniformly to an extension F. This "uniform approximation by Urysohn functions" technique is a model for many existence arguments in analysis: rather than writing down the answer, you build it as a limit of manageable pieces. The key insight is that Urysohn's lemma is the atomic building block — the ability to extend indicator-like functions — and Tietze shows that more complex functions are just combinations of these atoms.

The theorem has two equivalent formulations: the extension can be arranged to map X → [−1,1] when f maps A → [−1,1] (bounded case), or X → ℝ when f: A → ℝ (unbounded case). Both follow from the same argument. The geometric content is that **normal spaces are functionally rich** — they support enough continuous functions to interpolate from any closed subset to the ambient space. This is not trivially true in general: without normality (or some separation axiom), continuous functions can be scarce and extensions may fail. The Tietze theorem connects to your next topic of metrization: one characterization of metrizable spaces is that they are normal, and normality combined with second-countability is exactly what the Urysohn metrization theorem needs. Tietze is thus part of the chain showing that normal spaces behave like metric spaces in their function theory.
