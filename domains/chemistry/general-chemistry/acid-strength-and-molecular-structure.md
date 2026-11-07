---
id: acid-strength-and-molecular-structure
title: Acid Strength and Molecular Structure
domain: chemistry
course: general-chemistry
prerequisites:
- id: acid-base-strength-ka-kb-calculations
  type: hard
- id: electronegativity-and-bond-polarity
  type: hard
- id: bond-energy-and-enthaly
  type: soft
- id: resonance-structures
  type: soft
- id: periodic-trends
  type: soft
builds-toward:
- acidity-organic-compounds-pka
tags:
- acid strength
- binary acids
- oxoacids
- bond polarity
- conjugate base stability
stage: formal-systems
status: validated
---

# Acid Strength and Molecular Structure

## Core Idea
How strongly a molecule gives up a proton depends on its structure. For binary acids H–X, strength rises down a group because the H–X bond gets longer and weaker, and rises across a period because X becomes more electronegative. For oxoacids, strength rises with the electronegativity of the central atom and with the number of oxygen atoms not bonded to hydrogen, because both pull electron density from the O–H bond and stabilize the conjugate base.

## How It's Best Learned
Sort acids into families and compare only within a family: HF to HI, then CH₄ to HF, then HOCl to HClO₄, then HOCl, HOBr, HOI. For each pair, ask which effect dominates, bond strength or electron withdrawal. Draw the conjugate bases with resonance structures to see where the negative charge goes.

## Common Misconceptions
- The more electronegative the halogen, the stronger the hydrohalic acid, so HF is the strongest. (Down a group, bond strength dominates; HF is a weak acid in water and HI is the strongest of the four.)
- Acid strength depends only on how polar the H–X bond is. (Bond strength and the stability of the conjugate base also matter, and they can outweigh polarity.)
- Adding oxygen atoms makes an acid stronger because there are more hydrogens to lose. (In HOCl, HClO₂, HClO₃ and HClO₄ there is only one acidic hydrogen; the extra oxygens strengthen the acid by withdrawing electron density and spreading the negative charge of the anion.)

## Questions

```yaml
- question: "Which is the strongest acid in water?"
  type: multiple-choice
  options: ["HF", "HCl", "HBr", "HI"]
  answer: 3
  explanation: "Down group 17 the H–X bond becomes longer and weaker, so the proton is released more easily. This bond-strength effect outweighs the fall in electronegativity, making HI the strongest."
- question: "HF is a weak acid in water even though fluorine is the most electronegative element."
  type: true-false
  answer: true
  explanation: "The H–F bond is very strong, and this outweighs its high polarity. HF has a Ka of roughly 10⁻³ to 10⁻⁴, while HCl, HBr and HI are strong acids."
- question: "Rank HOCl, HClO₂, HClO₃ and HClO₄ from weakest to strongest acid, and explain the trend."
  type: short-answer
  answer: "HOCl < HClO₂ < HClO₃ < HClO₄. Each extra oxygen on chlorine withdraws electron density from the O–H bond and lets the negative charge of the conjugate base spread over more oxygen atoms."
  explanation: "The acidic proton is on an O–H group in each acid. More terminal oxygens make the O–H bond more polar and stabilize the anion by delocalization, so Ka rises sharply across the series."
- question: "Among HOCl, HOBr and HOI, which is the strongest acid?"
  type: multiple-choice
  options: ["HOCl", "HOBr", "HOI", "All are equal"]
  answer: 0
  explanation: "When the structure is the same, the more electronegative central atom pulls more electron density away from the O–H bond. Chlorine is the most electronegative of the three, so HOCl is the strongest."
```

## Explainer

You already know how to measure acid strength with Ka. This topic asks why one acid has a larger Ka than another. The answer comes from two features: how easily the H–A bond breaks and how stable the anion A⁻ is once the proton has left.

Start with binary acids, compounds of hydrogen with one other element. Across a period, from CH₄ to NH₃ to H₂O to HF, the atom bonded to hydrogen becomes more electronegative. It pulls bonding electrons toward itself, makes the bond more polar, and holds the negative charge of the conjugate base better. Acid strength therefore rises across the period. Methane is essentially not acidic in water, while HF is a weak acid.

Down a group, a different factor wins. From HF to HCl to HBr to HI, the halogen gets larger, the H–X bond gets longer, and the bond gets weaker. The negative charge of the anion also spreads over a larger volume. Even though electronegativity falls, the weaker bond makes the proton easier to remove. That is why HI is the strongest of the hydrohalic acids and HF is the only weak one.

Oxoacids have the acidic hydrogen on an oxygen, as in H–O–Y. Two features control their strength. First, a more electronegative Y draws electron density through the oxygen and weakens the O–H bond. So HOCl is stronger than HOBr, which is stronger than HOI. Second, more oxygen atoms on Y increase the pull and let the negative charge of the conjugate base spread over more atoms by resonance. In the chlorine series, Ka rises from HOCl, a weak acid, to HClO₄, one of the strongest common acids.

A useful habit is to compare acids only when one feature changes at a time. Keep the structure the same and vary the central atom, or keep the central atom the same and vary the number of oxygens. When both change at once, predictions become uncertain. The same reasoning reappears in organic chemistry, where you will compare carboxylic acids, alcohols and phenols by asking how well each conjugate base holds its negative charge.
