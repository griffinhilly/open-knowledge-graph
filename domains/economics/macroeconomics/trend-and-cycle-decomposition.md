---
id: trend-and-cycle-decomposition
title: Trend and Cycle Decomposition
domain: economics
course: macroeconomics
prerequisites:
- id: output-gap-and-potential-output
  type: hard
- id: business-cycles
  type: soft
builds-toward:
- recession-definition-measurement-dating
tags:
- business-cycles
- measurement
- filtering
stage: abstract-reasoning
status: draft
---

# Trend and Cycle Decomposition

## Core Idea
Time series decomposition separates output into trend (the sustainable path determined by fundamentals like productivity) and cycle (deviations due to demand and supply shocks). Methods like the Hodrick-Prescott filter isolate these components, though the decomposition depends on the method chosen and real-time estimates are noisy. The trend is often called the output gap when compared to actual output, and is critical for monetary policy decisions.

## Explainer

Every GDP time series contains two overlapping signals mixed together: a slowly-evolving **trend** and a faster-moving **cycle**. The trend reflects the economy's productive capacity — driven by capital accumulation, labor force growth, and technology — and changes gradually over decades. The cycle captures temporary departures from that capacity: boom periods where actual output exceeds its sustainable level, and recessions where it falls below. Decomposing these components is not just an academic exercise; it is how economists calculate the **output gap** — the central concept from your prerequisite — in practice.

The challenge is that neither the trend nor the cycle is directly observable. You only see the combined GDP series. One widely used approach is the **Hodrick-Prescott (HP) filter**, which mathematically separates a smooth trend by penalizing excessive curvature. The key parameter λ controls the smoothness of the extracted trend: high λ forces a nearly linear trend, while low λ allows the trend to track the actual series more closely. For quarterly GDP data, λ = 1600 is a standard choice. The cycle is then simply the residual — actual output minus the extracted trend.

Interpreting these components requires care. The estimated trend is not the same as "true" potential output — it is a statistical artifact of the filter. The HP filter has a well-known **end-point problem**: trend estimates at the edges of the sample are distorted because the filter has fewer data points to anchor both sides, making real-time estimates of the output gap unreliable. Policymakers who relied on real-time gap estimates have sometimes been misled into overly loose or overly tight policy stances. This is a reminder that statistical decomposition tools are only as good as the assumptions embedded in them.

The practical payoff is recognizing when a change in GDP reflects a **structural shift** in the economy versus a **cyclical fluctuation**. A pandemic that destroys productive capacity shifts the trend downward; a demand collapse leaves the trend intact but opens a large negative cycle. These two situations call for different policy responses — supply-side reforms versus demand stimulus — and conflating them leads to serious policy errors. Good macroeconomic analysis always asks first: is what I'm observing a trend event or a cycle event?
