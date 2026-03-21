---
id: trolley-problem
title: The Trolley Problem and Doing/Allowing
domain: philosophy
course: ethics
prerequisites:
- id: consequentialism
  type: hard
- id: deontological-ethics
  type: hard
- id: thought-experiments
  type: soft
- id: utilitarianism
  type: soft
builds-toward:
- applied-ethics-intro
- bioethics
tags:
- trolley-problem
- doing-allowing
- doctrine-of-double-effect
- moral-intuition
stage: formal-systems
status: validated
---
# The Trolley Problem and Doing/Allowing

## Core Idea
Philippa Foot's trolley problem and Judith Jarvis Thomson's variations are canonical thought experiments probing the moral significance of doing versus allowing harm, and of using someone as a means versus a side effect. In the standard case, diverting a runaway trolley from five people to one seems permissible; in the footbridge case, pushing a large man off a bridge to stop the trolley seems impermissible—though both save five by killing one. The cases are used to examine the doctrine of double effect (DDE), which permits acting with a bad foreseen but unintended side effect when other conditions are met. They reveal how moral intuitions can conflict with consequentialist arithmetic and motivate deontological side-constraints.

## How It's Best Learned
Work through several variants systematically: switch case, footbridge case, loop track, transplant surgeon. In each, identify what the consequentialist and deontologist each say, and check whether the DDE applies.

## Common Misconceptions
- The point of the trolley problem is not to resolve whether to pull the lever; it is to test moral theories against intuitions and identify the morally relevant distinctions.
- The doctrine of double effect does not simply permit any harm as a 'side effect'; it has four demanding conditions including proportionality.

## Questions

```yaml
- question: "In the footbridge case, is the large man's death best described as a 'foreseen side effect' of stopping the trolley?"
  type: multiple-choice
  options:
    - "Yes — you foresee his death just as you foresee the death of the one person in the switch case"
    - "No — his body is the mechanism that stops the trolley, making his death a means, not a side effect"
    - "Yes — intention never matters morally, only the foreseen consequences"
    - "No — because physically pushing someone is always intrinsically impermissible"
  answer: 1
  explanation: "This is the key distinction the doctrine of double effect (DDE) draws between the cases. In the switch case, the one person's death is a foreseen but genuinely incidental effect — the trolley would have endangered that track regardless. In the footbridge case, the man's body is the causal mechanism that stops the trolley: without his mass, nothing is achieved. He is used as a means, not merely harmed as a side effect. The DDE permits the side effect but forbids using a person as a means, which is why the cases receive different verdicts despite identical arithmetic."

- question: "What is the primary philosophical purpose of the trolley problem?"
  type: multiple-choice
  options:
    - "To demonstrate that consequentialism is the correct moral theory, since saving five outweighs saving one"
    - "To show that deontological ethics always requires inaction in crisis situations"
    - "To use diverging intuitions about structurally similar cases to reveal and examine implicit moral distinctions"
    - "To establish that the number of lives saved is always the decisive moral factor"
  answer: 2
  explanation: "The trolley problem is not designed to answer 'what should you do?' — it is designed to test moral theories against intuitions and expose the morally relevant distinctions embedded in those intuitions. The fact that most people judge switching permissible but pushing impermissible, despite identical outcomes, reveals that people implicitly hold distinctions like doing/allowing and means/side effect. The cases are a testing machine for those distinctions, not a policy recommendation."

- question: "A deontologist applying the doctrine of double effect can consistently permit diverting the trolley in the switch case, because the death of the one person is a foreseen but unintended side effect."
  type: true-false
  answer: true
  explanation: "The DDE has four conditions: the action is not intrinsically wrong, the agent intends only the good effect, the bad effect is a foreseen but unintended side effect, and there is proportionate reason. In the switch case, all four are plausibly satisfied: redirecting a trolley is not intrinsically wrong, the agent intends to save five, the one death is incidental (the track was already there), and saving five provides proportionate reason. This is precisely why the switch case is widely judged permissible even by deontologists."

- question: "Because the switch and footbridge cases both involve saving five lives at the cost of one, any moral theory that gives different verdicts for the two cases is internally inconsistent."
  type: true-false
  answer: false
  explanation: "The consequentialist arithmetic is identical, but the cases differ morally in ways that non-consequentialist theories treat as significant: doing vs. allowing, initiating a new causal chain vs. redirecting an existing one, using a person as a means vs. allowing a side effect. A theory that draws on these distinctions can consistently permit the switch case and forbid the footbridge case. The whole point of studying the trolley variants is to discover which distinctions, if any, can bear the weight of explaining our divergent intuitions."

- question: "Explain why pushing the man in the footbridge case feels like murder in a way that pulling the switch does not."
  type: short-answer
  answer: "In the switch case, you redirect an existing threat — the causal chain originated with the runaway trolley, and you merely alter its course. In the footbridge case, you initiate a new causal chain using another person's body as the instrument. The man's death is not a byproduct of stopping the trolley; it is how you stop it. Deontologists argue that treating a person as a tool for others' benefit — using them as a means — violates their status as an end in themselves, which is what makes pushing feel like murder rather than a tragic redirection."
  explanation: "This connects the doing/allowing distinction to the means/side effect distinction. Switching diverts; pushing uses. The asymmetry explains why identical outcomes can have different moral statuses: what matters is not just what results from your action but the nature of the causal role the harmed person plays in your plan. This is the insight that motivates deontological side-constraints and that pure consequentialism — by attending only to outcomes — cannot capture."
```

## Explainer

From your prerequisites, you know that consequentialism evaluates actions by their outcomes and deontology evaluates them by the nature of the action itself. The trolley problem is a testing machine for exactly this conflict: it constructs situations where consequentialist arithmetic points clearly in one direction while deontological intuitions resist. The philosophical point is not to tell you whether to pull the lever—it is to use your reaction to the cases to reveal the implicit moral distinctions you already hold.

In the **switch case** (Foot's original): a runaway trolley will kill five people unless you pull a lever diverting it to a side track where it will kill one. Most people judge diverting permissible. In the **footbridge case** (Thomson's variation): the only way to stop the trolley from killing five is to push a large man off a bridge into its path, killing him. Most people judge pushing impermissible. The consequentialist arithmetic is identical—five lives saved at the cost of one. Yet the intuitions diverge sharply. Something morally significant is different between the cases, and the task is to identify what.

The **doctrine of double effect (DDE)** is the traditional framework for distinguishing the cases. It holds that an action with a harmful effect is permissible when: (1) the action itself is not intrinsically wrong; (2) the agent intends only the good effect, not the bad one; (3) the bad effect is a foreseen but unintended side effect; and (4) there is proportionate reason for allowing the bad effect. In the switch case, the death of the one person is a foreseen side effect—the trolley would have endangered that track regardless. In the footbridge case, the man's death is the mechanism by which harm is prevented—his body is used as a means to stop the trolley. The DDE permits the side effect but forbids using someone as a means.

The **doing/allowing distinction** reinforces this asymmetry. In the switch case, you redirect an existing threat—the causal chain originated elsewhere and you merely alter its course. In the footbridge case, you initiate a new causal chain using another person's body. Deontologists argue that using someone as a means—treating them as an instrument for others' benefit—violates their status as a person with rights. This captures why pushing feels like murder in a way that switching does not. Consequentialism, which evaluates only outcomes, cannot explain the moral asymmetry between the cases; its inability to do so is precisely what motivates deontological side-constraints against treating persons merely as means.
