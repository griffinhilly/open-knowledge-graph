---
id: framing-effects
title: Framing Effects
domain: economics
course: behavioral-economics
prerequisites:
- id: prospect-theory
  type: hard
- id: loss-aversion
  type: soft
tags:
- framing
- reference-dependence
- Asian-disease-problem
- presentation-effects
stage: advanced
status: validated
---

# Framing Effects

## Core Idea
Framing effects occur when logically equivalent descriptions of the same decision problem lead to systematically different choices depending on whether the outcomes are presented as gains or losses. The classic demonstration is Tversky and Kahneman's Asian disease problem: when outcomes are framed as lives saved (gain frame), people prefer the certain option; when the same outcomes are framed as lives lost (loss frame), people prefer the risky option. Framing effects violate the invariance axiom of rational choice — that preferences should not change based on how options are described. They arise from prospect theory's reference-dependence and the different risk attitudes in the gain and loss domains, and they have profound implications for medical decisions, policy communication, and marketing.

## Questions

```yaml
- question: "In the Asian disease problem, 72% of subjects chose the certain option ('200 people will be saved') in the gain frame, while 78% chose the risky option in the loss frame ('400 people will die' with 1/3 probability of no deaths). This reversal occurs because..."
  type: multiple-choice
  options:
    - "People cannot do the math to see that the options are equivalent"
    - "The gain frame activates risk aversion (concave value function for gains) while the loss frame activates risk seeking (convex value function for losses)"
    - "People always prefer certain outcomes regardless of framing"
    - "The loss frame triggers anger, which causes random responding"
  answer: 1
  explanation: "Prospect theory predicts this pattern directly. In the gain domain, the value function is concave, producing risk aversion — people prefer the certain gain of saving 200 lives over the gamble. In the loss domain, the value function is convex, producing risk seeking — people prefer to gamble rather than accept the certain loss of 400 lives. The frame determines the reference point (all saved vs. all dead), which determines whether the outcomes are coded as gains or losses, which determines risk attitudes. The options are objectively identical; only the psychological coding differs."

- question: "Framing effects are irrational errors that can always be eliminated through education or deliberation."
  type: true-false
  answer: false
  explanation: "While awareness of framing effects can reduce their impact in some cases, they are remarkably robust. They persist among experts (physicians, statisticians), under high stakes, and even when subjects are shown both frames simultaneously. This persistence suggests that framing effects reflect a fundamental feature of human cognition — evaluation relative to reference points — rather than a correctable error. Education can make people more cautious about frame-dependent judgments, but it cannot eliminate the underlying reference-dependent evaluation process."

- question: "What does the existence of framing effects imply about the concept of 'revealed preferences' in economics?"
  type: short-answer
  answer: "Revealed preference theory assumes that choices reveal stable underlying preferences — if you choose A over B, you prefer A. Framing effects undermine this assumption because the same person can choose A over B in one frame and B over A in another, even when A and B are objectively identical options. This means choices do not reliably reveal a single, stable preference ordering — they reveal preferences that are partly constructed by the decision context, including how options are described."
  explanation: "This is a deep challenge for welfare economics and policy analysis. If preferences are frame-dependent, which frame reveals the 'true' preference? There may be no frame-independent preference to discover. Some behavioral economists argue that this means we need new normative criteria — perhaps based on what people would choose after reflective deliberation — rather than simply accepting choices at face value. Others argue that it means we must be very careful about the frames in which choices are presented, because the presentation is not neutral."
```

## Explainer

Framing effects demonstrate one of the most fundamental challenges to the standard model of rational choice: the way a problem is described should not affect the decision if preferences are stable and well-defined, but it consistently does. This is not a curiosity of the laboratory — it plays out in medical consultations, policy debates, financial decisions, and everyday consumer choices whenever the same information can be presented in gain or loss terms.

The Asian disease problem remains the paradigmatic demonstration. Subjects are told that 600 people will die from a disease and must choose between two programs. In the gain frame, Program A saves 200 people for certain, while Program B offers a 1/3 chance of saving all 600 and a 2/3 chance of saving no one. In the loss frame, Program A results in 400 deaths for certain, while Program B offers a 1/3 chance of zero deaths and a 2/3 chance of 600 deaths. The programs are objectively identical across frames, but the gain frame produces majority preference for the certain option (risk aversion) while the loss frame produces majority preference for the risky option (risk seeking).

Prospect theory explains this cleanly. The frame determines the reference point, which determines whether outcomes are coded as gains or losses. In the gain frame, saving 200 out of 600 is a gain relative to the implicit reference of "all die," and the concave value function for gains produces risk aversion. In the loss frame, 400 dying is a loss relative to the implicit reference of "all survive," and the convex value function for losses produces risk seeking. The frame does not change the objective options — it changes the psychological coding of those options, which changes the part of the value function that is applied.

The practical consequences are substantial. In medicine, whether a surgery is described as having a "90% survival rate" versus a "10% mortality rate" significantly affects patient and physician preferences — even though the information is identical. In consumer behavior, a product described as "95% fat-free" is more attractive than one described as "5% fat." In energy policy, framing conservation as avoiding a loss ($350/year wasted on energy inefficiency) is more motivating than framing it as achieving a gain ($350/year saved through efficiency). In each case, the frame is not additional information — it is a description choice that activates different psychological evaluation processes.

Framing effects raise fundamental questions about autonomy and paternalism. If choices depend on how options are presented, and if some entity (a doctor, a marketer, a policymaker) must choose a frame, then the choice of frame is an exercise of influence — whether intentional or not. Thaler and Sunstein's concept of "choice architecture" builds on this insight: since every presentation of options involves a frame, the question is not whether to influence choices but how to do so responsibly. This connects framing effects to the broader nudge agenda in behavioral public policy.
