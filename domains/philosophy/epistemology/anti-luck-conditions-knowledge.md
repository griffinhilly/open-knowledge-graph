---
id: anti-luck-conditions-knowledge
title: Anti-Luck Conditions and Sensitivity
domain: philosophy
course: epistemology
prerequisites:
- id: safety-condition-knowledge
  type: hard
- id: sensitivity-condition-knowledge
  type: hard
- id: gettier-cases-formal-analysis
  type: soft
tags:
- anti-luck
- safety
- sensitivity
- knowledge
stage: formal-systems
status: validated
---

# Anti-Luck Conditions and Sensitivity

## Core Idea
Anti-luck approaches to knowledge add conditions that exclude cases where someone believes something true mostly by luck. The safety condition requires that if the belief were held, the belief would very likely be true; sensitivity requires that if P were false, the belief would not be held. These modal conditions aim to capture the intuition that knowledge is incompatible with too much epistemic luck.

## How It's Best Learned
Test safety and sensitivity with lottery cases and fake barn cases. See why each condition handles some cases well but struggles with others. Consider whether combining conditions improves the account or creates new problems.

## Common Misconceptions
- Safety and sensitivity aren't about physical possibility; they concern what would happen under counterfactual variations near the actual case. - Strong versions of these conditions are subject to counterexamples, but moderate versions may survive. - Anti-luck accounts don't deny that all beliefs involve some luck; they identify problematic cases of excessive luck.

## Questions

```yaml
- question: "Henry drives through countryside where 99% of barn-shaped structures are fake facades, but he stops in front of the one real barn and forms the belief 'there is a barn in front of me.' Does his belief satisfy the safety condition?"
  type: multiple-choice
  options:
    - "Yes — Henry is actually looking at a real barn, so his belief is true in the actual world"
    - "Yes — Henry's belief is justified by normal perceptual faculties, which is all safety requires"
    - "No — in nearby possible worlds where he holds the same belief by the same method, he is mostly looking at facades, so his belief would frequently be false"
    - "No — safety requires that Henry know he is in fake-barn country before his belief can be assessed"
  answer: 2
  explanation: "Safety asks: in nearby worlds where you hold this belief by the same method, is the belief true? In worlds close to Henry's — also driving through fake-barn country, also relying on visual appearance — he would mostly be facing facades, and his belief 'there is a barn' would be false. Safety fails. His actual-world success is a matter of luck: he happened to stop at the one real barn, but his belief-forming method would easily have produced a false belief. This modal fragility is what anti-luck conditions are designed to capture."

- question: "How does the sensitivity condition explain why Henry's barn belief fails to constitute knowledge?"
  type: multiple-choice
  options:
    - "Sensitivity fails because Henry would still believe 'there is a barn' even if there were no barn — he would be looking at a convincing facade"
    - "Sensitivity fails because Henry cannot introspectively verify whether he is in fake-barn country"
    - "Sensitivity is satisfied here, which shows sensitivity alone cannot explain the barn case"
    - "Sensitivity requires that the belief track truth across all possible worlds, not only the nearest ones"
  answer: 0
  explanation: "Sensitivity (Nozick) requires: if P were false, you would not believe P. For Henry: if there were no barn in front of him, he would still believe there was one — he would be looking at an indistinguishable facade. The nearest 'no barn here' worlds are accessible, and his belief survives in them unchanged. Sensitivity fails, diagnosing the barn case as non-knowledge. His belief does not track the truth: it would persist even in error-worlds close to his actual situation."

- question: "A belief that satisfies the safety condition should also satisfy the sensitivity condition, and vice versa — the two conditions are equivalent."
  type: true-false
  answer: false
  explanation: "Safety and sensitivity can come apart. Lottery cases illustrate this: my pre-draw belief that I will not win satisfies sensitivity (if I had won, I would believe I had won — I'd see the ticket) but may fail safety (in nearby worlds where I hold that belief, there is a small but non-negligible chance I do win). Other cases push in the other direction. The conditions encode different modal relationships: sensitivity concerns what happens if the content is false; safety concerns what happens in nearby worlds where the belief is held. They are not equivalent."

- question: "Anti-luck conditions require that knowledge is incompatible with any element of luck — even ordinary epistemic luck like being in the right place at the right time to observe an event."
  type: true-false
  answer: false
  explanation: "Anti-luck accounts specifically target the kind of epistemic luck that severs the reliable connection between belief and truth — where you happen to be right but would easily have been wrong. Not all luck undermines knowledge. That you were lucky to glance up just as the rare bird flew past does not prevent you from knowing you saw it. The problematic luck is revealed by the counterfactual structure: if your belief would survive in nearby worlds where it is false, the connection between belief and truth is fragile, not robust. This is the relevant kind of luck, not luck in the circumstances of evidence-gathering."

- question: "Why do Gettier cases fail anti-luck conditions? Describe the modal structure that shows the belief is only luckily true."
  type: short-answer
  answer: "In Gettier cases, the actual world cooperates with the belief, but nearby counterfactual worlds do not. For the barn case: Henry believes truly in the actual world, but in very similar worlds — nearby in the space of possibilities — he is looking at a facade and his belief is false. The safety condition is violated: his belief-forming method frequently yields false beliefs in close worlds. The belief is 'fragile': it is true only because the actual world happened to place a real barn at Henry's stopping point, not because his belief-forming process reliably tracks truth. Anti-luck conditions reveal that Gettier cases lack the robust modal connection between belief and truth that knowledge requires."
  explanation: "The shift from justified true belief to anti-luck conditions relocates the analysis: instead of asking 'is this belief justified and true?', we ask 'does this belief reliably track truth across the nearby counterfactual landscape?' Gettier cases pass the first test but fail the second — their truth is accidental, not structural."
```

## Explainer

Your prerequisite work on Gettier cases showed that justified true belief is not sufficient for knowledge — someone can believe something, be justified in believing it, and be right, while still clearly not *knowing* it. The barn façade case is canonical: Henry drives through a region where nearly all visible structures are fake barn fronts, but happens to stop in front of the one real barn. He forms the belief "there is a barn in front of me," and he is justified (barn fronts look like barns) and true (it really is a barn). Yet philosophers widely agree Henry does not *know* there is a barn there. The reason is luck: he just happened to stop in front of the one real one. Anti-luck conditions are attempts to diagnose, precisely and rigorously, what kind of luck is incompatible with knowledge.

The **sensitivity condition** (Nozick) analyzes this in counterfactual terms: you know P only if, if P were false, you would not believe P. Consider the barn case: if there were no barn in front of Henry, he would still believe there was one (because he would be looking at a façade). Sensitivity fails — hence no knowledge. The condition has strong intuitive support. If my belief would remain unchanged even in a world where what I believe is false, something clearly has gone wrong. However, sensitivity runs into trouble with lottery cases. I believe I will not win the lottery; if I had won, I would believe I had won (I would see the ticket). My belief that I will lose is sensitive — but it seems odd to say I *know* I will lose before the draw.

The **safety condition** (Sosa, Williamson) reverses the conditional: you know P only if, in nearby possible worlds where you believe P by the same method, P is true. For Henry: in nearby worlds (driving through the same region), he believes "there is a barn" based on visual appearance, but in many of those worlds what he is looking at is a façade. Safety fails — hence no knowledge. Safety handles lottery cases more smoothly: in nearby worlds, I do not believe I won the lottery (I only believe it once I see the ticket), so my belief that I have not won can be safe.

The deeper point these conditions illuminate is that knowledge requires a certain kind of **modal connection** between your belief and the truth. It is not enough that you happened to believe truly; the truth must be reliably involved in why you believe. Your belief must not be the kind that would survive in error-worlds close to the actual one. Neither condition captures this perfectly — there are counterexamples to strong formulations of each — but they focus the investigation in a way that "justified true belief" never did. They explain *why* Gettier cases fail: in each case, the actual world happens to cooperate with the belief, but the nearby counterfactual structure reveals that the connection between belief and truth is fragile rather than robust. Anti-luck conditions try to make "not fragile" precise.
