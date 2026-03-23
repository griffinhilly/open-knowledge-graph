---
id: intestinal-mucosal-absorption-nutrient-transport
title: Intestinal Mucosal Absorption and Nutrient Transport
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: digestive-anatomy-and-motility
  type: hard
- id: epithelial-vectorial-transport-secretion
  type: hard
builds-toward:
- nutrient-digestion-and-absorption
tags:
- nutrient-absorption
- intestinal-transport
- brush-border
stage: formal-systems
status: draft
---

# Intestinal Mucosal Absorption and Nutrient Transport

## Core Idea
The small intestine absorbs carbohydrates, proteins, fats, and micronutrients through coordinated brush-border enzyme activity and selective transporter expression. Glucose enters via SGLT1 (Na⁺-dependent), fructose via GLUT5 (passive), and amino acids via multiple amino acid transporters. Fats are emulsified by bile, hydrolyzed to monoglycerides and fatty acids, and reconstituted into chylomicrons for lymphatic transport. Different nutrients are absorbed preferentially in different intestinal regions based on transporter distribution.

## Questions

```yaml
- question: "After a large carbohydrate-rich meal, glucose concentration in the intestinal lumen may actually be lower than inside the enterocyte. How does the intestine continue absorbing glucose under these conditions?"
  type: multiple-choice
  options:
    - "Glucose diffuses freely through the lipid bilayer without any transporter"
    - "SGLT1 uses the inward sodium gradient to co-transport glucose against its concentration gradient via secondary active transport"
    - "GLUT2 on the apical membrane drives glucose uptake using ATP directly"
    - "Glucose absorption pauses until luminal concentrations rise above cytoplasmic levels"
  answer: 1
  explanation: "SGLT1 (Sodium-Glucose Linked Transporter 1) is a secondary active transporter: it couples glucose uptake to the downhill movement of Na⁺ into the cell, exploiting the sodium gradient maintained by the basolateral Na⁺/K⁺-ATPase. This coupling allows glucose to be transported against its own concentration gradient — energy from Na⁺ flow drives glucose uptake. This is essential for efficient post-meal absorption. GLUT2 is on the basolateral membrane and uses facilitated diffusion (not active transport); GLUT5 handles fructose on the apical membrane."

- question: "After a high-fat meal, dietary triglycerides enter the bloodstream via which route?"
  type: multiple-choice
  options:
    - "Through the portal vein directly, like glucose and amino acids"
    - "Through the thoracic duct and lymphatic system as chylomicrons, bypassing the liver"
    - "Through the portal vein after being broken down to free fatty acids"
    - "Through passive diffusion directly across the intestinal epithelium into capillaries"
  answer: 1
  explanation: "Fats follow an entirely different route than carbohydrates and proteins. After entering enterocytes as monoglycerides and free fatty acids, they are re-esterified into triglycerides, packaged with cholesterol, phospholipids, and apolipoprotein B-48 into chylomicrons — particles too large to enter capillaries. Chylomicrons are secreted by exocytosis into the lacteals (lymphatic capillaries in each villus) and travel through the thoracic duct to enter systemic circulation at the subclavian vein. This bypasses first-pass hepatic metabolism, which is why high-fat meals raise systemic triglycerides before the liver can process them."

- question: "Glucose and fructose are both monosaccharides that are absorbed from the intestinal lumen by the same apical membrane transporter."
  type: true-false
  answer: false
  explanation: "Glucose and galactose use SGLT1 (a secondary active, Na⁺-coupled transporter) on the apical membrane. Fructose uses GLUT5, a facilitated diffusion transporter that requires no energy and moves fructose passively down its concentration gradient. This distinction has real physiological consequences: GLUT5 has limited capacity and can be overwhelmed by large fructose loads, while SGLT1 can actively concentrate glucose. Both sugars exit through GLUT2 on the basolateral membrane, but their apical entry mechanisms are entirely different."

- question: "Fat-soluble vitamins (A, D, E, K) are absorbed via the same lymphatic pathway as dietary fats, and their absorption depends on adequate dietary fat and bile salts."
  type: true-false
  answer: true
  explanation: "Fat-soluble vitamins are hydrophobic and require the same infrastructure as dietary fats: bile salts to form micelles that ferry them to the brush border, passive diffusion across the apical membrane, incorporation into chylomicrons within the enterocyte, and exit via lacteals into the lymphatic system. This is why very low-fat diets or bile salt deficiency can cause fat-soluble vitamin deficiencies, and why fat-soluble vitamin toxicity (e.g., vitamin A overdose) is possible — they accumulate in fatty tissues rather than being excreted in urine like water-soluble vitamins."

- question: "Why do dietary fats travel through the lymphatic system rather than directly entering portal blood, as glucose and amino acids do?"
  type: short-answer
  answer: "After re-esterification inside enterocytes, triglycerides are packaged into chylomicrons — large lipoprotein particles (80–1200 nm) that are too large to pass through the tight junctions and small fenestrations of intestinal capillaries. The lacteals (lymphatic capillaries) have larger, more permeable openings that accommodate chylomicron exocytosis. This structural constraint forces fats through lymphatics. The consequence is that dietary fat enters systemic circulation via the thoracic duct, bypassing the liver's first-pass metabolism — unlike glucose and amino acids, which go directly to the liver via the portal vein."
  explanation: "The size constraint is the mechanistic reason, but the physiological consequence matters equally. Portal delivery of glucose and amino acids allows the liver to immediately process and regulate their systemic levels. Chylomicron delivery via lymphatics means dietary fat reaches peripheral tissues before the liver can act — explaining why postprandial hyperlipidemia is primarily in systemic rather than portal blood, and why fat-soluble drugs and vitamins accumulate differently than water-soluble ones."
```

## Explainer

You already know from epithelial transport that epithelial cells are architecturally polarized — apical membranes face the lumen and are distinct in composition from basolateral membranes facing the bloodstream. The intestinal enterocyte applies this principle with extraordinary specificity. The apical surface is densely packed with **microvilli** forming the **brush border**, amplifying absorptive surface area roughly 600-fold. Embedded in the brush border membrane are digestive enzymes (lactase, sucrase-isomaltase, peptidases) and an array of nutrient transporters, each tuned to a different molecule class. The strategy: break nutrients into absorbable units at the apical surface, import them into the cell using specific transporters, and export them across the basolateral membrane into portal blood or lymph.

For **sugars**, the mechanism depends on the sugar. Glucose and galactose enter through **SGLT1** (Sodium-Glucose Linked Transporter 1) on the apical membrane — a secondary active transporter that co-transports one glucose molecule with two sodium ions, using the sodium gradient maintained by basolateral Na⁺/K⁺-ATPase as the energy source. This allows glucose uptake even against its concentration gradient, essential after a carbohydrate-rich meal when the lumen glucose concentration may still be lower than the cytoplasm. Fructose, however, uses **GLUT5**, a facilitated diffusion transporter that requires no energy — it simply flows down its concentration gradient. Both sugars then exit the cell through **GLUT2** on the basolateral membrane into the portal circulation. This distinction explains why fructose absorption can be overwhelmed (GLUT5 has limited capacity), causing osmotic diarrhea with very high fructose loads.

**Protein absorption** follows the same vectorial logic. Pancreatic proteases cleave luminal proteins into dipeptides, tripeptides, and amino acids. Short peptides enter via **PepT1**, a proton-coupled oligopeptide transporter on the apical membrane — one of the most clinically relevant intestinal transporters because many oral drugs mimic di/tripeptides and exploit it. Amino acids enter through a family of sodium-dependent and independent transporters, each selective for a different chemical class (neutral, cationic, anionic). Intracellular peptidases cleave peptides to free amino acids before export.

**Fat absorption** is the most structurally complex pathway because fats are hydrophobic and cannot be simply dissolved and transported. Bile salts from the liver emulsify dietary triglycerides into small droplets, increasing the surface area for pancreatic lipase to act. Lipase cleaves triglycerides into **2-monoglycerides** and **free fatty acids**, which are then incorporated into **micelles** — small bile-lipid assemblies that ferry the hydrophobic products to the brush border. Monoglycerides and fatty acids diffuse passively across the apical membrane into the enterocyte, where they are immediately re-esterified into triglycerides in the smooth ER. These are packaged with phospholipids, cholesterol, and **apolipoprotein B-48** into large lipoprotein particles called **chylomicrons**, which are too large to enter the portal capillaries. Instead, they are secreted by exocytosis into the **lacteals** — lymphatic capillaries running through each villus — and travel through the thoracic duct to enter systemic circulation, bypassing the liver on first pass. This is why a fatty meal produces a characteristic milky appearance in lymph (chyle) and why fat-soluble vitamins (A, D, E, K) travel the same lymphatic route.
