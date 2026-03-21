---
id: drug-induced-liver-injury-pathophysiology
title: 'Drug-Induced Liver Injury: Hepatocellular vs. Cholestatic Patterns and Mechanisms'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: hepatocellular-injury-mechanisms
  type: hard
- id: cytochrome-p450-metabolism
  type: soft
- id: hemostasis-pathophysiology
  type: soft
builds-toward:
  - acute-liver-failure-pathophysiology
tags:
- drug-induced-injury
- hepatotoxicity
- cholestasis
stage: advanced
status: draft
---
# Drug-Induced Liver Injury: Hepatocellular vs. Cholestatic Patterns and Mechanisms

## Core Idea
DILI occurs through direct toxicity (acetaminophen, statins) or idiosyncratic reactions (antibiotics, NSAIDs). Hepatocellular injury produces ALT elevation; cholestatic patterns involve bile duct obstruction or hepatic transport dysfunction. Immune-mediated mechanisms cause hypersensitivity reactions.

## Questions

```yaml
- question: "A patient overdoses on acetaminophen and develops acute liver injury. N-acetylcysteine (NAC) is administered as an antidote. Why does NAC work?"
  type: multiple-choice
  options:
    - "It blocks CYP2E1 enzyme activity, preventing further NAPQI formation from residual acetaminophen"
    - "It directly binds and neutralizes NAPQI in the bloodstream before it can reach hepatocytes"
    - "It replenishes glutathione, restoring the cellular defense that the overdose overwhelmed"
    - "It shifts drug metabolism away from hepatic CYP450 pathways to renal excretion"
  answer: 2
  explanation: "Acetaminophen is converted by CYP2E1 to NAPQI, a reactive metabolite. At therapeutic doses, glutathione neutralizes NAPQI efficiently. In overdose, glutathione is exhausted, NAPQI accumulates, and it attacks cellular proteins and mitochondria—causing centrilobular hepatocyte death. NAC works by replenishing glutathione (or serving as a glutathione precursor), restoring the defense mechanism the overdose depleted. It does not block CYP2E1 or directly bind NAPQI in vivo at clinically relevant concentrations."

- question: "A patient develops jaundice and elevated liver enzymes after 3 weeks on a standard therapeutic dose of amoxicillin-clavulanate, with no prior liver symptoms. This pattern is MOST consistent with:"
  type: multiple-choice
  options:
    - "Dose-dependent intrinsic DILI—the drug has accumulated to toxic levels over 3 weeks of treatment"
    - "Idiosyncratic DILI—an immune-mediated reaction that can occur after a variable latency period even at therapeutic doses"
    - "Coincidental alcoholic hepatitis that happened to occur during the antibiotic course"
    - "Direct CYP450 inhibition by the drug causing predictable hepatotoxicity at standard doses"
  answer: 1
  explanation: "Idiosyncratic DILI is the hallmark pattern here: it occurs in rare individuals at normal therapeutic doses, cannot be predicted from dose alone, and often has a variable latency period of days to weeks. Amoxicillin-clavulanate is one of the most common culprits. The mechanism involves the drug or its metabolite acting as a hapten, triggering immune recognition of modified liver proteins. Intrinsic (dose-dependent) DILI—like acetaminophen—occurs predictably at supratherapeutic doses, not after weeks at normal doses."

- question: "A patient who experienced idiosyncratic DILI from a drug is likely to have a faster onset and more severe reaction if re-exposed to the same drug."
  type: true-false
  answer: true
  explanation: "True. Idiosyncratic DILI typically involves an immune-mediated mechanism: the drug or its metabolite acts as a hapten, triggering an adaptive immune response against drug-modified liver proteins. After the initial sensitization, immunologic memory is established. Re-exposure activates this memory response more rapidly and potently than the initial reaction—shorter latency, greater severity. This is the same mechanism underlying drug hypersensitivity reactions in other organ systems."

- question: "A drug that causes cholestatic liver injury (elevated alkaline phosphatase and bilirubin, modest aminotransferase rise) carries the same risk of acute liver failure as a drug causing pure hepatocellular injury with equivalent bilirubin elevation."
  type: true-false
  answer: false
  explanation: "False. The pattern of injury predicts prognosis. Pure hepatocellular patterns—where hepatocytes themselves are dying and cytoplasmic enzymes (ALT, AST) leak dramatically—carry substantially greater risk of progressing to acute liver failure. Cholestatic patterns, where bile flow is impaired but hepatocyte death is limited, tend to be more self-limiting, though resolution can take months. The hepatocellular-versus-cholestatic distinction is therefore not just diagnostic but prognostically important."

- question: "Explain why idiosyncratic DILI is harder to predict and prevent than intrinsic (dose-dependent) DILI."
  type: short-answer
  answer: "Intrinsic DILI is dose-dependent: anyone who takes enough of the drug will develop injury, so it can be predicted from dose and detected in pre-clinical testing. Idiosyncratic DILI requires two conditions aligned in a rare individual—a metabolite that acts as a hapten plus an immune system primed to respond—making it unpredictable from dose, timing, or standard toxicological screening. Pre-clinical testing in animals does not reliably identify idiosyncratic reactions because the specific immune response depends on individual variation in metabolism and immune genetics."
  explanation: "The dose-dependence of intrinsic DILI makes it visible in animal toxicity studies and in dose-escalation trials—the injury signal is detectable before a drug reaches the market. Idiosyncratic DILI, by contrast, may affect only 1 in 10,000 patients and appears only in post-marketing surveillance once the drug is widely used. The hapten mechanism also means the reaction is not inherent to the drug's pharmacology but to how a specific individual's metabolism and immune system interact with it, making prospective prevention nearly impossible without genetic screening for susceptibility variants."
```

## Explainer

Your foundation in hepatocellular injury mechanisms gave you the basic toolkit: mitochondrial dysfunction, oxidative stress, and programmed cell death pathways. Your background in cytochrome P450 metabolism adds the critical pharmacological layer — drugs are not usually toxic in their parent form, but their CYP450-generated metabolites often are. Drug-induced liver injury (DILI) is where these two frameworks converge.

The clearest conceptual divide in DILI is between **intrinsic (predictable)** and **idiosyncratic (unpredictable)** injury. Intrinsic DILI is dose-dependent: anyone who takes enough acetaminophen will develop liver injury. The mechanism is CYP2E1-mediated conversion of acetaminophen to NAPQI (N-acetyl-p-benzoquinone imine), a reactive electrophile that depletes glutathione and then attacks cellular proteins and mitochondria. At therapeutic doses, glutathione neutralizes NAPQI efficiently. At overdose, glutathione is exhausted, NAPQI accumulates, and hepatocyte death follows in the centrilobular zone where CYP2E1 expression is highest. This is why N-acetylcysteine (a glutathione precursor) is the antidote — it replenishes the defense that the overdose overwhelmed.

Idiosyncratic DILI is more treacherous because it affects only rare individuals at normal therapeutic doses and cannot be predicted from dose alone. Mechanistically, idiosyncratic DILI typically involves two hits: the drug or its metabolite acts as a **hapten**, binding to liver proteins and triggering immune recognition, while simultaneously causing enough cell stress to activate danger signals that lower the threshold for immune attack. The immune system mounts a response against drug-modified liver proteins as if they were foreign. This explains why idiosyncratic reactions often occur with re-exposure at lower latency and greater severity — immunologic memory has been established. Amoxicillin-clavulanate is one of the most common culprits.

The **hepatocellular versus cholestatic** distinction reflects which liver function is primarily disrupted. Hepatocellular injury (elevated ALT, AST) means the hepatocytes themselves are dying — their cytoplasmic enzymes leak into blood. Cholestatic injury (elevated alkaline phosphatase and bilirubin, but modest aminotransferase rise) means bile is not flowing normally: either the bile ducts are damaged or the hepatic transporters that excrete bile into the canaliculi are impaired. Some drugs produce **mixed** patterns. Identifying the pattern matters clinically because it guides prognosis — pure hepatocellular patterns with high aminotransferase elevations carry greater risk of acute liver failure than cholestatic patterns, which tend to be self-limiting even if resolution takes months.
