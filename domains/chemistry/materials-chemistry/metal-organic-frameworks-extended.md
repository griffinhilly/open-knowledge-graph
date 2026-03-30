---
id: metal-organic-frameworks-extended
title: Metal-Organic Frameworks (Extended)
domain: chemistry
course: materials-chemistry
prerequisites:
- id: crystal-structures-and-unit-cells
  type: hard
- id: self-assembly-materials
  type: soft
- id: materials-chemistry-zeolites-mofs
  type: hard
builds-toward:
- catalytic-materials-design
tags:
- MOFs
- porous materials
- reticular chemistry
- gas storage
- secondary building units
stage: expert
status: validated
---

# Metal-Organic Frameworks (Extended)

## Core Idea
Metal-organic frameworks (MOFs) are crystalline porous materials constructed from metal ions or clusters (secondary building units, SBUs) connected by organic linkers. The modular design — choosing different metals and linkers — allows systematic tuning of pore size (3 to 98 Angstroms), surface area (up to 7,000+ m^2/g), and chemical functionality. Reticular chemistry provides the design framework: the topology of the net (how nodes are connected) is determined by the geometry of the SBU and linker, enabling prediction of new structures before synthesis. Applications span gas storage (H2, CH4, CO2), separation, catalysis, drug delivery, and sensing, with over 100,000 MOF structures reported.

## Questions

```yaml
- question: "MOF-5 uses Zn4O(COO)6 clusters as SBUs connected by linear 1,4-benzenedicarboxylate linkers. Replacing the linear linker with a tricarboxylate linker changes the topology from cubic to what?"
  type: short-answer
  answer: "A tricarboxylate linker (three connection points) changes the linker geometry from linear (2-connected) to trigonal (3-connected). Combined with the octahedral SBU geometry, this produces a different network topology. For example, using 1,3,5-benzenetricarboxylate with the same Zn4O cluster gives a structure with a different net than the primitive cubic topology of MOF-5. The key principle of reticular chemistry is that topology is determined by the connectivity and geometry of the building blocks — changing the linker geometry necessarily changes the network."
  explanation: "Reticular chemistry, pioneered by Omar Yaghi, treats MOF design as a geometry problem: given an SBU with n connection points in geometry G and a linker with m connection points in geometry H, what network topologies are possible? This reduces the astronomically large space of possible MOF compositions to a manageable set of topologies, each with predictable pore characteristics. The RCSR (Reticular Chemistry Structure Resource) database catalogs these topologies."

- question: "MOFs often have much higher surface areas than zeolites (7,000+ m^2/g vs. ~900 m^2/g). This higher surface area always makes MOFs better adsorbents for gas storage."
  type: true-false
  answer: false
  explanation: "Surface area is only one factor in gas storage performance. Volumetric storage capacity (amount stored per unit volume) often matters more than gravimetric capacity (per unit mass). Many high-surface-area MOFs have low crystal densities due to their large pores, giving poor volumetric performance. The optimal MOF for methane storage has moderate pore sizes (~8-11 Angstroms) that maximize methane density through overlapping van der Waals potential fields from opposing pore walls — not the largest possible surface area. Additionally, MOFs often have inferior hydrothermal stability compared to zeolites, limiting practical applications where water is present."

- question: "Post-synthetic modification (PSM) of MOFs involves chemically modifying the framework after it has been synthesized and crystallized. Why is PSM important?"
  type: multiple-choice
  options:
    - "PSM corrects defects that formed during crystallization"
    - "PSM allows introduction of functional groups that would not survive the solvothermal synthesis conditions or that would prevent framework formation"
    - "PSM is required to activate the MOF by removing solvent molecules"
    - "PSM increases the crystallinity of the framework"
  answer: 1
  explanation: "Some desirable functional groups (e.g., free amines, catalytic metal complexes, biomolecules) are incompatible with the high-temperature, acidic, or basic conditions of MOF solvothermal synthesis — they would decompose or interfere with crystallization. PSM strategies install these groups after the robust framework has formed. Common approaches include covalent modification of pendant functional groups on linkers (e.g., reacting an amino-functionalized linker with an anhydride), metal ion exchange at the SBUs, and encapsulation of guest molecules in the pores. This dramatically expands the functional scope of MOFs beyond what direct synthesis can achieve."

- question: "What is the main advantage of MOFs over activated carbon for gas separation applications?"
  type: short-answer
  answer: "MOFs offer uniform, crystallographically defined pore sizes and tunable surface chemistry, enabling highly selective separations based on precise molecular sieving or differential adsorption. Activated carbon has a broad distribution of pore sizes and relatively non-specific surface chemistry, so it adsorbs many gases with poor selectivity. A MOF can be designed with pores just large enough to admit CO2 but too small for N2, or with open metal sites that preferentially bind one gas over another. This designability — being able to engineer selectivity at the molecular level — is what activated carbon cannot offer."
  explanation: "The crystalline regularity of MOFs means every pore is identical in size and shape, unlike the heterogeneous pore structure of amorphous carbon. This translates directly to sharper separation selectivities. For CO2 capture from flue gas, for example, MOFs with amino-functionalized linkers or exposed metal sites show CO2/N2 selectivities 10-100x higher than activated carbon. The tradeoff is cost, scale, and stability — activated carbon is cheap and robust, while MOFs are expensive and often moisture-sensitive."
```

## Explainer

Metal-organic frameworks represent one of the most exciting developments in materials chemistry over the past two decades. The concept is elegant: take inorganic clusters (metal nodes) and connect them with organic molecules (linkers) to build an extended crystalline framework with permanent porosity. Unlike zeolites, which are limited to aluminosilicate compositions and a finite number of topologies, MOFs can be built from virtually any metal and an enormous library of organic linkers. This chemical versatility translates to unprecedented control over pore geometry, surface area, and chemical functionality.

The intellectual framework is **reticular chemistry** — the design of materials by linking molecular building blocks into predetermined network topologies. The secondary building unit (SBU) — a metal-oxide cluster with defined geometry and connectivity — serves as the node. The organic linker serves as the strut. The key insight is that the topology of the resulting net depends on the geometry of these building blocks, not their specific chemistry. A 6-connected octahedral node linked by linear ditopic linkers gives a cubic net regardless of whether the node is Zn4O, Cu2(COO)4, or Zr6O4(OH)4. This predictability allows you to design a MOF on paper before synthesizing it.

**Synthesis** typically involves solvothermal reactions: metal salts and organic linkers are dissolved in a solvent (often DMF) and heated to 80-150 degrees C for 12-72 hours. Crystallization produces single crystals or microcrystalline powders. After synthesis, the pores are filled with solvent that must be removed (**activation**) to access the porosity. Activation conditions matter enormously — collapsing the framework during solvent removal destroys porosity. Supercritical CO2 exchange and solvent exchange to low-surface-tension solvents are standard activation strategies. The surface area measured by N2 adsorption (BET method) serves as the primary metric of successful activation.

The applications of MOFs exploit their unmatched combination of high surface area, tunable pore size, and designable surface chemistry. **Gas storage** targets H2 and CH4 for clean energy applications — the DOE target for vehicular H2 storage drives much MOF research. **Gas separation** exploits selective adsorption for CO2 capture, hydrocarbon separation, and air purification. **Catalysis** uses open metal sites or functionalized linkers as active centers within a porous reactor. **Drug delivery** encapsulates therapeutic molecules in pores that release in response to pH or other stimuli. The field has grown to over 100,000 reported structures, and the challenge has shifted from making new MOFs to finding the best MOF for each application — a problem increasingly addressed by computational screening of hypothetical structures.
