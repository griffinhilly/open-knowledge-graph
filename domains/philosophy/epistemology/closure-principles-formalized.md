---
id: closure-principles-formalized
title: Closure Principles Formalized
domain: philosophy
course: epistemology
prerequisites:
- id: possible-worlds-semantics-knowledge
  type: hard
- id: epistemic-closure
  type: soft
- id: first-order-logic-syntax
  type: soft
- id: propositional-logic-introduction
  type: soft
tags:
- closure
- deductive-closure
- knowledge-transmission
stage: formal-systems
status: validated
---

# Closure Principles Formalized

## Core Idea
A closure principle states that if an agent knows p and knows that p entails q, she knows q. Formally: if Kₐp and Kₐ(p → q), then Kₐq. In possible-worlds semantics, closure fails when the agent fails to know a valid implication; for instance, one might know the premises of a long proof without knowing the conclusion. Closure is controversial: some epistemologists reject it to avoid skepticism, while others defend restricted versions.

## Questions

```yaml
- question: "You know that having two hands entails you are not a handless brain in a vat. You admit you cannot know you are not a brain in a vat. What does the closure principle force you to conclude?"
  type: multiple-choice
  options:
    - "You do know you are not a brain in a vat, since closure transmits knowledge forward from your knowledge of having hands"
    - "You do not know you have two hands, since closure by contraposition requires knowledge of the entailed proposition"
    - "Closure does not apply here because skeptical scenarios are not genuine epistemic possibilities"
    - "You can know you have two hands without the closure principle applying to skeptical entailments"
  answer: 1
  explanation: "By contrapositive, if Kₐ(p → ¬SK) and ¬Kₐ(¬SK), then ¬Kₐp. Closure doesn't just run forward (from premises to conclusions) — by contraposition it runs backward: failure to know the conclusion forces failure to know the premise. This is exactly the skeptical argument: since you can't rule out being a brain in a vat, closure forces you to admit you don't know you have hands. This is why Dretske and Nozick rejected closure — it collapses ordinary knowledge into skepticism."

- question: "Which of the following correctly states the basic closure principle?"
  type: multiple-choice
  options:
    - "If Kₐp is true, then p is true in all possible worlds"
    - "If Kₐp and Kₐ(p → q), then Kₐq"
    - "If p entails q and Kₐp, then Kₐq — regardless of whether the agent knows the entailment"
    - "If Kₐp and p is necessarily true, then Kₐq for any q"
  answer: 1
  explanation: "The closure principle requires both that the agent knows the premise AND that the agent knows the entailment from premise to conclusion. Option C states a stronger principle that drops the second knowledge condition — this would make knowledge automatically close under all logical consequences, even those the agent doesn't recognize. The standard principle requires the agent to know the implication, making it a condition on the agent's epistemic state rather than just on logical relations."

- question: "Philosophers who reject the closure principle typically do so in order to preserve ordinary knowledge claims while admitting ignorance of far-fetched skeptical scenarios."
  type: true-false
  answer: true
  explanation: "This is precisely the motivation articulated by Dretske and Nozick. By denying closure, they can say: 'I know I have two hands' and 'I don't know I'm not a brain in a vat' without contradiction, because the second doesn't follow from the first. Rejecting closure is not rejecting logic — it is denying that the logical transmission of truth is matched by a transmission of knowledge in all cases."

- question: "In possible-worlds semantics, the closure principle holds without exception: if p is true in most epistemically accessible worlds and p → q is true in most accessible worlds, then q is true in most accessible worlds."
  type: true-false
  answer: false
  explanation: "The logical argument in the possible-worlds framework is valid, but closure can still fail epistemically if the agent fails to know a valid implication. The formal analysis shows the logic is sound, but whether the agent's epistemic state satisfies all the conditions of closure is a separate question. More importantly, the closure debate often focuses on whether the possible-worlds account of knowledge itself must be revised — contextualist and relevant alternatives theories modify the accessibility relation in ways that make closure fail even within the framework."

- question: "State the closure principle formally using the Kₐ notation, then explain how its contrapositive form generates a skeptical argument against ordinary knowledge."
  type: short-answer
  answer: "Formal statement: If Kₐp and Kₐ(p → q), then Kₐq. Contrapositive: If ¬Kₐq and Kₐ(p → q), then ¬Kₐp. The skeptical argument: Let p = 'I have two hands' and q = 'I am not a brain in a vat.' Since p entails q, and I know this entailment, closure gives Kₐ(p → q). But I cannot know I am not a brain in a vat (¬Kₐq). By contrapositive closure, I therefore do not know I have two hands (¬Kₐp). The argument generalizes: any ordinary knowledge claim p entails 'I am not in a skeptical scenario,' so failure to know the skeptical denial propagates back to undermine all ordinary knowledge."
  explanation: "The power of the formal statement is that it makes the stakes inescapable: either accept closure and face skepticism, reject closure and explain why knowledge doesn't transmit in these cases, or find some other response (like arguing you can know the skeptical denial after all). Each horn of the dilemma has costs, and the formal clarity shows there is no cheap escape."
```

## Explainer

You've already studied epistemic closure informally and have tools from possible-worlds semantics and propositional logic. The closure principle can now be stated precisely. Using the notation **Kₐp** for "agent a knows that p" and "→" for material implication, the basic closure principle reads: if Kₐp and Kₐ(p → q), then Kₐq. In words: if an agent knows a proposition and knows that it implies another proposition, she knows the second proposition too. This seems almost definitionally obvious — knowledge should be "closed" under known implication, the way that valid deduction transmits truth from premises to conclusions.

In possible-worlds semantics (your prerequisite), knowledge is analyzed as truth in all epistemically accessible worlds — the worlds compatible with everything the agent knows. Closure then has a natural reading: if p is true in all accessible worlds, and p → q is true in all accessible worlds, then q must also be true in all accessible worlds, so Kₐq holds. The logic seems impeccable. But closure generates a powerful **skeptical argument** via contraposition. Consider: you know you have two hands (Kₐp). "I have two hands" entails "I am not a handless brain in a vat" (p → ¬SK). By closure, you must know you are not a brain in a vat — but do you? If you cannot rule out the skeptical hypothesis directly, closure forces the conclusion backward: since you don't know ¬SK, and you know p → ¬SK, you don't know p either. This is Nozick's and Dretske's motivation for **rejecting closure**: denying the principle lets you claim ordinary knowledge while admitting ignorance of far-fetched skeptical scenarios.

Those who defend closure, like John Hawthorne and Timothy Williamson, argue that abandoning it produces its own absurdities — allowing knowledge of a conclusion while denying knowledge of its obvious consequences. **Restricted closure** principles attempt a middle path: closure holds for "obvious" or "single-step" deductions but may fail for long deductive chains where each step adds some risk of error. This connects to your logic background: in a proof of 100 steps where each step is 99% reliable, the probability of a sound conclusion is about 37% — yet we speak of knowing the premises and knowing each step follows. Whether we thereby "know" the conclusion is exactly what the closure debate forces us to confront. Formalizing the principle makes the stakes unavoidable: you must decide whether knowledge is truly closed under deduction, and the answer has consequences that reach all the way to skepticism.
