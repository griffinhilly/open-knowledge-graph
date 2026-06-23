---
id: causal-explanation-science
title: "Causal Explanation"
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: counterfactual-causation
  type: hard
- id: deductive-nomological-explanation
  type: soft
- id: covering-law-model-explanation
  type: soft
- id: scientific-explanation-introduction
  type: soft
builds-toward:
- unification-model-explanation
- natural-kinds-classification
tags:
- causation
- explanation
- causal-mechanism
- intervention
stage: expert
status: validated
---

# Causal Explanation

## Core Idea
While the covering law model emphasizes universal laws, causal explanations emphasize mechanisms and causal processes. To explain why a match ignited is to cite the cause (striking it) and mechanism (heat + oxygen). This approach respects our intuition that explanation requires causal relevance, not mere correlation. Modern causal explanation employs counterfactual conditionals: A causes B if, had A not occurred, B would not have occurred. This framework accommodates actual causes (singular events) rather than only universal laws.

## Questions

```yaml
- question: "A barometer drops; a storm follows. We can derive 'storm will occur' from the barometer reading plus physical laws. Why does citing the barometer NOT constitute a causal explanation of the storm?"
  type: multiple-choice
  options:
    - "Because the derivation uses inductive rather than deductive logic, which is insufficient for scientific explanation"
    - "Because the barometer reading does not produce the storm through any mechanism — both are effects of the same atmospheric pressure change, making the barometer causally inert with respect to the storm"
    - "Because the laws connecting barometers to storms are not universal enough to support explanation"
    - "Because explanation requires knowing the storm's precise location and timing, which the barometer cannot provide"
  answer: 1
  explanation: "This is the canonical case showing that the covering-law (D-N) model is insufficient. We can derive the storm from the barometer reading plus the correct physical laws — the D-N conditions are satisfied — yet no one thinks the barometer explains the storm. What's missing is causal relevance: the causal arrow runs from low atmospheric pressure to both the barometer reading and the storm. The barometer doesn't produce the storm; they are parallel effects of the same common cause. Genuine explanation requires tracing the real mechanism."

- question: "Two assassins simultaneously fire lethal shots at a target. The target dies. Had Assassin A not fired, Assassin B's shot would have killed the target; had Assassin B not fired, A's would have. Under simple counterfactual causation, neither assassin caused the death. What does this illustrate?"
  type: multiple-choice
  options:
    - "Counterfactual causation correctly shows that joint actions cannot have singular causes"
    - "Overdetermination cases show that simple counterfactual dependence fails: both shots were causes, yet neither passes the 'had it not occurred' test — more refined accounts are needed"
    - "The counterfactual test works here: since both fired, the correct analysis is that each caused 50% of the death"
    - "This shows that causal explanation cannot handle intentional human action and only applies to physical events"
  answer: 1
  explanation: "Overdetermination is a genuine challenge for counterfactual accounts: when two independently sufficient causes both operate, neither is necessary (removing either leaves the other to produce the effect), so counterfactual dependence fails for both — yet intuitively both are causes. Resolutions include INUS conditions (each is an insufficient but necessary part of an unnecessary but sufficient condition), causal graph models (using actual vs. counterfactual causation), or probabilistic causation. These refinements preserve the core insight — explanation requires real causal mechanism — while handling complex causal structures."

- question: "The counterfactual account of causation — 'A caused B' means 'had A not occurred, B would not have occurred' — is sensitive to whether the causal mechanism was actually operative, unlike mere correlation."
  type: true-false
  answer: true
  explanation: "This is the central advantage of the counterfactual approach over pure correlation. The barometer correlates perfectly with the storm, but the counterfactual test reveals the asymmetry: had the barometer not dropped, the storm would still have come (because atmospheric pressure was already low). The counterfactual test correctly identifies that the barometer has no causal purchase on the storm. For the match: had it not been struck, it would not have lit — the counterfactual holds, confirming the striking as a genuine cause."

- question: "The deductive-nomological (covering-law) model is a complete account of scientific explanation because any successful derivation of a phenomenon from universal laws and initial conditions constitutes a genuine causal explanation."
  type: true-false
  answer: false
  explanation: "The barometer case directly refutes this: we can derive 'storm will occur' from the barometer reading plus physical laws via a valid deductive argument, but this is not a causal explanation of the storm — the barometer is causally inert with respect to the storm. The D-N model cannot distinguish genuinely explanatory laws from accidental correlations that happen to track the same underlying cause. This is the 'irrelevance' problem: D-N allows derivations using causally irrelevant factors that intuitively do not explain."

- question: "Why does citing a factor that merely correlates with an effect fail to constitute a causal explanation? Use either the barometer or the match example to illustrate the difference between correlation and causal mechanism."
  type: short-answer
  answer: "Causal explanation requires that the cited factor actually produces the effect through a real mechanism — a physical process connecting cause to effect. The barometer correlates perfectly with the storm but doesn't produce it; both are effects of low atmospheric pressure. Tracing the mechanism for the match — friction → heat → combustion temperature exceeded → chemical reaction with oxygen — shows each step as a real physical process. A correlation that tracks the same cause without being part of the causal chain from cause to effect is explanatorily empty."
  explanation: "The deeper point is about causal relevance: a genuine explanation must identify factors that would change the outcome if they were changed, and do so because they are part of the mechanism — not merely because they co-vary with something in the mechanism. This is why randomized controlled trials are the gold standard in science: they establish counterfactual dependence by intervening on the putative cause, ruling out common-cause explanations. The philosophical account of causal explanation directly motivates the methodology of experimental science."
```

## Explainer

The deductive-nomological model promised a clean account of explanation: to explain an event is to show it was nomologically inevitable given prior conditions and universal laws. This captures something real — laws genuinely explain. But it has a notorious blind spot: it cannot distinguish genuinely explanatory laws from mere accidental correlations. A barometer reading correlates perfectly with an impending storm, and you can construct a DN argument deriving "storm will occur" from the barometer reading plus the relevant physical laws. Yet intuitively, the barometer doesn't explain the storm — it merely tracks the same atmospheric conditions. What the DN model misses is **causal relevance**: the cause must actually produce the effect through a real mechanism, not merely co-vary with it.

Causal explanation fills this gap by requiring that an explanation trace the actual mechanism linking cause to effect. To explain why the match lit: friction generated heat at the match head, heat raised the local temperature above the combustion threshold of the phosphorus compounds, and combustion occurred in the presence of atmospheric oxygen. Each step tracks a real physical process. The barometer reading, by contrast, doesn't produce the storm through any mechanism — the causal arrow runs from atmospheric pressure change to both the barometer reading and the storm, making the barometer causally inert with respect to the storm.

Your prerequisite on **counterfactual causation** provides the formal tool: A causes B if, had A not occurred, B would not have occurred. This counterfactual test elegantly handles the barometer case. Had the barometer not dropped, the storm would still have come — atmospheric pressure was already low, and that's what drives storms. Counterfactual dependence fails, confirming that the barometer drop isn't a cause. For the match: had it not been struck, it would not have lit (under normal conditions). Counterfactual dependence holds, confirming the striking as a cause. The framework applies to singular events — this particular match on this particular occasion — not only to general patterns.

The main challenge for counterfactual causal explanation is handling complex causal structures. **Preemptive causation**: you push a rock toward a window; I simultaneously throw a rock that gets there first and breaks it. Had your rock not been thrown, mine would have broken the window anyway — yet we want to say my throw caused the break. The simple counterfactual test fails here. **Overdetermination**: two independently sufficient causes both operate (two assassins simultaneously shoot the target). Neither is necessary, since the other would have sufficed alone. These cases force refinements — INUS conditions (insufficient but necessary parts of unnecessary but sufficient conditions), causal models using directed graphs, or probabilistic causation — but the core insight stands: genuine explanation requires identifying a causal mechanism, not merely citing a correlated factor.
