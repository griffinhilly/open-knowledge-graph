---
id: proximal-tubule-reabsorption-secretion
title: Proximal Tubule Reabsorption and Secretion
domain: biology
course: physiology
prerequisites:
- id: glomerular-filtration-mechanism
  type: hard
- id: active-transport
  type: soft
builds-toward:
- loop-of-henle-concentration-gradient
tags:
- selective-reabsorption
- glucose-reabsorption
- organic-secretion
stage: formal-systems
status: draft
---

# Proximal Tubule Reabsorption and Secretion

## Core Idea
The proximal tubule performs selective reabsorption of glucose, amino acids, sodium, and other filtered nutrients via active and passive transport coupled to the Na+-gradient, while also secreting drugs, organic acids, and excess H+ from peritubular blood into the tubular lumen. These two processes together determine which substances are retained and which are excreted.

## Explainer

From glomerular filtration, you know that the kidney produces about 180 liters of filtrate per day — essentially plasma minus proteins. That filtrate contains everything the body needs: glucose, amino acids, electrolytes, bicarbonate, water. If the nephron simply excreted all of it, you would lose your entire plasma volume in minutes and all your blood glucose in under an hour. The **proximal tubule** prevents this catastrophe by reclaiming roughly 65% of the filtered water, sodium, and solutes before the fluid even reaches the loop of Henle.

The engine driving nearly all proximal tubule reabsorption is the **Na⁺/K⁺-ATPase pump** on the basolateral membrane (the side facing the blood). This pump continuously moves sodium out of the tubular cell and into the interstitial fluid, keeping intracellular sodium concentration low. This creates a steep sodium gradient across the apical membrane (the side facing the tubular lumen), and that gradient is harnessed by a family of **cotransporters** and **exchangers** on the apical surface. Sodium-glucose cotransporters (SGLT2 and SGLT1) carry glucose into the cell by riding sodium's downhill gradient. Sodium-amino acid cotransporters do the same for amino acids. A sodium-hydrogen exchanger (NHE3) swaps sodium inward for hydrogen ions outward, which drives bicarbonate reabsorption (the secreted H⁺ combines with filtered bicarbonate in the lumen to form CO₂ and water, which diffuse into the cell and are reconverted to bicarbonate). In each case, the Na⁺/K⁺-ATPase is the ultimate energy source — ATP hydrolysis creates the sodium gradient, and that gradient powers everything else.

Water follows the solutes. As sodium, glucose, and other solutes are reabsorbed, the osmolarity inside the tubular lumen drops slightly relative to the interstitium. Water then moves out of the lumen by osmosis through **aquaporin-1** channels in both the apical and basolateral membranes. This water reabsorption is so efficient and so tightly coupled to solute reabsorption that the fluid leaving the proximal tubule is still approximately **isosmotic** with plasma — the same concentration, just much less of it. The proximal tubule also reabsorbs most filtered phosphate, citrate, lactate, and small peptides, making it the nephron's primary recovery site.

Running in the opposite direction is **tubular secretion**: the proximal tubule actively pumps certain substances from the peritubular blood into the tubular lumen. Organic anion transporters (OATs) and organic cation transporters (OCTs) on the basolateral membrane take up drugs (like penicillin), toxins, and metabolic waste products (like urate and creatinine) from the blood, and apical transporters then dump them into the lumen. This is physiologically important because some substances are protein-bound in plasma and therefore cannot be filtered at the glomerulus — secretion provides a second route for their elimination. The proximal tubule also secretes hydrogen ions (via NHE3 and H⁺-ATPase), contributing to acid-base balance. Together, reabsorption and secretion in the proximal tubule accomplish the bulk of the nephron's work: recovering what the body needs while adding extra waste to the fluid destined to become urine.
