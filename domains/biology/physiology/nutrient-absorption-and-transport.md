---
id: nutrient-absorption-and-transport
title: Nutrient Absorption and Transport
domain: biology
course: physiology
prerequisites:
- id: digestive-system-overview
  type: hard
- id: passive-transport
  type: hard
- id: active-transport
  type: hard
- id: solution-concentration
  type: soft
tags:
- absorption
- villi
- cotransport
- chylomicrons
- portal circulation
stage: formal-systems
status: validated
---

# Nutrient Absorption and Transport

## Core Idea
Absorption of digested nutrients in the small intestine is maximized by the three-level surface amplification of mucosal folds, villi, and microvilli (brush border), collectively increasing absorptive surface ~600-fold. Monosaccharides (glucose, galactose) and amino acids enter enterocytes via Na⁺-coupled cotransporters (SGLT1, neutral amino acid transporters) on the apical membrane and exit into portal capillaries via facilitated diffusion on the basolateral side. Fatty acids and monoglycerides are reassembled into triglycerides inside enterocytes, packaged into chylomicrons, and exported via lacteals into the lymphatic system — bypassing portal circulation and initial hepatic metabolism. Fat-soluble vitamins (A, D, E, K) follow the lipid pathway; vitamin B12 requires intrinsic factor for receptor-mediated endocytosis in the terminal ileum.

## How It's Best Learned
Map the three macronutrient absorption routes separately, following each from the intestinal lumen to the bloodstream: glucose (SGLT1 apical → GLUT2 basolateral → portal vein → liver), amino acids (cotransporter → basolateral → portal vein), fats (micelle → enterocyte → re-esterification → chylomicron → lacteal → thoracic duct → bloodstream). Ask: why do fat-soluble drug overdoses take longer to reverse than water-soluble drug overdoses?

## Common Misconceptions
- Dietary fat does not enter the portal vein and is not subject to first-pass hepatic metabolism; it enters the circulation via lymphatics.
- 'Absorption' is not passive diffusion through a wall — most nutrients require specific membrane transporters and would not be absorbed without them.

## Questions

```yaml
- question: "A patient takes an oral lipophilic (fat-soluble) medication. Compared to a water-soluble drug of similar dose, how does its absorption route and first-pass hepatic metabolism differ?"
  type: multiple-choice
  options:
    - "The lipophilic drug is absorbed more slowly and undergoes more extensive first-pass hepatic metabolism because the liver must process all absorbed substances"
    - "The lipophilic drug is packaged into chylomicrons and exits via the lymphatic system, bypassing the liver entirely; the water-soluble drug enters portal circulation and undergoes first-pass hepatic metabolism"
    - "Both drugs are absorbed via the portal vein but the lipophilic drug is sequestered in adipose tissue before reaching the liver"
    - "The lipophilic drug requires active transport into enterocytes, which is slower than the passive diffusion used by water-soluble drugs"
  answer: 1
  explanation: "Lipophilic substances (including dietary fats, fat-soluble vitamins, and fat-soluble drugs) are packaged into chylomicrons inside enterocytes and exported via lacteals into the lymphatic system. They enter the bloodstream at the left subclavian vein, bypassing the liver entirely on first pass. Water-soluble nutrients and drugs are absorbed into capillaries within the villi and travel via the portal vein directly to the liver, where first-pass metabolism can significantly reduce bioavailability. This is why some fat-soluble drugs have very high oral bioavailability — the liver never gets the first chance to metabolize them."

- question: "A patient with pernicious anemia (autoimmune destruction of gastric parietal cells) develops vitamin B12 deficiency despite consuming adequate dietary B12. What is the most direct mechanism?"
  type: multiple-choice
  options:
    - "Parietal cell destruction reduces gastric acid production, preventing B12 release from food proteins"
    - "Without intrinsic factor (secreted by parietal cells), the terminal ileum cannot absorb B12 via receptor-mediated endocytosis, regardless of luminal B12 concentration"
    - "The autoimmune attack destroys B12-specific transporter proteins in the small intestinal epithelium"
    - "Parietal cell loss impairs bile production, reducing the micelle formation needed for B12 solubilization"
  answer: 1
  explanation: "Vitamin B12 absorption requires intrinsic factor, a glycoprotein secreted exclusively by gastric parietal cells. The B12-intrinsic factor complex binds to specific receptors (cubam receptors) in the terminal ileum and is absorbed by receptor-mediated endocytosis. Without intrinsic factor, there are no functional receptors to bind B12, and the vitamin passes through the ileum unabsorbed — even if luminal B12 concentrations are high from dietary sources. This is why pernicious anemia requires B12 supplementation by injection (bypassing the gut entirely) rather than oral supplementation."

- question: "Glucose absorption across the apical membrane of enterocytes is a passive process — glucose simply diffuses down its concentration gradient without any energy input from the cell."
  type: true-false
  answer: false
  explanation: "Glucose absorption across the apical membrane uses SGLT1 (sodium-glucose linked transporter 1), which is a secondary active transporter. SGLT1 co-transports one glucose molecule with two sodium ions; the sodium moves down its electrochemical gradient, providing the driving force to pull glucose into the cell even against a concentration gradient. The sodium gradient itself is maintained by Na⁺/K⁺-ATPase on the basolateral membrane, which actively pumps sodium out using ATP. So glucose absorption is ultimately driven by ATP hydrolysis, just indirectly. Fructose, by contrast, uses GLUT5 (passive facilitated diffusion) — explaining why fructose absorption has a lower capacity ceiling."

- question: "Dietary fat is not subject to first-pass hepatic metabolism because chylomicrons are too large to enter blood capillaries and instead travel through the lymphatic system before reaching the bloodstream."
  type: true-false
  answer: true
  explanation: "Chylomicrons assembled in enterocytes are large lipoprotein particles (~75–1200 nm diameter) — far too large to squeeze through the tight junctions and small fenestrae of blood capillaries. They are instead exocytosed into lacteals (lymphatic capillaries within each villus), travel through lymphatic vessels to the thoracic duct, and enter the venous bloodstream at the left subclavian vein. This route entirely bypasses the portal vein and hepatic first-pass metabolism. Dietary fat reaches the general circulation before the liver has any chance to process it — which is why triglycerides in chylomicrons are delivered first to peripheral tissues and adipose tissue, with the liver receiving chylomicron remnants only after lipolysis in peripheral capillaries."

- question: "Explain why the three-level surface amplification (mucosal folds → villi → microvilli) is functionally necessary, rather than just an anatomical curiosity."
  type: short-answer
  answer: "The small intestine must absorb the entire day's nutritional intake — hundreds of grams of carbohydrates, proteins, and fats — within a few hours, across the wall of a tube roughly 6 meters long. Without surface amplification, the absorptive area of the intestinal tube would be approximately 0.33 m² (the area of a smooth cylinder). The three-level amplification increases this to ~200 m² — about 600-fold — bringing the effective absorptive surface to roughly the area of a tennis court. This massive surface area is necessary because absorption rate is proportional to surface area (Fick's law); without it, nutrients would pass through faster than they could be absorbed, leading to malabsorption. The clinical consequence of losing this surface — as in celiac disease (villus atrophy) — is profound malabsorption of all macronutrients and many micronutrients."
  explanation: "Each level of amplification serves the same purpose: maximizing the number of transporter-bearing membrane surface per unit length of intestine. The brush border microvilli also carry digestive enzymes (brush border enzymes like maltase, sucrase, lactase) on their surface, so digestion and absorption occur simultaneously at the same membrane — a further efficiency gain."
```

## Explainer

Digestion breaks food into small molecules, but those molecules are useless until they cross the intestinal wall and enter the body. **Absorption** is the process by which digested nutrients move from the intestinal lumen, through the enterocyte epithelium, and into either the blood or the lymph. The small intestine is spectacularly designed for this task: its inner surface is folded into circular folds (plicae circulares), which bear finger-like projections called **villi**, which in turn are covered with **microvilli** (the brush border) on each enterocyte. This three-tiered amplification increases the absorptive surface area roughly 600-fold compared to a smooth tube — to approximately 200 square meters, about the area of a tennis court.

The absorption route depends on whether the nutrient is water-soluble or fat-soluble. **Monosaccharides** like glucose and galactose enter the enterocyte through **SGLT1** (sodium-glucose linked transporter 1) on the apical membrane — a secondary active transporter that harnesses the sodium gradient you studied in active transport. Inside the cell, glucose exits through **GLUT2** facilitated diffusion transporters on the basolateral membrane and enters capillaries within the villus. These capillaries drain into the **portal vein**, carrying glucose directly to the liver for first-pass metabolism. Amino acids follow a similar pattern: Na⁺-coupled cotransporters on the apical side, facilitated diffusion on the basolateral side, and portal venous delivery to the liver. Fructose is an exception — it uses GLUT5 (facilitated diffusion, not sodium-coupled) on the apical membrane, which is why fructose absorption is slower and capacity-limited.

**Lipid absorption** follows a completely different route. Long-chain fatty acids and monoglycerides are poorly soluble in the aqueous lumen, so bile salts package them into **micelles** — tiny aggregates with hydrophobic interiors and hydrophilic surfaces. Micelles ferry lipids to the enterocyte surface, where fatty acids and monoglycerides diffuse across the apical membrane (they are small and hydrophobic enough to cross the lipid bilayer directly). Inside the enterocyte, they are reassembled into triglycerides in the smooth endoplasmic reticulum, coated with apolipoproteins, and packaged into large lipoprotein particles called **chylomicrons**. Chylomicrons are too large to enter blood capillaries, so they are exocytosed into **lacteals** — lymphatic capillaries within each villus — and travel through the lymphatic system to the thoracic duct, entering the bloodstream at the left subclavian vein. This lymphatic route bypasses the liver entirely, which is why dietary fat is not subject to first-pass hepatic metabolism.

Fat-soluble vitamins (A, D, E, K) dissolve in micelles and follow the lipid pathway into chylomicrons. Water-soluble vitamins generally use specific transporters, with one notable exception: **vitamin B12** requires **intrinsic factor**, a glycoprotein secreted by gastric parietal cells, for its absorption. The B12-intrinsic factor complex binds to receptors in the terminal ileum and is absorbed by receptor-mediated endocytosis. This explains why gastric surgery or autoimmune destruction of parietal cells (pernicious anemia) causes B12 deficiency even when dietary intake is adequate — without intrinsic factor, the ileum cannot absorb B12 regardless of how much is present in the lumen.
