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
stage: formal-systems
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

## Questions

```yaml
- question: "A student prepares a buffer from 0.50 M acetic acid and 0.50 M sodium acetate (pKa = 4.74), then dilutes the entire solution to twice its volume with pure water. What happens to the pH and the buffer capacity?"
  type: multiple-choice
  options:
    - "pH increases and capacity stays the same, because dilution increases the proportion of the basic acetate component"
    - "pH stays approximately the same but capacity decreases, because the [A⁻]/[HA] ratio is unchanged but fewer total moles of conjugate pair remain"
    - "pH decreases because dilution shifts the acid-base equilibrium toward greater dissociation of HA"
    - "Both pH and capacity remain exactly the same because a buffer resists all changes, including dilution with water"
  answer: 1
  explanation: "Henderson-Hasselbalch shows pH depends on the logarithm of [A⁻]/[HA]. Diluting both components by the same factor leaves their ratio unchanged, so the log term is unchanged and pH barely moves. Buffer capacity, however, depends on the total moles of conjugate pair available to absorb acid or base — with half as many moles, the buffer exhausts faster. Dilution preserves pH but reduces capacity. Option 3 is the dangerous misconception: buffers resist pH changes from added acid or base, not changes in the number of available moles."

- question: "When a small amount of hydrochloric acid is added to a buffer containing acetic acid (HA) and acetate (A⁻), what prevents the pH from dropping sharply?"
  type: multiple-choice
  options:
    - "The acetic acid reacts with the added H⁺ to regenerate water and acetate, consuming the acid"
    - "The buffer dilutes the added H⁺ across the large solution volume, reducing its effective concentration"
    - "The acetate (A⁻) reacts with the added H⁺ to form acetic acid (HA), neutralizing the free proton before it can lower pH"
    - "Both HA and A⁻ react proportionally with H⁺, maintaining the ratio between them"
  answer: 2
  explanation: "The acetate ion is the basic component of the buffer. When H⁺ is added, A⁻ captures it: A⁻ + H⁺ → HA. This converts one buffer component into the other without allowing free H⁺ to accumulate. The ratio [A⁻]/[HA] shifts slightly (less A⁻, more HA), which nudges pH slightly per Henderson-Hasselbalch — but the change is far smaller than adding H⁺ to pure water. Option 0 is wrong because HA does not react with additional H⁺; it is the A⁻ (conjugate base) that acts as the proton acceptor."

- question: "A buffer solution can resist any amount of added acid or base indefinitely, as long as the solution's pH stays within one unit of the pKa."
  type: true-false
  answer: false
  explanation: "Buffers have finite capacity. When the limiting component (either A⁻ or HA) is consumed by added acid or base, buffering fails and pH changes sharply — just as it would in an unbuffered solution. A buffer containing 0.01 mol each of HA and A⁻ is exhausted by 0.01 mol of added strong acid. The ±1 pH unit range describes the effective operating window under normal conditions, not a guarantee of unlimited resistance. 'Buffer capacity' is a finite quantity that depends on total moles of conjugate pair."

- question: "Diluting a buffer solution with water does not significantly change its pH because the Henderson-Hasselbalch equation depends on the ratio [A⁻]/[HA], which remains constant upon dilution."
  type: true-false
  answer: true
  explanation: "Diluting multiplies both [A⁻] and [HA] by the same factor, leaving their ratio — and therefore the log term in Henderson-Hasselbalch — unchanged. pH stays essentially the same. (A very small second-order effect from changing ionic strength exists but is negligible for most purposes.) This is why standard pH buffers used to calibrate electrodes remain reliable even after minor dilution. Buffer capacity, by contrast, is proportionally reduced — fewer moles are available to neutralize added acid or base."

- question: "Why is buffer capacity maximized when [A⁻] = [HA], and what is the pH at that point?"
  type: short-answer
  answer: "When [A⁻] = [HA], the buffer holds equal reserves of both components — equal ability to absorb added acid (converting A⁻ to HA) or added base (converting HA to A⁻). Neither component is limiting, giving the greatest resistance to disturbance in either direction. At this 1:1 ratio, log([A⁻]/[HA]) = log(1) = 0, so pH = pKa exactly."
  explanation: "As the ratio moves away from 1:1 — say to 10:1 or 1:10 — one component becomes the minority. A buffer at [A⁻]/[HA] = 10:1 has ample capacity to absorb added acid (plenty of A⁻) but little capacity to absorb added base (small HA reserve). Maximum capacity in both directions simultaneously requires the 1:1 ratio. This is the practical reason for choosing a weak acid with pKa close to the target pH: it lets you prepare near the 1:1 ratio and operate at maximum capacity."
```

## Explainer

You already know that weak acids only partially dissociate in water, establishing an equilibrium between HA and its conjugate base A⁻. A **buffer solution** exploits this equilibrium by having substantial amounts of both HA and A⁻ present simultaneously. When you add a small amount of strong acid to the solution, the extra H⁺ ions react with A⁻ to form HA — converting one buffer component into the other rather than allowing H⁺ to accumulate freely and crash the pH. When you add strong base, the OH⁻ reacts with HA to produce A⁻ and water. In both cases, the equilibrium absorbs the disturbance, and the pH barely moves.

The **Henderson-Hasselbalch equation** — pH = pKa + log([A⁻]/[HA]) — gives you direct quantitative control. Since pH depends on the logarithm of the ratio [A⁻]/[HA], the pH is determined primarily by which component is in excess and by how much. When [A⁻] = [HA], the log term is zero and pH equals pKa exactly. This is the sweet spot: the buffer is equally prepared to absorb added acid or added base. As the ratio shifts toward 10:1 in either direction (±1 pH unit from pKa), the buffer approaches its limits. Beyond that range, one component is nearly exhausted and the buffer fails.

To solve buffer problems, work in two stages. First, treat the addition of strong acid or base as a **stoichiometric** problem: the strong acid converts A⁻ to HA mole-for-mole, or the strong base converts HA to A⁻ mole-for-mole. Calculate the new moles of each component after this reaction. Second, plug the new ratio into Henderson-Hasselbalch to find the resulting pH. This two-step approach — stoichiometry first, then equilibrium — prevents the common error of trying to apply the equilibrium equation to a system that has not yet been updated for the added reagent.

**Buffer capacity** measures how much acid or base the buffer can absorb before its pH changes significantly. It depends on the total concentration of the conjugate pair: a buffer made from 1.0 M acetic acid and 1.0 M sodium acetate can absorb far more HCl than a buffer at 0.01 M of each, even though both have the same pH. Diluting a buffer does not change the ratio [A⁻]/[HA] and therefore barely affects pH, but it does reduce capacity because there are fewer moles available to neutralize added acid or base. Choosing a buffer for a practical application means matching the pKa to the target pH and ensuring enough total concentration to handle the expected acid-base load.
