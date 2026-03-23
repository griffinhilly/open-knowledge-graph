---
id: anchoring-bias
title: Anchoring Bias
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: cognitive-biases-in-reasoning
  type: hard
tags:
- cognitive-bias
- anchoring
- heuristics
- framing
stage: formal-systems
status: validated
---

# Anchoring Bias

## Core Idea
Anchoring bias occurs when an initial piece of information — the 'anchor' — disproportionately influences subsequent judgments and decisions, even when the anchor is arbitrary or irrelevant. In Tversky and Kahneman's classic experiments, spinning a random number wheel before asking participants to estimate the percentage of African countries in the UN significantly shifted their answers toward the wheel's number. The bias persists because people adjust insufficiently from the anchor rather than reasoning from scratch. Anchoring affects negotiations, pricing, sentencing decisions, and any context where a starting value is presented before a judgment is made.

## How It's Best Learned
Run simple anchoring experiments with friends: present different starting numbers before asking estimation questions and observe how answers cluster around the anchors. Then examine real-world applications in retail pricing ('was $100, now $60'), salary negotiations, and legal sentencing to see how anchors shape outcomes.

## Common Misconceptions
- Thinking anchoring only works when people are unaware of it — research shows the bias persists even when people are explicitly warned about anchoring effects.
- Believing anchoring requires a plausible number; even absurdly high or low anchors shift estimates, though less dramatically.

## Questions

```yaml
- question: "You are selling a used car worth approximately $8,000. Based on anchoring research, what is the most strategically effective opening move in the negotiation?"
  type: multiple-choice
  options:
    - "Name $8,000 first — an accurate anchor avoids distorting the negotiation"
    - "Let the buyer name a price first to avoid imposing an anchor on them"
    - "Name a high anchor (e.g., $11,500) because subsequent bargaining will gravitate toward it, yielding a higher final price"
    - "Present your price alongside detailed documentation to neutralize anchoring effects"
  answer: 2
  explanation: "Anchoring research consistently shows that the first number named in a negotiation constrains the bargaining range. A high anchor pulls final settlements upward even as both parties adjust downward — the adjustment is systematically insufficient. Naming the accurate market value first sacrifices this advantage. Letting the buyer name first risks a low anchor that pulls your outcome downward. Documentation helps establish value but doesn't neutralize the anchoring effect of an initial number."

- question: "A researcher explicitly warns a group of participants: 'You are about to see a random number. Research shows it will bias your estimate. Try hard to correct for this.' She then shows the number 92 and asks them to estimate how many countries are in the United Nations. What does anchoring research predict?"
  type: multiple-choice
  options:
    - "Participants' estimates will be unaffected — explicit warnings fully neutralize anchoring bias"
    - "Participants will overcorrect and produce estimates far below the true answer by deliberately avoiding numbers near 92"
    - "Participants' estimates will still be pulled toward 92, because anchoring persists even when people are warned and try to correct for it"
    - "The warning will cause participants to reason entirely from scratch, eliminating any anchor effect"
  answer: 2
  explanation: "This is the most counterintuitive and important finding in anchoring research: the bias largely persists even with explicit warnings. You cannot introspect to find 'how much did the anchor shift me' and subtract that amount. You can adjust some in the right direction — warnings help partially — but you won't adjust enough to reach an unanchored estimate. The mechanism operates below conscious deliberation, which is why deliberate effort to 'be objective' doesn't fully compensate."

- question: "Anchoring bias only affects people who don't know the anchor is irrelevant — if you are aware that a number is random and has no connection to the question, it will not influence your estimate."
  type: true-false
  answer: false
  explanation: "This is precisely the misconception that anchoring research demolishes. In Tversky and Kahneman's classic wheel-spinning experiment, participants watched a wheel land on an obviously random number, knew it was random, yet their subsequent estimates of a completely unrelated quantity were significantly shifted toward that number. Awareness of irrelevance does not protect you from anchoring. The bias operates at a level below deliberate reasoning — it affects the starting point from which people adjust, a process that isn't fully accessible to conscious correction."

- question: "Even an anchor that is obviously arbitrary — such as a randomly spun number wheel — can shift numerical estimates on unrelated questions."
  type: true-false
  answer: true
  explanation: "This is the empirical foundation of anchoring research. Tversky and Kahneman's wheel experiment showed that groups exposed to the number 65 estimated 45% of UN members were African, while those exposed to 10 estimated 25% — a twenty-percentage-point difference driven by a visibly random anchor. The anchor doesn't need to be plausible or relevant; it simply needs to be present before the judgment is made. Even absurdly extreme anchors shift estimates, though less dramatically than plausible ones."

- question: "Why doesn't simply knowing about anchoring bias protect you from it, and what strategies can actually reduce its influence?"
  type: short-answer
  answer: "Anchoring operates through insufficient adjustment from a starting value — a process that occurs below deliberate reflection. You cannot introspect to determine how large the anchor's influence was, so you cannot simply subtract it. Strategies that genuinely help: generating your own estimate before seeing any anchor (inoculation before exposure); deliberately generating arguments for why the true value might be much higher and much lower, then synthesizing (multiple reference points); and designing decision environments that withhold numerical anchors until after independent estimates are formed."
  explanation: "The key is that correction requires knowing the magnitude of the distortion, and that information isn't available through introspection. You can improve your estimate by reasoning from multiple reference points rather than adjusting from a single one — this restructures the cognitive task so the anchor competes with other starting points rather than dominating. Awareness alone fails because it tells you the anchor is biasing you without telling you by how much."
```

## Explainer

From your study of cognitive biases, you already know that human reasoning regularly departs from the norms of formal logic and probability. **Anchoring bias** is one of the most thoroughly documented and practically consequential of these departures. It describes the tendency for an initial piece of information — even one that is explicitly random or irrelevant — to pull subsequent numerical estimates toward it. The mechanism is not gullibility; it appears to operate at a level below conscious deliberation.

The classic demonstration is Tversky and Kahneman's spinning wheel experiment: participants watched a wheel land on a number (rigged to land on 10 or 65), then estimated the percentage of African nations in the UN. The median estimate for the group that saw 65 was 45%; for the group that saw 10, it was 25%. The wheel was visibly random. The number was obviously irrelevant. Yet it shifted estimates by twenty percentage points. The reason appears to be that people begin from the anchor and **adjust insufficiently** — they move in the right direction but stop too early, leaving the anchor's influence embedded in the final answer.

What makes anchoring particularly powerful is its resistance to awareness. Unlike some biases that fade when people are warned, anchoring largely persists even when participants are told "there will be an anchor in this study and it will bias you — try to correct for it." This is unlike the correction most people imagine: you cannot simply subtract the anchor's influence because you don't know how large it was. You can adjust *some*, but you cannot introspect your way to the unanchored answer. This connects to your broader understanding of cognitive biases as features of system-one processing that aren't fully accessible to deliberate reflection.

The practical implications reach across high-stakes domains. In **negotiations**, the party who names a number first sets an anchor that constrains the bargaining range — knowing this, skilled negotiators deliberately anchor high before compromising. In **retail pricing**, "was $199, now $79" anchors on the original price to make the discount seem larger. In **legal sentencing**, studies show that even prosecutors' randomly assigned sentencing demands shift judges' actual sentences — a disturbing finding given that judicial decisions are supposed to be based on facts and law. In any context where an initial value is presented before a judgment, the cognitive ground is already tilted.

The corrective implications are modest but real. Because adjustment from an anchor is the mechanism, strategies that force reasoning from **multiple reference points** — generating arguments for why the true value might be much higher, much lower, and then synthesizing — produce less anchored estimates than simply "trying to be objective." Similarly, generating your own estimate before seeing any anchor inoculates you better than being told about anchoring after the fact. Knowing about anchoring doesn't make you immune, but it does let you design decision environments that reduce its distorting influence.
