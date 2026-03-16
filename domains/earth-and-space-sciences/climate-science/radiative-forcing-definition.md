---
id: radiative-forcing-definition
title: Radiative Forcing and Its Calculation
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-transfer-atmospheric
  type: hard
- id: energy-balance-models
  type: soft
builds-toward:
- radiative-feedback-water-vapor
- aerosol-radiative-forcing
- climate-sensitivity-radiative-feedbacks
tags:
- forcing
- perturbation
- greenhouse
- aerosol
- perturbation-analysis
stage: advanced
status: draft
---

# Radiative Forcing and Its Calculation

## Core Idea
Radiative forcing is the change in net energy flux in the stratosphere-adjusted atmosphere due to a perturbation (e.g., doubling CO₂, adding aerosols), measured in W/m². It quantifies how strongly an agent perturbs Earth's energy balance before temperatures have adjusted. Radiative forcing is a standardized metric for comparing the climate impact of different forcing agents (greenhouse gases, aerosols, solar variations) and is essential for interpreting climate model results and attributing observed climate change.

## How It's Best Learned
Use radiative transfer models to compute the change in outgoing longwave radiation and reflected solar radiation for a given perturbation (e.g., +1% solar, doubled CO₂). Compare forcing magnitudes across different agents.

## Common Misconceptions
Radiative forcing is not the equilibrium temperature change; it is the instantaneous energy imbalance. The actual temperature response depends on climate sensitivity and feedbacks. Also, forcing is defined at the tropopause, not the surface, to exclude rapid adjustments.

## Explainer

From your study of radiative transfer, you know that Earth's atmosphere absorbs and emits radiation at wavelengths determined by its composition. You also know from energy balance models that Earth maintains a rough equilibrium between incoming solar energy and outgoing longwave radiation. **Radiative forcing** is the metric that quantifies what happens when something disrupts that balance — it measures the change in net energy flux at the tropopause, in watts per square meter (W/m²), before the climate system has had time to respond by warming or cooling.

Think of it like a bank account analogy. Your energy balance model is the account ledger: energy in minus energy out equals zero at equilibrium. Radiative forcing is a sudden change in income or expenses — say, an unexpected $100/month raise. The moment the raise takes effect, your balance starts growing, but you have not yet changed your spending habits. The $100/month is the forcing; how you eventually adjust your lifestyle is the climate response. The key insight is that forcing is defined *before* the system adjusts. If you double atmospheric CO₂, the atmosphere absorbs more outgoing longwave radiation immediately, creating a positive forcing of roughly +3.7 W/m². The planet has not warmed yet — it simply has a new energy surplus that will *drive* warming over the coming decades and centuries.

The power of radiative forcing as a concept is that it provides a **common currency** for comparing wildly different climate perturbations. Greenhouse gases, volcanic aerosols, changes in solar output, and land-use changes all affect Earth's energy budget through different physical mechanisms. But by calculating each one's effect on the net energy flux at the tropopause, you can line them up on the same scale. A forcing of +2 W/m² from methane and a forcing of −1 W/m² from sulfate aerosols can be directly compared and summed, giving a net forcing of +1 W/m². This additivity is what makes forcing invaluable for climate attribution — determining how much of observed warming comes from CO₂ versus solar variability versus aerosol masking.

One subtlety worth noting: forcing is defined at the tropopause (the boundary between troposphere and stratosphere), not at the surface or top of atmosphere. This matters because the stratosphere adjusts to perturbations within weeks — much faster than the surface-troposphere system. By allowing the stratosphere to reach its new equilibrium before measuring the energy imbalance, **stratosphere-adjusted radiative forcing** removes a fast, noisy signal and isolates the sustained energy imbalance that actually drives surface temperature change. This is why doubling CO₂ produces a stratosphere-adjusted forcing of about +3.7 W/m² — a number that would be different (and less physically meaningful) if measured instantaneously at the top of atmosphere before stratospheric cooling occurs.
