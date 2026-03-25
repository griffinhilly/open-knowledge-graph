---
id: inflammatory-response-cellular
title: Cellular Mechanisms of Inflammation
domain: biology
course: immunology
prerequisites:
- id: cytokines-and-chemokines
  type: hard
- id: toll-like-receptors
  type: hard
- id: inflammation-and-wound-healing
  type: soft
builds-toward:
- natural-killer-cells
- hypersensitivity-reactions
tags:
- innate
- inflammation
- cellular-recruitment
stage: advanced
status: validated
---

# Cellular Mechanisms of Inflammation

## Core Idea
Cellular inflammation involves recruitment and activation of innate immune cells—macrophages, neutrophils, dendritic cells—through chemotactic signals and adhesion molecule expression. These cells produce additional cytokines and reactive oxygen species, amplifying the response. Endothelial cells increase permeability, allowing leukocyte extravasation into tissues.

## Questions

```yaml
- question: "What is the correct sequence of steps in the leukocyte extravasation cascade?"
  type: multiple-choice
  options:
    - "Diapedesis → selectin-mediated rolling → integrin-mediated firm arrest → chemokine gradient migration"
    - "Selectin-mediated rolling → chemokine-triggered integrin activation → firm arrest → diapedesis into tissue"
    - "Integrin-mediated firm arrest → rolling along endothelium → diapedesis → chemokine sensing"
    - "Vasodilation → chemokine release → diapedesis → selectin expression on neutrophils"
  answer: 1
  explanation: "Extravasation follows a precise multi-step adhesion cascade. First, endothelial P- and E-selectins grab passing neutrophils and cause them to roll slowly along the vessel wall. Rolling neutrophils then encounter chemokines displayed on the endothelial surface, triggering conformational activation of integrins from low-affinity to high-affinity state — causing firm arrest. The firmly arrested neutrophil then squeezes between endothelial cells (diapedesis) and follows the chemokine gradient into infected tissue. Each step is necessary: blocking selectins prevents rolling and eliminates all downstream steps."

- question: "During acute inflammation, fluid leaks out of blood vessels into tissue, causing swelling (edema). Which of the following best describes the functional role of this edema?"
  type: multiple-choice
  options:
    - "Edema is purely a harmful side effect that the body attempts to minimize; its only purpose is to signal pain"
    - "Edema delivers plasma containing complement proteins and antibodies into the infected tissue, providing additional antimicrobial defense"
    - "Edema dilutes toxins produced by pathogens, reducing their local concentration"
    - "Edema creates physical pressure that mechanically traps pathogens in the infected zone"
  answer: 1
  explanation: "Increased vascular permeability is not collateral damage — it is functional. The leaked plasma carries soluble immune components: complement proteins (which can directly kill bacteria, coat them for phagocytosis, and recruit more immune cells) and antibodies. These components reach the infected tissue through the same gaps in the endothelium that neutrophils will later use for diapedesis. The swelling is thus both a consequence and a contributor to the antimicrobial response. This is why anti-inflammatory drugs that reduce edema can, if used excessively early in infection, impair the immune response."

- question: "Neutrophils arrive at sites of infection before monocytes because neutrophils are the first white blood cells recruited through the leukocyte extravasation cascade during acute inflammation."
  type: true-false
  answer: true
  explanation: "Neutrophils are the first responders in acute inflammation, arriving within minutes to hours of the initial alarm signals. They are abundant in blood, express the selectin ligands and integrins needed for the adhesion cascade, and respond rapidly to the first wave of chemokines. Monocytes arrive later — typically over the next day or two — and differentiate into macrophages in the tissue. The sequential arrival reflects different sensitivities to chemokine signals and different adhesion molecule profiles. This temporal pattern means neutrophil-dominated inflammation characterizes early acute infection, while macrophage-dominated inflammation characterizes later phases and chronic infection."

- question: "The inflammatory response is self-perpetuating once started and must be suppressed by the adaptive immune system to resolve."
  type: true-false
  answer: false
  explanation: "Inflammation is self-limiting through intrinsic mechanisms that operate in parallel with pathogen clearance. As pathogens are eliminated, the pro-inflammatory cytokine stimulus diminishes. Anti-inflammatory cytokines like IL-10 and TGF-β shift the cytokine balance toward resolution. Macrophages switch from pro-inflammatory (M1) to tissue-repair (M2) phenotypes. These mechanisms are innate, not dependent on adaptive immunity — though adaptive immunity can accelerate and amplify both the inflammatory and resolution phases. Chronic inflammation occurs precisely when these self-limiting mechanisms fail, leading to persistent tissue damage in conditions like rheumatoid arthritis."

- question: "How does the cellular inflammatory response bridge innate and adaptive immunity?"
  type: short-answer
  answer: "Dendritic cells at the site of inflammation capture antigens from pathogens and, upon activation, undergo a maturation process that increases their antigen-presenting capacity and upregulates co-stimulatory molecules. They then migrate through lymphatic vessels to draining lymph nodes, where they present processed peptide fragments on MHC molecules to naïve T cells. This antigen presentation, combined with co-stimulatory signals and cytokines produced during the innate response, activates antigen-specific T cells to proliferate and differentiate — initiating the adaptive immune response. The innate inflammatory response thus provides both the antigen (via dendritic cell capture) and the co-stimulatory signals (via pattern recognition receptor activation) that are required for adaptive immunity to begin."
  explanation: "The dendritic cell is the key bridge cell. Without the inflammatory context provided by the innate response — particularly the danger signals detected by toll-like receptors and the cytokines produced by macrophages — dendritic cell maturation is incomplete, and naïve T cells encountering antigen without co-stimulation become anergic (tolerant) rather than activated. This is why adaptive immunity is activated by infection but tolerates self-tissues: self-antigens are typically presented in the absence of inflammatory danger signals."
```

## Explainer

You already know that cytokines and chemokines serve as the signaling molecules of inflammation, and that toll-like receptors detect pathogen-associated molecular patterns to initiate the innate immune response. The cellular inflammatory response is the physical process by which these molecular signals translate into an army of immune cells arriving at the site of infection or injury. The sequence follows a precise choreography: detection, alarm, recruitment, and amplification.

The process begins when **tissue-resident macrophages** and mast cells detect a pathogen through their toll-like receptors and other pattern recognition receptors. These sentinel cells release the first wave of pro-inflammatory cytokines — TNF-α, IL-1, and IL-6 — along with chemokines and histamine. These mediators act on the local blood vessel endothelium, triggering two critical changes: **vasodilation** (widening of blood vessels, increasing blood flow to the area) and **increased vascular permeability** (gaps open between endothelial cells, allowing fluid and proteins to leak into the tissue). This produces the classical signs of inflammation you may have learned about: redness, heat, swelling, and pain. The swelling is not mere collateral damage — the leaked plasma carries complement proteins and antibodies into the tissue, providing additional antimicrobial defense.

**Leukocyte extravasation** — the migration of white blood cells from the bloodstream into infected tissue — is the centerpiece of cellular inflammation. It proceeds through a multi-step adhesion cascade. First, cytokine-activated endothelial cells upregulate **selectins** (P-selectin and E-selectin), adhesion molecules that loosely grab passing neutrophils and cause them to roll slowly along the vessel wall. Rolling neutrophils then encounter chemokines displayed on the endothelial surface, which activate **integrins** on the neutrophil surface — these switch from a low-affinity to a high-affinity conformation, causing the neutrophil to firmly arrest on the endothelium. Finally, the neutrophil squeezes between endothelial cells (a process called **diapedesis**) and follows the chemokine gradient into the tissue. Neutrophils arrive first, within minutes to hours, followed by monocytes that differentiate into macrophages over the next day or two.

Once in the tissue, recruited neutrophils and macrophages destroy pathogens through **phagocytosis** (engulfment and digestion), the release of **reactive oxygen species** (superoxide, hydrogen peroxide) that are directly toxic to microbes, and the secretion of antimicrobial peptides and proteases from their granules. These activated cells also produce additional cytokines, creating a positive feedback loop that recruits more immune cells and amplifies the response. **Dendritic cells** at the site capture antigen and migrate to draining lymph nodes, where they present processed peptides to T cells — bridging the innate inflammatory response to the adaptive immune response. The inflammatory response is self-limiting: as the pathogen is cleared, anti-inflammatory cytokines like IL-10 and TGF-β shift the balance toward resolution, macrophages switch from pro-inflammatory to tissue-repair phenotypes, and the inflammation subsides.
