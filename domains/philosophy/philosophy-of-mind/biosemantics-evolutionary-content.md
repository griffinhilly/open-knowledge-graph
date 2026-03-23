---
id: biosemantics-evolutionary-content
title: 'Biosemantics: Evolutionary Grounding of Content'
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: intentionality
  type: hard
- id: teleosemantics-meaning
  type: hard
builds-toward:
- content-externalism-individuation
- representationalism
tags:
- semantics
- evolution
- function
- intentionality
- representation
stage: formal-systems
status: validated
---

# Biosemantics: Evolutionary Grounding of Content

## Core Idea
Biosemantics grounds mental content in evolutionary history: neural representations have their specific content because evolution selected for organisms using those representations to solve adaptive problems. Your fear response represents danger because natural selection favored ancestors whose fear representations accurately tracked genuine threats.

## How It's Best Learned
Trace a specific behavioral example (like a frog's snap response to flies) and ask: what makes that neural trigger 'about' flies? Evolution is the answer.

## Common Misconceptions
Thinking biosemantics requires full-blooded intentionality; confusing adaptive function with conscious purpose; assuming non-evolved systems cannot have content.

## Questions

```yaml
- question: "A researcher throws a small dark pellet into a frog's enclosure. The frog's fly-detection mechanism fires and the frog snaps at the pellet. According to biosemantics, what does this neural state represent, and why?"
  type: multiple-choice
  options:
    - "It represents 'small dark moving object' — because that is the proximate cause of the firing in this token case"
    - "It represents 'fly' — because ancestral frogs were selected for having this mechanism track flies; fly-tracking is its proper function regardless of what triggered this particular firing"
    - "It represents nothing, because the mechanism misfired and content requires accurate tracking"
    - "It represents whatever the frog most frequently encounters in its current environment"
  answer: 1
  explanation: "Biosemantics grounds content in selectional history, not in token-level causal relations. The mechanism was selected because ancestors whose mechanism fired in response to flies caught more flies and reproduced more successfully — 'fly' is its proper function. In this case the mechanism fires in response to a pellet, which is a token malfunction, not a change in content. The content stays 'fly' (determined by history) while the representation is incorrect (the token firing is a case of misrepresentation). This is precisely how biosemantics handles misrepresentation: content tracks proper function, not actual performance."

- question: "A philosopher objects: 'Biosemantics cannot explain misrepresentation — if a neural state represents whatever it was selected to track, and it fires, then by definition it is tracking what it represents and cannot be wrong.' What is the correct biosemantic reply?"
  type: multiple-choice
  options:
    - "The philosopher is right — biosemantics cannot adequately explain misrepresentation"
    - "Biosemantics distinguishes proper function (determined by selectional history) from actual performance (what the mechanism does in a given token case); misrepresentation occurs when the mechanism fires but fails to fulfill its proper function — when the trigger is not what the mechanism was selected to track"
    - "Misrepresentation is impossible in evolved biological systems; only artifact representations can be mistaken"
    - "A neural state can only misrepresent if the organism consciously believes something false"
  answer: 1
  explanation: "The biosemantic account of misrepresentation turns on the gap between proper function and actual performance. A heart has the proper function of pumping blood; a defective heart that fails to pump is malfunctioning, not redefining what hearts are 'supposed to do.' Similarly, the frog's mechanism has the proper function of firing in response to flies; when it fires at a pellet, the mechanism malfunctions — the representation is 'fly' but is incorrect in this case. Misrepresentation is the gap between what the mechanism is for and what it actually responds to. This gap is what gives content its correctness conditions."

- question: "On the biosemantics view, a neural state represents X because X is what reliably causes that state to fire in the organism's current environment."
  type: true-false
  answer: false
  explanation: "This is a description of a causal/informational theory of content, not biosemantics. On biosemantics, content is grounded in evolutionary selectional history — what the mechanism was selected for — not in current causal regularities. This distinction is crucial precisely for handling misrepresentation: if content were fixed by what currently causes firing, the frog's mechanism would represent 'pellet' after enough pellet encounters. Biosemantics insists the content remains 'fly' because that is what shaped the mechanism's evolution, not what happens to trigger it now."

- question: "A brain spontaneously assembled by a cosmic coincidence with an identical physical structure to a human brain would have the same mental content as a human brain, according to strict biosemantics."
  type: true-false
  answer: false
  explanation: "This thought experiment (a variant of the 'swamp person' case) is a direct challenge to biosemantics. The spontaneously assembled brain has no evolutionary history — its physical states have no proper functions because nothing was selected for. On the strict biosemantic view, proper function requires historical selectional processes, and without that history there are no proper functions and therefore no grounded content. The brain might behave exactly like a human brain, but on this view its internal states would not genuinely represent anything. Critics use this implication to challenge biosemantics; defenders either accept it or extend 'proper function' to include derived functions from learning and design."

- question: "Why is misrepresentation considered a crucial test case for any theory of mental content, and how does biosemantics explain it using the concept of evolutionary proper function?"
  type: short-answer
  answer: "Misrepresentation is crucial because it is constitutive of having content at all: if a state can only 'represent' what actually caused it, it cannot be wrong, and a state that cannot be wrong is not really representing anything. Any adequate theory of content must explain how a representation can occur in the absence of — or contrary to — what it represents. Biosemantics explains this by separating what a mechanism was selected to track (proper function, determining content) from what it happens to track in a given token case (actual performance). The frog's fly-detector has the content 'fly' because that is its proper function; when it fires at a pellet, the mechanism is performing below its proper function — it is genuinely representing fly (incorrectly) rather than successfully representing pellet."
  explanation: "The proper function framework provides the gap needed for misrepresentation: content is fixed by history (selectional function), but performance varies by case. Error is the failure of a mechanism to fulfill its proper function in a given instance. This gives biosemantics a principled account of false beliefs, perceptual illusions, and other cases where mental states fail to accurately represent their objects — which is essential for any realistic theory of mind."
```

## Explainer

From your prerequisite work on **intentionality** and **teleosemantics**, you know the core puzzle: mental states are *about* things — beliefs, desires, and perceptions have content that can be true or false, satisfied or unsatisfied, accurate or inaccurate. But the physical world seems to just consist of particles, fields, and causal processes — none of which are "about" anything. How does **content** enter a purely physical system? Biosemantics, developed primarily by Ruth Millikan and Fred Dretske, answers: through evolutionary history.

The central move is to ground content in **biological function**. A heart has the function of pumping blood — not because it actually pumps blood (a defective heart doesn't), but because pumping blood is what hearts were *selected for* over evolutionary history. Hearts that pumped blood reproduced better than hearts that didn't, so pump-blood became the heart's proper function. Biosemantics applies this same logic to neural representations: a mental state has the content *X* because it was selected for being caused by X-type situations and because its proper function is to respond to Xs. The frog's fly-detection mechanism has the content "fly" because ancestors whose mechanism fired in response to flies (rather than pellets or other small moving objects) caught more flies and reproduced more successfully.

This explains a key asymmetry: **misrepresentation**. For content to exist at all, it must be possible to get things wrong — a representation of X can occur even when no X is present. Many rival theories of content struggle to account for this. On biosemantics, misrepresentation is natural: the frog's mechanism can fire when presented with a small dark pellet, which is a malfunction — a case where the mechanism fails to perform its proper function. The content remains "fly" (because that's what the mechanism was selected to track), but the representation is incorrect in this token case. Misrepresentation is just the gap between proper function and actual performance.

The power and limits of the view become clear by examining the **selectional history requirement**. Biosemantics implies that content is constitutively tied to evolutionary history — something with no evolutionary past (a brain spontaneously formed from a cosmic coincidence, or an early artificial system) would have no genuine content on the strictest reading of the view. Defenders respond that "derived" functions from design or learning can also ground content; critics press that the appeal to selection is doing mysterious work. Understanding these tensions prepares you for the content externalism and representationalism debates this course builds toward, where the question is not just what grounds content, but whether content is determined by factors inside or outside the organism.
