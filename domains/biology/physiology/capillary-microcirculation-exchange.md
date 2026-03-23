---
id: capillary-microcirculation-exchange
title: Capillary Microcirculation and Fluid Exchange
domain: biology
course: physiology
prerequisites:
- id: capillary-filtration-and-reabsorption
  type: hard
- id: osmosis-and-tonicity
  type: hard
builds-toward:
- fluid-electrolyte-balance-regulation
- blood-pressure-volume-homeostasis
tags:
- capillary
- microcirculation
- filtration
- reabsorption
- Starling forces
stage: formal-systems
status: draft
---

# Capillary Microcirculation and Fluid Exchange

## Core Idea
Fluid exchange across capillaries follows Starling forces: hydrostatic pressure drives filtration while oncotic pressure opposes it. At the arterial end, hydrostatic pressure exceeds oncotic pressure, promoting filtration; at the venous end, oncotic pressure dominates and fluid is reabsorbed. Lymphatic vessels return excess interstitial fluid, completing the circuit. Disruption of Starling forces leads to edema.

## Questions

```yaml
- question: "At the arteriolar end of a capillary, hydrostatic pressure is 35 mmHg and plasma oncotic pressure is 25 mmHg. At the venular end, hydrostatic pressure has dropped to 15 mmHg while oncotic pressure remains at 25 mmHg. What is the net direction of fluid movement at each end?"
  type: multiple-choice
  options:
    - "Filtration (outward) at both ends, because blood pressure always exceeds oncotic pressure throughout the capillary"
    - "Filtration at the arteriolar end (net +10 mmHg outward) and reabsorption at the venular end (net −10 mmHg inward)"
    - "Reabsorption at the arteriolar end and filtration at the venular end, because high pressure retains fluid"
    - "No net movement at either end because all Starling forces cancel throughout the capillary"
  answer: 1
  explanation: "Net filtration pressure = capillary hydrostatic − plasma oncotic (ignoring the smaller interstitial contributions for this calculation). Arteriolar end: 35 − 25 = +10 mmHg, favoring outward filtration. Venular end: 15 − 25 = −10 mmHg, favoring inward reabsorption. This gradient along the capillary drives the exchange cycle: fluid leaves at the arterial end delivering dissolved nutrients, and returns at the venous end recovering water. Note that overall filtration slightly exceeds reabsorption — the excess ~3 L/day is returned via the lymphatic system."

- question: "A patient with severe liver failure has very low plasma albumin levels. Which form of edema would you predict, and which Starling force is disrupted?"
  type: multiple-choice
  options:
    - "Pulmonary edema from elevated capillary hydrostatic pressure, because the liver regulates arterial blood pressure"
    - "Peripheral edema from reduced plasma oncotic pressure — with less albumin to retain fluid in vessels, filtration exceeds reabsorption throughout the capillary bed"
    - "Lymphatic edema from hepatic obstruction of the thoracic duct drainage pathway"
    - "No edema, because the body compensates by lowering capillary hydrostatic pressure"
  answer: 1
  explanation: "Plasma oncotic pressure is generated primarily by albumin, synthesized by the liver. In liver failure, albumin production drops, reducing the oncotic force that opposes filtration and drives reabsorption at the venular end. The Starling balance tips toward net filtration throughout the capillary bed, and fluid accumulates in the interstitium faster than lymphatics can drain it. This is why ascites (peritoneal fluid accumulation) and peripheral edema are classic signs of liver failure. Pulmonary edema (option A) results from elevated capillary hydrostatic pressure — as in left heart failure where venous congestion backs up into pulmonary capillaries, a completely different Starling force."

- question: "The Starling model predicts that filtration at the arteriolar end is exactly balanced by reabsorption at the venular end, leaving no net fluid accumulation in the interstitium under normal conditions."
  type: true-false
  answer: false
  explanation: "In reality, filtration slightly exceeds reabsorption — approximately 3 liters per day of excess fluid accumulates in the interstitial space even under normal physiological conditions. This is why the lymphatic system is essential: lymphatic capillaries collect this excess fluid (now called lymph) along with any leaked plasma proteins and return it to the venous circulation via the thoracic duct. Without lymphatic drainage, even normal capillary function would produce progressive interstitial fluid accumulation. The Starling model describes the forces and their direction along the capillary, but the net balance slightly favors filtration."

- question: "In congestive heart failure, blood backs up in the venous circulation because the failing heart cannot pump it forward efficiently. This elevated venous pressure would be expected to contribute to edema formation."
  type: true-false
  answer: true
  explanation: "Elevated venous pressure transmits backward into the venular end of capillaries, raising capillary hydrostatic pressure throughout the capillary bed. This shifts the Starling balance — filtration increases and reabsorption decreases, producing net fluid accumulation in the interstitium that overwhelms lymphatic capacity. In left heart failure, pulmonary venous pressure rises and pulmonary edema results; in right heart failure or biventricular failure, systemic venous pressure rises and peripheral or abdominal (ascitic) edema results. Each case is the same mechanism: elevated hydrostatic pressure shifting Starling forces toward net filtration."

- question: "Explain the role of plasma oncotic pressure in Starling's model. Why do plasma proteins generate this force while small dissolved solutes do not?"
  type: short-answer
  answer: "Plasma oncotic pressure (colloid osmotic pressure) is an osmotic force generated by large plasma proteins — primarily albumin — that are too large to freely cross the capillary wall. Because they are retained inside the vessel while water and small solutes can exit, they create an osmotic gradient that draws water back into the capillary, opposing outward filtration and driving reabsorption at the venular end. Small solutes (glucose, sodium, chloride) do not generate significant oncotic pressure because they equilibrate freely across the capillary wall — they quickly reach the same concentration on both sides and create no lasting osmotic gradient. Only molecules selectively retained on one side of the membrane create an effective osmotic force."
  explanation: "When plasma protein levels fall — in malnutrition (kwashiorkor), liver disease, or protein-losing nephropathy — oncotic pressure drops and the reabsorptive force is reduced throughout the capillary bed. Net filtration exceeds lymphatic return capacity, producing edema. This distinction between oncotic (colloid) and crystalloid osmotic pressure matters clinically: infusing saline expands volume transiently but distributes throughout extracellular fluid without restoring oncotic pressure, while albumin infusion directly raises the reabsorptive force. The mechanism follows directly from which molecules can and cannot cross the capillary wall."
```

## Explainer

You already understand from your work on osmosis and tonicity that water moves across semipermeable membranes toward regions of higher solute concentration. And from capillary filtration and reabsorption, you know that capillary walls allow passage of water and small solutes but retain large plasma proteins. The question now is: what determines how much fluid leaves the blood, how much returns, and what happens when the balance goes wrong?

The answer lies in **Starling forces** — four pressures that act across the capillary wall. Two push fluid out of the capillary (filtration), and two push fluid back in (reabsorption). **Capillary hydrostatic pressure** (the blood pressure inside the capillary) pushes fluid outward through gaps between endothelial cells. Opposing this is **plasma oncotic pressure** (also called colloid osmotic pressure), generated by plasma proteins — especially albumin — that are too large to cross the capillary wall, so they osmotically hold water inside the vessel. On the interstitial side, **interstitial hydrostatic pressure** (usually near zero or slightly negative) and **interstitial oncotic pressure** (from small amounts of leaked protein) provide smaller, secondary contributions. The net filtration at any point equals the balance of all four forces.

The classic model describes a gradient along the length of the capillary. At the **arteriolar end**, capillary hydrostatic pressure is relatively high (~35 mmHg), exceeding the opposing oncotic pressure (~25 mmHg), so the net force favors filtration — fluid moves out into the tissue, delivering oxygen and nutrients dissolved in plasma. As blood flows toward the **venular end**, hydrostatic pressure drops (~15 mmHg) because of resistance along the capillary, but oncotic pressure remains nearly constant (protein concentration actually rises slightly as water leaves). Now oncotic pressure exceeds hydrostatic pressure, and fluid is reabsorbed back into the capillary. This creates a continuous cycle of outward flow at one end and inward flow at the other, bathing tissues in fresh interstitial fluid.

However, filtration slightly exceeds reabsorption overall — roughly 3 liters per day of excess fluid accumulates in the interstitial space. This is where the **lymphatic system** becomes essential. Lymphatic capillaries — blind-ended, highly permeable vessels — collect this excess fluid (now called lymph) along with any leaked proteins and return it to the venous circulation via the thoracic duct. Without lymphatic drainage, fluid would progressively accumulate in the tissues. This is exactly what happens in **edema**, which can result from elevated capillary hydrostatic pressure (as in heart failure, where venous congestion backs up into capillaries), reduced plasma oncotic pressure (as in liver disease or malnutrition, where albumin production drops), increased capillary permeability (as in burns or inflammation, where proteins leak out), or lymphatic obstruction (as in parasitic infections or after lymph node removal). Each cause disrupts a different Starling force, but all produce the same result: net fluid accumulation in the interstitial space.
