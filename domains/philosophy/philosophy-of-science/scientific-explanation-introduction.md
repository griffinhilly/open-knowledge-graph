---
id: scientific-explanation-introduction
title: 'Scientific Explanation: Core Problems'
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: causation-and-causal-relations
  type: hard
- id: deductive-reasoning
  type: soft
- id: logical-consequence-and-entailment
  type: soft
builds-toward:
- deductive-nomological-explanation
- causal-explanation-theories
tags:
- explanation
- causation
- understanding
stage: advanced
status: validated
---

# Scientific Explanation: Core Problems

## Core Idea
Scientific explanation differs from mere prediction: explaining why an event occurred appeals to underlying causes, principles, or laws, not just recognizing patterns in data. Understanding what constitutes a genuine scientific explanation—and whether all explanations share a common structure—is a central concern of philosophy of science.

## Questions

```yaml
- question: "A doctor knows that barometric pressure reliably drops before her patient's migraines. She tells the patient: 'Your migraine occurred because the barometer fell.' Is this a scientific explanation?"
  type: multiple-choice
  options:
    - "Yes — a reliable statistical correlation between two events is sufficient for scientific explanation"
    - "Yes — because the barometer allows prediction of the migraine, it provides a full explanation of it"
    - "No — the doctor needs to cite a law of nature explicitly; correlation without a stated law is not explanatory"
    - "No — the barometer reading is a correlate of the atmospheric change, not the cause; a genuine explanation would cite the actual causal process linking atmospheric pressure to neural events"
  answer: 3
  explanation: "The barometer falls because atmospheric pressure drops — the same change that (by some causal pathway) triggers the migraine. The barometer reading and the migraine share a common cause; neither causes the other. Citing the barometer 'explains' the migraine no more than citing the migraine could explain the barometer falling. This is the core insight: explanation requires the right kind of connection — causal or structural — to what produced the event, not merely a reliable pattern. Prediction can succeed on correlation alone; explanation cannot."

- question: "By the deductive-nomological (DN) model, a valid explanation must deduce the explanandum from laws of nature plus initial conditions. What is the 'asymmetry problem' that challenges this model?"
  type: multiple-choice
  options:
    - "The DN model applies only to deterministic laws, making it unable to handle probabilistic explanations in quantum mechanics or biology"
    - "The DN model requires too many initial conditions, making it practically impossible to apply to complex real-world events"
    - "The DN model licenses explanations in both causal directions — shadow length could 'explain' flagpole height just as validly as flagpole height explains shadow length"
    - "The DN model conflates explanation with description, since both involve citing facts about the world"
  answer: 2
  explanation: "The flagpole/shadow case illustrates the asymmetry problem precisely. The flagpole's height + sun angle entail the shadow length (a genuine explanation). But the shadow length + sun angle also mathematically entail the flagpole height — a valid DN 'explanation' that feels explanatorily backwards. We know the flagpole causes the shadow, not vice versa, but the DN model has no way to encode this asymmetry because it is purely logical. The explanatory direction is determined by causation, not by deductive validity — which is why causal theories of explanation were developed in response."

- question: "According to the DN model, predicting an event before it occurs and explaining it after it occurs require different logical structures."
  type: true-false
  answer: false
  explanation: "The DN model explicitly holds that prediction and explanation have the same logical structure. Both involve deriving a statement about an event from laws of nature plus initial conditions. The only difference is temporal: in prediction, you derive the event's occurrence before it happens; in explanation, you derive it after. Hempel called this 'the structural identity thesis.' Critics argued this was counterintuitive — it implies that any successful prediction is, in principle, also an explanation — but it follows directly from the DN model's purely logical account of explanation."

- question: "The asymmetry problem for the DN model shows that logical deducibility alone is insufficient to distinguish genuine explanations from explanatorily irrelevant or backwards derivations."
  type: true-false
  answer: true
  explanation: "This is precisely the lesson of the flagpole example and related cases (like explaining a person's height from their shadow, or explaining why a patient took aspirin by deriving it from a law that aspirin relieves headaches plus the fact that the patient had a headache — but their taking aspirin explained the headache disappearing, not vice versa). Valid logical entailment from laws and conditions is necessary but not sufficient for explanation. What's missing is directional constraint — causal, mechanistic, or otherwise — that the purely formal DN model cannot supply."

- question: "What is the difference between predicting that an event will occur and explaining why it occurred? Use a concrete example to show why successful prediction does not guarantee genuine explanation."
  type: short-answer
  answer: "Prediction requires only a reliable correlation or pattern: knowing the barometer falls before storms lets you predict rain without knowing why. Explanation requires identifying what actually produced the event — typically its cause, mechanism, or the law-governed structure responsible for it. A barometer predicts rain but does not explain it; atmospheric physics (low pressure systems causing moisture to condense) explains rain. Similarly, knowing a patient's age and risk factors may let a doctor predict a heart attack, but the explanation requires understanding the causal pathways of cardiovascular disease."
  explanation: "This distinction is central to philosophy of science. Science aims at both prediction and explanation, but they are not the same achievement. A purely predictive science — even one with perfect accuracy — would leave us without understanding of why the world works as it does. The puzzle the DN model was trying to solve is that explanation seems to involve more than correlation, and more than prediction: it tracks something about the underlying structure of reality — causes, mechanisms, or deep laws — that prediction does not require."
```

## Explainer

You already know from your prerequisite on causation that there is a difference between correlation and causation, between prediction and explanation. Saying "the barometer falls before storms" lets you predict rain; it does not explain why it rains. Explanation demands more — it demands the right kind of connection to what actually produced the event. The question this topic asks is: what *kind* of connection is that, exactly?

The most influential answer was Hempel and Oppenheim's **deductive-nomological (DN) model**, proposed in 1948. On this view, to explain an event is to show that it *had to happen*, given the laws of nature and the initial conditions. You **deduce** the explanandum (what's to be explained) from the **explananda** — a set of premises that include at least one **law of nature** and statements of initial conditions. Why did the metal rod expand? Because: (1) all metals expand when heated (a law), (2) this rod is metal and was heated (initial conditions), therefore (3) this rod expanded. The explanation is a valid deductive argument from lawful generalizations. The DN model honors your prerequisite on deductive reasoning: explanation and prediction have the same logical structure — the only difference is temporal, whether you derive the event before or after it occurs.

But the DN model faces sharp counterexamples that reveal something important. Consider this "explanation": the length of a flagpole and the angle of the sun *logically entail* the length of its shadow. The same facts, taken in reverse, also entail the height of the flagpole from the shadow length. By DN standards, both are valid explanations. But we feel that the shadow doesn't explain the flagpole height — the flagpole height (together with the sun angle) *causes* the shadow length, not the reverse. This is the **asymmetry problem**: the DN model cannot distinguish explanatorily relevant from irrelevant factors.

The asymmetry problem points toward **causal theories of explanation** — the idea that genuine explanation must track genuine causal structure. To explain why the flagpole casts a 15-meter shadow, you describe the causal process from the sun illuminating the flagpole to the shadow being cast. But causation faces its own philosophical difficulties (as your prerequisite established), which is why philosophers of science continue to debate whether causal, mechanistic, unificationist, or pragmatic accounts best capture what scientific explanation achieves. The upshot is practical: scientists don't just seek true predictions; they seek accounts of *why* — accounts that reveal the mechanisms, causes, or deep structure that generate the phenomena. What exactly that requires is this topic's central question.
