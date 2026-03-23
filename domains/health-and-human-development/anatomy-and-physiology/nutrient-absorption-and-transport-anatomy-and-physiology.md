---
id: nutrient-absorption-and-transport-anatomy-and-physiology
title: Nutrient Absorption and Transport
domain: health-and-human-development
course: anatomy-and-physiology
prerequisites:
- id: digestive-enzyme-function-and-control
  type: hard
- id: nutrient-digestion-and-absorption
  type: hard
- id: carrier-proteins-and-conformational-change
  type: hard
- id: membrane-transport-mechanisms
  type: hard
- id: intestinal-absorption-nutrient-transport
  type: hard
builds-toward:
- nutrient-storage-and-metabolism
tags:
- absorption
- intestinal-epithelium
- active-transport
- carrier-mediated
stage: formal-systems
status: draft
---

# Nutrient Absorption and Transport

## Core Idea
The small intestine absorbs digestion products through selective mechanisms: monosaccharides and amino acids via active transport (SGLT1, amino acid transporters), fats via micelle absorption and chylomicron formation, minerals via specific transporters (iron, calcium). The large surface area of villi and microvilli, combined with tight epithelial junctions, creates an efficient barrier that absorbs nutrients while excluding harmful substances.

## Questions

```yaml
- question: "After a high-fat meal, where do long-chain fatty acids first enter the bloodstream following absorption from the small intestine?"
  type: multiple-choice
  options:
    - "Directly into the portal vein from the intestinal epithelium, like glucose and amino acids"
    - "Into the portal vein after conversion to ketone bodies in the enterocyte"
    - "Into the thoracic duct via lymphatic lacteals, packaged as chylomicrons, then into the subclavian vein"
    - "Into the hepatic vein, after first being processed in the liver"
  answer: 2
  explanation: "Long-chain fatty acids follow a fundamentally different route from carbohydrates and amino acids. Inside the enterocyte, they are re-esterified into triglycerides, packaged with cholesterol, phospholipids, and apolipoproteins into chylomicrons, and secreted by exocytosis into lymphatic lacteals. Chylomicrons are too large to enter capillaries directly. They travel via lymphatic vessels to the thoracic duct, which empties into the left subclavian vein — bypassing the portal circulation and the liver entirely until after distribution to peripheral tissues. Short- and medium-chain fatty acids, being more water-soluble, do enter the portal blood directly."

- question: "A patient has a genetic defect that severely impairs Na⁺/K⁺-ATPase activity in intestinal epithelial cells. Which nutrient absorption process would be most directly compromised?"
  type: multiple-choice
  options:
    - "Long-chain fatty acid absorption (chylomicron pathway)"
    - "Glucose and amino acid absorption via sodium-coupled cotransporters like SGLT1"
    - "Fructose absorption via GLUT5 facilitated diffusion"
    - "Short-chain fatty acid absorption by passive diffusion"
  answer: 1
  explanation: "SGLT1 (sodium-glucose linked transporter 1) is a secondary active transporter: it uses the inward sodium gradient to cotransport glucose into the enterocyte. That sodium gradient is maintained by the basolateral Na⁺/K⁺-ATPase, which continuously pumps sodium out of the cell. If Na⁺/K⁺-ATPase is impaired, the sodium gradient collapses, and SGLT1 cannot drive glucose (or galactose) uptake. Many amino acid transporters are similarly sodium-dependent. In contrast, fructose enters via GLUT5 (facilitated diffusion, no sodium), fatty acids diffuse passively across the lipid bilayer, and chylomicron formation is an intracellular process unrelated to sodium gradients."

- question: "Long-chain fatty acids absorbed in the small intestine are packaged into chylomicrons and enter the lymphatic system rather than the portal blood directly."
  type: true-false
  answer: true
  explanation: "This is a defining feature of fat absorption and a key distinction from carbohydrate and amino acid absorption. Long-chain fatty acids are hydrophobic and cannot enter capillaries as free molecules. Inside enterocytes they are re-esterified into triglycerides, assembled into chylomicrons (large lipoprotein particles), and secreted into lymphatic lacteals. The lymphatic route bypasses the liver on the first pass, delivering fatty acids to peripheral tissues (muscle, adipose) via the thoracic duct before the remnants eventually reach the liver. This is why fat absorption causes a transient 'milky' lymph (chyle) in the lacteals after a fatty meal."

- question: "The body regulates iron balance primarily by adjusting urinary excretion of excess iron, similar to how it handles sodium and potassium imbalances."
  type: true-false
  answer: false
  explanation: "The body has no active pathway to excrete excess iron through the urine (or any other route). Iron homeostasis is controlled almost entirely at the level of intestinal absorption, regulated by the liver hormone hepcidin. When iron stores are adequate or elevated, hepcidin is secreted, which inhibits ferroportin (the iron export protein on enterocytes), trapping iron in enterocytes that are then shed into the gut lumen. When iron is scarce, hepcidin falls and absorption increases. This is why iron overload disorders (like hereditary hemochromatosis) are clinically serious — the excess iron cannot simply be excreted; it accumulates in organs and causes damage."

- question: "Explain why iron absorption in the small intestine is tightly regulated by hepcidin, while glucose absorption is not similarly regulated at the intestinal level. What does this reveal about a fundamental difference in how the body handles these two nutrients?"
  type: short-answer
  answer: "The body can dispose of excess glucose through insulin-stimulated uptake into cells, glycogen synthesis, and conversion to fat — multiple downstream pathways handle glucose excess. More fundamentally, cells use glucose continuously, so transient excess is rapidly metabolized. Iron, by contrast, has no dedicated excretion pathway: once absorbed, the only way iron leaves the body is through bleeding or cell turnover. This makes the intestine the sole control point for iron homeostasis. If absorption were unregulated (like glucose), iron would accumulate in organs over time, causing oxidative damage (hemochromatosis). Hepcidin-regulated absorption prevents this by gatekeeping entry rather than increasing excretion. The general principle: when a nutrient lacks an excretion pathway, absorption must serve as the regulatory valve."
  explanation: "This comparison reveals a design principle in physiology: regulatory control is placed where it is most effective and where the cost of dysregulation is highest. For iron — which is toxic in excess, essential in adequate amounts, and unexcretable — the only viable control point is absorption. For glucose — which is rapidly distributed, stored, and metabolized — systemic hormonal regulation (insulin, glucagon) handles excess after absorption. Understanding this explains the clinical consequences of regulation failure: iron overload from unregulated absorption vs. hyperglycemia from inadequate insulin signaling."
```

## Explainer

You have studied membrane transport mechanisms — the difference between passive diffusion, facilitated diffusion, and active transport — and you know that **carrier proteins** change conformation to shuttle specific molecules across membranes. Those principles apply directly to the brush border of the small intestinal epithelium, where digested food must cross from the gut lumen into the body. The intestine is not a passive sieve; it is a selective barrier, and the selectivity is built into the transporters embedded in its cells.

**Glucose** and **galactose** enter intestinal epithelial cells via **SGLT1** (sodium-glucose linked transporter 1), a classic secondary active transporter: the inward sodium gradient maintained by the basolateral Na⁺/K⁺-ATPase drives sodium in, and glucose hitchhikes along. This is the same cotransport class you encountered in renal proximal tubule glucose reabsorption. Fructose uses **GLUT5** (facilitated diffusion, no sodium). All three monosaccharides exit the basolateral membrane into portal blood via **GLUT2**. Amino acids use a family of sodium-dependent and sodium-independent transporters, with different carriers specializing in neutral, acidic, and basic amino acids — reflecting the chemical diversity of the amino acid pool.

Fat absorption follows an entirely different pathway because fatty acids are hydrophobic. Long-chain fatty acids and monoglycerides exit micelles, diffuse across the brush border membrane passively, and are **re-esterified** into triglycerides inside the endoplasmic reticulum of the epithelial cell. Those triglycerides are packaged with cholesterol, phospholipids, and **apolipoproteins** into **chylomicrons** — lipoprotein particles too large to enter capillaries directly. Chylomicrons are secreted by exocytosis into lymphatic lacteals and enter the bloodstream through the thoracic duct. Short- and medium-chain fatty acids, being more water-soluble, bypass this route and enter portal blood directly.

The physical architecture of the small intestine amplifies absorption enormously. The mucosa is folded into **circular folds (plicae circulares)**, each covered with finger-like **villi**, and each enterocyte surface covered with **microvilli** forming the brush border. This three-tier folding multiplies absorptive surface area roughly 600-fold — from roughly 0.5 m² to approximately 200–250 m² for a smooth tube of the same length. **Tight junctions** between epithelial cells enforce selectivity, preventing back-leakage of absorbed nutrients and blocking luminal bacteria from entering the bloodstream.

Mineral absorption adds yet another layer of regulation. **Iron** absorption is controlled at the intestinal level because the body has no active excretion pathway — absorption is the only control point. Enterocytes absorb ferrous iron (Fe²⁺) via **DMT1**, reduce dietary ferric iron (Fe³⁺) with brush-border duodenal cytochrome b, and export iron into blood via **ferroportin**, whose expression is regulated by the liver hormone **hepcidin**. **Calcium** absorption uses a vitamin D-dependent transcellular pathway (via TRPV6 channels and calbindin) as well as a paracellular route; vitamin D deficiency directly impairs calcium uptake. These micromineral systems illustrate a general principle: unlike macronutrients where the gut absorbs as much as arrives, mineral absorption is hormonally regulated to maintain systemic homeostasis.
