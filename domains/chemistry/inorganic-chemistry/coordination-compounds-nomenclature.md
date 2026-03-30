---
id: coordination-compounds-nomenclature
title: Coordination Compounds and Nomenclature
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: coordination-chemistry-basics
  type: hard
- id: oxidation-reduction-reactions
  type: soft
builds-toward:
- isomerism-coordination-compounds
- crystal-field-theory
tags:
- coordination compounds
- nomenclature
- IUPAC naming
- ligand naming
stage: formal-systems
status: validated
---

# Coordination Compounds and Nomenclature

## Core Idea
Coordination compounds are named using a systematic IUPAC nomenclature that encodes the identity and number of ligands, the central metal, its oxidation state, and the overall charge of the complex. Mastering this naming system is essential because the name uniquely specifies the compound's composition and structure.

## Questions

```yaml
- question: "What is the correct IUPAC name for [Co(NH₃)₅Cl]Cl₂?"
  type: multiple-choice
  options:
    - "Cobalt pentaammine chloride dichloride"
    - "Pentaamminechloridocobalt(III) chloride"
    - "Chloropentaamminecobalt(II) dichloride"
    - "Pentaamminecobalt(III) trichloride"
  answer: 1
  explanation: "The IUPAC rules require ligands listed alphabetically (ammine before chlorido), then the metal with oxidation state in Roman numerals. Inside the bracket: five NH₃ (pentaammine) and one Cl⁻ (chlorido) coordinated to Co. The cobalt oxidation state is +3 (the complex ion has charge +2 from Co, offset by one Cl⁻ inside, and two Cl⁻ outside balance the +2 ion charge: total Co charge must satisfy x + 0×5 + (−1) = +2, so x = +3). The two Cl⁻ outside the bracket are the counter ions, named as 'chloride.' Option A uses incorrect ligand ordering and format. Option C has the wrong oxidation state. Option D ignores the inner-sphere chloride."

- question: "In IUPAC nomenclature for coordination compounds, anionic ligands receive the suffix '-ido' (or '-o') while neutral ligands keep their usual names, with specific exceptions like aqua (H₂O), ammine (NH₃), carbonyl (CO), and nitrosyl (NO)."
  type: true-false
  answer: true
  explanation: "This is a core naming convention. Anionic ligands like Cl⁻ become chlorido, CN⁻ becomes cyanido, and OH⁻ becomes hydroxido. Neutral ligands generally use their molecular name, but four have special names by convention: water is aqua, ammonia is ammine (with double-m to distinguish from the organic amine), carbon monoxide is carbonyl, and nitric oxide is nitrosyl. These exceptions must be memorized because they appear constantly in coordination chemistry."

- question: "When naming the complex ion [Fe(CN)₆]⁴⁻, the metal is given the suffix '-ate' because it is in an anionic complex."
  type: true-false
  answer: true
  explanation: "When the overall complex ion carries a negative charge, the metal name receives the '-ate' suffix. Iron becomes ferrate (using the Latin root), copper becomes cuprate, and so on. So [Fe(CN)₆]⁴⁻ is hexacyanidoferrate(II). The oxidation state of iron is +2 because six CN⁻ ligands contribute −6 total, and the overall charge is −4: x + (−6) = −4, so x = +2. If the complex were cationic or neutral, the normal metal name would be used without the '-ate' ending."

- question: "The compound K₃[Fe(C₂O₄)₃] contains three bidentate oxalate ligands. Explain how the prefixes differ when naming multiple monodentate versus polydentate ligands, and give the correct IUPAC name for this compound."
  type: short-answer
  answer: "For monodentate ligands, Greek prefixes (di-, tri-, tetra-, penta-, hexa-) indicate the number. For polydentate ligands whose names already contain Greek prefixes or are complex, multiplicative prefixes (bis-, tris-, tetrakis-) are used, with the ligand name in parentheses. Oxalate (C₂O₄²⁻) is a polydentate ligand, so three of them uses 'tris' rather than 'tri.' The correct name is potassium tris(oxalato)ferrate(III). Iron's oxidation state: 3(−2) from oxalate + x = −3 overall charge balanced by 3 K⁺, so x = +3."
  explanation: "The bis/tris/tetrakis system exists specifically to avoid ambiguity. If you wrote 'trioxalatoferrate,' it could be misread as three 'oxalato' groups or one 'trioxalato' entity. Parentheses with multiplicative prefixes eliminate this confusion."

- question: "Why does IUPAC nomenclature list ligands in alphabetical order rather than by charge or donor atom type?"
  type: short-answer
  answer: "Alphabetical ordering provides a single unambiguous convention that works regardless of the ligands involved. Ordering by charge would create ties (multiple anionic or neutral ligands), requiring a secondary sorting rule. Ordering by donor atom type would be ambiguous for ambidentate ligands. Alphabetical order eliminates all such ambiguity: every chemist arrives at the same name for the same compound. The alphabetical ordering applies to the ligand name itself (ammine before chlorido because 'a' precedes 'c'), ignoring multiplicative prefixes like di-, tri-, or bis-."
  explanation: "This convention is purely practical — it ensures one-to-one correspondence between compound and name. The key subtlety is that prefixes indicating number (di, tri, bis, tris) are NOT considered when alphabetizing, so 'dichlorido' would be alphabetized under 'c', not 'd'."
```

## Explainer

From general chemistry, you learned that coordination complexes consist of a central metal ion bonded to surrounding ligands through coordinate covalent bonds. You can draw them, identify their charges, and predict their coordination numbers. But to communicate about these compounds precisely — in papers, databases, or conversations — you need a systematic naming convention. IUPAC nomenclature for coordination compounds is that convention, and it is designed so that the name uniquely determines the compound's composition.

The naming system follows a strict sequence. For a coordination compound like [Co(NH₃)₅Cl]Cl₂, you first name the cation, then the anion — just as with any ionic compound. Within the coordination sphere (the brackets), ligands are listed alphabetically by their IUPAC ligand name, ignoring numerical prefixes. Anionic ligands take the suffix '-ido' (chlorido, cyanido, hydroxido), while neutral ligands generally keep their molecular names with four important exceptions: water becomes aqua, ammonia becomes ammine, CO becomes carbonyl, and NO becomes nitrosyl. The number of each ligand is indicated by Greek prefixes (di-, tri-, tetra-) for simple ligands or multiplicative prefixes (bis-, tris-, tetrakis-) in parentheses for ligands with complex names. After all ligands, the metal is named with its oxidation state in Roman numerals in parentheses.

Two additional rules handle special cases. When the complex ion is an anion, the metal receives the '-ate' suffix, often using the Latin root: iron becomes ferrate, copper becomes cuprate, tin becomes stannate. When the complex is a cation or neutral species, the normal English metal name is used. The oxidation state is calculated by working backward from the known charges of the ligands and the overall charge of the complex ion. For [Co(NH₃)₅Cl]²⁺, five neutral NH₃ and one Cl⁻ coordinate to cobalt; the ion charge of +2 means Co must be +3 because +3 + 0 + (−1) = +2.

This naming system may seem like rote memorization, but it encodes real chemical information. The name tells you the metal, its oxidation state, the identity and number of all ligands, and the overall charge — from which you can infer the coordination geometry, possible isomers, and likely reactivity. As you encounter thousands of coordination compounds in inorganic chemistry, this systematic naming becomes your primary tool for organizing and retrieving information about them.
