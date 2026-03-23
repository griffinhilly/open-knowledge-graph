---
id: iron-metabolism-bioavailability-and-deficiency
title: Iron Metabolism, Bioavailability, and Deficiency States
domain: health-and-human-development
course: nutrition-science
prerequisites:
- id: minerals-and-trace-elements
  type: hard
- id: intestinal-absorption-nutrient-transport
  type: hard
- id: iron-oxygen-transport-dna-synthesis
  type: soft
- id: hemoglobin-cooperativity-oxygen-binding
  type: soft
tags:
- iron
- bioavailability
- metabolism
- deficiency
stage: formal-systems
status: draft
---

# Iron Metabolism, Bioavailability, and Deficiency States

## Core Idea
Dietary iron exists in two forms: heme iron (animal sources, ~15-35% bioavailability) and non-heme iron (plant sources, ~2-20% bioavailability). Absorption is regulated by hepcidin, which increases with iron stores and inflammation. Enhancers (vitamin C, meat) and inhibitors (phytates, polyphenols, calcium) significantly affect non-heme iron absorption. Iron deficiency progresses through depletion, early functional deficiency, and iron-deficiency anemia, each with distinct biochemical markers.

## Questions

```yaml
- question: "A vegetarian patient's diet is assessed to contain 18 mg of iron daily — meeting the recommended intake. Yet she is diagnosed with early-stage iron deficiency. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "18 mg is insufficient for women regardless of dietary source"
    - "She likely has an underlying gastrointestinal disorder blocking all iron absorption"
    - "The majority of her dietary iron is non-heme, which has far lower bioavailability than heme iron — so effective absorbed iron is well below the apparent intake"
    - "Iron deficiency in vegetarians is primarily caused by calcium from dairy products blocking absorption"
  answer: 2
  explanation: "This is the core paradox of iron nutrition: quantity on paper ≠ quantity absorbed. Non-heme iron (from plants and fortified foods) has 2–20% bioavailability vs. 15–35% for heme iron. A vegetarian diet may meet the RDA in raw milligrams while delivering a fraction of the absorbable iron a meat-eater would receive from the same number. This explains why vegetarians face higher deficiency risk even with apparently adequate dietary intake."

- question: "A patient with severe rheumatoid arthritis has low hemoglobin but normal-to-elevated ferritin. Iron supplementation has little effect. Which mechanism best explains this presentation?"
  type: multiple-choice
  options:
    - "Elevated hepcidin from chronic inflammation degrades ferroportin, trapping iron in storage depots and blocking its release into circulation"
    - "The patient's enterocytes are inflamed and absorbing less dietary iron"
    - "Rheumatoid arthritis causes occult blood loss that depletes storage iron faster than it accumulates"
    - "Elevated transferrin saturation from inflammation blocks additional iron uptake by the erythroid marrow"
  answer: 0
  explanation: "This is anemia of chronic disease. Inflammation independently raises hepcidin, which binds and degrades ferroportin — the transporter that moves iron from enterocytes and macrophages into the bloodstream. Iron is present in stores (hence normal ferritin) but cannot be released to make hemoglobin. Oral iron supplementation fails because it can be absorbed into the enterocyte but not exported. This illustrates that hepcidin is the master regulator of iron availability, not just iron absorption."

- question: "A falling hemoglobin level is the earliest reliable biochemical marker of iron deficiency."
  type: true-false
  answer: false
  explanation: "Hemoglobin falls only in the third and final stage of iron deficiency — iron-deficiency anemia. By that point, the body has already exhausted storage iron (marked by falling ferritin) and gone through a phase of iron-deficient erythropoiesis (falling transferrin saturation, rising RDW). Serum ferritin is the earliest and most sensitive marker because it reflects storage depletion before any functional iron compartment is affected. Waiting for hemoglobin to fall misses the window for easy treatment."

- question: "Consuming vitamin C alongside plant-based iron sources can substantially increase non-heme iron absorption."
  type: true-false
  answer: true
  explanation: "Vitamin C (ascorbate) reduces ferric iron (Fe³⁺) to ferrous iron (Fe²⁺) and chelates it in a soluble form that resists the inhibitory effects of phytates and polyphenols. Studies show up to sixfold enhancement of non-heme iron absorption when vitamin C is consumed in the same meal. This is clinically meaningful advice for vegetarians, pregnant women, and anyone at risk of deficiency — and illustrates how the dietary context surrounding iron matters as much as the iron content itself."

- question: "Why does iron deficiency progress through distinct stages before anemia develops, and why does this staging matter clinically?"
  type: short-answer
  answer: "The body maintains iron in separate compartments: storage iron (ferritin in liver, spleen, marrow), transport iron (transferrin-bound in blood), and functional iron (hemoglobin in red cells, enzymes). Deficiency depletes these compartments sequentially. Storage depletion comes first (ferritin falls), then transport iron drops (low transferrin saturation, rising RDW as new red cells are iron-poor), and only finally hemoglobin falls. This staging matters because ferritin-stage deficiency is easily corrected with supplementation, while full iron-deficiency anemia requires longer treatment, may signal chronic disease, and in vulnerable populations (children, pregnant women) has already caused measurable harm to cognition and fetal development."
  explanation: "The staging also explains why ferritin is the preferred screening test for at-risk populations. Treating stage 1 (depleted stores) prevents the downstream harms of stage 3. By contrast, if clinicians only check hemoglobin, they miss deficiency entirely until it is severe."
```

## Explainer

Iron is one of the most abundant elements on Earth yet one of the most common nutritional deficiencies globally. The paradox is explained by bioavailability — from your study of minerals and trace elements, you know that the amount of a mineral ingested tells only part of the story. Iron bioavailability is complicated by the fact that it comes in two chemically distinct forms with dramatically different absorption rates.

**Heme iron**, derived from hemoglobin and myoglobin in meat, fish, and poultry, is absorbed directly by enterocytes via a dedicated transporter and reaches the bloodstream at 15–35% efficiency. **Non-heme iron**, which makes up the majority of iron in plant foods and fortified products, must first be reduced from ferric (Fe³⁺) to ferrous (Fe²⁺) form by a brush-border enzyme before transport via **DMT1** (divalent metal transporter 1). This extra reduction step makes non-heme absorption highly variable (2–20%) and sensitive to luminal chemistry. This is why vegetarians and vegans face higher deficiency risk despite adequate dietary iron intake on paper — the form of iron matters as much as the quantity.

Once inside the enterocyte, iron takes one of two paths: it either enters circulation via **ferroportin** or is sequestered in ferritin within the cell and lost when the cell sloughs off. The decision is regulated by **hepcidin**, a peptide hormone made by the liver. When iron stores are replete, hepcidin is high — it binds ferroportin and triggers its degradation, trapping iron in the enterocyte. When stores are low, hepcidin falls, ferroportin remains open, and absorption increases. This elegant feedback loop also explains the anemia of chronic disease: inflammation raises hepcidin independently of iron stores, so the body has iron in its depots but cannot release it into circulation.

Iron deficiency follows a predictable three-stage progression that maps to the body's iron compartments. First comes **storage depletion**: serum ferritin (the most sensitive early marker) falls as liver stores empty, but hemoglobin remains normal. Second, **early functional deficiency**: iron-deficient erythropoiesis begins, transferrin saturation drops, and the red cell distribution width (RDW) widens as new red cells become smaller and paler. Only in the third stage — **iron-deficiency anemia** — does hemoglobin fall below threshold, producing the classic microcytic, hypochromic picture with symptoms of fatigue, pallor, and reduced cognitive performance. Understanding this progression explains why ferritin is the preferred screening test: catching deficiency before anemia develops makes treatment far easier.

Dietary context profoundly shapes practical outcomes. Vitamin C (ascorbate) reduces Fe³⁺ to Fe²⁺ and chelates it in soluble form, enhancing non-heme iron absorption up to sixfold — this is why consuming citrus alongside iron-rich plant foods is clinically meaningful advice. Conversely, phytates (in whole grains and legumes), polyphenols (in tea and coffee), and calcium (in dairy) all inhibit non-heme iron absorption by competing for the transporter or forming insoluble complexes. This creates a practical paradox: healthy dietary patterns high in whole grains, legumes, and plants also contain the highest concentrations of absorption inhibitors. For at-risk populations — women of reproductive age, vegetarians, infants — strategic meal timing and food pairing become real clinical tools.
