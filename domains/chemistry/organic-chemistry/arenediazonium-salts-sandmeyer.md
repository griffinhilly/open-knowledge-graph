---
id: arenediazonium-salts-sandmeyer
title: Arenediazonium Salts and the Sandmeyer Reaction
domain: chemistry
course: organic-chemistry
prerequisites:
- id: amines-structure-and-properties
  type: hard
- id: electrophilic-aromatic-substitution
  type: hard
- id: directed-ortho-para-effects
  type: soft
- id: nucleophilic-aromatic-substitution
  type: soft
builds-toward: []
tags:
- diazonium salts
- diazotization
- Sandmeyer reaction
- azo coupling
- aromatic synthesis
stage: formal-systems
status: validated
---

# Arenediazonium Salts and the Sandmeyer Reaction

## Core Idea
A primary aromatic amine reacts with nitrous acid in cold solution to give an arenediazonium salt, ArN₂⁺. Because N₂ is an excellent leaving group, the diazonium group can be replaced by Cl, Br, CN (Sandmeyer reactions with copper(I) salts), I, F, OH or H. Diazonium ions also act as weak electrophiles toward activated rings, forming azo dyes. This makes the amino group a temporary handle for substitution patterns that direct electrophilic aromatic substitution cannot reach.

## How It's Best Learned
Learn the diazotization conditions first (NaNO₂ and HCl at 0–5 °C), then make a one-page table of each replacement with its reagent. Practise multistep syntheses that use NH₂ as a removable director, for example making 1,3,5-tribromobenzene from aniline. End with azo coupling and connect it to the color of common dyes.

## Common Misconceptions
- All diazonium salts are stable intermediates. (Aliphatic diazonium ions lose N₂ almost at once; arenediazonium salts survive only in cold solution and can be explosive when dry.)
- The Sandmeyer reaction is an SN2 displacement on the ring. (Backside attack is impossible at an aromatic carbon; the copper-mediated replacement involves single-electron transfer and an aryl radical.)
- In azo coupling the diazonium ion is the nucleophile. (The diazonium ion is the electrophile, and it reacts only with electron-rich rings such as phenols and aromatic amines.)

## Questions

```yaml
- question: "Which reagent converts benzenediazonium chloride into benzonitrile, C₆H₅CN?"
  type: multiple-choice
  options: ["KCN alone at room temperature", "CuCN", "H₃PO₂", "HBF₄ then heat"]
  answer: 1
  explanation: "Copper(I) cyanide replaces the diazonium group with CN in a Sandmeyer reaction. H₃PO₂ replaces it with H, and HBF₄ followed by heat gives the aryl fluoride."
- question: "Which sequence converts aniline into 1,3,5-tribromobenzene?"
  type: multiple-choice
  options: ["Br₂/FeBr₃ on benzene three times", "Br₂ (excess), then NaNO₂/HCl at 0 °C, then H₃PO₂", "NaNO₂/HCl, then CuBr three times", "H₃PO₂, then Br₂ (excess)"]
  answer: 1
  explanation: "The strongly activating NH₂ group directs three bromines to its ortho and para positions, which are meta to each other. Diazotization and treatment with H₃PO₂ then remove the nitrogen, leaving three bromines in a 1,3,5 pattern."
- question: "Aliphatic diazonium salts are about as stable as arenediazonium salts and are equally useful in synthesis."
  type: true-false
  answer: false
  explanation: "An alkyl diazonium ion loses N₂ very rapidly to give a carbocation, which leads to mixtures of products. The aromatic ring stabilizes ArN₂⁺ enough to use it in cold solution."
- question: "What is azo coupling, and why does it require an activated aromatic ring?"
  type: short-answer
  answer: "Azo coupling is electrophilic aromatic substitution in which an arenediazonium ion attacks an electron-rich arene, usually a phenol or aromatic amine, to form an Ar–N=N–Ar′ azo compound. The diazonium ion is a weak electrophile, so it reacts only with strongly activated rings."
  explanation: "The extended conjugation through the N=N link makes azo compounds absorb visible light, which is why many dyes and indicators, such as methyl orange, are azo compounds."
```

## Explainer

Electrophilic aromatic substitution can add many groups to a benzene ring, but it cannot place every group in every position. Arenediazonium salts fill many of those gaps.

The starting point is a primary aromatic amine such as aniline. Treated with sodium nitrite and hydrochloric acid at 0–5 °C, it forms an arenediazonium salt, ArN₂⁺ Cl⁻. This step is called diazotization, and the nitrosonium ion, NO⁺, formed from nitrous acid is the species that attacks the amine nitrogen. The cold temperature matters. Warm diazonium solutions decompose, and dry diazonium salts can explode.

The diazonium group is valuable because it leaves as very stable nitrogen gas, so many groups can replace it. With copper(I) salts, the Sandmeyer reactions give aryl chlorides (CuCl), aryl bromides (CuBr) and aryl nitriles (CuCN). Traugott Sandmeyer discovered this chemistry in 1884. The copper(I) ion transfers one electron to the diazonium ion, which loses N₂ to form an aryl radical, and the radical then picks up the halide or cyanide. Other replacements need no copper. Potassium iodide gives aryl iodides. Heating the tetrafluoroborate salt gives aryl fluorides, a method called the Balz–Schiemann reaction. Warming in water gives phenols. Hypophosphorous acid, H₃PO₂, replaces the group with hydrogen.

The last reaction is surprisingly useful. It lets you use NH₂ as a temporary director. The amino group strongly activates its ortho and para positions. Brominating aniline gives 2,4,6-tribromoaniline, with the three bromines meta to each other. Diazotizing and then treating with H₃PO₂ removes the nitrogen. The product, 1,3,5-tribromobenzene, cannot be made by brominating benzene directly, because bromine is an ortho, para director.

Diazonium ions can also keep their nitrogen. They are weak electrophiles and attack electron-rich arenes such as phenols and aromatic amines, usually at the para position. This azo coupling forms compounds of the type Ar–N=N–Ar′. The long conjugated system absorbs visible light, so azo compounds are colored. Many textile dyes and acid-base indicators, including methyl orange, are made this way.

When planning an aromatic synthesis, consider whether an amino group, installed by nitration and reduction, could be converted later into the group you need.
