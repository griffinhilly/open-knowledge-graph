---
id: mass-spectrometry-fragmentation-analysis
title: 'Mass Spectrometry: Fragmentation Patterns and Structure Elucidation'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: mass-spectrometry-organic
  type: hard
- id: ion-formation-from-electron-transfer
  type: soft
tags:
- mass-spectrometry
- fragmentation
- ion
- analysis
stage: advanced
status: draft
---

# Mass Spectrometry: Fragmentation Patterns and Structure Elucidation

## Core Idea
Mass spectrometry ionizes molecules and measures mass-to-charge ratios of resulting fragments. Fragmentation patterns reflect molecular structure and bonding through preferential cleavage at weak bonds. The molecular ion peak (M⁺) provides molecular weight; fragment peaks reveal functional groups and connectivity. Understanding fragmentation mechanisms allows prediction of MS patterns and vice versa—structure determination from spectra.

## Questions

```yaml
- question: "A mass spectrum shows the molecular ion at m/z 120 and a prominent fragment at m/z 105. A student notes that 'the fragment at m/z 105 must be structurally important.' What is the most analytically useful interpretation of the relationship between these two peaks?"
  type: multiple-choice
  options:
    - "The fragment at m/z 105 identifies a specific functional group independently of any other peaks"
    - "The neutral loss of 15 mass units (120 − 105) is diagnostic for loss of a methyl group (CH₃), suggesting a methyl substituent adjacent to the ionization site"
    - "The molecular weight of the compound is 105, and the peak at 120 is an artifact"
    - "Since 105 is an odd mass, the compound must contain nitrogen"
  answer: 1
  explanation: "The key insight in mass spectral interpretation is that mass *differences* between peaks are what reveal structure, not the absolute m/z values in isolation. Loss of 15 = CH₃ is one of the most common and diagnostic neutral losses. The fragment at m/z 105 alone tells you little — what matters is that it is 15 mass units below the molecular ion, pointing to a methyl group at the fragmentation site. Students who memorize fragment masses without understanding mass differences often miss the structural information encoded in relationships between peaks."

- question: "Which of the following compounds would most likely undergo a McLafferty rearrangement in the mass spectrometer?"
  type: multiple-choice
  options:
    - "Acetone (propan-2-one), which has a methyl group on each side of the carbonyl"
    - "Formaldehyde, which has no alpha carbons"
    - "2-pentanone (methyl propyl ketone), which has a propyl chain providing a gamma hydrogen"
    - "An aromatic ketone where the phenyl ring is directly attached to the carbonyl"
  answer: 2
  explanation: "The McLafferty rearrangement requires three structural elements: a carbonyl (or C=C), a gamma hydrogen (on the carbon three bonds from the carbonyl oxygen), and a beta bond that can cleave. It proceeds through a six-membered cyclic transition state. Acetone has no gamma carbon (only alpha carbons), so it cannot rearrange. 2-Pentanone has a propyl chain: the propyl group's terminal CH₃ provides gamma hydrogens, enabling the rearrangement. The aromatic ring in option D is rigid and cannot adopt the required geometry."

- question: "The most abundant ion in a mass spectrum (the base peak) is always the molecular ion."
  type: true-false
  answer: false
  explanation: "The base peak is simply the most abundant ion — it is defined as 100% relative abundance on the spectrum, but it can be any fragment. For many compounds, the molecular ion is unstable and fragments so readily that M⁺• has very low abundance or is not observed at all. The base peak is typically the most stable fragment cation produced by alpha-cleavage or other rearrangements. For example, in many aldehydes and ketones, the acylium ion (RC≡O⁺) is the base peak, not the molecular ion."

- question: "A compound with one chlorine atom will show two molecular ion peaks (M and M+2) at approximately a 3:1 relative intensity ratio."
  type: true-false
  answer: true
  explanation: "Chlorine's two stable isotopes — ³⁵Cl (75.8% natural abundance) and ³⁷Cl (24.2%) — are present in roughly a 3:1 ratio. A compound containing one chlorine therefore produces an M peak (containing ³⁵Cl) and an M+2 peak (containing ³⁷Cl) in approximately 3:1 intensity. This distinctive doublet pattern is a reliable diagnostic for the presence of one chlorine atom. Bromine shows a 1:1 doublet (⁷⁹Br and ⁸¹Br are nearly equally abundant), which is a different but equally recognizable signature."

- question: "Explain why alpha-cleavage is such a common fragmentation pathway in electron-impact (EI) mass spectrometry."
  type: short-answer
  answer: "Electron-impact ionization preferentially removes an electron from the site of lowest ionization energy — typically a heteroatom lone pair or a pi bond. This creates a radical cation with the radical localized at that site. Alpha-cleavage breaks the bond one carbon away from the radical, which separates the radical from the charge and produces two stable fragments: a resonance-stabilized cation (such as an acylium ion RC≡O⁺ or an iminium ion from a nitrogen) and a neutral radical. The thermodynamic stability of these products drives the reaction. Because the products are particularly stable relative to alternative cleavages, alpha-cleavage is thermodynamically and kinetically favored over random bond breaking elsewhere in the molecule."
  explanation: "The logic connects ionization mechanism to fragmentation preference: the radical ends up where ionization occurred, and cleaving the adjacent bond maximizes stability of the resulting cation through resonance. Recognizing which site ionizes first (usually next to O or N) tells you which alpha-cleavage will predominate and which peaks to expect."
```

## Explainer

From your earlier study of mass spectrometry, you know the basic workflow: molecules are ionized (typically by electron impact, EI), the resulting ions are separated by mass-to-charge ratio (m/z), and a detector records the abundance of each m/z value. The spectrum is a bar graph of relative abundance versus m/z. The **molecular ion peak** (M⁺•) — formed when the molecule loses one electron without breaking any bonds — gives you the molecular weight directly. But the real structural information lies in how the molecular ion breaks apart.

**Fragmentation** occurs because the molecular ion has excess internal energy from the ionization process. This energy redistributes through the molecule's vibrational modes, and bonds break at the weakest points. The resulting fragment ions are detected (neutral fragments are not), and their m/z values tell you the masses of the pieces. The key analytical tool is the **mass difference**: if you see the molecular ion at m/z 120 and a prominent fragment at m/z 105, the difference of 15 mass units corresponds to loss of a CH₃ group. Common neutral losses are diagnostic: loss of 18 = H₂O (alcohols, carboxylic acids), loss of 28 = CO (carbonyls, phenols) or C₂H₄ (ethyl groups), loss of 31 = OCH₃ (methyl esters), loss of 45 = OC₂H₅ (ethyl esters).

The fragmentation of a molecule follows predictable rules rooted in thermodynamic stability and radical cation chemistry. **Alpha-cleavage** (cleavage of the bond adjacent to the radical cation site) is the most common mechanism — it produces a resonance-stabilized cation. For example, ketones fragment by alpha-cleavage on either side of the carbonyl, producing acylium ions (RC≡O⁺, which appear as strong peaks). **McLafferty rearrangement** is a six-membered transition state process where a gamma hydrogen transfers to the radical cation site with simultaneous beta-cleavage, producing a neutral alkene and a radical cation fragment. This rearrangement is diagnostic for carbonyl compounds with a gamma hydrogen and produces characteristic even-mass fragments from odd-mass molecular ions.

The **nitrogen rule** is a powerful shortcut: molecules with an even number of nitrogen atoms (including zero) have even molecular weights, while those with an odd number have odd molecular weights. This applies to molecular ions and can help you decide whether a fragment has retained or lost a nitrogen atom. Similarly, the **isotope pattern** at the molecular ion reveals elements like chlorine (M and M+2 in roughly 3:1 ratio) and bromine (M and M+2 in roughly 1:1 ratio).

Putting this together, structure elucidation from a mass spectrum proceeds as follows: (1) identify the molecular ion and determine the molecular weight; (2) check the isotope pattern for halogens and the nitrogen rule; (3) identify major fragment ions and calculate mass losses; (4) match losses and fragment masses to known functional group signatures; (5) propose candidate structures and verify that they predict the observed fragmentation. With practice, you begin to read a mass spectrum almost like a structural formula — each peak is a piece of the molecule, and the pattern of losses maps its connectivity.
