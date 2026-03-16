---
id: causal-explanation-science
title: Causal Explanation
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: counterfactual-causation
  type: hard
- id: deductive-nomological-explanation
  type: soft
builds-toward:
- unification-model-explanation
- natural-kinds-classification
tags:
- causation
- explanation
- causal-mechanism
- intervention
stage: advanced
status: draft
---

# Causal Explanation

## Core Idea
While the covering law model emphasizes universal laws, causal explanations emphasize mechanisms and causal processes. To explain why a match ignited is to cite the cause (striking it) and mechanism (heat + oxygen). This approach respects our intuition that explanation requires causal relevance, not mere correlation. Modern causal explanation employs counterfactual conditionals: A causes B if, had A not occurred, B would not have occurred. This framework accommodates actual causes (singular events) rather than only universal laws.

## Explainer

The deductive-nomological model promised a clean account of explanation: to explain an event is to show it was nomologically inevitable given prior conditions and universal laws. This captures something real — laws genuinely explain. But it has a notorious blind spot: it cannot distinguish genuinely explanatory laws from mere accidental correlations. A barometer reading correlates perfectly with an impending storm, and you can construct a DN argument deriving "storm will occur" from the barometer reading plus the relevant physical laws. Yet intuitively, the barometer doesn't explain the storm — it merely tracks the same atmospheric conditions. What the DN model misses is **causal relevance**: the cause must actually produce the effect through a real mechanism, not merely co-vary with it.

Causal explanation fills this gap by requiring that an explanation trace the actual mechanism linking cause to effect. To explain why the match lit: friction generated heat at the match head, heat raised the local temperature above the combustion threshold of the phosphorus compounds, and combustion occurred in the presence of atmospheric oxygen. Each step tracks a real physical process. The barometer reading, by contrast, doesn't produce the storm through any mechanism — the causal arrow runs from atmospheric pressure change to both the barometer reading and the storm, making the barometer causally inert with respect to the storm.

Your prerequisite on **counterfactual causation** provides the formal tool: A causes B if, had A not occurred, B would not have occurred. This counterfactual test elegantly handles the barometer case. Had the barometer not dropped, the storm would still have come — atmospheric pressure was already low, and that's what drives storms. Counterfactual dependence fails, confirming that the barometer drop isn't a cause. For the match: had it not been struck, it would not have lit (under normal conditions). Counterfactual dependence holds, confirming the striking as a cause. The framework applies to singular events — this particular match on this particular occasion — not only to general patterns.

The main challenge for counterfactual causal explanation is handling complex causal structures. **Preemptive causation**: you push a rock toward a window; I simultaneously throw a rock that gets there first and breaks it. Had your rock not been thrown, mine would have broken the window anyway — yet we want to say my throw caused the break. The simple counterfactual test fails here. **Overdetermination**: two independently sufficient causes both operate (two assassins simultaneously shoot the target). Neither is necessary, since the other would have sufficed alone. These cases force refinements — INUS conditions (insufficient but necessary parts of unnecessary but sufficient conditions), causal models using directed graphs, or probabilistic causation — but the core insight stands: genuine explanation requires identifying a causal mechanism, not merely citing a correlated factor.
