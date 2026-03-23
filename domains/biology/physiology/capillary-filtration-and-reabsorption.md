---
id: capillary-filtration-and-reabsorption
title: Capillary Filtration and Fluid Reabsorption (Starling Equation)
domain: biology
course: physiology
prerequisites:
- id: blood-composition-and-function
  type: hard
- id: osmosis-and-water-movement
  type: hard
builds-toward:
- renal-physiology-and-fluid-balance
tags:
- filtration
- oncotic-pressure
- edema
stage: formal-systems
status: validated
---

# Capillary Filtration and Fluid Reabsorption (Starling Equation)

## Core Idea
Fluid continuously moves between the capillary lumen and tissue interstitium, driven by the balance of hydrostatic and oncotic pressures described by Starling's equation. In health, this maintains tissue fluid balance; imbalance leads to edema (when capillary hydrostatic pressure or vascular permeability rises) or dehydration.

## How It's Best Learned
Calculate net filtration pressure using typical values for hydrostatic and oncotic pressures in arteriolar and venular ends of capillaries. Apply Starling's equation to clinical scenarios like liver disease, malnutrition, and inflammation.

## Questions

```yaml
- question: "A patient with severe liver cirrhosis develops significant abdominal edema (ascites). Which Starling mechanism best explains this finding?"
  type: multiple-choice
  options:
    - "Elevated capillary hydrostatic pressure, because liver scarring blocks venous return and raises venous pressure throughout the body."
    - "Reduced plasma oncotic pressure, because the damaged liver produces less albumin, weakening the inward pull that returns fluid to capillaries."
    - "Increased capillary permeability, because liver inflammation releases histamine into the systemic circulation."
    - "Reduced interstitial hydrostatic pressure, because liver scarring compresses the lymphatic vessels."
  answer: 1
  explanation: "The liver synthesizes albumin, the primary plasma protein responsible for oncotic pressure. When the liver is severely damaged, albumin synthesis falls and plasma protein concentration drops. With reduced oncotic pressure (the inward pull), the balance shifts toward net filtration — more fluid leaves the capillaries than is reabsorbed. This case illustrates why identifying which term in the Starling equation is disrupted is essential to understanding the mechanism of edema; different etiologies require different treatments."

- question: "Moving from the arteriolar end to the venular end of a capillary, why does the dominant process shift from filtration to reabsorption?"
  type: multiple-choice
  options:
    - "Blood velocity slows at the venular end, giving oncotic pressure more time to act."
    - "Capillary hydrostatic pressure falls as fluid is lost and resistance dissipates, while oncotic pressure stays roughly constant. This reverses the net balance."
    - "The capillary wall at the venular end is more permeable to proteins, allowing albumin to enter the interstitium and pull fluid back."
    - "Lymphatic vessels at the venular end actively pump fluid back into the capillary."
  answer: 1
  explanation: "At the arteriolar end, hydrostatic pressure (~35 mmHg) exceeds oncotic pressure (~25 mmHg), so net pressure pushes fluid out. As blood flows through the capillary, it loses fluid — lowering hydrostatic pressure to ~15 mmHg at the venular end — while the remaining plasma proteins become slightly more concentrated, keeping oncotic pressure roughly constant. Now oncotic pressure exceeds hydrostatic pressure, and the net force pulls fluid back in. This mechanism returns most filtered fluid to the circulation, with only a small residual collected by lymphatics."

- question: "In a person with severe malnutrition and low plasma protein levels, edema develops because the body cannot generate enough oncotic pressure to pull filtered fluid back into capillaries."
  type: true-false
  answer: true
  explanation: "Plasma oncotic pressure depends primarily on albumin concentration. Severe malnutrition reduces dietary protein intake, impairing albumin synthesis. With low oncotic pressure, the inward force at the venular end is insufficient to match even normal hydrostatic pressure. Net filtration exceeds reabsorption throughout the capillary bed, and excess fluid accumulates in the interstitium. This is the physiological basis of the characteristic edema seen in protein-deficiency malnutrition (kwashiorkor)."

- question: "Under normal physiological conditions, capillary hydrostatic pressure is approximately the same at both the arteriolar and venular ends of the capillary."
  type: true-false
  answer: false
  explanation: "Hydrostatic pressure drops significantly along the capillary length — from roughly 35 mmHg at the arteriolar end to about 15 mmHg at the venular end. This pressure drop occurs because fluid is continuously being pushed out through filtration, and because resistance along the capillary dissipates the driving pressure. This decline is precisely what reverses the net Starling force from filtration to reabsorption as blood travels toward the venular end."

- question: "Why does the Starling equation require two opposing pressure types (hydrostatic and oncotic) rather than just one driving force for capillary fluid exchange?"
  type: short-answer
  answer: "Hydrostatic pressure alone would push all fluid out of the capillaries into the tissues, causing massive edema and depleting the vascular volume. Oncotic pressure — the osmotic pull of plasma proteins too large to leave the capillary — provides the counterforce that pulls fluid back in. The interplay between the two, varying along the capillary's length, creates a controlled exchange: filtration at the arteriolar end delivers nutrients to tissues, and reabsorption at the venular end recovers the fluid."
  explanation: "The two-force system is what makes capillary exchange precise rather than all-or-nothing. A single driving force would saturate in one direction; the balance between hydrostatic push and oncotic pull creates a tunable equilibrium that varies in space and shifts in response to physiological conditions. This also explains why each type of edema requires different treatment: heart failure edema (high hydrostatic) is treated by reducing fluid overload, while hypoalbuminemia edema requires protein replacement."
```

## Explainer

You already understand that blood is a complex fluid containing plasma proteins, cells, and dissolved solutes, and that water moves by osmosis from regions of low solute concentration to regions of high solute concentration. At the capillary level, these principles govern a continuous exchange of fluid between the blood and the surrounding tissues — a process that delivers nutrients, removes waste, and maintains tissue fluid balance every second of your life.

Two opposing forces drive fluid movement across the capillary wall. **Hydrostatic pressure** is the physical pressure of blood pushing outward against the capillary wall, which tends to force fluid out of the capillary into the interstitial space. **Oncotic pressure** (also called colloid osmotic pressure) is the osmotic pull exerted by plasma proteins — primarily albumin — that are too large to cross the capillary wall, and this force tends to pull fluid back into the capillary. The **Starling equation** formalizes this balance: net filtration pressure equals the difference between hydrostatic pressures (capillary minus interstitial) minus the difference between oncotic pressures (capillary minus interstitial). When the net pressure is positive, fluid filters out; when negative, fluid is reabsorbed.

In a typical capillary, pressures shift along its length. At the **arteriolar end**, capillary hydrostatic pressure is relatively high (around 35 mmHg) because blood has just arrived from the arteriole. This exceeds the inward oncotic pull (~25 mmHg), so the net force pushes fluid out — filtration dominates. As blood flows toward the **venular end**, hydrostatic pressure drops (to about 15 mmHg) because fluid has been lost and resistance has dissipated, while oncotic pressure stays roughly constant (plasma proteins are concentrated by the fluid loss). Now oncotic pressure exceeds hydrostatic pressure, and fluid is pulled back in — reabsorption dominates. The result is that most of the filtered fluid returns to the capillary, and the small excess is collected by the lymphatic system.

When this balance is disrupted, the clinical consequence is **edema** — excess fluid accumulation in the interstitial space. Consider the mechanisms: if capillary hydrostatic pressure rises (as in heart failure, where venous congestion backs up into capillaries), more fluid is pushed out than can be reabsorbed. If plasma oncotic pressure falls (as in liver disease or malnutrition, where albumin synthesis drops), the inward pull weakens and fluid leaks out. If capillary permeability increases (as in inflammation or burns, where histamine and other mediators widen the gaps between endothelial cells), proteins escape into the interstitium, reducing the oncotic gradient. Each of these scenarios disrupts a different term in the Starling equation, but all produce the same result: fluid accumulates where it should not, and tissues swell.
