---
id: buffer-solutions
title: Buffer Solutions
domain: chemistry
course: general-chemistry
prerequisites:
- id: acid-base-chemistry
  type: hard
- id: chemical-equilibrium
  type: hard
- id: logarithms-intro
  type: hard
builds-toward:
- ph-and-acid-base-calculations
tags:
- Henderson-Hasselbalch
- buffer-capacity
- conjugate-pair
- buffer-preparation
- buffer-range
stage: abstract-reasoning
status: draft
---
# Buffer Solutions

## Core Idea
A buffer solution resists changes in pH when small amounts of acid or base are added. Buffers consist of a weak acid and its conjugate base (or a weak base and its conjugate acid) in appreciable concentrations. The Henderson-Hasselbalch equation, pH = pKa + log([A⁻]/[HA]), provides a direct way to calculate buffer pH. Buffer capacity — the amount of acid or base a buffer can absorb before significant pH change — depends on the total concentration of the conjugate pair and is greatest when [A⁻] ≈ [HA] (pH ≈ pKa). Effective buffering typically occurs within ±1 pH unit of the pKa.

## How It's Best Learned
Prepare buffer problems in two steps: first use stoichiometry to determine how added strong acid or base converts one buffer component to the other, then apply Henderson-Hasselbalch to the new ratio. Practice choosing appropriate conjugate pairs for a target pH by matching pKa values.

## Common Misconceptions
- Diluting a buffer changes its capacity (fewer moles to absorb acid/base) but does not significantly change its pH, because the ratio [A⁻]/[HA] remains the same.
- A buffer cannot resist unlimited acid or base. Once the limiting component is consumed, the solution loses its buffering ability and pH changes rapidly.

## Explainer

You already know that weak acids only partially dissociate in water, establishing an equilibrium between HA and its conjugate base A⁻. A **buffer solution** exploits this equilibrium by having substantial amounts of both HA and A⁻ present simultaneously. When you add a small amount of strong acid to the solution, the extra H⁺ ions react with A⁻ to form HA — converting one buffer component into the other rather than allowing H⁺ to accumulate freely and crash the pH. When you add strong base, the OH⁻ reacts with HA to produce A⁻ and water. In both cases, the equilibrium absorbs the disturbance, and the pH barely moves.

The **Henderson-Hasselbalch equation** — pH = pKa + log([A⁻]/[HA]) — gives you direct quantitative control. Since pH depends on the logarithm of the ratio [A⁻]/[HA], the pH is determined primarily by which component is in excess and by how much. When [A⁻] = [HA], the log term is zero and pH equals pKa exactly. This is the sweet spot: the buffer is equally prepared to absorb added acid or added base. As the ratio shifts toward 10:1 in either direction (±1 pH unit from pKa), the buffer approaches its limits. Beyond that range, one component is nearly exhausted and the buffer fails.

To solve buffer problems, work in two stages. First, treat the addition of strong acid or base as a **stoichiometric** problem: the strong acid converts A⁻ to HA mole-for-mole, or the strong base converts HA to A⁻ mole-for-mole. Calculate the new moles of each component after this reaction. Second, plug the new ratio into Henderson-Hasselbalch to find the resulting pH. This two-step approach — stoichiometry first, then equilibrium — prevents the common error of trying to apply the equilibrium equation to a system that has not yet been updated for the added reagent.

**Buffer capacity** measures how much acid or base the buffer can absorb before its pH changes significantly. It depends on the total concentration of the conjugate pair: a buffer made from 1.0 M acetic acid and 1.0 M sodium acetate can absorb far more HCl than a buffer at 0.01 M of each, even though both have the same pH. Diluting a buffer does not change the ratio [A⁻]/[HA] and therefore barely affects pH, but it does reduce capacity because there are fewer moles available to neutralize added acid or base. Choosing a buffer for a practical application means matching the pKa to the target pH and ensuring enough total concentration to handle the expected acid-base load.
