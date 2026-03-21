---
id: moral-knowledge
title: Moral Knowledge
domain: philosophy
course: ethics
prerequisites:
- id: metaethics-intro
  type: hard
- id: moral-realism
  type: soft
builds-toward:
- moral-particularism
tags:
- metaethics
- moral-epistemology
- moral-knowledge
- moral-intuitions
- reflective-equilibrium
stage: formal-systems
status: draft
---

# Moral Knowledge

## Core Idea
Moral epistemology asks whether and how we can have moral knowledge. If moral realism is true and there are mind-independent moral facts, how do we access them? Moral intuitionism (Ross, Audi) holds that some moral propositions are self-evident to mature moral agents, analogous to basic logical or mathematical truths. Reflective equilibrium (Rawls, Daniels) proposes that moral knowledge emerges from mutual adjustment between particular moral judgments, general principles, and background theories until they cohere. Moral coherentism and foundationalism mirror their counterparts in general epistemology. Skeptical challenges include the evolutionary debunking argument (Street, Joyce): if our moral intuitions were shaped by natural selection for reproductive fitness rather than tracking moral truth, their reliability is undermined. Defenders respond that evolutionary origins do not automatically debunk beliefs, just as the evolutionary origins of mathematical intuitions do not debunk mathematics.

## How It's Best Learned
Read Rawls's discussion of reflective equilibrium in A Theory of Justice (sections 4 and 9), then read Sharon Street's "A Darwinian Dilemma for Realist Theories of Value." Ask: does the evolutionary origin of a moral belief give us reason to doubt it? Compare this to the case of perceptual beliefs shaped by evolution—are these debunked too?

## Common Misconceptions
- Moral intuitionism does not claim that moral knowledge is infallible gut feeling; it holds that certain moral propositions are self-evident upon careful reflection, much like basic logical axioms.
- The existence of moral disagreement does not by itself refute moral knowledge; there is disagreement in science and mathematics too, and we do not conclude that scientific or mathematical knowledge is impossible.

## Questions

```yaml
- question: "The evolutionary debunking argument (Street, Joyce) challenges moral realism by arguing that our moral intuitions are unreliable guides to moral truth. What is the strongest response that defenders of moral knowledge offer?"
  type: multiple-choice
  options:
    - "Moral intuitions are infallible because they are hardwired by millions of years of evolution"
    - "Evolutionary origins do not automatically debunk beliefs — by the same logic, mathematical and logical intuitions would also be debunked, and we are not prepared to abandon mathematics"
    - "Evolution does track moral truth because organisms with correct moral beliefs survived longer"
    - "Moral knowledge does not require reliable intuitions because ethics is a matter of cultural consensus"
  answer: 1
  explanation: "The symmetry argument is the strongest response: if we should distrust moral intuitions because they evolved for fitness rather than truth, we must equally distrust mathematical and logical intuitions, which also have evolutionary histories. Since we are not prepared to abandon mathematics on these grounds, evolutionary origins alone cannot be sufficient to debunk a belief system. What matters is whether the belief-forming process is reliable, not whether evolution specifically aimed it at truth."

- question: "Rawls's method of reflective equilibrium holds that moral knowledge emerges from which process?"
  type: multiple-choice
  options:
    - "Deducing all moral principles from a single foundational axiom by pure reason"
    - "Identifying moral facts through direct perceptual observation of the world"
    - "Iterative mutual adjustment between considered judgments, general principles, and background theories until they cohere"
    - "Aggregating survey data on what most people find morally intuitive across cultures"
  answer: 2
  explanation: "Reflective equilibrium is an iterative coherence method, not deduction from axioms. It starts with 'considered judgments' — moral intuitions held with high confidence under favorable conditions — and seeks coherence between these, the principles that systematize them, and the background theories that support those principles. When tension arises, either the principle or the judgment can be revised, depending on relative confidence. Knowledge is the stable coherence achieved through this mutual adjustment."

- question: "Moral intuitionism holds that basic moral propositions are self-evident — analogous to logical axioms — not that they are infallible or unrevisable gut feelings."
  type: true-false
  answer: true
  explanation: "This is the key distinction the misconceptions section emphasizes. Intuitionists like Ross and Audi hold that propositions such as 'gratuitous cruelty is wrong' are grasped directly upon careful reflection, not through inference from prior premises — analogous to how logical axioms are not proven but understood. Crucially, self-evidence does not imply infallibility: a seemingly self-evident proposition can be rejected if compelling argument shows it conflicts with something we are even more confident about."

- question: "Widespread moral disagreement across cultures is sufficient to refute the possibility of moral knowledge."
  type: true-false
  answer: false
  explanation: "Disagreement is compatible with knowledge — there is ongoing disagreement in science and mathematics, and we do not conclude that scientific or mathematical knowledge is impossible. Moral disagreement shows that moral inquiry is difficult and that we may be in error about some moral beliefs, but it does not establish that no moral truth is accessible. The existence of some disagreement is a datum that any theory of moral knowledge must explain, not an automatic refutation of moral realism."

- question: "What core challenge do evolutionary debunking arguments pose to moral realism, and why can the realist not simply ignore the evolutionary origins of moral intuitions?"
  type: short-answer
  answer: "The debunking argument presents a dilemma: either explain why evolution would track mind-independent moral truth (which is hard — evolution is blind to truth and responds only to fitness), or accept that the correlation between our intuitions and moral facts is coincidental (which undermines their evidential value). The realist cannot ignore evolutionary origins because the credibility of moral intuitions as evidence depends on their being reliably connected to moral truth. If they were shaped entirely by fitness with no connection to truth, the realist has no remaining basis for treating intuitions as data about moral reality."
  explanation: "This is why the debate is genuine and live rather than easily dismissed. A moral realist who simply says 'I trust my intuitions' has not answered the debunker's challenge — they have merely restated their prior commitment. The realist must either show that fitness-tracking and truth-tracking can coincide (e.g., because welfare facts are both fitness-relevant and morally real), or argue by symmetry (the same debunking applies to math), or accept a more modest epistemological position. Each response has costs, which is why moral epistemology remains one of the most active areas in metaethics."
```

## Explainer

From your study of metaethics, you know the central debate: are there mind-independent moral facts (moral realism), or are moral claims merely expressions of attitude, projections of culture, or useful fictions? From your work on moral realism specifically, you know that if moral realism is true — if there really are facts about what is right and wrong independent of what anyone happens to think — then a natural question arises: how do we come to know these facts? The epistemology of morality picks up where metaethical ontology leaves off. It asks not whether moral facts exist but what our access to them looks like.

**Moral intuitionism**, defended by W.D. Ross and more recently by Robert Audi, holds that some basic moral propositions — "gratuitous cruelty is wrong," "keeping promises matters," "persons have dignity that must be respected" — are **self-evident** to any sufficiently reflective and attentive moral reasoner. The analogy is to logical and mathematical axioms: "If A = B and B = C, then A = C" is not proven from prior propositions; it is grasped directly upon understanding the concepts involved. Intuitionists claim that basic moral truths are similarly grasped — not through inference but through direct rational insight once you understand what is at stake. Crucially, intuitionism does not equate self-evidence with infallibility or unrevisability; a self-evident proposition can still be rejected if compelling argument shows it is inconsistent with other things we are more confident about. What intuitionism denies is that all moral knowledge is ultimately derived from inference from non-moral premises.

**Reflective equilibrium**, Rawls's methodology in *A Theory of Justice*, offers a different picture of how moral knowledge accumulates. The method begins with **considered judgments** — those moral intuitions we hold with high confidence under favorable conditions (we are calm, informed, and the case is not one in which we have obvious self-interest). These judgments serve as data points: "Slavery is wrong" and "torturing children for fun is wrong" are examples of considered judgments so firm that no abstract principle inconsistent with them should survive philosophical scrutiny. The method then seeks **coherence** between these judgments, the moral principles that best systematize them, and the background theories (about personhood, rationality, fairness) that support those principles. When there is tension between a principle and a considered judgment, you can go either direction: revise the principle or revise the judgment, depending on how confident you are in each. Knowledge emerges from the process of mutual adjustment toward stable coherence — what Rawls called **wide reflective equilibrium** when background theories are also adjusted.

The most powerful contemporary challenge to moral knowledge comes from **evolutionary debunking arguments**, associated with Sharon Street and Richard Joyce. The argument runs: our moral intuitions were shaped by natural selection for reproductive fitness, not for tracking mind-independent moral truth. Evolution equipped us with dispositions to care for kin, to cooperate with group members, to feel disgust at norm violations — all because these dispositions enhanced survival and reproduction. But there is no reason to think evolution would track moral truth; evolution is blind to truth and responsive only to fitness. If our moral intuitions are explained entirely by their fitness-enhancing role, we have no reason to think they are reliable guides to moral facts, even if those facts exist. Street argues this creates a fatal dilemma for the moral realist: either explain the correlation between moral facts and our evolved intuitions (which seems impossible, since evolution does not respond to moral facts), or accept that the correlation is a coincidence (which undermines the claim to moral knowledge).

Defenders of moral knowledge respond in several ways. Some argue that the evolutionary origins of beliefs do not by themselves debunk them — the same argument would debunk mathematical and logical intuitions, which also have evolutionary histories, and we are not prepared to abandon mathematics. What matters is whether the belief-forming process is reliable, not whether its evolutionary origin was specifically aimed at truth. Others argue that some moral truths — particularly those concerning welfare, suffering, and basic needs — may have been fitness-relevant for good reasons: organisms that correctly identified that suffering is bad and satisfaction is good were tracking something real about the nature of sentient experience that was also fitness-relevant. The debate between evolutionary debunking and its critics is live and unresolved, making moral epistemology one of the most active areas at the intersection of metaethics, philosophy of mind, and evolutionary theory.


