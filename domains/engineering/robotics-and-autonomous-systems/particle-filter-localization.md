---
id: particle-filter-localization
title: Particle Filter Localization (Monte Carlo Localization)
domain: engineering
course: robotics-and-autonomous-systems
prerequisites: []
builds-toward:
- motion-planning-algorithms
- simultaneous-localization-and-mapping
tags:
- particle-filter
- localization
- monte-carlo
- mobile-robotics
- probabilistic
stage: advanced
status: validated
---

# Particle Filter Localization (Monte Carlo Localization)

## Core Idea
Particle filtering is a non-parametric Bayesian method for robot localization that represents the robot's belief about its position as a weighted cloud of samples (particles) drawn from the posterior probability distribution. Unlike Kalman filters which assume Gaussian distributions, particle filters can represent arbitrary multimodal distributions and handle highly nonlinear motion and sensor models. The algorithm cycles through: (1) motion update — propagate particles forward using odometry; (2) weight update — reweight particles based on sensor measurements; (3) resampling — eliminate low-weight particles and duplicate high-weight ones. When properly tuned, the particle cloud converges around the true robot position even under global localization uncertainty or kidnapped robot scenarios.

## Questions

```yaml
- question: "A mobile robot localizes using 1,000 particles and a LiDAR sensor. After motion, particles are propagated using odometry with added Gaussian noise. Then particle weights are updated based on LiDAR beam measurements. Which step is most computationally expensive and why?"
  type: multiple-choice
  options:
    - "Propagating particles because odometry must be verified against wheel encoders for each particle"
    - "Resampling particles because systematic resampling requires sorting all 1,000 particles"
    - "Weight computation because each particle must compare its expected LiDAR scan (ray-cast through a map) against the actual measured scan, requiring ray-casting for each particle"
    - "Normalizing weights because normalizing 1,000 floating-point values is inherently slow"
  answer: 2
  explanation: "This three-step structure (predict, weight, resample) is the core of sequential importance resampling (SIR). The motion model pushes uncertainty outward (particles spread); the measurement pulls uncertainty inward (particles concentrate); resampling focuses computational resources on promising hypotheses. The algorithm is named 'particle filter' because it filters out bad hypotheses and concentrates particles around good ones, asymptotically converging to the true posterior as the number of particles increases."
```

## Explainer

Localization — determining the robot's position and orientation in the environment — is a foundational capability for any mobile autonomous robot. If you have a map, the problem becomes: given odometry estimates (which drift over time) and sensor measurements (which have noise), what is the robot's most likely pose? The Kalman filter, which you studied earlier, solves this elegantly when motion and sensor models are linear and noise is Gaussian. But robot localization often violates these assumptions. The motion model is highly nonlinear (especially in steering). Sensor measurements like LiDAR scans or camera images involve nonlinear relationships between pose and expected observations. And multimodal uncertainty — not knowing which of several plausible locations the robot is at — cannot be represented by a single Gaussian.

Particle filtering addresses these limitations by representing the posterior probability distribution as a cloud of discrete samples (particles), each one a hypothesis about the robot's pose, weighted by its likelihood given observations. A particle is simply a tuple (x, y, θ) representing a possible robot position and orientation. The weighted set of particles encodes the full posterior: regions of particle density correspond to high-probability poses; empty regions correspond to impossible or very unlikely poses.

The particle filter cycles through three steps each measurement cycle:

**Motion Update (Prediction)**: Each particle is moved using the motion model — the odometry or commanded velocity. If the robot reports it moved 1 meter forward (from wheel encoders), all particles move 1 meter forward in their respective orientations. Process noise is added: each particle's motion is perturbed by random noise sampled from the motion uncertainty distribution. This represents the fact that odometry drifts — the actual motion isn't exactly what the odometry reports. The effect is that the particle cloud spreads outward with each motion step, capturing growing positional uncertainty.

**Measurement Update (Weight Computation)**: Each particle now evaluates how likely the actual sensor measurement would be if that particle were at the true position. This is the likelihood function p(measurement | particle_pose). For LiDAR, this involves computing a virtual scan: imagine rays cast from the particle's hypothesized position, and check if they hit obstacles in the map where the real LiDAR rays did. The better the match, the higher the particle's weight. For a camera, the likelihood might be computed from image feature matches. The weights are often computed in log space to avoid numerical underflow when multiplying many small probabilities. After all particles are weighted, the weights are normalized so they sum to 1.

**Resampling**: The particle cloud is now biased — many particles have very low weight and contribute almost nothing to the estimate, while a few high-weight particles dominate. Resampling redistributes particles: particles with high weight are duplicated; particles with low weight are eliminated. This is done proportionally to weight, so a particle with weight 0.1 is roughly 10 times more likely to be duplicated than one with weight 0.01. After resampling, the particle cloud is smaller but denser — all particles are given equal weight again and are clustered in regions of high posterior probability.

Over multiple cycles, the particles converge toward the true robot position. If odometry were perfect, particles would concentrate in a single spot after a few measurements. If odometry drifts, the particle cloud spreads during motion and re-concentrates around sensor measurements, resulting in error bounded by measurement accuracy. A key property is **multimodality**: if the robot is genuinely ambiguous (could be in any of three locations, based on current measurements), the particle cloud bifurcates into three clusters, each representing one hypothesis. When motion or measurement disambiguates, all but one cluster will be downweighted and resampled away, leaving the correct hypothesis. This handles the **global localization** problem (robot doesn't know where it starts) better than Kalman filters, which must be initialized near the true position.

A subtle but critical issue is **particle depletion**: if resampling is too aggressive, all particles converge to identical copies of a few high-weight samples, losing diversity. When new measurements arrive, the robot has no particles exploring the true position if it happens to be low-weight at that moment. The solution is adaptive resampling: resample only when the effective sample size (a measure of how concentrated weights have become) drops below a threshold. This preserves diversity while still eliminating obviously bad hypotheses.

The computational bottleneck is typically the weight computation step — each measurement requires computing the likelihood for every particle, which for LiDAR means ray-casting through a map 1,000 times. Practical implementations use GPU acceleration, beam subsampling, or pre-computed likelihood maps to make this tractable.

