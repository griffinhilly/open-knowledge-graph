---
id: metal-carbonyls
title: Metal Carbonyls
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: organometallic-chemistry-fundamentals
  type: hard
- id: ligand-field-theory
  type: soft
builds-toward:
- catalytic-cycles-wilkinson-grubbs
- homogeneous-catalysis-mechanisms
tags:
- metal carbonyls
- CO bonding
- back-bonding
- IR spectroscopy
- syngas
stage: advanced
status: validated
---

# Metal Carbonyls

## Core Idea
Metal carbonyls are complexes where carbon monoxide serves as the primary ligand, bonding to the metal through both sigma donation (C lone pair to metal) and pi back-donation (metal d-electrons to CO π* orbitals). The synergistic sigma/pi bonding produces exceptionally strong metal-carbon bonds. The CO stretching frequency in infrared spectroscopy serves as a sensitive probe of electron density at the metal center, making IR the primary diagnostic tool for characterizing metal carbonyls and their derivatives.

## Questions

```yaml
- question: "Free CO absorbs in the IR at 2143 cm⁻¹. In Ni(CO)₄, the CO stretching frequency drops to ~2060 cm⁻¹. What causes this decrease?"
  type: multiple-choice
  options:
    - "The mass of the Ni atom attached to CO reduces the vibrational frequency through a simple mass effect"
    - "Pi back-donation from filled Ni d-orbitals into CO π* antibonding orbitals weakens the C≡O bond, lowering its stretching frequency"
    - "Sigma donation from CO to Ni strengthens the C-O bond by removing antibonding electron density"
    - "Intermolecular interactions between CO ligands in the complex shift the frequency"
  answer: 1
  explanation: "The CO stretching frequency directly reports on C-O bond strength. In free CO, the bond is a strong triple bond (2143 cm⁻¹). When CO coordinates to a metal, the metal's filled d-orbitals donate electron density into CO's π* antibonding orbitals (back-donation). Populating these antibonding orbitals weakens the C-O bond, reducing the bond order below 3 and lowering the stretching frequency. The more electron-rich the metal, the more back-donation occurs, and the lower the CO frequency drops. This makes ν(CO) a remarkably sensitive probe of metal electron density."

- question: "In a series of isoelectronic carbonyls [V(CO)₆]⁻, Cr(CO)₆, and [Mn(CO)₆]⁺, the CO stretching frequency increases from V⁻ to Mn⁺. This trend reflects decreasing back-donation as the metal center becomes more positively charged."
  type: true-false
  answer: true
  explanation: "All three species are isoelectronic (d⁶, 18 electrons) with the same octahedral geometry. The difference is the formal charge on the metal: V⁻ is electron-rich, Cr⁰ is neutral, and Mn⁺ is electron-poor. Greater positive charge on the metal reduces the electron density available for back-donation into CO π* orbitals, strengthening the C-O bond and raising ν(CO). [V(CO)₆]⁻: ~1860 cm⁻¹, Cr(CO)₆: ~2000 cm⁻¹, [Mn(CO)₆]⁺: ~2100 cm⁻¹. This isoelectronic series is a textbook demonstration of how ν(CO) tracks metal electron density."

- question: "All stable binary metal carbonyls (containing only metal and CO) obey the 18-electron rule."
  type: true-false
  answer: true
  explanation: "The binary metal carbonyls of transition metals all satisfy the 18-electron rule: Ni(CO)₄ (10 + 8 = 18), Fe(CO)₅ (8 + 10 = 18), Cr(CO)₆ (6 + 12 = 18). When a single metal center cannot reach 18 electrons, metals form M-M bonds in polynuclear carbonyls: Mn₂(CO)₁₀ (each Mn has 7 + 10 from five CO + 1 from M-M bond = 18), Co₂(CO)₈ (each Co has 9 + 6 from bridging/terminal CO + 1 from M-M bond, reaching 18 with the appropriate bridging arrangement). The regularity of this pattern makes the 18-electron rule the most reliable predictor of binary carbonyl stoichiometry."

- question: "Explain why replacing one CO in Cr(CO)₆ with PPh₃ to form Cr(CO)₅(PPh₃) shifts the remaining CO stretching frequencies to lower wavenumbers."
  type: short-answer
  answer: "PPh₃ is a stronger sigma-donor than CO but a weaker pi-acceptor. When PPh₃ replaces one CO, it donates more electron density to chromium through sigma bonding than the departing CO did, but it accepts less electron density through back-bonding. The net effect is increased electron density at the metal center. This excess electron density is redistributed to the remaining five CO ligands through enhanced back-donation into their π* orbitals. More back-donation weakens the C-O bonds of the remaining COs, lowering their stretching frequencies. Each CO serves as a 'reporter' of the total electron density at the metal."
  explanation: "This principle makes CO stretching frequencies in mixed-ligand complexes a powerful diagnostic. By comparing ν(CO) values before and after ligand substitution, you can rank ligands by their net donor/acceptor properties. Ligands that increase metal electron density (strong sigma-donors, weak pi-acceptors) lower ν(CO); ligands that decrease it (weak sigma-donors, strong pi-acceptors) raise ν(CO)."
```

## Explainer

Carbon monoxide is arguably the most important ligand in organometallic chemistry. Its bonding to transition metals illustrates the synergistic sigma-donation/pi-back-donation model that underpins all of organometallic bonding theory, and its infrared spectroscopy provides the most accessible window into electronic structure at the metal center. Understanding metal carbonyls thoroughly prepares you for the broader landscape of organometallic chemistry.

The CO-to-metal bond involves two complementary interactions. First, the carbon lone pair donates into an empty metal orbital (sigma donation), forming a conventional coordinate bond. Second, filled metal d-orbitals of appropriate symmetry donate electron density into the empty π* antibonding orbitals on CO (pi back-donation). These two processes reinforce each other: sigma donation increases electron density on the metal, making it a better back-donor; back-donation depletes metal electron density, making it a better sigma acceptor. The result is a synergistic bond that is remarkably strong — metal-CO bond dissociation energies typically range from 150 to 200 kJ/mol.

The infrared CO stretching frequency is the single most diagnostic measurement in metal carbonyl chemistry. Free CO absorbs at 2143 cm⁻¹. Upon coordination, back-donation populates the CO π* orbitals, weakening the C-O bond and lowering the frequency. The extent of the decrease reports directly on how much electron density the metal pushes into CO. In the isoelectronic series [V(CO)₆]⁻, Cr(CO)₆, [Mn(CO)₆]⁺, the CO frequency increases steadily as the metal becomes more positive and back-donation decreases: ~1860, ~2000, ~2100 cm⁻¹. Substituting a CO with a stronger donor ligand (like PPh₃) increases electron density at the metal, enhancing back-donation to the remaining COs and lowering their frequencies. Each CO ligand is a spectroscopic reporter of the electronic environment at the metal.

Binary metal carbonyls — compounds containing only metal atoms and CO ligands — provide the cleanest demonstration of the 18-electron rule. Every known stable binary carbonyl satisfies it: Ni(CO)₄, Fe(CO)₅, Cr(CO)₆, V(CO)₆⁻. When the electron count cannot reach 18 with terminal CO ligands alone, metals form M-M bonds (contributing one electron each to both partners) or bridging CO ligands. Mn₂(CO)₁₀ has a Mn-Mn bond, Co₂(CO)₈ has both bridging COs and a Co-Co bond. This predictive power extends to polynuclear clusters: the number of M-M bonds can be predicted from the deficit below 18 electrons per metal center, providing a simple route to predicting the structures of complex cluster compounds.
