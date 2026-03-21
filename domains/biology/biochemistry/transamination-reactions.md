---
id: transamination-reactions
title: Transamination and Aminotransferases
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-structure-and-properties
  type: hard
- id: enzyme-kinetics
  type: hard
- id: enzyme-cofactors-and-coenzymes
  type: soft
- id: nucleophile-electrophile-definitions
  type: soft
builds-toward:
  - oxidative-deamination
  - urea-cycle
tags:
- amino-acids
- enzymes
- nitrogen-transfer
stage: advanced
status: draft
---
# Transamination and Aminotransferases

## Core Idea
Transamination is the reversible transfer of an amino group from an amino acid to a keto acid, catalyzed by aminotransferases. The reaction requires pyridoxal phosphate (PLP) as a cofactor and is the primary mechanism for both amino acid synthesis and degradation. The amino group typically transfers to α-ketoglutarate, forming glutamate.

## How It's Best Learned
Draw the PLP-mediated mechanism showing Schiff base formation. Compare ALT and AST in serum—when and why they are elevated in disease. Calculate amino acid pools using transamination.

## Common Misconceptions
Transamination removes ammonia directly; it transfers the amino group to another keto acid. The reaction is freely reversible, not unidirectional.

## Questions

```yaml
- question: "A cell needs to synthesize the non-essential amino acid alanine and has ample pyruvate (a keto acid) and glutamate available. How can transamination accomplish this synthesis?"
  type: multiple-choice
  options:
    - "It cannot — transamination is a catabolic reaction that only degrades amino acids, not synthesizes them"
    - "Alanine aminotransferase (ALT) transfers the amino group from glutamate to pyruvate, forming alanine and α-ketoglutarate — the reaction runs in the biosynthetic direction"
    - "PLP directly adds an inorganic amino group (from NH₄⁺) to pyruvate to form alanine"
    - "Glutamate is first deaminated to release free NH₃, which then attaches spontaneously to pyruvate"
  answer: 1
  explanation: "Transamination is freely reversible. The ALT reaction — alanine + α-ketoglutarate ⇌ pyruvate + glutamate — runs in either direction depending on the relative concentrations of reactants and products. When pyruvate and glutamate are abundant, the reaction runs right-to-left: the amino group from glutamate is transferred to pyruvate, producing alanine. This is how cells synthesize nonessential amino acids from carbon skeletons (keto acids) when needed. The key misconception to avoid: transamination does not release free ammonia and is not inherently directional."

- question: "Why is ALT (alanine aminotransferase) elevated in blood tests following liver damage?"
  type: multiple-choice
  options:
    - "The damaged liver synthesizes extra ALT as part of the inflammatory repair response, releasing it into the bloodstream"
    - "Liver inflammation increases the rate of transamination reactions, generating more product ALT enzyme"
    - "Injured or dying hepatocytes lose membrane integrity and release their intracellular contents — including cytoplasmic ALT — into the circulation"
    - "ALT in the blood converts circulating amino acids into energy substrates to compensate for impaired hepatic metabolism"
  answer: 2
  explanation: "ALT and AST are normally intracellular enzymes concentrated in hepatocytes. When liver cells are injured (by toxins, viruses, ischemia), their membranes become permeable and their contents leak into the bloodstream. Elevated serum ALT and AST are therefore markers of hepatocyte death or injury, not increased metabolic activity. ALT is more liver-specific (also found in kidney and muscle), while AST is present in heart and skeletal muscle as well, which is why both are measured together and the ALT:AST ratio has diagnostic value."

- question: "PLP (pyridoxal phosphate) acts as a molecular intermediary in transamination, temporarily carrying the amino group as pyridoxamine phosphate (PMP) in a ping-pong mechanism before donating it to the incoming keto acid."
  type: true-false
  answer: true
  explanation: "This is the key mechanistic insight. PLP is not a passive cofactor — it is an active participant. First, the amino acid's amino group is transferred to PLP via Schiff base formation, converting PLP to PMP (pyridoxamine phosphate) and the amino acid to its corresponding keto acid. The enzyme is now in its PMP-bound form. Second, the incoming keto acid accepts the amino group from PMP, restoring PLP and releasing the new amino acid. This sequential half-reaction mechanism explains why the enzyme requires only one cofactor to handle two substrates, and why vitamin B₆ deficiency impairs amino acid metabolism broadly."

- question: "Transamination directly releases free ammonia (NH₃) from amino acids, which is immediately detoxified by the urea cycle."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about transamination. The reaction transfers an amino group from an amino acid to a keto acid — it does not release free ammonia. The amino group moves intact from one molecule to another. Free ammonia is released only in the subsequent step: oxidative deamination of glutamate by glutamate dehydrogenase. Transamination first concentrates nitrogen into glutamate (the universal nitrogen collector), and only then is free NH₄⁺ generated for entry into the urea cycle. This two-step mechanism prevents the toxic buildup of free ammonia during amino acid catabolism."

- question: "What role does transamination play as a 'nitrogen funnel,' and why is this mechanism important for amino acid catabolism?"
  type: short-answer
  answer: "Transamination funnels nitrogen from diverse amino acids into a single collector molecule — glutamate — by transferring their amino groups to α-ketoglutarate. Because most amino acids cannot be directly deaminated to release free ammonia, they must first donate their amino group to α-ketoglutarate via aminotransferases, producing glutamate. Glutamate then undergoes oxidative deamination by glutamate dehydrogenase to release NH₄⁺, which enters the urea cycle. This two-step funnel allows the body to handle nitrogen from all 20 amino acids through a single controlled release point rather than generating free ammonia throughout metabolism."
  explanation: "The funnel mechanism is elegant because it solves two problems simultaneously: (1) diversity — there are 20 amino acids with different structures, but all can donate their amino group to α-ketoglutarate, channeling nitrogen into one carrier; (2) safety — free ammonia is highly toxic to cells (especially neurons), so the body minimizes free ammonia by first collecting nitrogen as glutamate before releasing it in a controlled, tissue-specific manner. The clinical consequences of disrupting this system — as in urea cycle disorders — illustrate how essential the funnel is."
```

## Explainer

Amino acids are unique among biomolecules because they carry nitrogen — and managing that nitrogen is one of metabolism's central challenges. **Transamination** is the reaction that shuttles amino groups between molecules, and it is the entry point for both amino acid synthesis and degradation. If you understand amino acid structure (an amino group, a carboxyl group, and a variable R group on a central carbon) and the basics of enzyme kinetics, transamination is where those concepts converge in a single, elegant reaction.

The reaction itself is conceptually simple: an **amino acid** donates its amino group to a **keto acid** (an α-keto acid, which has a carbonyl where the amino group would be). The amino acid becomes a keto acid, and the keto acid becomes an amino acid. It is a molecular swap — nitrogen moves from one carbon skeleton to another, and neither molecule is destroyed. For example, alanine (amino acid) + α-ketoglutarate (keto acid) → pyruvate (keto acid) + glutamate (amino acid). The enzyme catalyzing this particular reaction is **alanine aminotransferase (ALT)**, and its counterpart **aspartate aminotransferase (AST)** transfers the amino group from aspartate to α-ketoglutarate. Both are clinically measured in blood tests — elevated ALT and AST indicate liver damage because these enzymes leak from injured hepatocytes.

What makes transamination mechanistically fascinating is its absolute dependence on the cofactor **pyridoxal phosphate (PLP)**, the active form of vitamin B₆. PLP acts as a molecular intermediary: first, it forms a **Schiff base** (a covalent bond between its aldehyde group and the amino acid's amino group), then facilitates the transfer of the amino group through a series of electron rearrangements. Midway through the reaction, PLP temporarily carries the amino group as pyridoxamine phosphate (PMP), then donates it to the incoming keto acid. This ping-pong mechanism means the enzyme cycles between two forms — PLP-bound and PMP-bound — with each half-reaction handling one substrate.

The metabolic significance of transamination lies in its role as a **nitrogen funnel**. Most amino acids cannot be directly deaminated (have their nitrogen removed as free ammonia). Instead, their amino groups are first transaminated onto α-ketoglutarate, producing **glutamate** — the universal nitrogen collector. Glutamate can then be oxidatively deaminated by glutamate dehydrogenase to release free NH₄⁺, which enters the urea cycle for excretion. This two-step process (transamination → oxidative deamination) is how the body safely handles the nitrogen from protein breakdown. Because the reaction is freely reversible, transamination also works in the biosynthetic direction — cells can synthesize nonessential amino acids by transferring amino groups onto available carbon skeletons.
