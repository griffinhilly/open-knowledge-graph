---
id: output-gap-macroeconomic
title: The Output Gap
domain: economics
course: macroeconomics
prerequisites:
- id: potential-output-and-capacity
  type: hard
- id: real-vs-nominal-gdp
  type: hard
builds-toward:
- okun-law
- fiscal-policy-macroeconomics
tags:
- cycles
- gap
- measurement
stage: abstract-reasoning
status: draft
---

# The Output Gap

## Core Idea
The output gap is the difference between actual real GDP and potential output, expressed as a percentage of potential. A positive gap (overheating) signals demand exceeds supply and inflation is likely to rise; a negative gap (slack) suggests unemployment will remain elevated. The output gap is central to policy decisions but unobservable, requiring real-time estimation.

## How It's Best Learned
Use HP filter or trend-cycle decomposition to estimate the output gap from historical GDP data. Compare different estimation methods and note how estimates diverged during the 2008 crisis and subsequent recovery.

## Common Misconceptions
- The output gap can be precisely measured in real time. - A negative output gap always means deflation is coming. - The relationship between output gap and inflation is stable and predictable over long periods.

## Explainer

You know from studying real and nominal GDP that the economy fluctuates around some underlying trend. The **output gap** makes this comparison precise: it is the difference between actual real GDP and **potential output** (what the economy could produce if all resources were fully and efficiently employed), expressed as a percentage of potential. A positive gap means the economy is running hot — firms are operating above normal capacity, unemployment is below its natural rate, and inflation is likely to accelerate. A negative gap means the economy has slack — workers and capital are underutilized, and inflation is likely to fall.

The intuition is clearest with a manufacturing analogy. A factory has a **rated capacity** — the output level at which it runs efficiently without excessive overtime or equipment strain. If orders surge and the factory runs at 110% of rated capacity by calling in every worker and running equipment around the clock, it can produce more in the short run, but costs rise, maintenance suffers, and the pace is unsustainable. That's an economy with a positive output gap. Conversely, if orders collapse and the factory runs at 70% of capacity — some lines idle, some workers laid off — it's operating well below potential. That's a negative gap. Policymakers care deeply about which regime the economy is in because the appropriate policy response differs: stimulate when there's slack, tighten when overheating.

The problem is that potential output is **unobservable**. You can directly measure actual GDP every quarter (though even that gets revised repeatedly). But potential GDP is a theoretical construct — what the economy *would* produce under efficient full employment — and must be estimated. The most common approaches are statistical filters (like the Hodrick-Prescott filter, which smooths actual GDP to extract a trend), production function methods (estimate potential based on labor force, capital, and total factor productivity), and multivariate models that use multiple indicators simultaneously. Each method produces different estimates, and disagreements among them can be substantial, especially around turning points like recessions.

The policy implications of the output gap run through its relationship to inflation — specifically the **Phillips curve**. When the output gap is positive (demand exceeds potential), firms face cost pressures, workers have bargaining power, and prices rise: inflation tends to increase. When the gap is negative, the reverse: inflation tends to fall. This relationship is the conceptual foundation for central bank policy — the Fed's decisions about interest rates are largely driven by estimates of where the output gap stands and where it is heading. But the Phillips curve relationship has proven unstable over time: the "missing inflation" of the 2010s recovery (when a large negative gap failed to produce deflation) and the "too-fast inflation" of 2021-22 (when the gap seemed moderate but inflation surged) showed that the gap-inflation link depends on inflation expectations and supply-side factors in ways that simple models don't capture. Estimating the output gap in real time and predicting its inflation consequences remains one of the hardest problems in practical macroeconomics.

