---
id: two-phase-homogeneous-flow-equilibrium
title: Two-Phase Flow and Homogeneous Equilibrium Model
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: compressible-flow-isentropic-flow
  type: hard
- id: saturated-superheated-property-regions
  type: hard
- id: gibbs-phase-rule-multicomponent
  type: soft
builds-toward:
- cavitation-inception-vapor-formation
tags:
- two-phase
- homogeneous-equilibrium
- quality
- slip-ratio
- pressure-drop
stage: formal-systems
status: validated
---

# Two-Phase Flow and Homogeneous Equilibrium Model

## Core Idea
The homogeneous equilibrium model assumes liquid and vapor move together (slip ratio = 1) in thermal and mechanical equilibrium. Properties are quality-weighted: v = v_f + x(v_g - v_f). This simplification works for slow processes; rapid flashing or separation requires slip-flow models. Application to choked flow, pump cavitation, and turbine exit conditions is essential in power engineering.

## Questions

```yaml
- question: "In the homogeneous equilibrium model, what is the specific volume of a two-phase steam-water mixture with quality x, saturated liquid specific volume vₗ, and saturated vapor specific volume vᵥ?"
  type: multiple-choice
  options:
    - "v = x · vᵥ"
    - "v = vₗ + x(vᵥ − vₗ)"
    - "v = √(vₗ · vᵥ)"
    - "v = vᵥ / x"
  answer: 1
  explanation: "The HEM treats the two-phase mixture as a single pseudo-fluid with quality-weighted properties. Specific volume is a linear interpolation between saturated liquid and saturated vapor: v = vₗ + x(vᵥ − vₗ), which is equivalent to v = (1−x)vₗ + x·vᵥ. This follows directly from the mass-weighted average: x fraction of the mass is vapor (volume per unit mass = vᵥ) and (1−x) is liquid (vₗ). Options A ignores the liquid phase entirely; C and D have no physical basis in mixture thermodynamics."

- question: "Two-phase steam-water mixtures choke (reach maximum mass flow) at velocities far below what would choke pure steam or pure water. The best explanation is:"
  type: multiple-choice
  options:
    - "Two-phase flow has much higher viscosity than either pure phase, restricting flow more severely"
    - "The mixture speed of sound is very low because it combines the high compressibility of vapor with the high density of liquid"
    - "Phase separation at the choke point creates a vapor plug that blocks liquid flow entirely"
    - "Choking in two-phase flow is governed by surface tension at the liquid-vapor interface"
  answer: 1
  explanation: "The speed of sound in a medium depends on compressibility and density: c = √(1/ρκ), where κ is compressibility. Pure liquid has high density but very low compressibility (high bulk modulus) → high sound speed (~1500 m/s). Pure vapor has low density but high compressibility → moderate sound speed. A two-phase mixture is compressible like vapor (because the vapor phase readily changes volume under pressure) yet dense like liquid (the liquid dominates the mass). The result — high density combined with high compressibility — produces a very low mixture sound speed, sometimes only a few m/s. Choking occurs when flow velocity reaches the local speed of sound, so choking happens at much lower velocities in two-phase flow."

- question: "Quality (x) in two-phase flow represents the volume fraction of vapor in the mixture."
  type: true-false
  answer: false
  explanation: "Quality x is the *mass fraction* of vapor: x = mᵥ/(mₗ + mᵥ). Because vapor is far less dense than liquid, even a small mass fraction of vapor occupies a large volume. The *void fraction* α = Vᵥ/(Vₗ + Vᵥ) is the volume fraction of vapor, and α >> x in most practical conditions. For example, at low quality in a steam-water system, nearly all the mass is liquid but a substantial fraction of the volume can be vapor. This distinction matters: the HEM predicts void fraction from quality via the mixture specific volume, and slip-flow models correct for cases where the HEM underestimates actual void fraction."

- question: "The homogeneous equilibrium model becomes less accurate in vertical pipes with large liquid-vapor density ratios because buoyancy-driven slip causes vapor to rise faster than liquid, making the actual void fraction larger than HEM predicts."
  type: true-false
  answer: true
  explanation: "The HEM's slip ratio = 1 assumption means both phases travel at the same velocity. In reality, buoyancy in vertical flows causes the less-dense vapor phase to rise faster than the liquid — the slip ratio S = vᵥ/vₗ > 1. When vapor moves faster than the model predicts, the actual vapor volume fraction (void fraction) is higher than the HEM calculation yields. This means the HEM underestimates void fraction (and thus overestimates liquid inventory) in these regimes — a potentially non-conservative error in safety analysis where knowing how much coolant remains is critical. Lockhart-Martinelli correlations and full two-fluid models correct for slip."

- question: "Why does the homogeneous equilibrium model assume a slip ratio of 1, and under what physical conditions does this assumption break down most severely?"
  type: short-answer
  answer: "The HEM assumes slip ratio S = vᵥ/vₗ = 1 (vapor and liquid travel at the same velocity) because it treats the two-phase mixture as a single homogeneous pseudo-fluid. This is a valid approximation when the phases have little time to separate — at high flow velocities, in horizontal flows where gravity doesn't drive separation, or when the mixture is near thermodynamic equilibrium with finely dispersed bubbles. The assumption breaks down most severely when: (1) vapor-liquid density ratios are large (as in high-pressure steam systems), (2) flow is vertical (buoyancy drives vapor upward faster than liquid), and (3) flow velocities are low enough for phase separation to occur. In these regimes, vapor actually travels significantly faster than liquid, and the HEM underestimates void fraction and overestimates the remaining liquid inventory."
  explanation: "The practical consequence is that HEM is conservative for choking calculations (it tends to overestimate maximum mass flow) but may be non-conservative for coolant inventory during accident scenarios. Engineers select the model based on which type of error is acceptable for the specific safety application."
```

## Explainer

When vapor and liquid coexist in a flowing system — inside a boiling tube, downstream of a throttle valve, at the exit of a steam turbine — you have **two-phase flow**. In principle, liquid and vapor can move at different velocities, forming complex structures like bubbles, slugs, or annular films. But in many engineering calculations, especially near thermodynamic equilibrium, a powerful simplification works: assume the two phases travel together at the same velocity and are always in thermal equilibrium with each other. This is the **homogeneous equilibrium model (HEM)**.

The HEM's defining assumption is that the **slip ratio** S = vᵥ/vₗ = 1 — vapor and liquid velocities are identical. With this, the two-phase mixture behaves as a single pseudo-fluid whose properties are quality-weighted averages. Specific volume becomes **v = vₗ + x(vᵥ − vₗ)**, where x is **quality** (vapor mass fraction) and vₗ, vᵥ are the saturated liquid and vapor specific volumes from your property tables. Similarly, enthalpy: **h = hₗ + x hₗᵥ**, and entropy: **s = sₗ + x sₗᵥ**. These mixing rules, which you've already used when working with saturated property regions, now apply to a flowing mixture. The full toolbox of single-phase compressible-flow analysis — continuity, momentum, and energy equations — carries over directly, using mixture properties in place of single-phase ones.

The HEM is particularly powerful for **choked flow** calculations. Recall from compressible flow that choking occurs when the local flow velocity reaches the speed of sound, creating a maximum in mass flow rate that no downstream pressure reduction can exceed. In two-phase flow, the **mixture speed of sound** is dramatically lower than in either pure phase alone — sometimes only a few meters per second, compared to ~1500 m/s in liquid water. This happens because the mixture combines the high compressibility of vapor (which compresses readily under pressure) with the high density of liquid, and low sound speed results from high compressibility at moderate density. Choking at low velocities explains why two-phase relief valves and rupture discs behave very differently from single-phase devices, and why HEM is the standard first model in nuclear and process safety analysis for sizing pressure-relief systems.

The limits of the HEM are as important as its application. The assumption S = 1 breaks down when flow velocities are high, when the pipe is vertical (buoyancy drives vapor upward), or when liquid-vapor density ratios are large. In these regimes, vapor rises above liquid due to buoyancy-driven **slip**, and the actual void fraction (volume fraction of vapor) exceeds the HEM prediction — meaning less liquid is present than the model assumes. For design cases requiring high accuracy, engineers use void-fraction correlations (such as the Lockhart-Martinelli parameter) or full two-fluid models that track each phase separately. But the HEM provides the essential baseline: a rapid, closed-form estimate of mixture properties, pressure drop, and choking conditions that is exact in the equilibrium limit and usefully conservative in many safety applications.
