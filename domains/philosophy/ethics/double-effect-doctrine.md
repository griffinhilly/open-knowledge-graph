---
id: double-effect-doctrine
title: Doctrine of Double Effect
domain: philosophy
course: ethics
prerequisites:
- id: deontological-ethics
  type: hard
- id: trolley-problem
  type: soft
builds-toward:
- bioethics
tags:
- normative-ethics
- double-effect
- intended-vs-foreseen
- permissibility
- Aquinas
- just-war
stage: formal-systems
status: draft
---

# Doctrine of Double Effect

## Core Idea
The Doctrine of Double Effect (DDE), originating in Aquinas's discussion of self-defense, holds that it can be permissible to cause a harmful effect as a foreseen but unintended side effect of pursuing a good end, even when it would be impermissible to cause that same harm as an intended means to the same end. The doctrine has four conditions: the action itself must not be intrinsically wrong; the agent must intend the good effect, not the bad one; the bad effect must not be the means to the good effect; and there must be proportionately grave reason for permitting the bad effect. The DDE explains the asymmetry in trolley cases (diverting the trolley foreseeably kills one, but the death is not the means; pushing the man uses his death as the means) and is applied in medical ethics (palliative sedation that foreseeably hastens death), military ethics (collateral damage in just war theory), and end-of-life care. Critics question whether the intended/foreseen distinction is morally relevant, whether it can be drawn clearly, and whether agents can genuinely not intend what they knowingly cause.

## How It's Best Learned
Read Aquinas's Summa Theologica II-II, Q. 64, Art. 7, then Philippa Foot's "The Problem of Abortion and the Doctrine of the Double Effect." Apply the four conditions to each trolley variant and to palliative care cases. Ask: can the intended/foreseen distinction bear the moral weight placed on it?

## Common Misconceptions
- The DDE does not permit any harm as long as it is merely foreseen; the proportionality condition requires that the good achieved be serious enough to justify the foreseen harm.
- The DDE is not exclusively a Catholic doctrine; it is widely discussed in secular ethics and has defenders across religious and non-religious traditions.

## Questions

```yaml
- question: "A military commander orders an airstrike on a weapons factory, knowing civilians in adjacent buildings will be killed. He claims this is permitted by the Doctrine of Double Effect. Which condition, if violated, would most directly invalidate the DDE's application here?"
  type: multiple-choice
  options:
    - "The commander cannot intend a good effect (destroying weapons) while also causing harm"
    - "The civilian deaths are the means by which the weapons are destroyed — their presence is being exploited to enable the strike"
    - "Any action that foreseeably causes civilian deaths is intrinsically wrong, so the first condition fails"
    - "The proportionality condition is automatically violated whenever civilians are killed"
  answer: 1
  explanation: "Condition 3 is the most critical: the harmful effect must not be the means to the good effect. If the civilians are instrumentally necessary for achieving the military goal — their deaths are the mechanism — the DDE does not apply. In the standard collateral-damage case, the civilian deaths are a foreseen side effect of a strike directed at the factory, not the means. The DDE can then proceed to the proportionality weighing. Option C is false: bombing a military target is not intrinsically wrong, so condition 1 holds. Option D is false: proportionality is a weighing judgment, not an automatic disqualifier."

- question: "Which of the following cases most clearly violates the Doctrine of Double Effect's third condition (the bad effect must not be the means to the good effect)?"
  type: multiple-choice
  options:
    - "A surgeon administers morphine knowing it may hasten death, intending to relieve pain"
    - "A soldier diverts an artillery shell toward one enemy combatant to prevent it from hitting a group of five"
    - "A doctor performs surgery knowing there is a 10% chance the patient will not survive the procedure"
    - "A general orders execution of civilian hostages to compel the enemy to surrender"
  answer: 3
  explanation: "Option D is the clear violation: the civilian deaths are the intended means — the mechanism of coercion — so the general needs the hostages to die in order to produce the surrender. This is categorically different from a side effect. Options A, B, and C all involve harmful outcomes that are foreseen side effects of actions directed at other goals (pain relief, redirecting a shell, necessary surgical risk). The test: 'Would the good outcome still occur if the bad effect somehow did not happen?' If yes, the bad effect is a side effect; if no, it is the means."

- question: "According to the Doctrine of Double Effect, an action is permissible whenever the agent intends the good effect and merely foresees (but does not intend) the harmful effect."
  type: true-false
  answer: false
  explanation: "Intending the good and merely foreseeing the bad is necessary but not sufficient for DDE permissibility. There are four conditions, all of which must be met: (1) the act must not be intrinsically wrong; (2) the agent must intend the good and not the bad; (3) the bad effect must not be the means to the good effect; (4) there must be proportionate reason. An agent could sincerely intend only the good while the bad effect is the very mechanism of the good (violating condition 3), or while the harm is wildly disproportionate to the good achieved (violating condition 4)."

- question: "The Doctrine of Double Effect applies differently to diverting a trolley versus pushing a bystander onto the tracks, even though both actions result in one person dying to save five."
  type: true-false
  answer: true
  explanation: "This asymmetry is exactly what the DDE is designed to explain. When you divert the trolley, the one person's death is a foreseen side effect of redirecting the trolley — the death is not the means by which the five are saved. When you push the bystander, his body is the means: you need his mass to stop the trolley, so his death (or at least his body's position) is the mechanism of rescue. Condition 3 of the DDE prohibits using someone's death as the means, which is why pushing is DDE-impermissible while diverting can be DDE-permissible."

- question: "What is the third condition of the Doctrine of Double Effect, and why do philosophers consider it the most contested? Illustrate with an example."
  type: short-answer
  answer: "The third condition states that the harmful effect must not be the means to the good effect — the harm may be a foreseen side effect, but it cannot be the instrument by which the good is achieved. It is the most contested because drawing this line in practice is difficult and potentially manipulable: an agent can re-describe their action to make a harm that is functionally instrumental appear to be 'merely foreseen.' For example, one might argue that in the trolley footbridge case, the bystander's death is a side effect of 'placing weight on the tracks' rather than the means — showing how the intended/means distinction can blur under redescription."
  explanation: "Critics argue that agents who knowingly use harm as a tool can simply reframe their intentions to satisfy condition 3 verbally. DDE proponents respond that the structure of the action itself — not the agent's verbal description — determines whether harm is means or side effect. The counter-factual test: if removing the harmful consequence would defeat the good effect, it was a means; if not, it was a side effect. This test is the most commonly used criterion for applying condition 3 in applied ethics contexts."
```

## Explainer

From your study of deontological ethics, you know that deontology holds that certain acts are intrinsically right or wrong regardless of consequences, and that **agent-relative constraints** — duties not to kill, lie, or violate rights — cannot be overridden simply by producing better outcomes. This creates a practical problem: what do you do when pursuing a genuinely good end unavoidably causes harm? A surgeon administering high-dose painkillers to a terminally ill patient knows the drugs may hasten death. A military commander targeting a weapons depot knows civilians nearby may be killed. A person using lethal force in self-defense knows they may kill the attacker. Deontology says some acts are impermissible, but these cases seem like they might be permissible — and the Doctrine of Double Effect is the framework developed to explain why.

The doctrine's central distinction is between **intended effects** and **foreseen-but-unintended side effects**. When you act, your action typically has multiple effects: some you aim at (as ends or as means to ends), and some you merely foresee will occur without aiming at them. The DDE holds that this distinction is morally significant: you are directly responsible for what you intend, but only indirectly responsible for what you merely foresee. Returning to the surgeon: if she administers morphine intending to relieve pain, and the death is a foreseen but unintended side effect, the DDE can permit the action. If she administered the same drug intending to hasten death (even to relieve suffering), she would be killing rather than treating — a fundamentally different act under the doctrine.

The **four conditions** give the doctrine its precision. First, the act itself must not be intrinsically wrong — a genuinely evil act is not permissible just because you attach good intentions to it. Second, the agent must sincerely intend the good effect and not the harmful one — the harmful effect must be a side effect, not the aim. Third, and most contested, the harmful effect must not be the **means** to the good effect — you may not use harm as a tool to produce good, even foreseeably. This is what distinguishes diverting the trolley from pushing the man off the bridge in the trolley problem: in diversion, the one person's death is a foreseen side effect of redirecting the trolley; in pushing, the man's body is the means (you need him to stop the trolley). Fourth, there must be **proportionate reason** — the good achieved must be serious enough to justify allowing the foreseen harm. Minor goods do not justify major harms, even as side effects.

The DDE's most important applications are in medical and military ethics. In **palliative care**, the doctrine permits administering pain-relieving medications at doses that may hasten death, provided the intent is relief, not death, and the dosing is proportionate to the patient's suffering. This is sometimes called the "principle of double effect in end-of-life care" and shapes both medical ethics guidelines and legal frameworks in many jurisdictions. In **just war theory**, the doctrine permits bombing a military target even when civilian casualties are foreseen, provided the military objective is legitimate, the civilian deaths are not intended as the means to that objective, and the expected civilian harm is proportionate to the military gain. "Collateral damage" is the just war vocabulary for permissible foreseen-but-unintended civilian harm under DDE-style reasoning.

Critics press on two fronts. The first is the **metaphysical challenge**: is the intended/foreseen distinction always clear? Agents can be self-deceived about their intentions, or their "intentions" can be post-hoc rationalizations of what they were going to do anyway. If a general "intends" only to destroy the depot but "merely foresees" killing a hundred civilians, it can seem like a verbal maneuver rather than a genuine moral distinction. The second is the **normative challenge**: even granting that the distinction is real, why does it bear the moral weight the DDE assigns to it? A consequentialist will point out that the civilians are equally dead whether their deaths were intended or foreseen, and that if outcomes are what matter morally, the distinction is irrelevant. Elizabeth Anscombe and Philippa Foot, who defended the doctrine against Judith Jarvis Thomson's challenges in the trolley debates, argued that our intuitions about the asymmetry between intended and foreseen harms track something real about the nature of agency and responsibility — that what you aim at constitutes who you are as an agent in a way that what you merely foresee does not. This debate remains one of the most productive in contemporary applied ethics.


