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
status: validated
---

# Proximal Tubule Reabsorption and Secretion

## Core Idea
The proximal tubule performs selective reabsorption of glucose, amino acids, sodium, and other filtered nutrients via active and passive transport coupled to the Na+-gradient, while also secreting drugs, organic acids, and excess H+ from peritubular blood into the tubular lumen. These two processes together determine which substances are retained and which are excreted.

## Questions

```yaml
- question: "A toxin selectively and completely inhibits Na⁺/K⁺-ATPase in proximal tubule cells. Which consequence is most directly predicted by understanding the reabsorption mechanism?"
  type: multiple-choice
  options:
    - "Glucose and amino acids accumulate inside tubule cells because they can no longer exit into the blood"
    - "Glucose and amino acids remain in the tubular filtrate and are lost in urine, because the sodium gradient driving cotransporter uptake collapses"
    - "Water reabsorption increases to compensate for the loss of solute transport"
    - "Secretion of drugs and organic acids into the lumen increases because the apical transporters are now unregulated"
  answer: 1
  explanation: "The Na⁺/K⁺-ATPase is the ultimate energy source for all Na⁺-coupled transport. By maintaining low intracellular Na⁺, it creates the gradient that SGLT2, SGLT1, and amino acid cotransporters harness to pull glucose and amino acids from the lumen into the cell. Block the ATPase, and intracellular Na⁺ rises, the gradient collapses, and cotransporters stop working. Glucose and amino acids that would normally be reabsorbed remain in the filtrate and appear in urine (glucosuria, aminoaciduria). Option A confuses direction — the ATPase powers uptake from lumen to cell, not from cell to blood."

- question: "A patient takes penicillin, which is more than 60% protein-bound in plasma. Despite this, the drug is rapidly cleared by the kidneys. What mechanism explains this?"
  type: multiple-choice
  options:
    - "Protein-bound penicillin is freely filtered at the glomerulus because the glomerular barrier is not selective for proteins"
    - "Penicillin displaces from albumin inside the glomerular capillary and the free fraction is filtered"
    - "Proximal tubule secretion via organic anion transporters picks up protein-bound penicillin from peritubular blood and delivers it to the tubular lumen for excretion"
    - "Penicillin is reabsorbed and then secreted in a recycling process that concentrates it in the filtrate"
  answer: 2
  explanation: "Protein-bound drugs cannot cross the glomerular filtration barrier — only free (unbound) drug is filtered. Tubular secretion provides an alternative elimination route: OATs on the basolateral membrane of proximal tubule cells actively transport organic anions (including penicillin) from peritubular blood into the cell, and apical transporters then dump them into the lumen. This is physiologically important because it allows elimination of substances that filtration alone cannot handle. It is also clinically relevant — probenecid blocks this OAT-mediated secretion and was historically used to prolong penicillin's half-life."

- question: "The transport of glucose from the tubular lumen into proximal tubule cells is driven by the sodium concentration gradient rather than directly by ATP hydrolysis."
  type: true-false
  answer: true
  explanation: "SGLT2 and SGLT1 are cotransporters that move glucose into the cell by coupling it to the movement of Na⁺ down its concentration gradient. The ATP is consumed one step removed, by the Na⁺/K⁺-ATPase that maintains the low intracellular Na⁺. The cotransporter itself uses no ATP directly — it is 'secondary active transport.' This distinction matters clinically: SGLT2 inhibitors (gliflozins) block glucose reabsorption without directly affecting the ATPase, allowing glucose to spill into urine as a blood sugar–lowering mechanism."

- question: "The proximal tubule generates a large osmotic gradient along its length by reabsorbing solutes faster than water, concentrating the remaining filtrate."
  type: true-false
  answer: false
  explanation: "The proximal tubule reabsorbs solutes and water in nearly equal proportions, so the fluid leaving the proximal tubule remains approximately isosmotic with plasma. Water follows solutes through aquaporin-1 channels by osmosis so efficiently that no significant concentration gradient builds up. Urine concentration happens much later, in the loop of Henle and collecting duct — the proximal tubule's job is volume recovery (reclaiming ~65% of filtered water), not concentration."

- question: "Explain why the Na⁺/K⁺-ATPase is considered the 'engine' of proximal tubule reabsorption, even though it does not directly transport glucose or amino acids."
  type: short-answer
  answer: "The Na⁺/K⁺-ATPase on the basolateral membrane pumps Na⁺ out of tubule cells into the interstitium, keeping intracellular Na⁺ concentration very low. This creates a steep electrochemical gradient for Na⁺ across the apical membrane. Cotransporters like SGLT2 (for glucose) and sodium-amino acid cotransporters exploit this gradient: Na⁺ flows downhill into the cell, and these cotransporters harness that energy to carry glucose or amino acids uphill against their own concentration gradients. The ATPase is the ultimate energy source — without it, the Na⁺ gradient collapses, and all Na⁺-coupled cotransport stops even though those cotransporters themselves use no ATP directly."
  explanation: "This hierarchy — ATPase → Na⁺ gradient → cotransporters — illustrates secondary active transport. It is a common energetic architecture in biology wherever cells need to concentrate substances against their gradients without each transporter needing its own ATP supply."
```

## Explainer

From glomerular filtration, you know that the kidney produces about 180 liters of filtrate per day — essentially plasma minus proteins. That filtrate contains everything the body needs: glucose, amino acids, electrolytes, bicarbonate, water. If the nephron simply excreted all of it, you would lose your entire plasma volume in minutes and all your blood glucose in under an hour. The **proximal tubule** prevents this catastrophe by reclaiming roughly 65% of the filtered water, sodium, and solutes before the fluid even reaches the loop of Henle.

The engine driving nearly all proximal tubule reabsorption is the **Na⁺/K⁺-ATPase pump** on the basolateral membrane (the side facing the blood). This pump continuously moves sodium out of the tubular cell and into the interstitial fluid, keeping intracellular sodium concentration low. This creates a steep sodium gradient across the apical membrane (the side facing the tubular lumen), and that gradient is harnessed by a family of **cotransporters** and **exchangers** on the apical surface. Sodium-glucose cotransporters (SGLT2 and SGLT1) carry glucose into the cell by riding sodium's downhill gradient. Sodium-amino acid cotransporters do the same for amino acids. A sodium-hydrogen exchanger (NHE3) swaps sodium inward for hydrogen ions outward, which drives bicarbonate reabsorption (the secreted H⁺ combines with filtered bicarbonate in the lumen to form CO₂ and water, which diffuse into the cell and are reconverted to bicarbonate). In each case, the Na⁺/K⁺-ATPase is the ultimate energy source — ATP hydrolysis creates the sodium gradient, and that gradient powers everything else.

Water follows the solutes. As sodium, glucose, and other solutes are reabsorbed, the osmolarity inside the tubular lumen drops slightly relative to the interstitium. Water then moves out of the lumen by osmosis through **aquaporin-1** channels in both the apical and basolateral membranes. This water reabsorption is so efficient and so tightly coupled to solute reabsorption that the fluid leaving the proximal tubule is still approximately **isosmotic** with plasma — the same concentration, just much less of it. The proximal tubule also reabsorbs most filtered phosphate, citrate, lactate, and small peptides, making it the nephron's primary recovery site.

Running in the opposite direction is **tubular secretion**: the proximal tubule actively pumps certain substances from the peritubular blood into the tubular lumen. Organic anion transporters (OATs) and organic cation transporters (OCTs) on the basolateral membrane take up drugs (like penicillin), toxins, and metabolic waste products (like urate and creatinine) from the blood, and apical transporters then dump them into the lumen. This is physiologically important because some substances are protein-bound in plasma and therefore cannot be filtered at the glomerulus — secretion provides a second route for their elimination. The proximal tubule also secretes hydrogen ions (via NHE3 and H⁺-ATPase), contributing to acid-base balance. Together, reabsorption and secretion in the proximal tubule accomplish the bulk of the nephron's work: recovering what the body needs while adding extra waste to the fluid destined to become urine.
