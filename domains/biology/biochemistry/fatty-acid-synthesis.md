---
id: fatty-acid-synthesis
title: Fatty Acid Synthesis and Regulation
domain: biology
course: biochemistry
prerequisites:
- id: fatty-acid-oxidation-beta-oxidation
  type: hard
- id: pentose-phosphate-pathway
  type: soft
builds-toward:
- cholesterol-synthesis
- metabolic-integration-hormonal-regulation
tags:
- fatty acid synthesis
- acetyl-CoA carboxylase
- fatty acid synthase
- NADPH
stage: formal-systems
status: validated
---

# Fatty Acid Synthesis and Regulation

## Core Idea
Fatty acid synthesis (lipogenesis) is an anabolic pathway that builds fatty acids from acetyl-CoA units, primarily in the liver, adipose tissue, and mammary glands. The process requires acetyl-CoA carboxylase (catalyzes the first committed step, forming malonyl-CoA) and fatty acid synthase (a large multienzymatic complex catalyzing the iterative condensation, reduction, and dehydration of malonyl units). Unlike β-oxidation, synthesis uses NADPH (from the pentose phosphate pathway and malic enzyme) rather than NAD⁺/FAD. Fatty acid synthesis is allosterically activated by citrate and inhibited by AMP, palmitoyl-CoA, and glucagon.

## Questions

```yaml
- question: "A cell has high AMP levels and low citrate. What happens to fatty acid synthesis, and why?"
  type: multiple-choice
  options:
    - "Synthesis accelerates because AMP signals that the cell needs more energy storage"
    - "Synthesis is inhibited because AMP activates AMPK, which phosphorylates and inactivates acetyl-CoA carboxylase"
    - "Synthesis is unaffected — AMP only regulates glycolysis"
    - "Synthesis accelerates because low citrate removes feedback inhibition from fatty acid synthase"
  answer: 1
  explanation: "High AMP signals energy deficit (low ATP:AMP ratio), activating AMP-activated protein kinase (AMPK). AMPK phosphorylates acetyl-CoA carboxylase (ACC), inactivating it and blocking malonyl-CoA production — the first committed step of fatty acid synthesis. Low citrate compounds the inhibition: citrate is the allosteric activator of ACC, and without it, the committed step is further suppressed. The cell would be foolish to spend energy building fat when it is starved for ATP. This is a textbook example of the cell reading its energy state through ACC."

- question: "Which of the following correctly identifies a key difference between fatty acid synthesis and β-oxidation?"
  type: multiple-choice
  options:
    - "Synthesis uses NADPH as the electron donor; β-oxidation produces NADH and FADH₂"
    - "Both pathways use the same enzymes but run in opposite directions"
    - "Synthesis occurs in mitochondria; β-oxidation occurs in the cytoplasm"
    - "Synthesis produces acetyl-CoA; β-oxidation consumes acetyl-CoA"
  answer: 0
  explanation: "Fatty acid synthesis is explicitly not the reverse of β-oxidation. It uses NADPH (from the pentose phosphate pathway and malic enzyme) as the reducing agent, while β-oxidation produces NADH and FADH₂ as it oxidizes fatty acids. The pathways also use different enzymes, different subcellular compartments (synthesis in cytoplasm, β-oxidation in mitochondria), and different acyl carriers. This separation allows the cell to regulate them independently — a crucial design principle since running both simultaneously in the same compartment would waste energy."

- question: "The CO₂ added by acetyl-CoA carboxylase is incorporated into the final palmitate product."
  type: true-false
  answer: false
  explanation: "This is a classic misconception. Acetyl-CoA carboxylase adds CO₂ to acetyl-CoA to form malonyl-CoA — but this CO₂ is immediately released in the next step when malonyl-CoA condenses with the growing chain on fatty acid synthase. The CO₂ is not incorporated into the final fatty acid; it serves as a thermodynamic 'handle' that makes the condensation reaction energetically favorable (the decarboxylation drives the reaction forward). Palmitate contains only the carbons from acetyl-CoA units."

- question: "Fatty acid synthesis is regulated by hormonal signals: insulin promotes synthesis while glucagon suppresses it."
  type: true-false
  answer: true
  explanation: "Insulin, secreted when blood glucose is high, stimulates lipogenesis by activating ACC phosphatase, which dephosphorylates and activates ACC — promoting malonyl-CoA production and fatty acid synthesis. Glucagon (and epinephrine), secreted during energy deficit or stress, promotes ACC phosphorylation via PKA, inactivating the enzyme and suppressing synthesis. This hormonal axis ensures fat synthesis is linked to nutritional state: excess glucose that cannot all be stored as glycogen is channeled into fat, a process coordinated by pancreatic hormones."

- question: "Why does fatty acid synthesis require a separate 'activation' step that adds and immediately removes a CO₂ group, rather than simply condensing two acetyl-CoA molecules directly?"
  type: short-answer
  answer: "Direct condensation of two acetyl-CoA molecules (a Claisen condensation) is thermodynamically unfavorable — the equilibrium strongly favors the reverse reaction. By first carboxylating acetyl-CoA to malonyl-CoA (using ATP), the subsequent condensation step gains driving force from the simultaneous decarboxylation of malonyl-CoA. The CO₂ is added and immediately released, but the energy cost of its addition is what makes the overall condensation favorable. This is a common biochemical strategy: thermodynamically uphill reactions are driven by coupling to ATP hydrolysis or decarboxylation."
  explanation: "The CO₂ trick is analogous to the biotin-dependent carboxylation strategy used in other biosynthetic pathways (e.g., pyruvate carboxylase). The cell spends one ATP to add the CO₂ via ACC, then 'cashes in' the energy stored in the C–COO⁻ bond to drive the condensation on fatty acid synthase. Without this step, the chain-elongation chemistry would not proceed spontaneously, and the entire pathway would be thermodynamically blocked."
```

## Explainer

If β-oxidation is the process of chopping fatty acids into two-carbon acetyl-CoA units, fatty acid synthesis is essentially the reverse challenge: stitching two-carbon units back together into a long hydrocarbon chain. But cells do not simply run β-oxidation backwards. Instead, fatty acid synthesis uses a completely different set of enzymes, a different cellular compartment (the cytoplasm rather than the mitochondrial matrix), and a different electron carrier — **NADPH** instead of NADH and FADH₂. This separation is a recurring theme in metabolism: catabolic and anabolic pathways for the same molecule are kept distinct so the cell can regulate them independently.

The pathway begins with a critical problem: acetyl-CoA is produced inside mitochondria, but synthesis happens in the cytoplasm. Acetyl-CoA cannot cross the inner mitochondrial membrane directly, so it is shuttled out as citrate (via the citrate shuttle), then regenerated in the cytoplasm. Once there, **acetyl-CoA carboxylase (ACC)** catalyzes the first committed step: adding a CO₂ to acetyl-CoA to form **malonyl-CoA**, a three-carbon activated building block. This carboxylation is the key regulatory point of the entire pathway — ACC is activated by citrate (signaling energy abundance) and inhibited by palmitoyl-CoA (the end product, providing feedback inhibition) and by phosphorylation driven by AMP-activated protein kinase when cellular energy is low.

From malonyl-CoA, the heavy lifting is done by **fatty acid synthase (FAS)**, a large homodimeric enzyme complex that carries the growing chain on an acyl carrier protein domain. Each cycle adds two carbons: malonyl-CoA condenses with the growing chain (releasing the CO₂ that was added by ACC), then the resulting β-keto group is reduced, dehydrated, and reduced again — four reactions per cycle, each consuming NADPH. After seven cycles, the 16-carbon saturated fatty acid **palmitate** is released. The NADPH consumed at each reduction step comes from two sources you already know: the **pentose phosphate pathway** (which produces NADPH in its oxidative phase) and the malic enzyme reaction that converts malate to pyruvate in the cytoplasm.

The regulation of fatty acid synthesis reflects the cell's overall energy state. When glucose is plentiful and energy stores are full, citrate accumulates in mitochondria and is exported to the cytoplasm, where it both provides the carbon source (via acetyl-CoA) and allosterically activates ACC. Insulin stimulates lipogenesis by activating ACC phosphatase, while glucagon and epinephrine suppress it by promoting ACC phosphorylation. This hormonal control ensures that the body synthesizes fat only when energy intake exceeds immediate needs — the biochemical basis of why chronic caloric surplus leads to fat accumulation.
