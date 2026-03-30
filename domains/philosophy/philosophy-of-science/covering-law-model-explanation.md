---
id: covering-law-model-explanation
title: The Covering Law Model
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: deductive-nomological-explanation
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: propositional-logic-introduction
  type: soft
builds-toward:
- causal-explanation-science
- explanatory-power-and-unification
tags:
- covering-law
- inductive-statistical
- explanation
- laws
stage: advanced
status: validated
---

# The Covering Law Model

## Core Idea
The covering law model extends the D-N model to include inductive-statistical explanations where the explanans makes the explanandum probable by subsuming it under statistical laws. This captures explanations in quantum mechanics, genetics, and social science using probabilistic laws rather than strict universals. However, high statistical correlation provides a covering law but intuitively fails to explain: a barometer's rise doesn't explain incoming storms even though both are covered by meteorological laws.

## Questions

```yaml
- question: "Given the height of a flagpole, the angle of the sun, and the law of light propagation, you can validly deduce the length of the pole's shadow. You can also reverse the deduction: given the shadow length and sun's angle, validly deduce the pole's height. According to the covering law model, what should we conclude — and what does this reveal about the model?"
  type: multiple-choice
  options:
    - "Both deductions are valid explanations; the covering law model correctly identifies both as explanatory"
    - "Only the first is an explanation; the second fails because the covering law model requires that laws run in the causal direction"
    - "Both deductions are valid arguments, but the second (shadow explains pole height) is not a genuine explanation — revealing that the covering law model cannot distinguish causal direction"
    - "The second deduction is invalid because the premises don't lawfully imply the pole's height"
  answer: 2
  explanation: "Both deductions are logically valid and satisfy all the covering law model's requirements: they use natural laws, the premises are true, and the conclusion follows deductively. But intuitively only the first is a real explanation — the pole's height explains the shadow's length, not vice versa. The covering law model has no resources to distinguish them because it only requires logical structure, not causal direction. This asymmetry problem shows that something is missing from the model: explanations track causal structure, but the covering law model is blind to causation."

- question: "In the inductive-statistical model, rising barometric pressure raises the probability of an approaching storm. Does the barometer's reading explain the storm? What does this case reveal?"
  type: multiple-choice
  options:
    - "Yes — the I-S model says that any factor that raises the probability of an event explains it"
    - "No — but only because the statistical correlation isn't strong enough to meet the high-probability requirement"
    - "No — the barometer and the storm are both caused by low pressure; the barometer doesn't cause the storm, revealing that correlation under a law is insufficient for explanation"
    - "Yes — in statistical explanation, all that matters is the probability-raising relationship, not the causal mechanism"
  answer: 2
  explanation: "The barometer and the storm share a common cause (low atmospheric pressure); the barometer doesn't cause the storm. Even if the correlation is high enough to satisfy the I-S model's probability requirement, citing the barometer reading does not explain the storm — it merely correlates with it. This is the irrelevance problem: the covering law model cannot rule out explanans that are statistically associated with the explanandum but causally disconnected from it. The missing ingredient is causal structure — not just any lawful probability-raising relationship, but the right kind of causal connection."

- question: "The covering law model requires that the laws cited in an explanation run in the same direction as causation."
  type: true-false
  answer: false
  explanation: "False. This is precisely what the covering law model lacks and what the flagpole-shadow case reveals. The model only requires that the explanation be a valid (or probabilistically strong) argument from laws plus initial conditions. It has no requirement about causal direction. The shadow-to-pole deduction is as logically valid as the pole-to-shadow deduction; the model cannot distinguish them. The absence of any causal-direction requirement is the core inadequacy, motivating causal-mechanical accounts that build directionality explicitly into the analysis of explanation."

- question: "The inductive-statistical model requires that the explanatory premises make the explanandum highly probable — not merely possible."
  type: true-false
  answer: true
  explanation: "True. Hempel's I-S model specifies a high-probability requirement: the statistical law plus initial conditions must make the event to be explained very likely, not merely raise its probability somewhat. This is why a 90% cure rate for penicillin treating strep can explain a patient's recovery, while a 10% survival rate for a disease does not explain a survivor's recovery. The requirement is also what introduces the reference class problem: whether the event has high probability depends on which reference class you use to describe the patient, and there is no principled way to choose without already knowing the answer."

- question: "What does the flagpole-shadow case reveal about the fundamental inadequacy of the covering law model as an account of scientific explanation?"
  type: short-answer
  answer: "The flagpole-shadow case shows that the covering law model permits explanations to run in logically valid but causally backwards directions. You can validly deduce the pole's height from the shadow length and sun angle using the same laws, but that deduction does not explain the pole's height — the height explains the shadow, not vice versa. Since the covering law model only requires a valid deductive argument from laws, it cannot distinguish genuine from spurious explanations when the same laws support both directions. This reveals that explanation requires asymmetric causal structure, which the purely logical framework of the covering law model omits."
  explanation: "This case motivated a major shift in philosophy of science toward causal theories of explanation (Salmon, Woodward) that treat explanation as tracking actual causal mechanisms or counterfactual dependencies, not merely lawful logical entailment. The symmetry problem, along with the barometer irrelevance problem, are the two classic challenges that the covering law model failed to handle — showing that logical form and probabilistic laws, however necessary, are not sufficient for explanation."
```

## Explainer

You already understand the **deductive-nomological (D-N) model**: an explanation is a valid deductive argument whose premises include at least one natural law, and whose conclusion is the phenomenon to be explained. The covering law model is the generalization of that framework. It says that all scientific explanation has a common logical structure: the phenomenon is *covered* — subsumed — by one or more laws, and citing those laws is what makes something an explanation rather than a mere description. The D-N model is the deductive special case; the covering law model also includes the **inductive-statistical (I-S) model**, which handles probabilistic laws.

The I-S extension matters because much real science is irreducibly statistical. In quantum mechanics, a law might say that a radioactive atom has a 50% chance of decaying in a given interval — not that it *will* decay. In epidemiology, smoking raises the probability of lung cancer without guaranteeing it. In Mendelian genetics, a heterozygous parent passes a dominant allele to each offspring with probability 1/2. The I-S model says these probabilistic laws still explain outcomes by raising their probability. The key requirement is **high probability**: the law-plus-conditions must make the event very likely. An explanation of why this patient recovered from strep throat by citing that penicillin cures strep infections in 90% of cases is a genuine explanation precisely because the probability is high — you've been covered by a strong statistical law.

This generates an immediate problem: **the reference class problem**. Whether an event has high probability depends entirely on how you describe it. The same patient might also belong to a subclass — say, patients with a particular allergy — where the recovery rate is much lower. There is no principled way to choose the "right" reference class without already knowing what the explanation should look like. This threatened to make I-S explanations circular or indeterminate, and prompted Hempel to introduce the **requirement of maximal specificity**: use the most specific reference class for which you have relevant information.

The deeper challenge is **the asymmetry and irrelevance problems**. Suppose a law says that the height of a flagpole's shadow correlates perfectly with the pole's height plus the sun's angle. You can deduce the pole's height from the shadow length and the angle — but that doesn't *explain* the pole's height; it's the other way around. The covering law model permits explanations to run in logically valid but causally backward directions. Similarly, the barometer case: rising barometric pressure and approaching storms are both covered by the same meteorological laws, but the barometer's reading does not explain the storm. These cases suggest that explanation requires something the covering law model omits: **asymmetric causal structure**. This failure motivates rival accounts — causal-mechanical explanation and unificationist explanation — which build causation or explanatory power directly into the analysis.
