---
id: microvascular-exchange-and-fluid-balance
title: Microvascular Exchange and Fluid Balance
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: vascular-physiology-and-hemodynamics
  type: hard
- id: fluid-balance-and-electrolytes
  type: hard
builds-toward:
- edema-and-fluid-disorders
tags:
- capillary-exchange
- starling-forces
- transcapillary
- oncotic-pressure
stage: formal-systems
status: draft
---

# Microvascular Exchange and Fluid Balance

## Core Idea
Fluid exchange across capillary walls is governed by Starling forces: the balance between hydrostatic pressure (pushing fluid out) and oncotic pressure (pulling fluid in). Arteriolar hydrostatic pressure typically exceeds plasma oncotic pressure, promoting filtration; venous hydrostatic pressure drops below oncotic pressure, promoting reabsorption. Lymphatic return of filtered fluid completes the circuit.

## How It's Best Learned
Calculate net filtration pressure using measured values from different capillary beds. Consider how edema develops when any Starling force becomes abnormal.

## Common Misconceptions
- Assuming all filtered fluid is reabsorbed at the venous end; approximately 10% is normally returned by lymphatics.
- Thinking edema only forms when capillary hydrostatic pressure is high; edema also forms with low plasma proteins or lymphatic obstruction.

## Questions

```yaml
- question: "A patient with severe liver cirrhosis develops widespread edema and ascites. Their capillary hydrostatic pressure is measured as normal. The Starling force most responsible for their edema is:"
  type: multiple-choice
  options:
    - "Elevated capillary hydrostatic pressure from portal venous congestion"
    - "Elevated interstitial oncotic pressure from inflammatory protein leakage"
    - "Reduced plasma oncotic pressure from decreased albumin synthesis by the damaged liver"
    - "Lymphatic obstruction caused by liver fibrosis compressing the thoracic duct"
  answer: 2
  explanation: "The liver is the primary site of albumin synthesis. In cirrhosis, hepatocyte destruction reduces albumin production, lowering plasma protein concentration and therefore plasma oncotic pressure (πc). With reduced πc, the inward osmotic force that opposes filtration at the venular end is diminished — fluid that would normally be reabsorbed instead remains in the interstitium. This is why the edema of liver disease and malnutrition (kwashiorkor) can occur even with normal capillary hydrostatic pressure. The Starling equation makes the mechanism explicit: reduced πc means the (πc − πi) term shrinks, shifting net filtration pressure toward outward flow throughout the capillary bed."

- question: "At the venular end of a systemic capillary, which force configuration produces net fluid reabsorption?"
  type: multiple-choice
  options:
    - "Capillary hydrostatic pressure (~35 mmHg) exceeds plasma oncotic pressure (~28 mmHg)"
    - "Interstitial hydrostatic pressure rises above plasma oncotic pressure, forcing fluid inward"
    - "Plasma oncotic pressure (~28 mmHg) exceeds the now-reduced capillary hydrostatic pressure (~15 mmHg), creating net inward osmotic pull"
    - "Lymphatic drainage reduces interstitial pressure enough to pull fluid back into the capillary"
  answer: 2
  explanation: "As blood travels from the arteriolar to the venular end, capillary hydrostatic pressure falls from ~35 mmHg to ~15 mmHg as energy is dissipated. Plasma oncotic pressure remains roughly constant at ~25–28 mmHg throughout (proteins don't leave the capillary in large amounts under normal conditions). At the venular end, the hydrostatic outward force (~15 mmHg) is now less than the oncotic inward force (~28 mmHg), so net flow reverses and fluid is reabsorbed. This is the classic textbook depiction of Starling equilibrium, though in reality the system is slightly net-filtration and lymphatics return the remainder."

- question: "In normal physiology, approximately 10% of the fluid filtered from capillaries at the arteriolar end is not reabsorbed at the venular end and must be returned to circulation by the lymphatic system."
  type: true-false
  answer: true
  explanation: "The capillary exchange system is not perfectly balanced — net filtration slightly exceeds net reabsorption over the length of a typical capillary. Approximately 2–4 liters of fluid per day escapes into the interstitium and is not recaptured at the venular end. The lymphatic system collects this excess, along with small amounts of plasma protein that leak through capillary walls, and returns them to the venous circulation via the thoracic duct. This makes lymphatics an essential component of fluid homeostasis, not a backup system. Lymphatic obstruction (filariasis, lymph node dissection) causes severe edema — lymphedema — even when all four Starling forces are completely normal."

- question: "All fluid filtered from capillaries at the arteriolar end is reabsorbed at the venular end, meaning the lymphatic system is only needed when Starling forces are abnormal."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about microvascular exchange. Under normal conditions, approximately 90% of filtered fluid is reabsorbed at the venular end, but the remaining ~10% (2–4 liters per day) requires lymphatic return. The lymphatic system is not a reserve mechanism — it is continuously active in normal physiology, draining excess fluid and the plasma proteins that leak through capillary walls. If lymphatics are blocked, fluid accumulates even when capillary hydrostatic and oncotic pressures are entirely normal. This explains why lymphedema is such a severe and chronic condition."

- question: "Using the Starling forces framework, explain how lymphatic obstruction leads to edema even when capillary hydrostatic and oncotic pressures are normal."
  type: short-answer
  answer: "Under normal conditions, Starling forces produce slight net filtration — slightly more fluid leaves capillaries than is reabsorbed at the venular end. The lymphatic system continuously drains this excess (~10% of filtered fluid) and returns it to circulation. When lymphatics are obstructed, this drainage stops. Filtered fluid accumulates in the interstitium, raising interstitial hydrostatic pressure (Pi). As Pi rises, it increases the outward-opposing force and simultaneously elevates interstitial oncotic pressure (πi) as leaked proteins concentrate. Even though capillary hydrostatic and plasma oncotic pressures are normal, the interstitial compartment fills because the normal lymphatic outflow is blocked."
  explanation: "This answer demonstrates understanding of the four-force system as a dynamic equilibrium, not a static balance. The lymphatics are part of the normal steady state — the Starling equilibrium assumes their function. Removing lymphatic drainage is equivalent to adding a fourth force abnormality: interstitial pressure rises until a new (pathological) steady state is reached with a swollen interstitium. Filariasis, in which parasitic worms block lymphatic vessels, produces elephantiasis through exactly this mechanism. Cancer treatment involving lymph node dissection produces the same result in the affected limb."
```

## Explainer

From your study of vascular physiology, you know that blood moves through the circulatory system because of pressure gradients, and that arterioles control blood pressure by adjusting their resistance. When blood reaches the capillaries — the thin-walled exchange vessels you learned about in vessel structure — the pressure is still positive but much lower than in the arterioles. At this interface, a different physics takes over: instead of bulk flow through tubes, the question is whether fluid crosses the capillary wall into the surrounding interstitium. That exchange is governed by four competing pressures collectively called **Starling forces**.

Two forces push fluid *out* of the capillary: **capillary hydrostatic pressure (Pc)**, the blood pressure at that location (~35 mmHg at the arteriolar end, ~15 mmHg at the venular end), and **interstitial oncotic pressure (πi)**, created by the small amount of protein that leaks into the interstitium (~3–5 mmHg). Two forces pull fluid *in*: **plasma oncotic pressure (πc)**, the osmotic pressure exerted by plasma proteins, mainly albumin (~25–28 mmHg), and **interstitial hydrostatic pressure (Pi)**, which is slightly negative in most tissues because lymphatics drain fluid away. The **net filtration pressure** equals (Pc − Pi) − (πc − πi). At the arteriolar end, the high hydrostatic pressure wins and fluid is filtered outward. At the venular end, hydrostatic pressure has fallen and oncotic pressure dominates, pulling fluid back in.

This is not a perfectly balanced system. Roughly 10% of the filtered fluid — about 2–4 liters per day — is not reabsorbed at the venous end. The **lymphatic system** collects this excess, along with the small amount of plasma protein that leaks through, and returns it to the circulation via the thoracic duct. Lymphatics are the sanitation system of the interstitium. If they are blocked — as occurs in filariasis or after lymph node dissection — fluid accumulates as the severe swelling called **lymphedema**.

Understanding these four forces explains every common form of **edema**. Heart failure raises venous (and therefore capillary) hydrostatic pressure on the venous side, flooding the interstitium faster than it can be drained — the mechanism behind pulmonary edema and dependent ankle swelling. Liver cirrhosis and malnutrition reduce plasma albumin, dropping πc and eliminating the inward pull — the mechanism behind ascites and the edema of kwashiorkor. Inflammation increases capillary permeability, allowing proteins to leak into the interstitium and raise πi, further drawing fluid out. Each pathological state maps onto one or more Starling forces gone wrong, and the four-force framework gives you a systematic way to reason through all of them.
