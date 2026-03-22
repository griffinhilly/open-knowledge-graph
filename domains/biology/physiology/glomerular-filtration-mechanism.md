---
id: glomerular-filtration-mechanism
title: Glomerular Filtration and Filtration Rate Regulation
domain: biology
course: physiology
prerequisites:
- id: renal-physiology-and-fluid-balance
  type: hard
- id: capillary-filtration-and-reabsorption
  type: soft
builds-toward:
- proximal-tubule-reabsorption-secretion
tags:
- gfr
- ultrafiltration
- afferent-efferent-arterioles
stage: advanced
status: draft
---

# Glomerular Filtration and Filtration Rate Regulation

## Core Idea
Glomerular filtration begins with ultrafiltration of plasma across the three-layer glomerular filtration barrier (fenestrated endothelium, basement membrane, and podocyte slit diaphragms), driven by the Starling pressure gradient and determined by glomerular filtration rate (GFR, ~120 mL/min). Regulation of afferent and efferent arteriolar resistance adjusts GFR to maintain body fluid composition.

## Questions

```yaml
- question: "A drug that moderately constricts only the efferent arteriole is administered. What effect does this have on GFR, and why?"
  type: multiple-choice
  options:
    - "GFR decreases because the drug reduces total blood flow through the glomerulus"
    - "GFR increases because outflow resistance raises glomerular capillary hydrostatic pressure"
    - "GFR is unchanged because the kidney's autoregulation fully compensates"
    - "GFR decreases because Bowman's capsule pressure rises to match the elevated capillary pressure"
  answer: 1
  explanation: "Moderate efferent arteriole constriction impedes outflow while blood still enters through the afferent arteriole, backing up pressure in the glomerular capillaries. This elevated hydrostatic pressure increases the net filtration pressure and raises GFR. The common misconception is that constricting any vessel downstream must reduce GFR — but the unique dual-arteriole architecture means efferent resistance specifically raises intraglomerular pressure rather than simply cutting flow. (Severe constriction eventually reduces GFR by cutting total flow, but moderate constriction increases it.)"

- question: "What makes the glomerular capillary bed structurally unique compared to most systemic capillary beds?"
  type: multiple-choice
  options:
    - "It is surrounded by a porous membrane that lacks the standard three-layer filtration barrier"
    - "It is positioned between two arterioles — the afferent and efferent — rather than between an arteriole and a venule"
    - "It operates at unusually low hydrostatic pressure to prevent excessive protein loss"
    - "It lacks oncotic pressure because plasma proteins freely cross the filtration barrier"
  answer: 1
  explanation: "In most capillary beds, blood flows from arteriole → capillary → venule. The glomerulus is sandwiched between two arterioles: the afferent (inflow) and efferent (outflow). This architecture allows the kidney to independently regulate pressure within the glomerular capillaries by adjusting resistance at either end, enabling fine-tuned control of GFR that would be impossible with a single downstream venule."

- question: "Constricting the afferent arteriole increases GFR by raising glomerular capillary hydrostatic pressure."
  type: true-false
  answer: false
  explanation: "Afferent arteriole constriction reduces blood flow into the glomerulus, lowering glomerular capillary hydrostatic pressure and therefore decreasing GFR — the opposite effect. This is what happens during sympathetic activation in severe hemorrhage: the body diverts blood away from the kidneys by constricting the afferent arteriole. Efferent constriction (not afferent) is what raises intraglomerular pressure."

- question: "Albumin is nearly absent from the glomerular filtrate partly because the negatively charged proteoglycans in the glomerular basement membrane repel it, not just because of albumin's large molecular size."
  type: true-false
  answer: true
  explanation: "The glomerular filtration barrier uses two selection principles: size and charge. The glomerular basement membrane contains negatively charged proteoglycans that electrostatically repel negatively charged molecules like albumin. In conditions that damage this charge barrier (e.g., minimal change disease), significant albumin appears in the urine even though albumin's size hasn't changed. Both the physical size filter and the electrostatic charge barrier must be intact for effective filtration."

- question: "During severe hemorrhage, GFR falls sharply. Using the concept of arteriolar resistance, explain the two mechanisms responsible for this drop."
  type: short-answer
  answer: "First, sympathetic nervous system activation causes afferent arteriole constriction, reducing blood flow into the glomerulus and lowering glomerular capillary hydrostatic pressure — directly reducing net filtration pressure and GFR. Second, systemic blood pressure itself falls due to hemorrhage, which also reduces the pressure driving blood into the glomerulus. Together, these two mechanisms — neural afferent constriction and reduced perfusion pressure — drastically lower GFR, conserving what little fluid remains in circulation."
  explanation: "Understanding this requires seeing GFR as directly dependent on glomerular capillary hydrostatic pressure, which is itself governed by (1) the pressure of blood arriving from the systemic circulation and (2) the resistance of the afferent arteriole regulating how much of that pressure reaches the glomerulus. Sympathetic activation is an active protective mechanism — it deliberately sacrifices renal filtration to preserve blood pressure in vital organs."
```

## Explainer

From your study of renal physiology and capillary filtration, you know that the kidneys filter blood to regulate fluid balance and eliminate waste, and that fluid movement across capillary walls is governed by hydrostatic and oncotic pressure gradients (the Starling forces). Glomerular filtration takes these familiar principles and applies them in a specialized structure optimized for high-volume plasma filtration.

Each kidney contains about one million **nephrons**, and each nephron begins with a **glomerulus** — a tuft of capillaries enclosed within Bowman's capsule. Blood enters the glomerulus through the **afferent arteriole** and exits through the **efferent arteriole** (notably, this is a capillary bed sandwiched between two arterioles, not between an arteriole and a venule like most capillary beds). The glomerular capillary pressure is unusually high — about 55 mmHg, roughly twice the pressure in most systemic capillaries — because the efferent arteriole's resistance maintains back-pressure. This high hydrostatic pressure is the engine driving filtration. Opposing it are Bowman's capsule hydrostatic pressure (~15 mmHg, from fluid already filtered) and the **glomerular capillary oncotic pressure** (~30 mmHg, from plasma proteins that cannot cross the filter). The net filtration pressure of about 10 mmHg drives roughly 180 liters of plasma ultrafiltrate per day — an extraordinary volume that the tubules then selectively reabsorb and modify.

The **glomerular filtration barrier** itself is a three-layer structure exquisitely designed for selective permeability. The innermost layer is the **fenestrated endothelium** of the capillary, with pores that freely pass water and small solutes but block blood cells. The middle layer is the **glomerular basement membrane (GBM)**, a dense meshwork of collagen and negatively charged proteoglycans that restricts passage of large and negatively charged molecules — this charge barrier is a key reason why albumin (a large, negatively charged plasma protein) is almost entirely excluded from the filtrate. The outer layer consists of **podocytes**, specialized epithelial cells whose foot processes interdigitate to form **slit diaphragms** — the final size-selective barrier. Together, these three layers ensure that the filtrate is essentially protein-free plasma: water, electrolytes, glucose, amino acids, urea, and other small molecules pass freely, while proteins and blood cells are retained.

The body regulates **glomerular filtration rate (GFR)** primarily by adjusting the resistance of the afferent and efferent arterioles. Constricting the **afferent arteriole** reduces blood flow into the glomerulus, lowering capillary pressure and decreasing GFR — this is what happens during sympathetic activation in severe hemorrhage, diverting blood away from the kidneys. Constricting the **efferent arteriole** has a more nuanced effect: moderate constriction actually increases glomerular capillary pressure (by impeding outflow) and raises GFR, while severe constriction reduces blood flow so much that GFR falls. Angiotensin II preferentially constricts the efferent arteriole, helping maintain GFR even when systemic blood pressure drops. The kidney also employs **tubuloglomerular feedback**: specialized cells in the distal tubule (the macula densa) sense the filtrate's sodium chloride concentration and signal the adjacent afferent arteriole to constrict or dilate, forming a local feedback loop that stabilizes GFR. These regulatory mechanisms ensure that despite wide fluctuations in blood pressure, the kidneys maintain remarkably constant filtration — a process called **autoregulation** — keeping GFR near 120 mL/min across a mean arterial pressure range of roughly 80–180 mmHg.
