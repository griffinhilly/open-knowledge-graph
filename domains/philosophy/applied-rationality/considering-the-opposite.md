---
id: considering-the-opposite
title: "Considering the Opposite"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: debiasing-techniques
    type: hard
  - id: motivated-reasoning
    type: hard
  - id: confirmation-bias
    type: soft
builds-toward:
  - steelmanning
  - intellectual-humility-and-calibrated-uncertainty
tags: ["debiasing", "confirmation-bias", "technique", "critical-thinking"]
stage: advanced
status: draft
---

## Core Idea

Considering the opposite is the most robust single debiasing technique in the experimental literature. When you catch yourself leaning toward a conclusion, deliberately generate reasons why the opposite conclusion might be true. Lord, Lepper, and Preston (1984) showed that this technique significantly reduces confirmation bias and belief perseverance. It works because confirmation bias is partly a search problem — we naturally search for confirming evidence and stop, but considering the opposite forces a search for disconfirming evidence. The technique is most powerful when applied before commitment to a position, and when the opposite-case arguments are taken seriously rather than treated as a formality.

## How It's Best Learned

Practice with a belief you hold with moderate confidence. Write three strong arguments for it, then force yourself to write three strong arguments against it. Notice whether the exercise changes your confidence — if it does, you were underweighting available counterevidence.

## Common Misconceptions

- Considering the opposite is not the same as playing devil's advocate casually — it requires genuinely engaging with the strongest counterarguments.
- This technique does not mean all positions are equally valid — it means you should check whether your position survives serious scrutiny before committing.

## Explainer

From your work on debiasing techniques, you know that awareness of a bias is insufficient to correct it -- specific procedural countermeasures are required. From motivated reasoning, you know that desires and identity can steer your reasoning toward predetermined conclusions without your conscious awareness. Considering the opposite is the single most effective technique for counteracting these failures, and it works because it targets the right cognitive mechanism.

Confirmation bias is partly a **search problem**. When you form a hypothesis, your mind naturally searches for evidence that confirms it and stops searching once enough confirmation is found. You do not deliberately ignore counterevidence -- you simply never go looking for it. The search terminates early, leaving a skewed evidence set. Considering the opposite intervenes at exactly this point: by forcing you to generate reasons why the opposite conclusion might be true, it launches a second search -- one that targets the disconfirming evidence your initial search never retrieved. Lord, Lepper, and Preston's 1984 study demonstrated that this simple technique significantly reduces confirmation bias and belief perseverance, outperforming vague instructions to "be objective" or "consider all the evidence."

In practice, the technique is straightforward but requires genuine engagement. When you catch yourself leaning toward a conclusion -- that a job candidate is the right hire, that a business strategy will work, that a political position is correct -- pause and deliberately generate the strongest reasons why the opposite might be true. Not weak, easily dismissed reasons, but the actual considerations that a smart person on the other side would raise. If you are evaluating a job candidate and leaning toward hiring, ask: what would a thoughtful person who wants to reject this candidate say? What evidence in the resume or interview supports that view? The exercise is most powerful when done before you have publicly committed to a position, because once commitment hardens, the psychological cost of reversing course amplifies motivated reasoning.

The critical distinction is between considering the opposite as a genuine inquiry and treating it as a formality. A perfunctory "well, I suppose the other side might say X, but that's obviously wrong" is not the technique working -- it is the technique being co-opted by the same confirmation bias it is meant to counter. The real test is whether the exercise changes your confidence. If you consider the opposite seriously and return to your original belief with unchanged confidence, that is a legitimate outcome -- your position survived scrutiny. But if you find that the counterarguments are stronger than you expected, that shift in confidence is exactly the kind of evidence you were missing. The technique succeeds not by changing your mind every time, but by ensuring your conclusions survive the challenge they would face from the best available counterevidence.

## Questions

```yaml
- question: "A physician forms an early diagnosis of pneumonia and then reviews the patient's history. She unconsciously attends to symptoms consistent with pneumonia and passes quickly over those that might suggest a different cause. Which intervention would most directly address this bias according to the experimental literature?"
  type: multiple-choice
  options:
    - "Review the patient's chart a second time without any hypothesis in mind"
    - "Deliberately generate specific reasons why the diagnosis might be wrong before committing to it"
    - "Ask a colleague to confirm the diagnosis to get a second opinion"
    - "Slow down and consciously try to be more objective when reading the chart"
  answer: 1
  explanation: "Considering the opposite works because confirmation bias is a search problem — we naturally stop searching once we find confirming evidence. Deliberately generating reasons why the diagnosis might be *wrong* forces a targeted search for disconfirming evidence that the biased search would skip. Option A (reviewing without a hypothesis) doesn't solve the search problem. Option C (a colleague) helps but is external. Option D ('trying to be objective') is ineffective precisely because the bias operates outside awareness — the technique must be deliberate and structured."

- question: "According to Lord, Lepper, and Preston (1984), why does considering the opposite reduce confirmation bias rather than just making people feel they've been balanced?"
  type: multiple-choice
  options:
    - "It activates the prefrontal cortex, which suppresses emotional reasoning"
    - "It forces a structured search for disconfirming evidence that the biased search would otherwise not generate"
    - "It slows down thinking, giving more time for careful evaluation of all evidence"
    - "It reverses the order of evidence presentation, which reduces anchoring effects"
  answer: 1
  explanation: "Confirmation bias is partly a search termination problem: we stop collecting evidence once we have enough to confirm our hypothesis. Considering the opposite forces us to search the same evidence space looking for disconfirmation — a qualitatively different search that reveals evidence we would otherwise stop short of finding. Slowing down (option C) by itself doesn't change what you look for, only how long you look. The technique's power comes from redirecting the search, not from adding processing time."

- question: "Considering the opposite is most powerful when applied after you have already committed to a position, because commitment forces you to take the counterarguments seriously."
  type: true-false
  answer: false
  explanation: "The technique is most powerful when applied *before* commitment. Once you have committed — publicly, emotionally, or socially — motivated reasoning intensifies and you are more likely to treat counterarguments as obstacles to neutralize rather than information to genuinely evaluate. Lord, Lepper, and Preston found that considering the opposite significantly reduced belief perseverance specifically when applied before positions hardened. Applying it after commitment can still help, but the resistance is higher and the effect is smaller."

- question: "A person who carefully considers the opposite and then returns to their original belief with the same confidence has failed to apply the technique correctly."
  type: true-false
  answer: false
  explanation: "The goal of considering the opposite is not to change your mind — it is to check whether your position survives serious scrutiny. If the counterarguments you generate are genuinely weak relative to the arguments for your position, returning to it with unchanged confidence is the correct outcome. The technique has succeeded if you engaged seriously with the strongest opposing case. Failure would be dismissing the counterarguments without genuine engagement, or treating the exercise as a formality to be completed before reasserting your original view."

- question: "Why is confirmation bias described as partly a 'search problem,' and how does considering the opposite address it at the level of cognitive mechanism?"
  type: short-answer
  answer: "Confirmation bias leads people to search for evidence that confirms their existing hypothesis and stop once sufficient confirmation is found — they never search the space of disconfirming evidence. The bias is not only about how we *evaluate* evidence we encounter; it's about which evidence we go looking for. Considering the opposite addresses this by forcing a second, deliberate search targeting the opposite conclusion — generating arguments and evidence for why the current belief might be wrong. This populates the mental evidence set with disconfirming information that the original biased search would never have retrieved."
  explanation: "This is the key mechanistic insight: if you only fix how you *weigh* evidence, you still miss evidence you never looked for. Considering the opposite changes the search itself, not just the evaluation. This is why vague instructions to 'be more objective' are ineffective — they address evaluation but not search. The technique's success in Lord et al.'s experiments came precisely from redirecting the search process."
```
