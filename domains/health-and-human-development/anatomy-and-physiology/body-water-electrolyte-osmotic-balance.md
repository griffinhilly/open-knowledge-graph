---
id: body-water-electrolyte-osmotic-balance
title: Body Water, Electrolytes, and Osmotic Balance
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: body-organization-and-terminology
  type: hard
- id: cell-membrane-structure
  type: hard
- id: osmosis-and-tonicity
  type: hard
- id: colligative-properties
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- fluid-balance-and-electrolytes
- renal-regulation-of-fluid-balance
tags:
- fluid-compartments
- osmolarity
- water-balance
stage: formal-systems
status: validated
---

# Body Water, Electrolytes, and Osmotic Balance

## Core Idea
Total body water (~60% of weight) partitions into intracellular (2/3) and extracellular (1/3) fluid. These compartments maintain osmotic equilibrium because water freely crosses membranes while osmotically active solutes are compartmentalized. Vasopressin adjusts collecting duct permeability to preserve plasma osmolarity (~290 mOsm/L), while sodium content determines extracellular volume. Disturbances in either osmolarity or sodium alter water distribution and cellular function.

## Questions

```yaml
- question: "A patient presents with severe hyponatremia: plasma sodium is 118 mEq/L (normal ~140 mEq/L). What is the primary osmotic consequence, and which compartment is most acutely endangered?"
  type: multiple-choice
  options:
    - "Plasma becomes hypertonic relative to cells; cells shrink as water moves out into the circulation"
    - "Plasma becomes hypotonic relative to cells; water moves into cells, causing them to swell — neurons are especially vulnerable"
    - "Only the extracellular compartment is affected because sodium is confined to the extracellular space"
    - "The intracellular compartment is unaffected because the Na⁺/K⁺-ATPase pump rapidly compensates by adjusting ion gradients"
  answer: 1
  explanation: "Plasma osmolarity is approximately 2 × [Na⁺], so a fall in plasma sodium directly reduces extracellular osmolarity. Water follows osmotic gradients across cell membranes toward higher solute concentration. With low extracellular osmolarity, water moves INTO cells, which swell. Neurons are particularly vulnerable because the skull is rigid — swelling neurons cannot expand outward, causing dangerously elevated intracranial pressure. This is why severe acute hyponatremia is a neurological emergency. The Na⁺/K⁺-ATPase cannot compensate fast enough and only maintains the gradient under steady-state conditions, not acute osmotic shifts."

- question: "A patient is hypovolemic (low blood volume) but has normal plasma osmolarity. A physician wants to restore blood volume without altering osmolarity. Which intervention is most appropriate?"
  type: multiple-choice
  options:
    - "Administer pure water IV, which will distribute evenly throughout all body fluid compartments"
    - "Administer isotonic saline (0.9% NaCl), which has the same osmolarity as plasma and stays primarily in the extracellular compartment"
    - "Administer vasopressin to promote water retention by the kidneys"
    - "Administer a concentrated sodium solution to pull water from the intracellular compartment into the blood"
  answer: 1
  explanation: "Volume expansion requires adding fluid to the extracellular (especially intravascular) compartment. Isotonic saline has an osmolarity (~308 mOsm/L) close to plasma (~290 mOsm/L), so it creates no osmotic gradient across cell membranes — it stays in the extracellular space and expands blood volume. Pure water would create a hypotonic extracellular solution, driving water into cells and providing relatively little volume expansion per liter administered. Vasopressin retains existing water but doesn't add volume from outside. Hypertonic saline would raise osmolarity, which is not desired here."

- question: "Vasopressin (ADH) regulates plasma osmolarity by controlling how much water the kidney retains, without directly altering the amount of sodium in the body."
  type: true-false
  answer: true
  explanation: "Vasopressin acts specifically on the collecting duct of the kidney, inserting aquaporin-2 water channels to allow more water reabsorption. This dilutes the plasma — reducing osmolarity back toward normal — without changing total body sodium. It is a pure water-handling mechanism: more vasopressin → more water retained → lower osmolarity. This contrasts with aldosterone, which acts on the collecting duct to retain sodium (and water secondarily), affecting volume rather than osmolarity. The distinction is clinically essential: vasopressin corrects the concentration, aldosterone corrects the amount."

- question: "Plasma osmolarity and extracellular fluid volume are both regulated by the same hormonal system — vasopressin controls both by adjusting how much water the kidney retains."
  type: true-false
  answer: false
  explanation: "These are two separate regulatory systems. Vasopressin (ADH) regulates osmolarity by controlling renal water reabsorption — it responds to osmoreceptors in the hypothalamus detecting osmolarity changes. Volume regulation is primarily governed by the renin-angiotensin-aldosterone system (RAAS) and natriuretic peptides, which control sodium retention and excretion and respond to baroreceptors detecting blood pressure and volume changes. A patient can be simultaneously hypovolemic AND hyponatremic — low volume AND low osmolarity — which requires addressing sodium balance (volume) and water balance (osmolarity) separately. Treating one without the other, or confusing vasopressin for a volume regulator, leads to clinical errors."

- question: "A hospitalized patient has both low blood volume (hypovolemia) and low plasma sodium (hyponatremia). Why are these two separate problems requiring different treatments? Use the distinction between osmolarity regulation and volume regulation in your answer."
  type: short-answer
  answer: "Volume and osmolarity are regulated by distinct hormonal systems responding to different signals. Volume is controlled primarily by the RAAS and aldosterone, which regulate sodium retention — because sodium is the dominant extracellular solute, how much sodium is in the body determines how much water stays in the extracellular compartment (and therefore blood volume). Osmolarity is controlled by vasopressin, which regulates water retention independent of sodium. Hypovolemia means too little total sodium (and thus too little extracellular fluid) — treated by adding isotonic sodium chloride to expand volume. Hyponatremia means the sodium that is present is too dilute (too much water relative to sodium) — treated by restricting water intake or, in severe cases, carefully administering hypertonic saline. Giving a hyponatremic patient a large volume of hypotonic fluid to treat their volume deficit would worsen the sodium dilution. Getting treatment right requires diagnosing each problem separately."
  explanation: "The practical lesson is that the body treats 'how much fluid do I have?' and 'how concentrated is my fluid?' as two independent questions with two independent answers. The sensors (volume receptors vs. osmoreceptors), the hormones (aldosterone vs. vasopressin), and the effector mechanisms (sodium reabsorption vs. water channel insertion) are all distinct. Clinical hyponatremia management is notoriously complex precisely because volume status and osmolarity status can point in different directions."
```

## Explainer

Start with the physics you already know from osmosis and tonicity: water moves across a semipermeable membrane toward the side with higher solute concentration until osmotic equilibrium is reached. The body applies this principle across two nested membranes — the cell membrane separating intracellular from extracellular fluid, and the capillary wall separating plasma from interstitial fluid. Because cell membranes are freely permeable to water but tightly control which solutes cross, the body can maintain very different solute compositions on each side while water distributes itself to equalize **osmolarity** (total solute concentration) across compartments.

The intracellular compartment (about 40% of body weight, or two-thirds of total body water) is dominated by potassium, phosphate, and large negatively charged proteins. The extracellular compartment (about 20% of body weight) is dominated by sodium and chloride. This asymmetry is actively maintained by the Na⁺/K⁺-ATPase pump in every cell membrane. Because sodium is the dominant extracellular solute, plasma **osmolarity** is approximated simply as 2 × [Na⁺] + glucose/18 + BUN/2.8. When sodium concentration rises, so does osmolarity — water shifts out of cells, concentrating intracellular contents and shrinking cells. When sodium falls, water shifts in, swelling cells. This is why osmolarity disturbances are clinically dangerous: neurons are particularly sensitive to shrinkage and swelling.

The body regulates osmolarity and volume through separate but interacting systems. **Vasopressin** (antidiuretic hormone, ADH) is released by the posterior pituitary when osmoreceptors in the hypothalamus detect plasma osmolarity rising above ~290 mOsm/L. It inserts aquaporin water channels into the collecting duct of the kidney, allowing more water to be reabsorbed and diluting the plasma back to normal. This is a pure osmolarity-correction mechanism — it moves water without moving sodium. **Volume regulation**, by contrast, is governed primarily by sodium balance: aldosterone promotes renal sodium (and thus water) retention when blood pressure falls. Understanding this distinction is crucial — a patient who is both hypovolemic and hyponatremic has two separate problems requiring different treatments.

Electrolytes do more than set osmotic pressure. Potassium's intracellular dominance sets the resting membrane potential of excitable cells (neurons, muscle). Calcium ions trigger muscle contraction and neurotransmitter release. Phosphate buffers intracellular pH and is the backbone of ATP. **Hypokalemia** flattens the resting membrane potential, making cells hyper-excitable (cardiac arrhythmias); **hyperkalemia** depolarizes cells to the point of inexcitability (cardiac arrest). These clinical consequences flow directly from the biophysics of ionic gradients you already know from cell membrane structure and colligative properties — the body is simply running those same principles at physiological scale, with hormonal feedback loops keeping the system within tight tolerances.

