---
id: competing-substitution-and-elimination
title: Competition Between Substitution and Elimination Pathways
domain: chemistry
course: organic-chemistry
prerequisites:
- id: sn1-mechanism-kinetics-and-factors
  type: hard
- id: sn2-mechanism-kinetics-and-factors
  type: hard
- id: e1-mechanism-zaitsev-rule
  type: hard
- id: e2-mechanism-hoffmann-rule
  type: hard
- id: substitution-vs-elimination
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- sn-vs-e
- selectivity
- prediction
- reaction-mechanism
stage: formal-systems
status: validated
---

# Competition Between Substitution and Elimination Pathways

## Core Idea
Substitution and elimination reactions compete under the same conditions, with the dominant pathway determined by substrate structure (primary/secondary/tertiary), nucleophile strength and basicity, solvent polarity, and temperature. Predicting product distributions requires analyzing all four mechanisms (SN1, SN2, E1, E2) simultaneously.

## Questions

```yaml
- question: "A tertiary alkyl bromide is treated with sodium tert-butoxide (NaOtBu) in a polar aprotic solvent. Which product predominates, and why?"
  type: multiple-choice
  options:
    - "SN1 substitution product, because tertiary substrates readily form stable carbocations"
    - "E2 elimination product, because tert-butoxide is a strong, bulky base that cannot access the crowded tertiary carbon but can abstract a β-hydrogen"
    - "SN2 substitution product, because tert-butoxide is a strong nucleophile"
    - "E1 elimination product, because tertiary substrates always ionize in polar protic solvents"
  answer: 1
  explanation: "Tertiary substrates cannot undergo SN2 — backside attack is blocked by steric hindrance. SN1 requires a weak nucleophile/base in a polar protic solvent, not a strong base like NaOtBu. Tert-butoxide is too bulky to attack the tertiary carbon but is an effective base for abstracting a β-hydrogen in an E2 mechanism. The result is E2 elimination. The common mistake is defaulting to SN1 for tertiary substrates without considering the strength and character of the reagent."

- question: "A secondary alkyl bromide is treated with NaCN in DMSO. Which product predominates?"
  type: multiple-choice
  options:
    - "E2 elimination product, because secondary substrates preferentially undergo elimination"
    - "SN1 substitution product, because polar solvents stabilize carbocation intermediates"
    - "SN2 substitution product, because CN⁻ is a strong nucleophile and DMSO enhances nucleophilicity without solvating the anion"
    - "No reaction, because CN⁻ is too weak to displace a bromide leaving group"
  answer: 2
  explanation: "CN⁻ is a strong nucleophile but a weak base — it favors substitution over elimination. DMSO is a polar aprotic solvent: it does not hydrogen-bond with the nucleophile, leaving CN⁻ unsolvated and highly reactive, strongly favoring SN2. Secondary substrates are accessible to SN2 when the nucleophile is strong and the substrate is not overly hindered. SN1 requires a polar protic solvent and weak nucleophile/base, neither of which applies here."

- question: "Increasing reaction temperature generally favors elimination over substitution because elimination produces more molecules from one substrate, giving a larger positive entropy change."
  type: true-false
  answer: true
  explanation: "Elimination reactions produce two molecules (alkene + HX or conjugate acid) from one substrate, yielding a positive ΔS. Because ΔG = ΔH − TΔS, larger positive entropy terms become increasingly favorable at higher temperatures. This is a consistent principle: when temperature is raised in an S_N vs. E competition, the E product fraction typically increases. Enthalpy differences also play a role, but the entropy advantage of elimination is the dominant thermodynamic driver of this temperature dependence."

- question: "A primary alkyl halide treated with a strong base like NaOEt will primarily undergo SN1 because primary substrates ionize readily to form primary carbocations stabilized by the alkoxide."
  type: true-false
  answer: false
  explanation: "Primary carbocations are extremely unstable — they essentially cannot form under normal conditions. This rules out both SN1 and E1 for primary substrates, since both require prior ionization to a carbocation. With NaOEt (a strong base but not excessively bulky), the primary substrate undergoes either SN2 (backside attack is unhindered) or E2 (proton abstraction by ethoxide). The statement is wrong in predicting SN1 and in invoking carbocation stabilization by alkoxide, which is not a real stabilization pathway."

- question: "What is the first step when predicting which mechanism dominates in a substitution/elimination problem, and why is it performed before analyzing the reagent?"
  type: short-answer
  answer: "Identify the substrate class — primary, secondary, or tertiary — because substrate structure immediately eliminates impossible mechanisms. Primary substrates cannot undergo SN1 or E1 (primary carbocations are too unstable). Tertiary substrates cannot undergo SN2 (steric hindrance blocks backside attack). This filtering step narrows the field to feasible mechanisms before reagent character, solvent, or temperature are evaluated."
  explanation: "Starting with substrate structure is decisive because it imposes hard constraints, not just tendencies. Once impossible mechanisms are eliminated, the remaining candidates are assessed using: nucleophile/base character (strong nucleophile-weak base favors S_N; strong base-poor nucleophile favors E; both properties → look at substrate and solvent), solvent polarity (polar protic → SN1/E1; polar aprotic → SN2), and temperature (higher → more elimination). Skipping the substrate analysis step leads to predicting impossible mechanisms and wrong products."
```

## Explainer

You have now studied all four mechanisms individually — SN1, SN2, E1, and E2 — and understand their kinetics, stereochemistry, and preferred conditions. The challenge in real chemistry is that when you mix a haloalkane with a reagent, all four pathways are potentially available simultaneously. The dominant products depend on how four variables interact: **substrate structure**, **nucleophile/base character**, **solvent**, and **temperature**. Learning to predict which pathway wins is the central skill of this topic.

Start with substrate structure, because it is the strongest filter. **Primary substrates** strongly favor SN2 — the unhindered carbon is accessible to backside attack by a nucleophile. E2 can compete if you use a strong, bulky base (like tert-butoxide), because the base is too sterically hindered to attack carbon but can still abstract a β-hydrogen. SN1 and E1 are essentially impossible for primary substrates because primary carbocations are too unstable to form. **Tertiary substrates** are the opposite: the carbon bearing the leaving group is too crowded for the SN2 backside attack, so SN2 is ruled out. Instead, tertiary substrates follow SN1/E1 (with weak nucleophiles in polar protic solvents) or E2 (with strong bases). **Secondary substrates** are the most ambiguous — all four mechanisms are potentially operative, and the other variables become decisive.

Next, consider the reagent. A **strong nucleophile that is a weak base** (like I⁻, CN⁻, or RS⁻) favors substitution. A **strong base that is a poor nucleophile** (like tert-butoxide or DBU) favors elimination. A reagent that is both a strong nucleophile and a strong base (like hydroxide or ethoxide) can go either way, and you must look at the substrate and conditions to decide. Weak nucleophiles/weak bases (like water or alcohols) point toward SN1/E1 pathways, which do not require a strong nucleophile because the rate-determining step is unimolecular ionization of the substrate.

Solvent and temperature provide the final adjustments. **Polar protic solvents** (water, alcohols) stabilize carbocations and promote ionization, favoring SN1 and E1. **Polar aprotic solvents** (DMSO, DMF, acetone) do not stabilize cations but do enhance nucleophilicity by not solvating the nucleophile, strongly favoring SN2. Higher temperature generally tips the balance toward elimination (E1 or E2) over substitution, because elimination has a larger positive entropy change — two product molecules form from one substrate.

In practice, the decision tree works like this: identify the substrate class first, eliminate impossible mechanisms, then use the nucleophile/base character and solvent to pick the winner among the remaining candidates. For a tertiary substrate with a strong base, it is E2. For a primary substrate with a good nucleophile in a polar aprotic solvent, it is SN2. For a secondary substrate with a weak nucleophile in a polar protic solvent, SN1 and E1 compete, with E1 favored at higher temperatures. Drilling problems across all substrate classes until this logic becomes automatic is the only way to build reliable predictive skill.
