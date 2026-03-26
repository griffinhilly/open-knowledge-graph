---
id: compressor-staging-multistage
title: Multistage Compressor Design and Intercooling
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: polytropic-efficiency-real-machinery
  type: hard
- id: gas-mixtures-partial-pressures-daltons-law
  type: soft
builds-toward:
- brayton-cycle-intercooling-reheating
tags:
- compressor
- multistage
- intercooling
- pressure-ratio
- power-input
stage: formal-systems
status: validated
---

# Multistage Compressor Design and Intercooling

## Core Idea
Multistage compression with intercooling reduces the total compressor work by maintaining lower inlet temperatures to downstream stages. Optimal stage pressure ratios are equal when polytropic efficiency is constant. Intercooling between stages approaches isothermal compression in the limit, minimizing compression work while meeting high pressure ratios economically.

## Questions

```yaml
- question: "A plant needs to compress air from 1 bar to 16 bar using two stages with intercooling. What intermediate pressure minimizes total shaft work, and why?"
  type: multiple-choice
  options:
    - "8 bar (arithmetic mean), because splitting the pressure range equally minimizes work per stage"
    - "4 bar (geometric mean: √(16×1)), because equal pressure ratios per stage minimize total work when efficiency is constant"
    - "Any intermediate pressure gives the same total work, because energy must be conserved regardless of staging"
    - "4 bar, but only if the intercooler can cool the gas below the original inlet temperature"
  answer: 1
  explanation: "With equal polytropic efficiency, total shaft work is minimized when each stage handles the same pressure ratio: r_stage = √(r_total) = √16 = 4. So P_int = 1 × 4 = 4 bar. This follows from calculus: differentiating total work with respect to P_int and setting it to zero yields P_int = √(P_inlet × P_final). Option C is wrong because staging with intercooling genuinely reduces total work by cooling the gas before the second stage — conservation of energy applies, but the work input decreases because the compressed gas's enthalpy rise is reduced by the intercooler's heat removal."

- question: "Why does adding intercoolers between compression stages reduce total shaft work input?"
  type: multiple-choice
  options:
    - "Intercoolers reduce the pressure drop across each stage, so each stage compresses a smaller ratio"
    - "Cooling the gas between stages reduces its temperature and density, so subsequent stages compress cooler, lower-density gas requiring less work"
    - "Intercoolers convert the heat of compression back into mechanical work, reducing net energy input"
    - "Cooling increases the gas's specific heat ratio, making the compression path more efficient"
  answer: 1
  explanation: "Compression work scales with inlet temperature (for polytropic compression, W ∝ T_inlet). When a single stage compresses gas, the discharge is hot — and that hot gas requires more work to compress further because its specific volume is higher. Intercooling removes the heat and returns the gas approximately to T₁. The second stage then compresses cool, denser gas, doing less work than if it received the hot discharge. The intercooler is rejecting heat to the environment (not converting it to work), which is why the process approaches isothermal compression — the theoretical minimum work — with more stages and better intercooling."

- question: "With infinitely many compression stages and perfect intercooling (each intercooler returns gas exactly to the original inlet temperature), multistage compression approaches isothermal compression, achieving the minimum possible work for a given pressure ratio."
  type: true-false
  answer: true
  explanation: "This is the theoretical limit. With infinite stages and intercoolers, the compression path becomes infinitely many tiny isentropic rises interrupted by isobaric coolings back to T₁ — the net effect is a reversible isothermal process (T = constant throughout). Isothermal compression minimizes work because work input equals the area under the P-V curve on a pressure-volume diagram, and the isothermal path lies below any polytropic path between the same pressure endpoints. Real multistage compressors approach but never reach this limit."

- question: "Doubling the number of compression stages and intercoolers typically approximately halves the total power consumption, so industrial designers should use as many stages as economically feasible."
  type: true-false
  answer: false
  explanation: "The relationship exhibits strong diminishing returns. Going from 1 stage to 2 stages captures a large fraction of the available work savings; adding a 3rd stage helps further but by less; by 6 stages, the compression path is already very close to isothermal and additional stages yield minimal additional savings. Industrial compressors typically use 3–6 stages because beyond that, the added capital cost (stage hardware, intercoolers, piping), pressure drops in the intercoolers, and system complexity outweigh the marginal work savings. The relationship is logarithmic in benefit, not linear."

- question: "Why is equal pressure ratio per stage the optimal design when polytropic efficiency is constant across all stages, and what changes this optimum if efficiencies differ between stages?"
  type: short-answer
  answer: "With constant polytropic efficiency, the work input per stage depends only on the pressure ratio and inlet temperature of that stage (since all other parameters are the same). Minimizing total work by choosing the intermediate pressures is then a symmetric optimization: each stage contributes equally to the total pressure ratio at minimum cost. Setting dW_total/dP_int = 0 yields the geometric mean condition — equal ratios per stage. If efficiencies differ, a more efficient stage can handle a larger pressure ratio more cheaply, so the optimum shifts more work toward the efficient stage. The equal-ratio rule applies only under the symmetry assumption of equal efficiencies."
  explanation: "This equal-ratio result is the standard starting point for multistage compressor preliminary design. In practice, designers verify it with detailed performance maps for each stage and adjust to account for real efficiency variations, intercooler pressure drops, and inlet conditions that may differ from the design point."
```

## Explainer

From your study of polytropic compression, you know that real compressor work lies between two idealized extremes: **isothermal compression** (constant temperature, minimum work, impossible to achieve exactly) and **isentropic compression** (adiabatic and reversible, maximum work for a given pressure ratio). A single-stage compressor compresses gas from inlet to final pressure in one pass. As the gas is compressed, its temperature rises substantially — and that hot, dense gas requires more work to compress further than cool gas at the same pressure would. The single-stage machine is fighting against its own heat output.

The central insight of multistage compression with **intercooling** is that you can partially undo this penalty. After the first stage raises gas pressure to an intermediate level, an intercooler (a heat exchanger) removes the heat of compression and returns the gas approximately to the original inlet temperature T₁. The second stage then compresses this cooler, lower-density gas — doing noticeably less work than if it had received the hot discharge from stage one. With more stages and intercoolers, the overall compression path becomes a staircase of isentropic rises and isobaric (constant pressure) coolings, approaching the isothermal limit as the number of stages increases.

The equal-pressure-ratio result follows from an optimization. For two stages with overall pressure ratio r_total = P_final/P_inlet, you choose intermediate pressure P_int to minimize total shaft work. Setting up the work expressions for each polytropic stage and differentiating with respect to P_int, the minimum occurs when P_int/P_inlet = P_final/P_int, meaning each stage handles the square root of the total pressure ratio. For n stages: r_stage = r_total^(1/n). This result assumes equal polytropic efficiency and that each intercooler returns gas to the same inlet temperature — both reasonable approximations for preliminary design. When efficiencies differ or intercooling is incomplete, the optimum shifts, but equal pressure ratios remain a practical starting point.

The engineering benefit compounds with more stages, but with diminishing returns. Two stages dramatically reduce work compared to one; three stages improve further but by less; six stages get very close to isothermal. Industrial gas compressors in air separation plants, natural gas processing, and chemical synthesis commonly use three to six stages. The tradeoffs are hardware cost (each stage and intercooler adds equipment), pressure drop in the intercoolers (which reduces the effective pressure ratio and hurts efficiency), and increased system complexity. The Brayton cycle with intercooling extends this principle to gas turbines, where intercooling reduces compressor work share of the cycle, improving overall thermal efficiency when combined with regeneration.
