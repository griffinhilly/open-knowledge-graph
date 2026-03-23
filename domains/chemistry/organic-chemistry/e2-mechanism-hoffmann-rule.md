---
id: e2-mechanism-hoffmann-rule
title: E2 Elimination Mechanism and Hoffmann's Rule
domain: chemistry
course: organic-chemistry
prerequisites:
- id: e2-elimination
  type: hard
- id: alkene-structure-and-nomenclature
  type: hard
- id: haloalkane-structure-nomenclature
  type: hard
builds-toward:
- competing-substitution-and-elimination
tags:
- e2
- elimination
- bimolecular
- hoffmann
- anti-periplanar
stage: formal-systems
status: draft
---

# E2 Elimination Mechanism and Hoffmann's Rule

## Core Idea
E2 is a bimolecular elimination occurring in a single step via an anti-periplanar transition state. Hoffmann's rule states that when Zaitsev's rule is expected to give a minor product (due to steric hindrance), the less substituted alkene becomes the major product. E2 is favored by primary and secondary substrates, strong bases, and low temperatures.

## Questions

```yaml
- question: "2-Bromobutane undergoes E2 elimination with potassium tert-butoxide (KOtBu). What is the major product, and why?"
  type: multiple-choice
  options:
    - "2-Butene (more substituted), because Zaitsev's rule always predicts the thermodynamically stable product"
    - "1-Butene (less substituted), because the bulky base cannot reach the more hindered internal β-hydrogen"
    - "2-Butene (more substituted), because the anti-periplanar requirement favors the internal hydrogen"
    - "A mixture of equal amounts of 1-butene and 2-butene, since base size doesn't affect regiochemistry"
  answer: 1
  explanation: "KOtBu is sterically bulky. The internal β-hydrogen (adjacent to the more substituted carbon) is blocked by surrounding methyl groups, preventing the base from abstracting it. The external β-hydrogen (on the less substituted carbon) is more accessible, so 1-butene (the Hoffmann product) is the major product. Option A describes Zaitsev selectivity with a small base — it's wrong here because Hoffmann's rule overrides Zaitsev when the base is bulky."

- question: "The anti-periplanar requirement in E2 elimination means that..."
  type: multiple-choice
  options:
    - "The base must attack from the same face as the leaving group"
    - "The β-hydrogen and leaving group must be 180° apart when viewed along the breaking C–C bond"
    - "The reaction only proceeds when the substrate is a secondary alkyl halide"
    - "The reaction is reversible, allowing the molecule to adopt the required conformation"
  answer: 1
  explanation: "Anti-periplanar means the H being abstracted and the leaving group must be on opposite sides (180° dihedral) along the C–C bond axis — this is a strict geometric requirement for the single concerted step of E2. It applies regardless of base size and regardless of whether Zaitsev or Hoffmann selectivity operates. The anti-periplanar arrangement allows simultaneous bond breaking (C–H and C–LG) and π bond formation."

- question: "Switching from sodium ethoxide (NaOEt) to potassium tert-butoxide (KOtBu) as the base for an E2 reaction can change the major alkene product without changing the substrate."
  type: true-false
  answer: true
  explanation: "This is exactly the point of Hoffmann's rule. The substrate is the same; only the base changes. NaOEt is small and strong — it accesses the more hindered hydrogen and gives the Zaitsev (more substituted) product. KOtBu is bulky and strong — it is sterically blocked from the hindered hydrogen and abstracts the accessible one, giving the Hoffmann (less substituted) product. Same mechanism (E2, anti-periplanar), different regioselectivity driven purely by base steric bulk."

- question: "Hoffmann's rule states that E2 eliminations always produce the less substituted alkene as the major product."
  type: true-false
  answer: false
  explanation: "Hoffmann's rule only applies when a sterically bulky base is used. With a small, strong base (like NaOEt or NaOH), E2 elimination follows Zaitsev's rule — the more substituted (more stable) alkene is the major product. Hoffmann selectivity is a consequence of steric inaccessibility of the more hindered β-hydrogen, not an absolute rule that always overrides Zaitsev."

- question: "Explain why a bulky base like KOtBu produces the less substituted alkene in E2 elimination, even though the more substituted alkene is thermodynamically more stable."
  type: short-answer
  answer: "The bulky tert-butoxide base is physically blocked from abstracting the more hindered β-hydrogen (adjacent to the more substituted carbon) because surrounding alkyl groups create steric congestion. The base can only access the less hindered β-hydrogen (adjacent to the less substituted carbon), so it abstracts that one instead. The reaction is kinetically controlled — the product distribution reflects which β-hydrogen the base can reach, not which product is more stable."
  explanation: "E2 is concerted and irreversible under these conditions, so thermodynamic stability of the product is irrelevant once the transition state determines which hydrogen is abstracted. The Zaitsev product would be thermodynamically preferred, but the bulky base cannot reach the transition state that leads to it. This is a classic example of kinetic vs thermodynamic control: base size determines kinetic accessibility, not the product stability."
```

## Explainer

You already know that E2 elimination removes a proton and a leaving group in a single concerted step, requiring them to be **anti-periplanar** — positioned 180° apart when viewed along the C–C bond axis. This geometric requirement is the key to understanding why the E2 mechanism sometimes defies the usual Zaitsev selectivity and instead follows **Hoffmann's rule**, producing the less substituted alkene as the major product.

Under normal E2 conditions with a moderately sized base like ethoxide (EtO⁻), Zaitsev's rule predicts the more substituted alkene — the thermodynamically more stable product. But when the base is **sterically bulky** — think potassium tert-butoxide ((CH₃)₃CO⁻ K⁺) — the base cannot easily reach the more hindered internal hydrogen. It is physically blocked by the surrounding methyl groups. Instead, it abstracts the more accessible hydrogen on the less substituted side, producing the **Hoffmann product** (the less substituted alkene). The reaction is still E2 in mechanism — concerted, bimolecular, anti-periplanar — but the steric environment of the base shifts the regiochemistry.

Consider 2-bromobutane as a concrete example. With NaOEt (a small base), the major product is 2-butene (Zaitsev: more substituted). With KOtBu (a bulky base), the major product is 1-butene (Hoffmann: less substituted). The substrate is identical in both cases; only the base changes. This demonstrates that regioselectivity in E2 is not purely a property of the substrate but depends on the steric interplay between base and substrate.

Hoffmann selectivity is also observed when the substrate itself is heavily branched. Quaternary ammonium salts undergoing Hofmann elimination (a different but related context) preferentially lose the least hindered proton for the same steric reasons. The practical takeaway is a decision rule: use a small, strong base (NaOEt, NaOH) when you want the Zaitsev (more substituted) alkene, and use a bulky, strong base (KOtBu) when you want the Hoffmann (less substituted) alkene. The anti-periplanar requirement remains non-negotiable in either case — always check that the desired β-hydrogen can achieve the correct geometry before predicting the product.
