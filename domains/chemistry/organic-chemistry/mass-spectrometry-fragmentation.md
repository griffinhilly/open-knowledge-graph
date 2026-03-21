---
id: mass-spectrometry-fragmentation
title: 'Mass Spectrometry: Molecular Ion and Fragmentation Patterns'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: mass-spectrometry-organic
  type: hard
tags:
- mass-spectrometry
- molecular-ion
- m-z
- fragmentation
- base-peak
stage: advanced
status: draft
---

# Mass Spectrometry: Molecular Ion and Fragmentation Patterns

## Core Idea
Mass spectrometry ionizes molecules and measures mass/charge (m/z) of resulting ions and fragments. The molecular ion peak (M⁺) gives the molecular weight; the base peak is the most abundant fragment. Fragmentation patterns are characteristic: α-cleavage (loss of atoms adjacent to heteroatoms), loss of small molecules (H₂O, CO), and rearrangements (McLafferty). MS used alongside IR and NMR determines molecular formula and functional groups.

## Questions

```yaml
- question: "A mass spectrum shows a base peak at m/z = 91, with the molecular ion at m/z = 134. What does the base peak immediately suggest about the compound's structure?"
  type: multiple-choice
  options:
    - "The molecular weight is 91 daltons"
    - "A tropylium cation (C₇H₇⁺) is the most stable fragment, indicating a benzene ring with at least one attached carbon"
    - "The compound lost a methyl group (43 mass units) from a 134 g/mol molecule"
    - "The compound contains a carbonyl group based on the characteristic fragment mass"
  answer: 1
  explanation: "The base peak is the most abundant fragment, not the molecular ion — a common misconception. The tropylium cation (C₇H₇⁺) at m/z = 91 is one of the most recognized signatures in organic MS: it forms by benzylic cleavage and is exceptionally stable due to its aromatic, fully delocalized 6π-electron structure. Whenever you see a prominent peak at 91, think benzene ring plus an attached carbon. The molecular weight here is 134 (the molecular ion), not 91."

- question: "A compound with an even-mass molecular ion at m/z = 114 shows a prominent fragment at m/z = 72. The loss of 42 mass units (propylene, C₃H₆) and the even mass of the fragment strongly suggest:"
  type: multiple-choice
  options:
    - "α-cleavage adjacent to a heteroatom producing an acylium ion"
    - "McLafferty rearrangement, requiring a carbonyl group and a γ-hydrogen"
    - "Loss of water (18) followed by loss of CO (28) in two sequential steps"
    - "Benzylic cleavage producing a resonance-stabilized cation"
  answer: 1
  explanation: "The McLafferty rearrangement produces an even-mass fragment from an even-mass molecular ion (both are even here, consistent with no nitrogen). It requires a carbonyl group with a hydrogen on the γ-carbon, proceeding through a six-membered cyclic transition state to expel a neutral alkene. The loss of propylene (42 = C₃H₆) is a classic McLafferty signature. α-Cleavage (option A) would produce an acylium ion at a different position, and water loss is only 18 mass units."

- question: "The base peak in a mass spectrum always corresponds to the molecular ion, because the intact molecule is the most abundant species detected."
  type: true-false
  answer: false
  explanation: "The base peak is the tallest peak (most abundant ion) in the spectrum, but it represents the most stable fragment — which is very often NOT the molecular ion. Many molecular ions are unstable and fragment before reaching the detector. Highly stable fragments like the tropylium cation (m/z = 91) or acylium ions can dominate the spectrum even though they have lower masses than M⁺. The molecular ion, when it appears, may be a relatively weak peak."

- question: "The difference in m/z between the molecular ion peak and any fragment ion in the mass spectrum equals the mass of the neutral species lost during that fragmentation."
  type: true-false
  answer: true
  explanation: "This is the fundamental relationship for interpreting mass spectra. When a molecular ion fragments, one piece retains the charge (detected as a fragment ion) and the other departs as a neutral radical or molecule (undetected). Mass: M⁺ → fragment⁺ + neutral. Therefore m/z(neutral loss) = m/z(M⁺) − m/z(fragment). For example, M⁺ at 128 and a fragment at 113 means a loss of 15, which immediately suggests CH₃ (methyl group)."

- question: "Why does α-cleavage occur preferentially at bonds adjacent to heteroatoms, and what structural feature of the resulting cation accounts for its stability?"
  type: short-answer
  answer: "α-Cleavage occurs because a heteroatom (oxygen, nitrogen, etc.) can stabilize an adjacent positive charge through resonance donation of a lone pair. When the bond between the heteroatom-bearing carbon and an adjacent carbon breaks, the charge centers on the carbon bonded to the heteroatom. The heteroatom donates electron density into the empty orbital, producing a resonance-stabilized oxocarbenium or iminium cation. This resonance stabilization lowers the energy of the product ion, making α-cleavage a favorable and common fragmentation pathway."
  explanation: "The key is resonance stabilization of the product cation, not just proximity to the heteroatom. For a ketone, α-cleavage on either side of the carbonyl produces an acylium ion (R–C≡O⁺), which is stable due to the triple bond resonance structure. For an amine, α-cleavage gives an iminium ion. In each case, the charge is spread over two atoms through resonance, lowering the fragment's energy and making this fragmentation pathway kinetically and thermodynamically favorable."
```

## Explainer

From your introduction to mass spectrometry, you know the basic workflow: a molecule is ionized (typically by electron impact, where a high-energy electron knocks out one of the molecule's electrons), producing a **radical cation** (M⁺•) with the same mass as the original molecule. This molecular ion is accelerated through a magnetic or electric field that separates ions by their mass-to-charge ratio (m/z), and a detector records the abundance of each ion. The resulting spectrum is a bar graph of m/z values versus relative intensity. Now the question becomes: how do you read that spectrum to determine structure?

The **molecular ion peak** (M⁺) is your starting point — its m/z value gives the molecular weight directly. But many molecular ions are unstable and break apart before reaching the detector, producing **fragment ions** at lower m/z values. The **base peak** is the tallest peak in the spectrum (assigned 100% relative intensity) and represents the most stable, most abundantly formed fragment — not necessarily the molecular ion. The difference between the molecular ion and any fragment tells you the mass of what was lost, and these neutral losses are your primary clues. A loss of 15 suggests a methyl group (CH₃), 18 means water (H₂O, common for alcohols), 28 could be CO (from carbonyls) or ethylene (C₂H₄), and 29 suggests a formyl group (CHO) or an ethyl radical.

Fragmentation follows predictable rules rooted in carbocation and radical stability. **α-Cleavage** is the most common pattern for molecules containing a heteroatom: the bond between the carbon bearing the heteroatom and the adjacent carbon breaks, generating a resonance-stabilized cation. For example, a ketone fragments α to the carbonyl, producing an acylium ion (R–C≡O⁺, often a prominent peak) and an alkyl radical. Alcohols undergo α-cleavage too, and they also readily lose water (M − 18). **Benzylic cleavage** produces the very stable tropylium cation (C₇H₇⁺, m/z = 91), which is a signature peak for compounds containing a benzene ring with at least one carbon substituent.

The **McLafferty rearrangement** is a more complex but highly diagnostic fragmentation. It requires a carbonyl group and a hydrogen on the carbon four atoms away (the γ-carbon). Through a six-membered cyclic transition state, the γ-hydrogen transfers to the carbonyl oxygen while the bond between the α- and β-carbons breaks. The result is loss of a neutral alkene and retention of charge on the carbonyl-containing fragment. Recognizing a McLafferty pattern — an even-mass fragment when the molecular ion is even, or a clear alkene loss from a carbonyl compound — immediately tells you that a γ-hydrogen and an appropriately long chain are present. Together, these fragmentation rules let you work backward from a spectrum to reconstruct the molecule's carbon skeleton and functional groups.
