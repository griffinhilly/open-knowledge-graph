---
id: digestive-enzyme-function-and-control
title: Digestive Enzyme Function and Control
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: enzyme-kinetics
  type: hard
- id: digestive-anatomy-and-motility
  type: hard
- id: hormone-receptor-signaling-physiology
  type: soft
builds-toward:
- nutrient-absorption-and-transport
tags:
- enzyme
- digestion
- salivary-amylase
- pepsin
- pancreatic-enzymes
stage: formal-systems
status: validated
---

# Digestive Enzyme Function and Control

## Core Idea
Digestion is controlled by hormonal and neural signals that coordinate enzyme secretion with food arrival. Salivary amylase initiates starch digestion; pepsin in the acidic stomach hydrolyzes protein; pancreatic enzymes (trypsin, amylase, lipase) in the small intestine complete carbohydrate, protein, and fat digestion. Cholecystokinin and secretin coordinate gallbladder contraction with pancreatic secretion and bile flow.

## Questions

```yaml
- question: "Why are pancreatic proteases (trypsin, chymotrypsin, elastase) secreted as inactive zymogens rather than as active enzymes?"
  type: multiple-choice
  options:
    - "To reduce the metabolic energy required for their synthesis"
    - "To prevent the pancreas from digesting itself before the enzymes reach the intestinal lumen"
    - "Because active enzymes would be destroyed by stomach acid before reaching the duodenum"
    - "To allow easier transport through the narrow pancreatic duct"
  answer: 1
  explanation: "Proteolytic enzymes that are active in the secretory cell would digest the cell proteins that produce them — a catastrophic autodigestion. The zymogen design is a safety mechanism: the enzymes are inert until enteropeptidase on the duodenal brush border activates trypsinogen, and active trypsin then cascades to activate the remaining zymogens. Option C is wrong because zymogens would also be stable in acid; the point is protecting the pancreas, not surviving the stomach."

- question: "A patient has a genetic defect that abolishes enteropeptidase (enterokinase) activity on the duodenal brush border. Which consequence best follows?"
  type: multiple-choice
  options:
    - "All protein digestion fails because pepsin also requires enteropeptidase for activation"
    - "Only trypsin fails to activate; chymotrypsin and elastase self-activate from stomach acid"
    - "Pancreatic proteases including trypsin, chymotrypsin, and elastase remain as inactive zymogens in the duodenum"
    - "Protein digestion is delayed but ultimately complete once pancreatic acid activates the zymogens"
  answer: 2
  explanation: "Enteropeptidase activates trypsinogen to trypsin, and trypsin is the master activator that converts all the other pancreatic zymogens in a cascade. Without enteropeptidase, the cascade never starts, leaving all pancreatic proteases inactive. Option A is wrong because pepsin is activated by gastric acid and autocatalysis — it has nothing to do with enteropeptidase. Option D is wrong because the pancreatic zymogens are designed to resist acid activation; they need trypsin."

- question: "Salivary amylase stops digesting starch once it reaches the stomach because pepsin degrades it."
  type: true-false
  answer: false
  explanation: "Salivary amylase is inactivated by the low pH of the stomach (pH 1.5–3.5), not by pepsin. Amylase has an optimal pH range of about 6–7 and is denatured by acid. This pH sensitivity is actually a design feature: the acidic stomach environment is required for pepsin's optimal function and for denaturing dietary proteins to expose their peptide bonds. The handoff from amylase to pepsin is pH-mediated, not protease-mediated."

- question: "Pepsinogen and trypsinogen both exemplify the zymogen mechanism: each protects the cell that secretes it by remaining inactive until it reaches its target compartment."
  type: true-false
  answer: true
  explanation: "Yes — both are inactive precursors for the same reason. Pepsinogen is secreted by gastric chief cells and activated by hydrochloric acid (and autocatalytically by pepsin) once in the stomach lumen. Trypsinogen is secreted by the pancreas and activated only after enteropeptidase in the duodenum initiates the cascade. In both cases, the zymogen design prevents the enzyme from destroying the cell that made it."

- question: "Why must bile salts emulsify dietary fat before pancreatic lipase can digest it efficiently, and what structural feature of fat makes emulsification necessary?"
  type: short-answer
  answer: "Dietary fats are hydrophobic and coalesce into large globules that minimize surface area. Lipase is a water-soluble enzyme that can only act at the water-fat interface. Large globules have very little surface area relative to their volume, severely limiting lipase access. Bile salts are amphipathic molecules that insert their hydrophobic ends into fat droplets and their hydrophilic ends into water, breaking large globules into microscopic droplets — dramatically increasing the surface area available for lipase action."
  explanation: "Colipase, secreted alongside pancreatic lipase, also plays a role by anchoring lipase to the lipid-bile salt interface. This is a general principle: enzymes that act on insoluble substrates require mechanisms to maximize the interface between the aqueous enzyme and the substrate. Emulsification is the digestive system's solution to this geometry problem."
```

## Explainer

From your study of enzyme kinetics, you know that enzymes are biological catalysts — proteins with active sites shaped to bind specific substrates, lower activation energy, and speed reactions without being consumed. Digestive enzymes apply these principles to a logistical problem: a large, mixed bolus of food must be broken into absorbable monomers (glucose, amino acids, fatty acids) as it travels through a tube roughly nine meters long. The system solves this by staging different enzymes along the tract, each tuned to the pH and substrate conditions of its specific region.

**Salivary amylase** begins starch hydrolysis in the mouth, cleaving α-1,4 glycosidic bonds between glucose units. It stops working when it reaches the acidic stomach — this is not a flaw but a design feature, since the stomach's low pH is needed for the next enzyme. **Pepsinogen**, secreted by chief cells in the gastric mucosa, is a zymogen — an inactive precursor — that is converted to active **pepsin** by hydrochloric acid and by pepsin itself (autocatalytic activation). This is a critical safety mechanism: you cannot store active protein-cleaving enzymes in the cells that secrete them without destroying those cells. The acid environment (pH 1.5–3.5) denatures most dietary proteins, unfolding them and making their peptide bonds accessible to pepsin.

When partially digested chyme enters the duodenum, it triggers the release of two hormones you know from your prerequisite on hormone-receptor signaling: **secretin**, released in response to acid, stimulates the pancreas to secrete bicarbonate-rich fluid that neutralizes the acid; **cholecystokinin (CCK)**, released in response to fats and protein, stimulates pancreatic enzyme secretion and gallbladder contraction. The pancreas responds by releasing a suite of zymogens — **trypsinogen**, **chymotrypsinogen**, **proelastase** — plus active amylase and lipase. Trypsinogen is activated by **enteropeptidase** (enterokinase) on the duodenal brush border, and active trypsin then activates the other zymogens in a cascade. This cascade structure ensures enzymes are not activated until they reach the intestinal lumen, protecting the pancreas from autodigestion.

**Pancreatic lipase** presents a unique challenge: fats are hydrophobic and form droplets that minimize surface area, but enzymes work at surfaces. Bile salts from the gallbladder **emulsify** fat globules into microscopic droplets, dramatically increasing surface area and allowing lipase to work efficiently. Colipase, a cofactor secreted with pancreatic lipase, anchors lipase to the lipid-bile salt interface. The integrated result of this orchestrated system is that by the mid-jejunum, carbohydrates are reduced to monosaccharides, proteins to dipeptides and amino acids, and fats to monoglycerides and fatty acids — all in forms ready for transport across the intestinal epithelium.
