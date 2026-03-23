---
id: amide-formation-and-properties
title: Amide Formation and Properties
domain: chemistry
course: organic-chemistry
prerequisites:
- id: carboxylic-acids-and-derivatives
  type: hard
- id: amine-reactivity-nucleophile-base
  type: hard
- id: nucleophilic-acyl-substitution
  type: hard
builds-toward:
- relative-reactivity-carboxylic-acid-derivatives
tags:
- amide-formation
- resonance
- restricted-rotation
- peptide-bond
stage: formal-systems
status: validated
---

# Amide Formation and Properties

## Core Idea
Amides form from nucleophilic acyl substitution of an amine on a carboxylic acid, acid chloride, or ester. The C-N bond has significant double-bond character due to resonance delocalization, restricting rotation and creating syn and anti conformers. Amides are weak nucleophiles and bases but excellent hydrogen bond donors and acceptors, making them abundant in proteins and synthetic polymers.

## Questions

```yaml
- question: "A biochemist wants to recover free amino acids from a peptide by hydrolysis at room temperature in pH 7 aqueous buffer. After 24 hours, no free amino acids are detected. What best explains this result?"
  type: multiple-choice
  options:
    - "Peptide bonds require a nucleophile to be attacked, and water is too weak a nucleophile at neutral pH"
    - "Amides are the least reactive carboxylic acid derivatives because resonance ties up nitrogen's lone pair, making them resistant to hydrolysis under mild conditions"
    - "The peptide dissolved completely, so no solid material was left to hydrolyze"
    - "Amide hydrolysis requires an acid chloride intermediate, which is not available at pH 7"
  answer: 1
  explanation: "Amides resist hydrolysis under mild conditions precisely because nitrogen's lone pair is delocalized into the carbonyl through resonance, reducing the electrophilicity of the carbonyl carbon and making the nitrogen a poor leaving group. This is why proteins can survive in aqueous environments — amide bonds are the least reactive carboxylic acid derivatives. Complete acid or base hydrolysis of peptides requires concentrated acid or base and elevated temperatures."

- question: "Why is the C–N bond in an amide shorter and rotationally restricted compared to a typical C–N single bond in an amine?"
  type: multiple-choice
  options:
    - "The carbonyl oxygen withdraws electrons from nitrogen through induction, stiffening the C–N bond"
    - "Nitrogen's lone pair donates into the carbonyl π-system through resonance, giving the C–N bond roughly 40% double-bond character"
    - "The large carbonyl group creates steric hindrance that physically prevents rotation around C–N"
    - "Hydrogen bonding between amide groups in proteins locks the conformation in place"
  answer: 1
  explanation: "The restricted rotation is an electronic effect, not a steric one. Resonance donation of nitrogen's lone pair into the adjacent carbonyl creates a second resonance structure with C=N double-bond character and negative charge on oxygen. The C–N bond in the resonance hybrid is shorter (between single and double bond) and has a rotational barrier of ~75 kJ/mol. This planarity is the structural origin of protein backbone rigidity and the regular geometry of secondary structures."

- question: "The nitrogen in an amide is a stronger base than a typical amine nitrogen because the adjacent carbonyl group stabilizes the positive charge on nitrogen after protonation."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. Resonance donation of nitrogen's lone pair into the carbonyl makes amide nitrogen a *weaker* base (pKa of conjugate acid ≈ −1) compared to a typical amine (pKa ≈ 10–11). Because the lone pair is tied up in resonance with the carbonyl, it is less available to accept a proton. The carbonyl does not stabilize the protonated form — it competes with protonation for the nitrogen's lone pair."

- question: "The planarity of the peptide (amide) bond, enforced by restricted C–N rotation, is essential for the formation of protein secondary structures like α-helices and β-sheets."
  type: true-false
  answer: true
  explanation: "True. Because the amide bond locks the six atoms of the amide unit into a plane, the overall fold of a protein is determined by rotations around only the bonds flanking each rigid amide unit (the φ and ψ backbone angles). This restricted geometry is what makes regular secondary structures like α-helices and β-sheets geometrically possible — they arise from repeating patterns of these constrained rotational angles. If amide bonds rotated freely, proteins would have far more conformational flexibility and stable secondary structures would be much harder to maintain."

- question: "Why are amides simultaneously excellent hydrogen bond donors and acceptors, yet poor nucleophiles and weak bases? Explain using resonance."
  type: short-answer
  answer: "Resonance delocalization of nitrogen's lone pair into the carbonyl creates partial negative charge on oxygen and partial positive charge on nitrogen. The carbonyl oxygen (partial negative charge) accepts hydrogen bonds readily, and the N–H (in primary/secondary amides) donates hydrogen bonds. But this same resonance means nitrogen's lone pair is not freely available — it is tied up in the π-system — making nitrogen a poor nucleophile and a very weak base (pKa of conjugate acid ≈ −1). The two properties are two sides of the same resonance coin."
  explanation: "This is the central paradox of amide chemistry: the resonance that creates excellent hydrogen bonding (partial charges on both O and N, N-H donor) also destroys nucleophilicity and basicity by delocalization of the nitrogen lone pair. Nature exploits both consequences simultaneously — amide hydrogen bonds hold protein secondary structures together, while amide bond resistance to hydrolysis (from low reactivity) keeps proteins intact in aqueous environments."
```

## Explainer

You already know from nucleophilic acyl substitution that a nucleophile attacks the electrophilic carbonyl carbon of an acyl compound, forming a tetrahedral intermediate that then collapses by expelling the leaving group. **Amide formation** follows exactly this pattern: an amine (the nucleophile, with its lone pair on nitrogen) attacks an activated acyl species — typically an acid chloride, anhydride, or ester — and the leaving group (Cl⁻, carboxylate, or alkoxide) departs. Directly reacting a carboxylic acid with an amine is less straightforward because the amine, being a base, first deprotonates the acid to form a carboxylate salt; strong heating is then required to drive off water and force the amide bond to form.

What makes amides special among carboxylic acid derivatives is the remarkable electronic structure of the C–N bond. Nitrogen's lone pair donates into the carbonyl π-system through **resonance**, giving the C–N bond roughly 40% double-bond character. You can draw two important resonance structures: one with a C=O double bond and a C–N single bond, and another with a C–O single bond (negative charge on oxygen) and a C=N double bond (positive charge on nitrogen). The hybrid means the C–N bond is shorter, stronger, and — most importantly — **rotationally restricted**. Unlike a typical C–N single bond that rotates freely, the amide bond has a rotational barrier of about 75 kJ/mol, effectively locking the six atoms of the amide group (O=C–N plus the two substituents on N and the one on C) into a plane.

This planarity has enormous biological consequences. The **peptide bond** linking amino acids in proteins is an amide bond, and its restricted rotation is what gives protein backbones their structural rigidity. Each peptide bond locks into either a *syn* or *anti* configuration (anti is strongly favored for steric reasons), and the overall fold of the protein emerges from rotations around the bonds flanking each rigid amide unit. Additionally, the partial charges created by resonance — slight positive on nitrogen, slight negative on oxygen — make amides superb **hydrogen bond donors and acceptors**, which is why proteins fold into stable secondary structures like α-helices and β-sheets held together by networks of amide hydrogen bonds.

The same resonance that gives amides their structural importance also explains their low reactivity. Because nitrogen's lone pair is tied up in resonance with the carbonyl, amide nitrogen is a very weak base (pKa of the conjugate acid ~−1) and a poor nucleophile compared to a free amine. This makes amides the least reactive carboxylic acid derivatives — they resist hydrolysis under mild conditions, which is exactly why nature chose them as the backbone linkage for proteins that must survive in aqueous environments.
