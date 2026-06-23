---
id: oxidative-deamination
title: Oxidative Deamination
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-structure-and-properties
  type: hard
- id: enzyme-cofactors-and-coenzymes
  type: hard
- id: oxidation-reduction-basics
  type: soft
- id: transamination-reactions
  type: soft
builds-toward:
  - urea-cycle
  - ammonia-metabolism
tags:
- amino-acids
- redox-chemistry
- nitrogen-metabolism
stage: advanced
status: validated
---
# Oxidative Deamination

## Core Idea
Oxidative deamination removes the amino group from glutamate (or other amino acids) while oxidizing the carbon skeleton, producing the corresponding α-keto acid and ammonia. The reaction is catalyzed by glutamate dehydrogenase in mitochondria and is reversible, linking amino acid catabolism to ammonia metabolism.

## Questions

```yaml
- question: "A patient has a rare genetic disorder that eliminates glutamate dehydrogenase (GDH) activity in the liver. Which process would be most directly disrupted?"
  type: multiple-choice
  options:
    - "Transamination of individual amino acids, since GDH is required for each transfer reaction"
    - "The final liberation of free ammonia from the amino acid pool, since most amino acids funnel nitrogen into glutamate before GDH releases it"
    - "The first step of protein catabolism, since GDH initiates breakdown of all dietary amino acids"
    - "The citric acid cycle, since GDH synthesizes citrate from glutamate"
  answer: 1
  explanation: "GDH is not the first step of amino acid catabolism — it is the central convergence point. Most amino acids first donate their amino group to α-ketoglutarate via transamination (catalyzed by aminotransferases), converting themselves to α-keto acids and forming glutamate. GDH then deaminates glutamate, releasing free NH₄⁺. Losing GDH would block this final ammonia-liberation step, even though transamination could still proceed. Nitrogen would accumulate in glutamate with no route to the urea cycle, leading to ammonia toxicity."

- question: "Why does glutamate serve as the central amino donor in oxidative deamination rather than each amino acid being deaminated directly by its own enzyme?"
  type: multiple-choice
  options:
    - "Because glutamate is the most abundant amino acid in the body and has the highest affinity for GDH"
    - "Because transamination funnels nitrogen from many different amino acids into glutamate, allowing a single enzyme (GDH) to handle nitrogen removal for the entire amino acid pool"
    - "Because only glutamate contains the correct α-keto acid structure required for oxidative deamination"
    - "Because the liver lacks the enzymes to deaminate amino acids directly and must convert them to glutamate first"
  answer: 1
  explanation: "This is the key architectural insight of nitrogen metabolism. Transamination reactions (using aminotransferases like ALT and AST) rapidly transfer amino groups from diverse amino acids to α-ketoglutarate, producing glutamate as a common carrier. GDH then acts on this single substrate to release NH₄⁺ in one centralized reaction. This is efficient: rather than requiring a separate deaminase for each of the 20 amino acids, the cell uses aminotransferases to converge nitrogen onto glutamate and a single GDH to extract it."

- question: "Glutamate dehydrogenase can run in reverse, incorporating free ammonia into α-ketoglutarate to synthesize glutamate when conditions favor this direction."
  type: true-false
  answer: true
  explanation: "GDH is reversible — this is one of its most biologically significant properties. The forward reaction (oxidative deamination: glutamate → α-ketoglutarate + NH₄⁺) dominates when amino acid catabolism is active and ammonia needs to be cleared for the urea cycle. The reverse reaction (reductive amination: α-ketoglutarate + NH₄⁺ → glutamate) is favored when ammonia concentrations are elevated and α-ketoglutarate is available. This makes GDH a switch point: it can either feed nitrogen into excretion pathways or recapture it for amino acid biosynthesis, depending on the cell's metabolic state."

- question: "Most dietary amino acids undergo oxidative deamination directly as the first step in their catabolism, with glutamate dehydrogenase acting on each amino acid individually."
  type: true-false
  answer: false
  explanation: "This is incorrect. Most amino acids are NOT direct substrates for glutamate dehydrogenase. Only glutamate is efficiently deaminated by GDH. Other amino acids first undergo transamination — they transfer their amino group to α-ketoglutarate (catalyzed by aminotransferases), forming glutamate and an α-keto acid. GDH then acts on the resulting glutamate. This indirect two-step route (transamination → oxidative deamination) is the standard pathway for nitrogen removal from the amino acid pool."

- question: "Explain why oxidative deamination by glutamate dehydrogenase is described as a 'metabolic crossroads' rather than simply a degradative reaction."
  type: short-answer
  answer: "GDH sits at a crossroads because the reaction is reversible and its direction determines whether nitrogen is directed toward excretion or toward biosynthesis. In the forward direction (deamination), it liberates NH₄⁺ for the urea cycle and produces α-ketoglutarate for the citric acid cycle — a purely catabolic outcome. In the reverse direction (reductive amination), it incorporates free ammonia into glutamate, which can serve as a nitrogen donor for biosynthesis of other amino acids. The enzyme is also allosterically regulated (activated by ADP and leucine, inhibited by GTP), making it responsive to the cell's energy state. This bidirectionality and regulation make it a decision point, not just a disposal step."
  explanation: "The 'crossroads' framing captures the dual role: GDH connects amino acid degradation to the urea cycle (via ammonia), to central energy metabolism (via α-ketoglutarate entering the citric acid cycle), and to amino acid biosynthesis (via reductive amination). Its regulation by energy signals (GTP inhibits, ADP activates) means it senses whether the cell needs more energy from amino acids or less, and adjusts nitrogen flux accordingly. This integration of anabolic and catabolic pathways through one reversible enzyme is what earns it the 'crossroads' description."
```

## Explainer

When the body breaks down amino acids — whether from dietary protein or recycling of damaged cellular proteins — it faces a unique challenge that carbohydrate and fat metabolism do not: amino acids contain nitrogen, and that nitrogen must be removed before the carbon skeleton can be fed into energy-producing pathways. **Oxidative deamination** is the primary reaction that strips nitrogen from the amino acid pool and releases it as free ammonia (NH₄⁺).

The central player is the enzyme **glutamate dehydrogenase (GDH)**, located in the mitochondrial matrix. This enzyme catalyzes the removal of the amino group from glutamate, producing **α-ketoglutarate** (a citric acid cycle intermediate) and free ammonia. The reaction is an oxidation — the carbon that bore the amino group is oxidized as the nitrogen leaves — and it uses either NAD⁺ or NADP⁺ as the electron acceptor. Glutamate is the focal point because, as you know from amino acid structure, most amino acids do not undergo oxidative deamination directly. Instead, they first transfer their amino group to α-ketoglutarate via **transamination** (catalyzed by aminotransferases), funneling nitrogen from many different amino acids into a single molecule — glutamate. Oxidative deamination of glutamate then liberates the nitrogen as ammonia in one centralized reaction.

The reversibility of glutamate dehydrogenase is biologically significant. When ammonia levels are high and α-ketoglutarate is available, the reaction runs in reverse — **reductive amination** — incorporating free ammonia back into glutamate. This means GDH sits at a metabolic crossroads: it can either release nitrogen for excretion (via the urea cycle, which you will study next) or recapture it for biosynthesis of new amino acids. The direction depends on the cell's needs and the relative concentrations of substrates and products. GDH is allosterically regulated accordingly: GTP inhibits it (signaling sufficient energy), while ADP and leucine activate it (signaling a need for carbon skeletons or energy from amino acid catabolism).

The ammonia released by oxidative deamination is toxic at even modest concentrations — it can disrupt brain function by depleting α-ketoglutarate and altering neurotransmitter balance. This is why the reaction occurs in the mitochondria of the liver, where ammonia is immediately channeled into the **urea cycle** for safe conversion to urea and excretion by the kidneys. Oxidative deamination is therefore not just a disposal reaction; it is the critical junction that connects amino acid degradation to nitrogen excretion and, through α-ketoglutarate, links protein catabolism to the central energy-producing pathways of the cell.
