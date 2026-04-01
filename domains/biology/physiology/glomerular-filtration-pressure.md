---
id: glomerular-filtration-pressure
title: Glomerular Filtration Pressure and Filtration Rate
domain: biology
course: physiology
prerequisites:
- id: glomerular-filtration-mechanism
  type: hard
builds-toward:
- kidney-tubular-processing-urine
- renal-blood-pressure-regulation
tags:
- glomerular filtration
- GFR
- Starling forces
- autoregulation
- kidney
stage: formal-systems
status: validated
---

# Glomerular Filtration Pressure and Filtration Rate

## Core Idea
Glomerular filtration rate (GFR) is driven by net filtration pressure—the balance of hydrostatic pressure in the glomerulus and oncotic pressure in both the glomerulus and Bowman's space. Autoregulation maintains constant GFR despite blood pressure changes via myogenic and tubuloglomerular feedback mechanisms. Changes in GFR must be matched by reabsorption or excretion to maintain fluid balance.

## Questions

```yaml
- question: "A patient's mean arterial pressure rises substantially due to hypertension, yet their GFR remains largely stable. What mechanism is primarily responsible?"
  type: multiple-choice
  options:
    - "The glomerular capillary membrane becomes less permeable at high pressures, reducing filtration to compensate"
    - "Efferent arteriole dilation reduces downstream resistance, preventing pressure from building in the glomerulus"
    - "Autoregulation via the myogenic response causes the afferent arteriole to constrict when pressure rises, preventing the increase from reaching the glomerulus"
    - "Increased oncotic pressure from higher blood protein concentration counterbalances the elevated hydrostatic pressure"
  answer: 2
  explanation: "The myogenic response is intrinsic to the afferent arteriole smooth muscle: when increased blood pressure stretches the vessel wall, the muscle contracts reflexively, increasing vascular resistance and shielding the glomerulus from the pressure surge. Tubuloglomerular feedback provides a second layer: if GFR briefly rises, more NaCl reaches the macula densa, which signals the afferent arteriole to constrict further. Together these mechanisms maintain GFR across a wide arterial pressure range (~80–180 mmHg). This is essential because even small uncompensated changes in GFR — 180 L/day of filtrate — would devastate fluid balance."

- question: "As blood flows through the glomerular capillary from the afferent to the efferent end, what happens to net filtration pressure along the way?"
  type: multiple-choice
  options:
    - "It remains constant, because the kidney's autoregulatory mechanisms maintain a stable driving force throughout"
    - "It increases, because flow resistance rises as blood becomes more concentrated toward the efferent end"
    - "It decreases, because filtered fluid leaves the blood and concentrates the remaining plasma proteins, raising oncotic pressure and opposing filtration"
    - "It is determined entirely by systemic blood pressure and does not change along the capillary length"
  answer: 2
  explanation: "As blood is filtered along the glomerular capillary, water and small solutes leave but proteins stay behind. The remaining blood becomes progressively more concentrated in protein, raising its oncotic pressure. Since net filtration pressure = glomerular hydrostatic pressure − oncotic pressure − Bowman's capsule pressure, rising oncotic pressure reduces the driving force. By the efferent end, the NFP may approach zero (filtration equilibrium). This declining gradient along the capillary explains why GFR depends so sensitively on the balance of Starling forces."

- question: "Glomerular hydrostatic pressure is higher than in most systemic capillary beds because the glomerulus is positioned between two arterioles, keeping pressure elevated throughout the capillary length."
  type: true-false
  answer: true
  explanation: "True. Most capillaries lie between an arteriole and a venule; pressure drops substantially from the arterial to venous end. The glomerulus instead sits between the afferent arteriole (which delivers pressure) and the efferent arteriole (which maintains resistance and keeps pressure high rather than allowing it to dissipate). This anatomical arrangement sustains glomerular hydrostatic pressure at ~55 mmHg — roughly 1.5–2× typical systemic capillary pressure — maximizing filtration. It is a structural specialization that distinguishes the glomerulus from all other capillary beds."

- question: "Serum creatinine is a useful clinical marker for GFR because creatinine is actively secreted into the tubule at a rate proportional to how much is filtered, making plasma levels directly reflect filtration rate."
  type: true-false
  answer: false
  explanation: "False. Creatinine is useful precisely because it is freely filtered and only minimally secreted — it is not actively secreted in proportion to GFR. Because creatinine passes the glomerular filter freely and is not significantly reabsorbed or secreted, its plasma concentration is inversely proportional to filtration rate: when GFR falls, less creatinine is cleared per unit time, so it accumulates in the blood. If it were actively secreted, the relationship would be confounded. Small amounts of tubular secretion do slightly overestimate actual GFR, which is why cystatin C is sometimes preferred for precise measurement."

- question: "Explain how the tubuloglomerular feedback mechanism works to maintain stable GFR when filtration rate temporarily rises too high."
  type: short-answer
  answer: "When GFR rises above normal, more filtrate flows through the nephron and more NaCl reaches the distal tubule. The macula densa — a cluster of specialized epithelial cells at the junction of the thick ascending limb and distal convoluted tubule — senses the elevated NaCl concentration and flow. It responds by releasing paracrine signals (including ATP and adenosine) that act on the adjacent afferent arteriole, causing it to constrict. Afferent arteriolar constriction increases resistance before the glomerulus, reducing glomerular hydrostatic pressure and thereby lowering GFR back toward the set point. This is a negative feedback loop: high GFR → high tubular NaCl → macula densa signal → afferent constriction → lower GFR."
  explanation: "Tubuloglomerular feedback is a communication between the distal tubule and the same nephron's glomerulus — an elegant intra-nephron feedback loop. Combined with the myogenic response (which reacts to pressure stretch directly), these two mechanisms provide robust autoregulation that operates over seconds to minutes, well before hormonal systems like the renin-angiotensin system engage."
```

## Explainer

From your study of Starling forces in the microcirculation, you know that fluid movement across capillary walls is governed by the balance between hydrostatic pressure (pushing fluid out) and oncotic pressure (pulling fluid back in via plasma proteins). The glomerulus applies this same principle, but with a crucial anatomical twist: it is designed to maximize filtration rather than balance it. **Glomerular hydrostatic pressure** is unusually high — about 55 mmHg, compared to roughly 35 mmHg in most systemic capillaries — because the glomerulus sits between two arterioles (afferent and efferent) rather than between an arteriole and a venule. The efferent arteriole's resistance keeps pressure elevated throughout the entire length of the glomerular capillary.

The **net filtration pressure** (NFP) at any point along the glomerulus equals glomerular hydrostatic pressure minus both the oncotic pressure of glomerular blood and the hydrostatic pressure in Bowman's capsule. At the afferent end, this works out to roughly 55 − 30 − 15 = 10 mmHg favoring filtration. As blood flows through the glomerulus and fluid is filtered out, the protein concentration in the remaining blood rises, increasing oncotic pressure. By the efferent end, oncotic pressure may reach 35 mmHg or more, narrowing the NFP and eventually approaching **filtration equilibrium** — the point where net driving pressure approaches zero. Despite this declining pressure gradient, the enormous surface area and high permeability of the glomerular capillaries produce a GFR of approximately 125 mL/min, or about 180 liters per day.

The kidney cannot afford to let GFR fluctuate with every change in systemic blood pressure — losing even 10% more filtrate than usual would rapidly deplete blood volume. Two **autoregulatory mechanisms** stabilize GFR across a wide range of arterial pressures (roughly 80–180 mmHg). The **myogenic response** is intrinsic to the afferent arteriole: when blood pressure rises and stretches the vessel wall, smooth muscle cells contract reflexively, increasing resistance and preventing the pressure increase from reaching the glomerulus. The **tubuloglomerular feedback** mechanism operates through the macula densa, a cluster of specialized cells in the distal tubule that senses the flow rate and NaCl concentration of the filtrate. If GFR is too high, more NaCl reaches the macula densa, which signals the adjacent afferent arteriole to constrict, reducing glomerular pressure and restoring GFR toward normal.

Understanding GFR is clinically essential because it is the single best measure of overall kidney function. When GFR declines — as in chronic kidney disease — waste products like creatinine accumulate in the blood, and the kidney loses its ability to regulate fluid volume, electrolyte balance, and acid-base status. Clinicians estimate GFR from serum creatinine levels precisely because creatinine is freely filtered at the glomerulus and minimally secreted, making its plasma concentration inversely proportional to filtration rate. A falling GFR is often the first quantitative signal that kidney function is deteriorating.
