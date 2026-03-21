---
id: intestinal-absorption-nutrient-transport
title: Intestinal Absorption and Nutrient Transport
domain: biology
course: physiology
prerequisites:
- id: nutrient-absorption-and-transport
  type: hard
- id: intestinal-brush-border-digestion
  type: soft
builds-toward:
- gastrointestinal-secretion-motility
tags:
- intestinal
- absorption
- transport
- nutrients
- epithelium
stage: advanced
status: draft
---

# Intestinal Absorption and Nutrient Transport

## Core Idea
The small intestine absorbs most nutrients via specific transporters: glucose and galactose by active transport, fructose by facilitated diffusion, amino acids by cotransporters. Fat is emulsified by bile and absorbed as monoglycerides and fatty acids, then resynthesized into triglycerides for packaging into chylomicrons. The intestinal epithelium continuously renews (every 3-5 days) and maintains a selective barrier via tight junctions.

## Questions

```yaml
- question: "A drug blocks the Na⁺/K⁺-ATPase on the basolateral membrane of intestinal enterocytes. Which nutrient's absorption would be most directly impaired?"
  type: multiple-choice
  options:
    - "Fructose, because it requires sodium cotransport to cross the apical membrane"
    - "Dietary fat, because micelle formation depends on the sodium gradient"
    - "Glucose, because its apical transport via SGLT1 is driven by the sodium gradient maintained by Na⁺/K⁺-ATPase"
    - "All nutrients equally, because the Na⁺/K⁺-ATPase powers the general absorptive machinery"
  answer: 2
  explanation: "SGLT1 (the glucose/galactose transporter on the apical membrane) is a secondary active transporter: it uses the sodium electrochemical gradient as its energy source, pulling glucose into the cell as sodium flows down its gradient. The Na⁺/K⁺-ATPase on the basolateral side maintains this sodium gradient by continuously pumping sodium out of the cell. Block the ATPase, sodium accumulates inside, the gradient collapses, and SGLT1 can no longer drive glucose uptake against its concentration gradient. Fructose uses GLUT5 (facilitated diffusion, no sodium required) and would be largely unaffected. Fat absorption is passive and also unaffected."

- question: "Why do absorbed dietary fats enter the lymphatic system (via lacteals) rather than flowing directly into blood capillaries like glucose and amino acids?"
  type: multiple-choice
  options:
    - "Fat is chemically incompatible with blood plasma and would cause clotting if it entered directly"
    - "Chylomicrons are too large to cross the basement membrane of blood capillaries, but can enter the more permeable lacteals"
    - "The portal vein cannot transport lipids, so an alternative route to the liver is needed"
    - "Fat-soluble vitamins require a low-oxygen environment that only the lymphatics provide"
  answer: 1
  explanation: "After reassembly in the smooth endoplasmic reticulum, triglycerides are packaged into chylomicrons — lipoprotein particles that are too large (typically 75–1200 nm diameter) to squeeze through the tight junctions and basement membranes of blood capillaries. Lacteals, the lymphatic capillaries within intestinal villi, have loose junctions and a more permeable structure that allows chylomicrons to enter. The chylomicron-laden lymph travels through the thoracic duct and empties into the bloodstream at the subclavian vein. This is why fatty meals temporarily produce a milky-white lymph (chyle) in the lacteals."

- question: "Fructose absorption has a lower intestinal capacity than glucose absorption because fructose uses facilitated diffusion (GLUT5) rather than active transport (SGLT1)."
  type: true-false
  answer: true
  explanation: "Active transport via SGLT1 can move glucose against its concentration gradient, maintaining a steep inward gradient regardless of how much glucose is already inside the cell. Facilitated diffusion via GLUT5 can only move fructose down its concentration gradient, and transport rate plateaus once the concentration gradient is small. This capacity difference explains why excessive fructose intake can overwhelm the system, with unabsorbed fructose reaching the colon where it is fermented by bacteria — producing gas, osmotic water pull, and diarrhea."

- question: "Dietary fat is absorbed into the bloodstream in the same way as glucose — by crossing the intestinal epithelium and entering capillaries in the intestinal villi."
  type: true-false
  answer: false
  explanation: "The paths are fundamentally different. Glucose is a small, water-soluble molecule that crosses the apical membrane via SGLT1, moves through the enterocyte, exits via GLUT2 on the basolateral side, and enters blood capillaries directly. Fat is hydrophobic and must be solubilized by bile salts into micelles before it can approach the brush border. Once absorbed, fatty acids are reassembled into triglycerides, packaged into chylomicrons in the smooth ER, and secreted into lacteals (lymphatic capillaries) — not blood capillaries. Chylomicrons eventually reach the blood via the thoracic duct, bypassing the portal circulation entirely."

- question: "Why does blocking the sodium gradient impair glucose absorption but not fructose absorption, even though both are monosaccharides absorbed by the same enterocytes?"
  type: short-answer
  answer: "Glucose and galactose cross the apical membrane via SGLT1, a secondary active transporter that couples glucose uptake to the flow of sodium ions down their electrochemical gradient. This gradient is maintained by the Na⁺/K⁺-ATPase pumping sodium out of the cell. If the gradient is disrupted, SGLT1 cannot function and glucose cannot be actively absorbed. Fructose, by contrast, uses GLUT5 — a facilitated diffusion transporter that requires no sodium and no energy source beyond the fructose concentration gradient itself. Disrupting the sodium gradient leaves GLUT5 fully functional and fructose absorption unaffected."
  explanation: "This contrast illustrates that transport mechanism is determined by the transporter's biochemistry, not by the nutrient category. Two monosaccharides with similar molecular size can use fundamentally different transport systems with different energy requirements and regulatory properties — a key principle of membrane transport physiology."
```

## Explainer

From your earlier study of nutrient absorption and brush border digestion, you know that the small intestine breaks macromolecules into absorbable units — monosaccharides, amino acids, and lipid fragments — at the epithelial surface. The next question is: how do these molecules actually cross the intestinal wall and enter the bloodstream? The answer is not a single mechanism but a set of **specific transport systems**, each matched to the chemical properties of what it carries.

**Carbohydrate absorption** illustrates the principle clearly. Glucose and galactose are absorbed by **SGLT1** (sodium-glucose linked transporter 1) on the apical (lumen-facing) membrane of enterocytes. This is secondary active transport: sodium ions flow down their concentration gradient (maintained by the Na⁺/K⁺-ATPase on the basolateral side), and glucose hitches a ride against its own gradient. Think of it like a revolving door powered by the sodium stream — glucose gets pulled through even when its concentration inside the cell is already higher than in the lumen. Once inside the enterocyte, glucose exits through **GLUT2** transporters on the basolateral membrane into the capillary blood by facilitated diffusion. Fructose takes a different route entirely: it crosses the apical membrane via **GLUT5** (facilitated diffusion, no sodium required) and exits basolaterally through GLUT2. This is why fructose absorption has a lower capacity than glucose absorption and why excessive fructose intake can overwhelm the system, causing osmotic diarrhea.

**Fat absorption** is fundamentally different because lipids are hydrophobic and cannot dissolve in the aqueous environment of the intestinal lumen. Bile salts (from the liver and gallbladder) solve this problem by forming **mixed micelles** — tiny aggregates with hydrophobic interiors that shuttle monoglycerides, fatty acids, cholesterol, and fat-soluble vitamins to the brush border surface. At the membrane, lipids diffuse out of the micelles and cross into the enterocyte (largely by passive diffusion, aided by fatty acid transport proteins). Inside the cell, the process reverses: monoglycerides and fatty acids are reassembled into **triglycerides** in the smooth endoplasmic reticulum, packaged with cholesterol and apolipoprotein B-48 into large lipoprotein particles called **chylomicrons**, and secreted into the lacteals (lymphatic capillaries) rather than directly into blood capillaries. This lymphatic route is necessary because chylomicrons are too large to enter blood capillaries directly; they eventually reach the bloodstream via the thoracic duct.

The intestinal epithelium that performs all this work is one of the most rapidly renewing tissues in the body, replacing itself every **3–5 days**. Stem cells at the base of intestinal crypts continuously divide and produce new enterocytes that migrate upward along the villus, mature, perform their absorptive function, and are eventually shed from the villus tip into the lumen. This rapid turnover is both a strength — damaged epithelium heals quickly — and a vulnerability, because chemotherapy drugs that target rapidly dividing cells often cause severe intestinal side effects. The tight junctions between enterocytes form a **selective barrier**, allowing paracellular transport of water and small ions while preventing bacteria and large molecules from crossing. When these junctions are disrupted (by inflammation, infection, or conditions like celiac disease), the barrier fails and both absorption efficiency and immune protection are compromised.
