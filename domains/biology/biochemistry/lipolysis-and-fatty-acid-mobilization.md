---
id: lipolysis-and-fatty-acid-mobilization
title: Lipolysis and Fatty Acid Mobilization
domain: biology
course: biochemistry
prerequisites:
- id: fatty-acid-structure-and-classification
  type: hard
- id: hormone-signaling-mechanisms
  type: soft
builds-toward:
- ketone-body-metabolism
- fatty-acid-oxidation-beta-oxidation
tags:
- lipolysis
- hormone-sensitive-lipase
- fatty-acid-release
stage: formal-systems
status: validated
---

# Lipolysis and Fatty Acid Mobilization

## Core Idea
Lipolysis is the breakdown of triglycerides into glycerol and free fatty acids, catalyzed by hormone-sensitive lipase (HSL) in adipose tissue. Epinephrine and glucagon activate HSL via PKA-mediated phosphorylation; insulin inhibits it. Released fatty acids bind albumin and are transported to liver and muscle for oxidation.

## Questions

```yaml
- question: "During prolonged fasting, which sequence correctly describes how glucagon triggers fatty acid release from adipocytes?"
  type: multiple-choice
  options:
    - "Glucagon → insulin receptor blockade → HSL activation → fatty acid release"
    - "Glucagon → GPCR → adenylyl cyclase → cAMP → PKA → phosphorylation of HSL and perilipin → fatty acid release"
    - "Glucagon → direct binding to HSL → conformational change → fatty acid release"
    - "Glucagon → phosphodiesterase activation → cAMP rise → PKA → fatty acid release"
  answer: 1
  explanation: "Glucagon binds a G-protein-coupled receptor on adipocytes, activating adenylyl cyclase, which raises cAMP. Elevated cAMP activates protein kinase A (PKA), which phosphorylates both HSL (activating it) and perilipin (exposing the lipid droplet surface). Together these allow HSL to access and hydrolyze triglycerides. Option D is wrong because glucagon activates phosphodiesterase would degrade cAMP — the opposite of what happens. Option C is wrong because glucagon never binds HSL directly."

- question: "Why must free fatty acids travel through the bloodstream bound to albumin rather than freely dissolved?"
  type: multiple-choice
  options:
    - "Albumin acts as an enzyme that activates fatty acids for oxidation during transport"
    - "Fatty acids are electrically charged and would repel red blood cells without albumin"
    - "Fatty acids are hydrophobic and would be toxic to cell membranes at high free concentrations; albumin provides soluble carrier capacity"
    - "Free fatty acids would be immediately oxidized by plasma enzymes without albumin protection"
  answer: 2
  explanation: "Free fatty acids are hydrophobic — they don't dissolve readily in the aqueous plasma, and at high free concentrations they can intercalate into and disrupt cell membranes. Albumin, a large plasma protein with multiple fatty acid binding sites, effectively solubilizes them, allowing safe transport at the concentrations required during active lipolysis. Albumin does not activate or protect fatty acids enzymatically; it purely provides a hydrophilic carrier."

- question: "Hormone-sensitive lipase (HSL) alone is sufficient to fully hydrolyze a triglyceride into glycerol and three free fatty acids."
  type: true-false
  answer: false
  explanation: "Triglyceride breakdown requires three distinct lipases acting sequentially. ATGL (adipose triglyceride lipase) removes the first fatty acid, producing diacylglycerol. HSL then removes the second, producing monoacylglycerol. Finally, monoacylglycerol lipase (MGL) removes the third fatty acid, yielding free glycerol. HSL is the most hormonally regulated step and is often described as the 'rate-limiting' enzyme, but it cannot complete the job alone."

- question: "Insulin inhibits lipolysis by activating phosphodiesterase 3B, which degrades cAMP and thereby keeps PKA and HSL inactive."
  type: true-false
  answer: true
  explanation: "This is the molecular mechanism of insulin's anti-lipolytic effect. Insulin signaling activates phosphodiesterase 3B (PDE3B) in adipocytes. PDE3B degrades cAMP to AMP, collapsing the cAMP signal that would otherwise activate PKA. Without active PKA, HSL remains dephosphorylated and inactive, and perilipin keeps the lipid droplet surface inaccessible. This explains why lipolysis is suppressed in the fed state and why insulin resistance — which weakens this brake — leads to excess fatty acid release even during meals."

- question: "Explain why the insulin-to-glucagon ratio functions as a master switch for lipolysis, and what goes wrong in insulin resistance."
  type: short-answer
  answer: "When the ratio is high (fed state), insulin dominates: it activates PDE3B, degrading cAMP and keeping PKA and HSL inactive, so triglycerides stay stored. When the ratio is low (fasting, exercise), glucagon (and epinephrine) dominate: cAMP rises, PKA activates, and HSL is phosphorylated to break down triglycerides. In insulin resistance, adipocytes respond poorly to insulin's inhibitory signal, so lipolysis continues even when blood glucose is high, flooding the liver and blood with excess fatty acids and contributing to dyslipidemia and fatty liver disease."
  explanation: "The ratio matters more than absolute levels of either hormone. Even if glucagon is low, if insulin is also very low (as in starvation), cAMP can rise. Insulin resistance is particularly damaging because the system loses its 'fed state' brake: adipose tissue releases fatty acids throughout the day regardless of food intake, worsening metabolic syndrome."
```

## Explainer

Your body stores energy primarily as **triglycerides** — three fatty acid chains esterified to a glycerol backbone — packed into lipid droplets inside adipocytes. When energy demand rises (during fasting, exercise, or stress), those stored fats must be broken down and shipped to tissues that can oxidize them. This breakdown process is **lipolysis**, and understanding it means following a hormonal signal from the bloodstream all the way to the release of free fatty acids.

The signaling cascade works through the hormone-signaling mechanisms you already know. During fasting, the pancreas releases **glucagon**; during exercise or stress, the adrenal medulla releases **epinephrine**. Both hormones bind G-protein-coupled receptors on adipocytes, activating adenylyl cyclase, which raises intracellular cAMP. Rising cAMP activates **protein kinase A (PKA)**, which phosphorylates two key targets: **hormone-sensitive lipase (HSL)** and **perilipin**, the protein coating the lipid droplet surface. Phosphorylated perilipin changes conformation, exposing the triglyceride core, while phosphorylated HSL translocates from the cytosol to the droplet surface. The process is actually sequential: **adipose triglyceride lipase (ATGL)** removes the first fatty acid (producing diacylglycerol), HSL removes the second (producing monoacylglycerol), and **monoacylglycerol lipase (MGL)** removes the third. The net result is one glycerol and three free fatty acids per triglyceride molecule.

**Insulin** acts as the brake on this system. In the fed state, insulin activates phosphodiesterase 3B, which degrades cAMP, shutting down PKA and keeping HSL dephosphorylated and inactive. This is why lipolysis is suppressed after meals and activated during fasting — the insulin-to-glucagon ratio is the master switch. In insulin resistance, this brake weakens: adipocytes release fatty acids even when blood glucose is high, flooding the liver with lipid and contributing to fatty liver disease and dyslipidemia.

Once released, free fatty acids face a transport problem — they are hydrophobic and would be toxic to membranes at high concentrations. The solution is **serum albumin**, a large plasma protein with multiple fatty acid binding sites. Albumin ferries fatty acids through the blood to the liver (for ketogenesis or re-esterification) and to skeletal and cardiac muscle (for beta-oxidation). Glycerol, being water-soluble, travels freely to the liver, where glycerol kinase phosphorylates it to glycerol-3-phosphate, feeding it into glycolysis or gluconeogenesis. This division of labor — fatty acids for oxidation, glycerol for glucose production — makes lipolysis a critical node connecting fat metabolism to carbohydrate metabolism during fasting.
