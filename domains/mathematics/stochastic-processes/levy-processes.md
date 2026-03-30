---
id: levy-processes
title: Lévy Processes
domain: mathematics
course: stochastic-processes
prerequisites:
- id: brownian-motion
  type: hard
- id: poisson-processes
  type: hard
- id: characteristic-functions
  type: hard
tags:
- levy-process
- levy-khintchine
- jump-diffusion
- infinitely-divisible
stage: expert
status: validated
---

# Lévy Processes

## Core Idea
A Lévy process is a stochastic process with stationary and independent increments and càdlàg (right-continuous with left limits) sample paths. The Lévy-Khintchine formula characterizes its distribution through three components: a deterministic drift b, a Gaussian (Brownian) part with variance σ², and a jump part described by a Lévy measure ν. Every Lévy process decomposes as X(t) = bt + σW(t) + J(t), where J captures all jumps. This unifies Brownian motion (ν = 0), Poisson processes (σ = 0, ν atomic), and their combinations.

## Questions

```yaml
- question: "The Lévy-Khintchine formula states that the characteristic exponent ψ(u) = log E[e^{iuX(1)}] of a Lévy process has the form ψ(u) = ibu - σ²u²/2 + ∫(e^{iux} - 1 - iux·1_{|x|<1}) ν(dx). The three terms correspond to:"
  type: multiple-choice
  options:
    - "Mean, variance, and skewness of X(1)"
    - "Drift (deterministic motion), diffusion (Brownian component), and jumps (Lévy measure ν)"
    - "Real part, imaginary part, and modulus of the characteristic function"
    - "Small jumps, medium jumps, and large jumps"
  answer: 1
  explanation: "The Lévy-Khintchine formula is the complete classification of infinitely divisible distributions: ibu is a deterministic drift, -σ²u²/2 is the Gaussian (Brownian) component, and the integral captures all jump activity through the Lévy measure ν. The measure ν(dx) describes the rate of jumps of size x: ν(A) is the expected number of jumps per unit time whose size falls in the set A. The truncation function 1_{|x|<1} compensates for small jumps (which may be so frequent that their sum needs centering). Every Lévy process is uniquely determined by the triplet (b, σ², ν)."

- question: "Brownian motion is a Lévy process with (b, σ², ν) = (0, 1, 0) and a Poisson process with rate λ has (b, σ², ν) = (0, 0, λδ₁). A compound Poisson process with jump rate λ and jump distribution F has Lévy measure:"
  type: multiple-choice
  options:
    - "ν(dx) = λF(dx), concentrating ν on the jump-size distribution weighted by the jump rate"
    - "ν(dx) = λδ₀(dx), concentrating all mass at zero"
    - "ν(dx) = F(dx)/λ, inversely proportional to the rate"
    - "ν(dx) = λ²F(dx), squared because the process is compound"
  answer: 0
  explanation: "A compound Poisson process has jumps arriving at rate λ, each with size drawn from F. The Lévy measure ν(dx) = λF(dx) encodes both the rate and size distribution: the total mass ν(ℝ\\{0}) = λ is the jump rate, and the normalized measure F(dx) = ν(dx)/λ gives the jump size distribution. Key property: compound Poisson processes have ν(ℝ\\{0}) < ∞ (finite jump rate). Lévy processes with ∫ν(dx) = ∞ (like the Cauchy process or variance-gamma process) have infinitely many jumps in every interval — a qualitatively different behavior."

- question: "Explain the Lévy-Itô decomposition and why it is the 'structure theorem' for Lévy processes."
  type: short-answer
  answer: "The Lévy-Itô decomposition writes every Lévy process as the independent sum of three components: X(t) = bt + σW(t) + X^{large}(t) + X^{small}(t). The first is deterministic drift, the second is a Brownian motion (continuous Gaussian part), and the third and fourth capture jumps. Large jumps (|x| ≥ 1) form a compound Poisson process X^{large} (finitely many per unit time). Small jumps (|x| < 1) are handled by a compensated sum X^{small} = lim_{ε→0} (sum of jumps in (ε,1) minus their mean) — this converges because the compensation removes the potentially divergent mean. The decomposition shows that drift, diffusion, and jumps are the three and only three types of behavior a Lévy process can exhibit."
  explanation: "The decomposition is 'structural' because it is exhaustive and canonical: there is no fourth type of behavior. Any process with stationary independent increments must be a combination of these three. This is the content of the Lévy-Khintchine theorem — the triplet (b, σ², ν) parametrizes all possibilities."
```

## Explainer

**Lévy processes** are the natural generalization of Brownian motion and Poisson processes to a unified framework. A Lévy process X(t) has three defining properties: X(0) = 0, stationary increments (X(t+s) - X(t) has the same distribution as X(s)), independent increments, and càdlàg paths (right-continuous with left limits, allowing jumps). Brownian motion satisfies these with continuous paths; the Poisson process satisfies them with piecewise-constant paths. Lévy processes include both extremes and everything in between — processes that simultaneously diffuse continuously and jump randomly.

The **Lévy-Khintchine formula** provides a complete classification. Every Lévy process is determined by a characteristic triplet (b, σ², ν), where b ∈ ℝ is a drift, σ² ≥ 0 is the Brownian variance, and ν is a Lévy measure on ℝ\{0} satisfying ∫min(1, x²)ν(dx) < ∞. The characteristic exponent ψ(u) = log E[e^{iuX(1)}] = ibu - σ²u²/2 + ∫(e^{iux} - 1 - iux·1_{|x|<1})ν(dx) uniquely determines the distribution. This formula is the continuous-time analogue of the fact that infinitely divisible distributions are classified by Gaussian and Poisson components. The condition ∫min(1,x²)ν(dx) < ∞ allows ν to have infinite total mass (infinitely many small jumps per unit time) but requires the small jumps to be square-integrable.

The **Lévy-Itô decomposition** provides the pathwise structure. Every Lévy process decomposes as the independent sum of: (1) a deterministic drift bt, (2) a Brownian motion σW(t), (3) a compound Poisson process of large jumps (|x| ≥ 1, occurring at finite rate), and (4) a compensated sum of small jumps (|x| < 1, centered to have zero mean). This decomposition is canonical — there is no other type of behavior a process with stationary independent increments can exhibit. It is the continuous-time analogue of the decomposition of an infinitely divisible random variable into Gaussian and Poisson components.

Important examples beyond Brownian motion and Poisson processes include: the **compound Poisson process** (finite Lévy measure, finitely many jumps per unit time), the **Cauchy process** (stable process with index 1, ν(dx) = c/|x|² dx, infinite jump activity), the **variance-gamma process** (a Brownian motion with drift time-changed by a gamma process, used in finance for heavy-tailed returns), and **stable processes** (self-similar Lévy processes, the continuous-time analogues of stable distributions). In mathematical finance, Lévy processes address the key deficiency of geometric Brownian motion: they can produce heavy tails, skewness, and discontinuous price movements (jumps), all observed in real market data. The stochastic calculus for Lévy processes extends Itô calculus by adding a jump integral ∫∫f(x)(N(dt,dx) - ν(dx)dt) against the compensated Poisson random measure.
