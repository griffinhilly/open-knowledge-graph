---
id: nutrient-digestion-and-absorption
title: Nutrient Digestion and Absorption
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: digestive-anatomy-and-motility
  type: hard
- id: nutrient-absorption-and-transport
  type: hard
- id: active-transport
  type: soft
- id: passive-transport
  type: soft
- id: digestive-system-overview
  type: soft
- id: enzyme-structure-and-function
  type: soft
tags:
- carbohydrates
- proteins
- lipids
- villi
- microvilli
- portal-circulation
stage: formal-systems
status: validated
---

# Nutrient Digestion and Absorption

## Core Idea
Macronutrient digestion involves mechanical breakdown and enzymatic hydrolysis: carbohydrates are cleaved by salivary and pancreatic amylases then brush border enzymes into monosaccharides; proteins are denatured by stomach acid and hydrolyzed by pepsin, then pancreatic proteases into amino acids and small peptides; lipids are emulsified by bile salts and hydrolyzed by pancreatic lipase into fatty acids and monoglycerides. Absorption occurs primarily in the jejunum via enterocytes bearing microvilli (brush border) that increase absorptive area ~600-fold. Sugars and amino acids enter the portal circulation; long-chain fatty acids are packaged as chylomicrons and enter lymphatic lacteals before reaching the bloodstream.

## How It's Best Learned
Create a table with columns: nutrient class, enzymes, site of action, absorbed form, transport route. Then use clinical cases (celiac disease affecting villi, pancreatitis affecting enzyme secretion) to apply it.

## Common Misconceptions
- Fat absorption does NOT enter the portal vein directly; long-chain fats travel via lymphatics as chylomicrons, bypassing first-pass liver metabolism.
- Stomach acid does not digest food chemically in the same way enzymes do — it denatures proteins and activates pepsinogen.

## Questions

```yaml
- question: "After enterocytes in the jejunum absorb long-chain fatty acids and monoglycerides, these lipids reach the bloodstream by:"
  type: multiple-choice
  options:
    - "Entering the portal vein and traveling directly to the liver"
    - "Being packaged into chylomicrons that enter lymphatic lacteals"
    - "Binding to albumin and crossing the basolateral membrane into capillaries"
    - "Being converted to glucose in the enterocyte and entering the portal circulation"
  answer: 1
  explanation: "Long-chain fatty acids are reassembled into triglycerides inside enterocytes and packaged with cholesterol and apolipoproteins into chylomicrons. Because chylomicrons are too large to cross capillary walls, they are secreted into lymphatic lacteals in the villus and travel via the thoracic duct to enter the bloodstream at the subclavian vein — bypassing the liver's first-pass metabolism. Short- and medium-chain fatty acids, by contrast, do enter portal circulation."

- question: "Stomach acid (HCl) digests proteins through enzymatic hydrolysis of peptide bonds."
  type: true-false
  answer: false
  explanation: "HCl does not break peptide bonds enzymatically. Its roles are to denature proteins (unfolding them so enzymes can access cleavage sites) and to convert the inactive zymogen pepsinogen into active pepsin by cleaving an inhibitory peptide. Pepsin — not acid — then performs enzymatic hydrolysis of peptide bonds. This distinction matters clinically: antacids neutralize acid but do not directly inhibit proteolysis."

- question: "Why must lipids be emulsified by bile salts before pancreatic lipase can efficiently digest them in the small intestine?"
  type: short-answer
  answer: "Lipids are hydrophobic and aggregate into large fat droplets in the aqueous intestinal environment, exposing only a small surface to the surrounding fluid. Bile salts are amphipathic — they have both hydrophobic and hydrophilic regions — and break large droplets into tiny micelles, dramatically increasing the total surface area available for pancreatic lipase to bind and act. Without emulsification, lipase can only access the outer layer of large globules, making digestion far too slow."
  explanation: "This is an application of surface chemistry: enzymatic reactions occur at interfaces, so surface area is the rate-limiting factor. Bile salts do not digest lipids themselves; they are a physical delivery system that optimizes the conditions for lipase activity. Absence of bile (e.g., bile duct obstruction) leads to fat malabsorption and steatorrhea even when pancreatic lipase secretion is normal."
```

## Explainer

By the time food reaches the small intestine, it has already been partially processed — chewed, mixed with salivary amylase in the mouth, and churned with stomach acid and pepsin in the stomach. But the small intestine, particularly the jejunum, is where the majority of nutrient digestion is completed and virtually all absorption occurs. Understanding this process requires tracking three separate nutrient classes — carbohydrates, proteins, and lipids — through their distinct enzymatic and transport pathways.

Carbohydrate digestion begins in the mouth with salivary amylase, which cleaves starch into smaller oligosaccharides. Pancreatic amylase continues this work in the duodenum. But amylases cannot break the final bonds between individual monosaccharides — that work falls to brush border enzymes (maltase, sucrase, lactase) embedded in the microvilli of enterocytes. These enzymes finish the job, releasing glucose, galactose, and fructose, which are then transported into enterocytes by SGLT1 (sodium-glucose co-transport) and GLUT5, cross the basolateral membrane via GLUT2, and enter the portal vein to reach the liver.

Protein digestion follows a similar pattern of enzyme relay. Stomach acid denatures proteins and converts pepsinogen to pepsin, which begins cleaving peptide bonds. In the duodenum, pancreatic proteases — trypsin, chymotrypsin, elastase, and carboxypeptidases — continue hydrolysis. Brush border peptidases complete the breakdown to amino acids and small di- and tripeptides. These are absorbed by specific transporters and also enter the portal circulation.

Lipid digestion requires an additional step: emulsification. Because fats are hydrophobic, they clump into large globules that offer minimal surface area for enzymes. Bile salts secreted from the liver (stored in the gallbladder) are amphipathic — they surround fat droplets and break them into tiny micelles, vastly increasing the surface available to pancreatic lipase. Lipase then cleaves triglycerides into fatty acids and monoglycerides. Inside enterocytes, long-chain fatty acids are reassembled into triglycerides, packaged into chylomicrons, and secreted into lymphatic lacteals — not the portal vein — traveling through the lymphatic system before entering the bloodstream near the heart.

The architectural feature that makes the jejunum so effective at absorption is the amplification of surface area at three scales: folds of Kerckring (large mucosal folds), villi (finger-like projections), and microvilli on enterocytes (the "brush border") combine to increase absorptive surface area roughly 600-fold compared to a smooth tube. Clinical disruptions to this architecture — villous atrophy in celiac disease, or lipase deficiency in pancreatitis — predictably impair absorption of specific nutrient classes in ways that directly map to the pathways described here.
