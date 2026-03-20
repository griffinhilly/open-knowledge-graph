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

## Explainer

From your introduction to mass spectrometry, you know the basic workflow: a molecule is ionized (typically by electron impact, where a high-energy electron knocks out one of the molecule's electrons), producing a **radical cation** (M⁺•) with the same mass as the original molecule. This molecular ion is accelerated through a magnetic or electric field that separates ions by their mass-to-charge ratio (m/z), and a detector records the abundance of each ion. The resulting spectrum is a bar graph of m/z values versus relative intensity. Now the question becomes: how do you read that spectrum to determine structure?

The **molecular ion peak** (M⁺) is your starting point — its m/z value gives the molecular weight directly. But many molecular ions are unstable and break apart before reaching the detector, producing **fragment ions** at lower m/z values. The **base peak** is the tallest peak in the spectrum (assigned 100% relative intensity) and represents the most stable, most abundantly formed fragment — not necessarily the molecular ion. The difference between the molecular ion and any fragment tells you the mass of what was lost, and these neutral losses are your primary clues. A loss of 15 suggests a methyl group (CH₃), 18 means water (H₂O, common for alcohols), 28 could be CO (from carbonyls) or ethylene (C₂H₄), and 29 suggests a formyl group (CHO) or an ethyl radical.

Fragmentation follows predictable rules rooted in carbocation and radical stability. **α-Cleavage** is the most common pattern for molecules containing a heteroatom: the bond between the carbon bearing the heteroatom and the adjacent carbon breaks, generating a resonance-stabilized cation. For example, a ketone fragments α to the carbonyl, producing an acylium ion (R–C≡O⁺, often a prominent peak) and an alkyl radical. Alcohols undergo α-cleavage too, and they also readily lose water (M − 18). **Benzylic cleavage** produces the very stable tropylium cation (C₇H₇⁺, m/z = 91), which is a signature peak for compounds containing a benzene ring with at least one carbon substituent.

The **McLafferty rearrangement** is a more complex but highly diagnostic fragmentation. It requires a carbonyl group and a hydrogen on the carbon four atoms away (the γ-carbon). Through a six-membered cyclic transition state, the γ-hydrogen transfers to the carbonyl oxygen while the bond between the α- and β-carbons breaks. The result is loss of a neutral alkene and retention of charge on the carbonyl-containing fragment. Recognizing a McLafferty pattern — an even-mass fragment when the molecular ion is even, or a clear alkene loss from a carbonyl compound — immediately tells you that a γ-hydrogen and an appropriately long chain are present. Together, these fragmentation rules let you work backward from a spectrum to reconstruct the molecule's carbon skeleton and functional groups.
