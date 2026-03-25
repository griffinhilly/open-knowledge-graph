---
id: moral-psychology
title: Moral Psychology
domain: philosophy
course: ethics
prerequisites:
- id: moral-responsibility
  type: soft
- id: virtue-ethics
  type: soft
- id: cognitive-biases-in-reasoning
  type: soft
- id: vices-and-moral-defects
  type: soft
- id: moral-exemplars-and-ideals
  type: soft
tags:
- moral-psychology
- moral-intuition
- dual-process
- emotion
- character
stage: formal-systems
status: validated
---
# Moral Psychology

## Core Idea
Moral psychology investigates the psychological processes underlying moral judgment, motivation, and development. It bridges philosophy and empirical psychology, asking: what are moral intuitions and how reliable are they? How do emotions like empathy and disgust shape moral responses? Are moral character traits stable across contexts (situationism vs. virtue)? Jonathan Haidt's social intuitionist model argues that moral judgments are primarily emotional and automatic, with reasoning post-hoc rationalization. This challenges the rationalist tradition (Kohlberg's stages) and raises normative questions about when we should trust intuitions versus revise them. Joshua Greene's dual-process theory uses trolley-problem data to argue that deontological intuitions stem from emotional responses while consequentialist reasoning is more deliberate.

## How It's Best Learned
Read Haidt's 'The Emotional Dog and its Rational Tail' (Psychological Review, 2001) and Greene's papers on the trolley problem. Then evaluate: do empirical findings about how we reason debunk our moral judgments, or do they merely explain their causal history without undermining their epistemic status?

## Common Misconceptions
- Showing that a moral belief has an emotional cause does not automatically show it is unreliable; many reliable beliefs have emotional reinforcement.
- Moral psychology describes how people make moral judgments; it does not by itself settle what the correct moral judgments are.

## Questions

```yaml
- question: "Researchers find that people's disgust responses reliably predict moral condemnation of 'harmless but disgusting' acts (e.g., consensual sibling incest with no consequences). Haidt interprets this as support for the social intuitionist model. Does this finding show that such condemnations are unjustified?"
  type: multiple-choice
  options:
    - "Yes — if a judgment originates in disgust rather than principled reasoning, it is automatically unreliable and should be revised"
    - "No — the causal origin of a belief in emotional processes does not by itself determine whether the belief is correct or epistemically justified"
    - "Yes — empirical findings about moral psychology directly reveal which moral judgments are accurate"
    - "No — but only because disgust is a reliable guide to moral harm whenever it occurs"
  answer: 1
  explanation: "This is the genetic fallacy applied to moral psychology: the causal history of a belief does not automatically determine its justificatory status. A belief caused by disgust could still be correct, and disgust can be reliable in domains it's calibrated to (e.g., avoiding pathogens). The debunking worry becomes compelling when two additional conditions hold: (1) the intuition is in tension with other intuitions or careful reasoning, and (2) the causal mechanism clearly wasn't tracking moral truth in this domain. Disgust applied to harmless acts satisfies both — but the mere fact that disgust caused the judgment is not sufficient alone to debunk it."

- question: "In Greene's trolley-problem research, most people say they would pull a lever to divert a trolley (killing one, saving five) but would not push a large person off a bridge (same arithmetic outcome). Greene's explanation is:"
  type: multiple-choice
  options:
    - "People correctly apply a valid deontological distinction between killing by action and killing as a side-effect of redirection"
    - "Physical contact triggers an emotional alarm system, generating a strong 'don't do it' response that feels different despite identical utilitarian math"
    - "People are poorly informed about the consequences of the bridge case and would agree if better explained"
    - "The cases differ morally because pushing involves more certainty about the victim's death"
  answer: 1
  explanation: "Greene's dual-process account explains the asymmetry through the emotional salience of physical contact. The footbridge case — pushing someone — activates an alarm system in the brain (associated with personal force and direct harm) that generates a strong deontological intuition against pushing. The switch case lacks this visceral trigger. Since the utilitarian math is identical, Greene argues the moral difference in intuitive responses reflects different cognitive processes (System 1 emotional vs. System 2 deliberative), not a genuine moral distinction. This challenges deontological theories that treat the distinction as principled."

- question: "Haidt's social intuitionist model claims that moral reasoning typically precedes and produces moral judgment, with emotions serving mainly as post-hoc motivational support."
  type: true-false
  answer: false
  explanation: "Haidt argues precisely the opposite: moral judgment is primary (fast, automatic, and emotionally driven), while moral reasoning is typically post-hoc rationalization — constructing arguments after the judgment has already been made. This inverts the rationalist picture (Kohlberg's stages) in which careful reasoning produces the judgment. Haidt's model draws on dual-process psychology: moral intuitions operate like System 1 perception, and the 'reasoning' we produce to justify them is typically motivated rationalization, not the true cause of the verdict."

- question: "Demonstrating that a moral intuition has an evolutionary or emotional causal explanation is sufficient by itself to show that the intuition is unreliable and should be revised."
  type: true-false
  answer: false
  explanation: "This confuses causal explanation with epistemic debunking. Many reliable beliefs have evolutionary or emotional causes. The debunking argument requires showing not just that the belief has a non-rational cause, but that the causal mechanism was not tracking moral truth — that it was calibrated to something else (reproductive fitness, pathogen avoidance, in-group signaling) rather than moral facts. The combination of a non-truth-tracking mechanism AND conflict with careful reasoning or other intuitions gives specific grounds to revise. A blanket dismissal of emotionally-caused moral beliefs would eliminate much of our moral knowledge."

- question: "What is the 'debunking problem' in moral psychology, and under what conditions does it give genuine reason to revise a moral intuition?"
  type: short-answer
  answer: "The debunking problem asks whether explaining the causal origin of a moral belief — in evolution, emotional responses, or social conditioning — undermines its epistemic justification. The answer is not automatic: a belief can have an emotional cause and still be correct, since emotions can reliably track morally relevant features of situations. The debunking argument gains force under two conditions: first, the causal mechanism that produced the intuition was not tracking moral truth (e.g., disgust evolved to avoid pathogens, not to detect moral wrongness); and second, the intuition conflicts with other intuitions or with careful reasoning. When both conditions hold together — a non-truth-tracking mechanism and internal tension — there are specific grounds to revise the intuition rather than trust it. In the absence of conflict, even an emotionally-caused intuition may be trustworthy."
  explanation: "Haidt's framework is descriptive — it explains how moral judgments are formed — but it does not directly answer the normative question of which intuitions we should trust. Moral psychology supplies the tools for that decision: by identifying the causal mechanism behind an intuition, we can assess whether it's the kind of mechanism likely to be calibrated to moral reality. Disgust applied to consensual harmless acts is a paradigm case where the mechanism (pathogen avoidance) is clearly miscalibrated. Empathic responses to suffering may be more reliably calibrated. The debunking problem thus points toward a nuanced reflective equilibrium, not blanket skepticism or blanket trust."
```

## Explainer

You already know from virtue ethics that moral character involves stable dispositions—the virtuous person acts well because of who they are, not just because they calculated the right answer. Moral psychology takes a step back from normative ethics and asks a more empirical question: how do human beings actually form moral judgments? The answer turns out to be far messier than the rationalist tradition assumed, and the implications for ethics are genuinely unsettling.

Jonathan Haidt's **social intuitionist model** is the starting point. The key claim is that moral judgments are typically fast, automatic, and emotionally driven—more like perceiving than reasoning. When you see someone kick a dog for fun, you don't compute consequences and consult principles; you feel immediate revulsion and only later, if pressed, reach for reasons. Haidt calls the reasons we produce afterward **post-hoc rationalization**: the judgment was already made; the argument is constructed to justify it. This inverts the rationalist picture (Kohlberg's stages) where careful moral reasoning produces the judgment. Think of your cognitive biases work: we already know that humans are poor at recognizing when reasoning is motivated rather than objective. Haidt is applying that insight directly to ethics.

Joshua Greene extended this with **dual-process theory**, using trolley-problem data. The famous footbridge case—where you must push a large stranger off a bridge to stop a trolley from killing five—generates strong deontological intuitions in most people (you shouldn't push), even though the utilitarian math is identical to the switch-lever case (where most people say pull the lever). Greene argues the difference is emotional proximity: physical contact triggers an alarm system in the brain, generating a strong "don't do it" response. More deliberate, System 2 reasoning tends to favor consequentialist conclusions. So deontological and consequentialist intuitions may map onto different cognitive systems, not just different principles.

The deepest question moral psychology raises is what philosophers call the **debunking problem**: if a moral belief has a causal explanation in emotional mechanisms—mechanisms that evolved for reasons having nothing to do with moral truth—does that undermine the belief's justification? Not automatically. The causal history of a belief doesn't automatically determine its epistemic status; true beliefs can have non-truth-tracking causes, and emotions can be reliable guides in domains they're calibrated to. But the debunking worry is sharpest when intuitions conflict with each other or with careful argument. If your disgust response tells you something is wrong but no principled reason emerges, the fact that disgust is a blunt evolutionary instrument gives you grounds to revise. Moral psychology supplies tools for deciding when to trust and when to override our moral intuitions—a decision that ordinary ethics can't make without this empirical backdrop.
