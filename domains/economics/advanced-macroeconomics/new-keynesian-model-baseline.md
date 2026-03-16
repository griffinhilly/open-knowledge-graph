---
id: new-keynesian-model-baseline
title: Baseline New Keynesian Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: calvo-pricing-model
  type: hard
- id: real-business-cycle-theory
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: linearization-nonlinear-systems
  type: soft
builds-toward:
- phillips-curve-dynamics
- monetary-policy-transmission
- dsge-models-framework
tags:
- new-keynesian
- monetary-policy
- price-stickiness
- welfare-analysis
stage: advanced
status: draft
---

# Baseline New Keynesian Model

## Core Idea
The New Keynesian model synthesizes Keynesian demand-side insights (sticky prices create monetary non-neutrality) with classical supply-side microfoundations (rational expectations, optimizing agents) and competitive labor markets. It features monopolistically competitive firms with Calvo pricing, forward-looking consumption determined by intertemporal optimization, and monetary policy conducted through interest-rate rules. The model shows how monetary policy affects output and inflation in the short run while being neutral in the long run, reconciling old Keynesian and classical insights.

## Explainer

The baseline New Keynesian model builds directly on two frameworks you already know. From **real business cycle (RBC) theory**, it inherits the supply side: optimizing households that choose consumption and labor supply, competitive factor markets, and rational expectations. From the **Calvo pricing model**, it inherits the key friction: firms cannot adjust prices every period but instead face a random probability of being able to reset their price in any given period. The New Keynesian model is essentially an RBC model with one critical addition — sticky prices — and this single friction is enough to make monetary policy matter for real output.

The model reduces, after log-linearization, to three equations that form its analytical core. The first is the **New Keynesian IS curve**, derived from the household's Euler equation: current output depends positively on expected future output and negatively on the real interest rate. This captures the demand side — when the central bank raises rates, households save more and consume less, reducing output. The second is the **New Keynesian Phillips Curve** (NKPC), derived from Calvo pricing: current inflation depends on expected future inflation and the current output gap. Firms that can reset prices set them based on current and expected future marginal costs; when output is above its natural level, marginal costs are high, and firms that get the chance to adjust prices raise them, generating inflation. The third equation is a **monetary policy rule** (typically a Taylor rule): the central bank sets the nominal interest rate in response to inflation and the output gap.

The eigenvalue structure you know from linear algebra determines whether the model has a unique, stable solution. The system has two forward-looking variables (output and inflation) and one policy instrument. For a unique rational expectations equilibrium, the Taylor rule must satisfy the **Taylor principle**: the central bank must raise the nominal interest rate by more than one-for-one with inflation. If it responds too weakly, multiple equilibria (including self-fulfilling inflation spirals) become possible — the model is **indeterminate**. If it responds appropriately, expectations are anchored and there is a unique path for output and inflation. This is where eigenvalues matter concretely: determinacy requires that the number of unstable eigenvalues equals the number of forward-looking variables.

The model's key insight is that **monetary non-neutrality arises entirely from price stickiness**. In the flexible-price limit (where all firms can adjust prices every period), output always equals its natural level and monetary policy has no real effects — the model collapses back to the RBC benchmark. With sticky prices, a monetary expansion lowers real interest rates (because not all prices adjust immediately to reflect the new money), stimulating demand and raising output above its natural level. But the effect is temporary: as more firms eventually reset prices, the price level catches up, real variables return to their natural levels, and only nominal variables are permanently affected. This captures the old Keynesian observation that money matters in the short run while preserving the classical result that money is neutral in the long run — a synthesis that gives the model its name and its central place in modern monetary policy analysis.
