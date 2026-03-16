---
id: steam-tables-property-diagrams
title: Using Steam Tables and Thermodynamic Diagrams
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: saturated-superheated-property-regions
  type: hard
- id: thermodynamic-property-diagrams
  type: hard
builds-toward:
- rankine-power-generation-cycles
tags:
- steam-tables
- property-diagrams
- problem-solving
- reference
stage: advanced
status: draft
---

# Using Steam Tables and Thermodynamic Diagrams

## Core Idea
Steam tables provide tabulated h, s, v for saturated liquid, saturated vapor, and superheated steam at various T and P. The T-s diagram visualizes processes as paths on the saturation envelope; the h-s (Mollier) diagram enables rapid property lookup and entropy generation visualization. Power cycle analysis relies on accurate table interpolation and graphical process representation for speed and clarity.

## Explainer

You already know that water/steam is the working fluid of choice for most large power plants, and you understand the saturated and superheated property regions. **Steam tables** are the quantitative bridge between that conceptual knowledge and actual engineering calculations. They tabulate specific enthalpy h, specific entropy s, and specific volume v at defined thermodynamic states — giving you exact numbers for states you previously could only describe qualitatively.

Steam tables come in three parts. The **saturated tables** (indexed by either temperature or pressure) give properties of saturated liquid (subscript f) and saturated vapor (subscript g) on the phase boundary. The difference h_fg = h_g − h_f is the **latent heat of vaporization** — the enthalpy required to boil one unit mass entirely. When a state is in the **two-phase (wet steam) region**, you use the **quality** x (fraction by mass that is vapor): h = h_f + x·h_fg, s = s_f + x·s_fg, v = v_f + x·v_fg. The **superheated tables** cover steam above the saturation temperature at a given pressure; these are doubly indexed by both T and P, requiring **interpolation** when your state falls between table entries. Linear interpolation is standard: h at the target T ≈ h₁ + (T − T₁)/(T₂ − T₁) · (h₂ − h₁).

The **T-s diagram** is the clearest way to visualize thermodynamic processes. The two-phase dome occupies the center; the critical point is its apex. Horizontal lines (constant T) inside the dome represent phase change at constant temperature and pressure. The saturated liquid curve and saturated vapor curve are the dome's left and right boundaries. Reversible processes are paths on this diagram: a reversible, adiabatic (isentropic) expansion is a **vertical line** (constant s); an irreversible expansion bows rightward because irreversibility generates entropy. This makes inefficiency *visible* — a turbine's isentropic efficiency is literally the ratio of the actual enthalpy drop to the vertical-drop enthalpy drop.

The **h-s diagram (Mollier diagram)** rearranges the same information with enthalpy on the vertical axis and entropy on the horizontal axis. This is especially convenient for turbines and nozzles, where the work output equals the enthalpy drop. The slope of a line on the Mollier diagram at any state equals the temperature (from dh = T ds + v dP at constant P). The saturation curve appears as the lower-left boundary; isobars curve upward and to the right in the superheated region. Engineers doing Rankine cycle calculations often jump between the tables (for precise numbers) and the Mollier diagram (for visual checking of the cycle path) rather than using one or the other exclusively.
