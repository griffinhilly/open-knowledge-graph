---
id: carbohydrate-digestion-and-monosaccharide-absorption
title: Carbohydrate Digestion and Monosaccharide Absorption
domain: health-and-human-development
course: nutrition-science
prerequisites:
- id: carbohydrate-structure-and-function
  type: hard
- id: nutrient-digestion-and-absorption
  type: hard
- id: carbohydrate-structure-and-classification
  type: soft
- id: digestive-enzyme-secretion-and-regulation
  type: soft
builds-toward:
- glycemic-index-load-and-postprandial-glucose
- glucose-homeostasis-fed-fasted-metabolic-states
tags:
- carbohydrate-digestion
- monosaccharides
- enzymes
- absorption-mechanisms
stage: formal-systems
status: validated
---

# Carbohydrate Digestion and Monosaccharide Absorption

## Core Idea
Carbohydrate digestion begins with salivary amylase in the mouth and continues with pancreatic amylase in the small intestine, cleaving polysaccharides and disaccharides into glucose, fructose, and galactose. Brush-border enzymes (maltase, sucrase, lactase) complete hydrolysis. Active transport via SGLT1 absorbs glucose and galactose; fructose absorption is passive (GLUT5). Absorption rate and completeness determine postprandial glucose response and affect satiety.

## How It's Best Learned
Compare digestion rates of simple sugars, disaccharides, and complex carbohydrates by studying blood glucose curves and satiety ratings after consumption. Examine lactase persistence and individual differences in absorption capacity.

## Common Misconceptions
- Starch is instantly converted to glucose; in fact, enzymatic digestion takes 1–2 hours. - All monosaccharides are absorbed equally fast; fructose and galactose use different transporters and are absorbed more slowly than glucose.

## Questions

```yaml
- question: "After food is swallowed, salivary amylase stops digesting starch. What is the primary reason?"
  type: multiple-choice
  options:
    - "Salivary amylase is physically washed away by stomach secretions"
    - "Salivary amylase is denatured and inactivated by the low pH of stomach acid"
    - "The stomach secretes inhibitors that block salivary amylase activity"
    - "Starch digestion is complete by the time food reaches the stomach"
  answer: 1
  explanation: "Salivary amylase has an optimal pH around 6–7. The stomach's highly acidic environment (pH 1–3) denatures the enzyme, terminating its activity. This is why the stomach is not a major site of carbohydrate digestion. Option D is wrong: starch is not fully digested in the mouth — most remains as oligosaccharides and dextrins when swallowed."

- question: "A person consumes a very large amount of fructose. Some fructose reaches the colon and is fermented by bacteria, causing gas and bloating. What is the most direct biochemical explanation?"
  type: multiple-choice
  options:
    - "The small intestine lacks sufficient brush-border enzymes to cleave fructose from sucrose"
    - "Fructose absorption via GLUT5 is passive facilitated diffusion and can be saturated by high concentrations"
    - "Excess fructose inhibits SGLT1, reducing glucose absorption and leaving fructose unabsorbed"
    - "The pancreas cannot produce enough amylase to digest fructose-containing polysaccharides"
  answer: 1
  explanation: "Fructose is a monosaccharide — no brush-border enzyme is needed. The bottleneck is the GLUT5 transporter, which is a facilitated diffusion transporter with a fixed capacity. At high lumen concentrations, GLUT5 saturates and cannot transport all available fructose, leaving the remainder to pass to the colon. Options A and D are wrong because fructose is already a monosaccharide requiring no enzymatic digestion."

- question: "Lactase deficiency causes gastrointestinal symptoms not because lactose itself is toxic, but because undigested lactose reaches the colon and is fermented by bacteria."
  type: true-false
  answer: true
  explanation: "Without functional lactase, intact lactose passes through the small intestine unabsorbed and enters the colon, where resident bacteria ferment it, producing gas (hydrogen, methane) and short-chain fatty acids. The osmotic effect of unabsorbed lactose also draws water into the lumen, causing diarrhea. This accurately describes the mechanism of lactose intolerance."

- question: "Glucose and fructose are both monosaccharides, so they are absorbed from the intestinal lumen by the same transporter."
  type: true-false
  answer: false
  explanation: "Glucose (and galactose) are absorbed by SGLT1, a sodium-linked active transporter that moves glucose against a concentration gradient. Fructose uses GLUT5, a passive facilitated diffusion transporter. This mechanistic difference makes glucose absorption faster and more efficient, while fructose absorption is slower, concentration-dependent, and can be overwhelmed by large loads. All three monosaccharides then exit the enterocyte via GLUT2."

- question: "Why does glucose absorption remain efficient even when blood glucose levels are already high, while fructose absorption slows down when large amounts are consumed at once?"
  type: short-answer
  answer: "Glucose absorption via SGLT1 is active transport coupled to sodium's electrochemical gradient, maintained by the Na/K-ATPase pump. SGLT1 can move glucose from the intestinal lumen into the cell even against a concentration gradient — it does not depend on a lumen-to-blood concentration difference. Fructose enters via GLUT5 through facilitated diffusion, which requires fructose to be more concentrated in the lumen than in the cell. When large amounts of fructose flood the lumen simultaneously, GLUT5 becomes saturated — it has a finite number of transporter molecules — and the surplus remains in the lumen."
  explanation: "The key distinction is active versus passive transport. Active transporters can work against gradients and are not limited by ambient concentration differences; passive transporters cannot, and they saturate. This is why SGLT1 ensures efficient glucose absorption under varying conditions, while GLUT5 creates a ceiling on fructose absorption capacity per unit time."
```

## Explainer

From your study of carbohydrate structure and function, you know that dietary carbohydrates range from simple monosaccharides (glucose, fructose, galactose) through disaccharides (sucrose, lactose, maltose) to complex polysaccharides (starch, glycogen, fiber). From your work on nutrient digestion and absorption, you know that large molecules must be broken down to absorbable units before the intestinal epithelium can take them up. Carbohydrate digestion is the process that bridges these two facts: it is a sequential enzymatic disassembly that converts complex carbohydrates down to individual monosaccharides.

Digestion begins in the mouth, where **salivary amylase** (α-amylase) cleaves internal α-1,4-glycosidic bonds in starch and glycogen, producing shorter chains called **maltose** (a disaccharide) and **dextrins** (branched oligosaccharides). This oral phase is brief — food is swallowed quickly — and the enzyme is inactivated by stomach acid once it reaches the stomach. The stomach itself contributes no carbohydrate enzymes; this is why the stomach is not a major site of carbohydrate digestion. The main action resumes in the **duodenum**, where **pancreatic amylase** continues cleaving α-1,4 bonds in any remaining starch, producing maltose, maltotriose, and α-limit dextrins (branched fragments that α-amylase cannot fully resolve). The key point: at this stage, even after pancreatic amylase, you still do not have free glucose — you have small oligosaccharides and disaccharides.

The final hydrolysis step occurs at the **brush border** of the small intestinal epithelium, performed by membrane-bound enzymes named for their substrates. **Maltase** cleaves maltose into two glucose units; **sucrase** cleaves sucrose into glucose + fructose; **lactase** cleaves lactose into glucose + galactose; **isomaltase** cleaves the α-1,6 branch points of the α-limit dextrins. This is why lactase deficiency causes lactose intolerance — without functional lactase, lactose reaches the colon intact, where gut bacteria ferment it, producing gas, osmotic diarrhea, and bloating. The enzyme rather than the substrate is the rate-limiting step.

Once monosaccharides are free in the intestinal lumen, absorption occurs by two different mechanisms depending on the sugar. Glucose and galactose are absorbed by **SGLT1** (Sodium-Glucose Linked Transporter 1), an **active transport** protein that co-transports one glucose and two sodium ions simultaneously. Because it runs on the electrochemical gradient for sodium (maintained by the Na/K-ATPase on the basolateral side), SGLT1 can transport glucose against a concentration gradient — this is why glucose absorption is so efficient and rapid even when lumen concentrations are low. Fructose, in contrast, uses **GLUT5**, a **facilitated diffusion** transporter that moves fructose passively down its concentration gradient. This is slower, saturable, and explains why consuming large amounts of fructose (e.g., from high-fructose corn syrup) can overwhelm GLUT5 capacity, leaving unabsorbed fructose to reach the colon. Once inside the enterocyte, all three monosaccharides exit into the portal bloodstream via **GLUT2**, a low-affinity, high-capacity bidirectional transporter on the basolateral membrane. The glucose then travels to the liver via the portal vein, triggering the insulin response and downstream metabolic consequences you will study when you examine postprandial glucose regulation.
