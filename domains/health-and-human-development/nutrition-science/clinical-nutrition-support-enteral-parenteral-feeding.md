---
id: clinical-nutrition-support-enteral-parenteral-feeding
title: 'Clinical Nutrition Support: Enteral and Parenteral Feeding'
domain: health-and-human-development
course: nutrition-science
prerequisites:
- id: nutritional-assessment-dietary-analysis-methods
  type: hard
- id: energy-expenditure-components-and-measurement
  type: soft
builds-toward:
- malnutrition-pathophysiology-refeeding-syndrome
- nutrition-across-the-lifespan
tags:
- clinical-nutrition
- enteral-nutrition
- parenteral-nutrition
- tube-feeding
- medical-nutrition-therapy
stage: formal-systems
status: draft
---

# Clinical Nutrition Support: Enteral and Parenteral Feeding

## Core Idea
Clinical nutrition support provides nutrition when oral intake is inadequate or impossible. Enteral nutrition (tube feeding via nasogastric, nasojejunal, gastrostomy, or jejunostomy tubes) preserves gut structure and function and is preferred when the gastrointestinal tract is functional. Parenteral nutrition (intravenous feeding of amino acids, glucose, lipid emulsions, electrolytes, vitamins, and trace elements) bypasses the GI tract and is used when the gut is non-functional or inaccessible. Complications include refeeding syndrome (metabolic derangements when nutrition is reintroduced), aspiration, infection, and metabolic imbalances. Nutrient requirements must be calculated based on indirect calorimetry or predictive equations and adjusted for clinical status.

## How It's Best Learned
Calculate energy and macronutrient requirements for specific disease states (trauma, sepsis, critical illness); design enteral and parenteral nutrition regimens and identify complication risks.

## Common Misconceptions
- Parenteral nutrition is always superior in critical illness; enteral nutrition is preferred when feasible and improves outcomes. - Refeeding syndrome only occurs with rapid feeding; it can occur with appropriate rates if baseline deficits are severe.

## Questions

```yaml
- question: "A critically ill patient on mechanical ventilation has a functioning gastrointestinal tract but cannot eat. Which nutrition route is most appropriate and why?"
  type: multiple-choice
  options:
    - "Parenteral nutrition, because it bypasses aspiration risk and delivers nutrients with greater precision"
    - "Enteral nutrition, because it maintains gut barrier integrity, gut-associated immune function, and prevents bacterial translocation"
    - "Parenteral nutrition, because it is faster to initiate and requires no tube placement"
    - "Either route is equivalent as long as caloric and protein targets are met"
  answer: 1
  explanation: "When the GI tract is functional, enteral nutrition is always preferred. The gut is not merely a passive conduit — it is an active immune and endocrine organ. Luminal nutrition maintains the intestinal epithelium, stimulates gut-associated lymphoid tissue, and prevents the bacterial translocation that can occur when the mucosa atrophies during prolonged fasting. Option A reflects a common clinical misconception; parenteral nutrition is reserved for when the gut is non-functional or inaccessible."

- question: "A 24-year-old woman with severe anorexia nervosa is admitted after weeks of near-total starvation. On day 3 of enteral refeeding at a modest caloric rate, she develops cardiac arrhythmias and acute respiratory weakness. The most likely explanation is:"
  type: multiple-choice
  options:
    - "Aspiration pneumonia from the nasogastric tube, causing hypoxia and cardiac irritability"
    - "Hyperglycemia from the carbohydrate load causing osmotic fluid shifts into cells"
    - "Hypophosphatemia from intracellular phosphate shift driven by insulin release upon carbohydrate reintroduction"
    - "Central line-associated bloodstream infection causing septic arrhythmia"
  answer: 2
  explanation: "This is classic refeeding syndrome. During starvation, intracellular phosphate stores are depleted while serum levels are maintained near-normal through compensatory shifts. When carbohydrate is reintroduced, insulin surges and drives glucose into cells for metabolism — taking phosphate (needed for glycolysis and ATP synthesis) with it. Serum phosphate plummets, causing hypophosphatemia severe enough to impair cardiac muscle, respiratory muscle, and erythrocyte function. Option D is wrong because she is on enteral, not parenteral, nutrition."

- question: "Pre-refeeding serum electrolyte levels in a severely malnourished patient are often near-normal, suggesting that refeeding syndrome risk is low."
  type: true-false
  answer: false
  explanation: "This is the critical misconception that makes refeeding syndrome so dangerous. During starvation, cells release phosphate, potassium, and magnesium into the bloodstream, and the kidneys conserve these minerals — keeping serum levels apparently normal despite massively depleted intracellular stores. The 'normal' serum value is a compensated equilibrium, not a reflection of true body stores. When refeeding begins and insulin drives these minerals back into cells, serum levels can fall precipitously."

- question: "Parenteral nutrition bypassing the gut means that every nutrient that would normally be absorbed from food must be explicitly included in the formulation."
  type: true-false
  answer: true
  explanation: "Unlike enteral nutrition, which can rely on normal digestive and absorptive processes to extract nutrients from formula, parenteral nutrition requires the clinician to prescribe each component individually: glucose, lipid emulsion, crystalline amino acids, electrolytes (sodium, potassium, calcium, magnesium, phosphate), vitamins, and trace elements. This provides precise control but also means that any omission or error in compounding is directly delivered to the bloodstream with no absorptive buffering."

- question: "Why does refeeding syndrome cause dangerous drops in serum phosphate, and why do near-normal serum phosphate levels before refeeding begins give a false sense of security?"
  type: short-answer
  answer: "During starvation, cells release phosphate into the bloodstream and the kidneys retain it, maintaining serum levels near-normal despite depleted intracellular stores. This compensated state collapses when carbohydrates are reintroduced: insulin secretion surges, driving glucose into cells for glycolysis and ATP synthesis — a process that consumes large amounts of phosphate. Phosphate rushes into cells faster than the depleted stores can buffer the shift, and serum levels plummet. The pre-refeeding 'normal' serum value is an artifact of starvation physiology, not a reflection of total body phosphate."
  explanation: "The practical implication is that risk stratification for refeeding syndrome must rely on clinical history (duration of starvation, degree of weight loss, underlying conditions) rather than serum electrolyte levels. High-risk patients require electrolyte repletion before refeeding begins, slow initiation of nutrition, and close monitoring during the first week regardless of their pre-refeeding lab values."
```

## Explainer

From your study of nutritional assessment and energy expenditure, you know how to determine what a patient needs: dietary recall and biomarkers to characterize nutritional status, indirect calorimetry or predictive equations to estimate resting energy expenditure, and clinical context to adjust for metabolic stress. Clinical nutrition support starts at exactly this point — but for patients who cannot eat. The inability to eat is common in hospital settings: a stroke patient who cannot swallow safely, a surgical patient with an open abdomen, a critically ill patient on mechanical ventilation, a cancer patient whose tumor obstructs the esophagus. In every case, the nutritional assessment you know how to perform determines what needs to be delivered; the route and formulation of nutrition support determine how it gets there.

**Enteral nutrition (EN)** means feeding through the gastrointestinal tract via a tube. The GI tract is not merely a conduit — it is an active endocrine and immune organ, and maintaining luminal nutrition preserves **gut barrier integrity**, stimulates gut-associated immune tissue, and prevents the bacterial translocation that can occur when the intestinal epithelium atrophies during prolonged fasting. This is why EN is preferred over parenteral nutrition whenever the gut is functional and accessible. Routes include **nasogastric (NG)** tubes (nose to stomach, easiest to place, used short-term), **nasojejunal** tubes (past the pylorus, indicated when gastric motility is impaired), and surgically placed tubes for longer-term use: **gastrostomy** (PEG tube) and **jejunostomy**. Enteral formulas range from polymeric (intact proteins and complex carbohydrates, used when digestion is intact) to elemental (pre-digested amino acids and simple sugars, for impaired absorptive capacity). Complications include aspiration pneumonia, tube dislodgement, and GI intolerance (nausea, diarrhea).

**Parenteral nutrition (PN)** bypasses the GI tract entirely and delivers nutrients directly into the bloodstream via a central venous catheter (total parenteral nutrition, **TPN**) or a peripheral vein (peripheral parenteral nutrition, **PPN**). A PN formulation is a compounded mixture containing glucose, lipid emulsions, crystalline amino acids, electrolytes, vitamins, and trace elements — every nutrient that would otherwise be absorbed from food must be provided explicitly and in precise amounts. PN is indicated when the gut is non-functional (short bowel syndrome, severe ileus, high-output fistula, bowel obstruction) or inaccessible. Because it bypasses gut absorption, it allows very precise control of nutrient delivery. But it carries risks that EN does not: central line-associated bloodstream infection (CLABSI), hyperglycemia (the glucose load is delivered directly intravenously), hepatic steatosis with long-term use, and loss of gut mucosal integrity over time.

**Refeeding syndrome** is the most dangerous complication specific to nutrition support initiation in malnourished patients. During starvation, the body depletes intracellular phosphate, magnesium, and potassium while maintaining serum levels at near-normal through intracellular-to-extracellular shifts and renal conservation. When carbohydrate is reintroduced, insulin secretion rises sharply, driving these minerals back into cells for metabolic use — and serum levels plummet. Profound **hypophosphatemia** is the hallmark and can cause cardiac arrhythmia, respiratory failure, rhabdomyolysis, and death. Prevention requires identifying at-risk patients (prolonged starvation, anorexia nervosa, chronic alcoholism, severe weight loss), repleting electrolytes before and during refeeding, starting nutrition slowly, and monitoring serum electrolytes closely during the first week. This is why the principle "start low, go slow" applies to refeeding severely malnourished patients regardless of how urgently improved nutrition is needed.
