---
id: naturalizing-intentionality
title: Naturalizing Intentionality
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: intentionality
  type: hard
- id: physicalism-about-mind
  type: hard
tags:
- teleosemantics
- Dretske
- Millikan
- informational-semantics
- naturalism
- mental-content
stage: formal-systems
status: validated
---

# Naturalizing Intentionality

## Core Idea
The project of naturalizing intentionality seeks to explain how physical systems can have mental states that are about things, using only the resources of the natural sciences — no irreducible mental notions allowed. Informational semantics (Dretske) holds that a mental state represents what it reliably carries information about: a neural state means 'there is a fly' if it is reliably caused by the presence of flies. The disjunction problem arises immediately: since the frog's detector also fires for BBs and shadows, it seems to represent the disjunction 'fly or BB or shadow.' Teleosemantics (Millikan) addresses this by appealing to biological function: the detector's content is 'fly' because that is what it was selected for by evolution. Fodor's asymmetric dependency theory offers another route: the fly-to-detector connection is basic, and the BB-to-detector connection depends on and is parasitic upon it.

## How It's Best Learned
Start with the basic puzzle: a thermometer 'represents' temperature, but we do not think it has genuine intentionality. What would need to be added? Then work through each naturalization strategy (information, teleology, asymmetric dependence) and its specific vulnerabilities. Dretske's Knowledge and the Flow of Information and Millikan's Language, Thought, and Other Biological Categories are the foundational texts.

## Common Misconceptions
- Naturalizing intentionality is not the same as denying that intentionality exists; it is the attempt to show that aboutness is a natural phenomenon explicable in physical and biological terms.
- Teleosemantics does not claim that all meaning is biological; it uses evolutionary function as a model for the kind of normativity that distinguishes correct from incorrect representation.

## Questions

```yaml
- question: "A frog's fly-detector fires in response to a small dark moving pellet (a BB). A student using informational semantics concludes: 'Since the BB caused the firing, the detector's content in this instance is BB.' What problem with informational semantics does this expose?"
  type: multiple-choice
  options:
    - "Informational semantics requires conscious awareness, which frogs lack"
    - "The disjunction problem: since the detector fires for flies, BBs, and shadows alike, informational semantics cannot determine whether the content is 'fly,' 'BB,' or 'fly-or-BB-or-shadow' — the causal story alone cannot select one content over the others"
    - "The BB caused the firing by mistake, so this case should be excluded from the analysis"
    - "Informational semantics only applies to human perceptual systems, not animal neural states"
  answer: 1
  explanation: "The disjunction problem arises because any physical detector fires in response to a range of stimuli, not just the 'intended' one. Informational semantics defines content in terms of reliable causal connection — but the frog's detector is reliably caused by flies AND by small dark blobs AND by BBs. There is no purely causal basis to choose 'fly' as the content rather than 'small dark moving blob.' This is the central vulnerability of informational semantics: it cannot solve misrepresentation without invoking additional non-causal resources."

- question: "How does teleosemantics resolve the disjunction problem that challenges informational semantics?"
  type: multiple-choice
  options:
    - "By requiring that the detector only fire for the single stimulus it was trained on"
    - "By using statistical frequency of different causes to determine the 'real' content"
    - "By appealing to evolutionary function — the content is fixed by what the mechanism was selected over evolutionary history to detect, not by what currently triggers it"
    - "By defining content as the organism's behavioral output rather than the cause of the internal state"
  answer: 2
  explanation: "Teleosemantics shifts from causal history to biological function. The frog's detector was shaped by natural selection because it reliably triggered fly-catching behavior that caught actual flies — not BBs or shadows. Evolution is the normative source: the content is 'fly' because that is what the mechanism was designed (by selection) to detect. Crucially, this allows misrepresentation: a BB-induced firing is a misfiring — the detector represents a fly incorrectly, not a BB correctly. Function, not current causation, determines content."

- question: "On teleosemantics, a frog's fly-detector can represent 'fly' even when it is triggered by a BB, because content is determined by biological function rather than current causal trigger."
  type: true-false
  answer: true
  explanation: "This is the key distinction teleosemantics introduces between being triggered by something and representing something. The detector was shaped by evolution to respond to flies; a BB-induced firing is a misfiring — the detector is mistakenly treating the BB as a fly. This allows teleosemantics to make sense of misrepresentation, which purely causal theories struggle with: if content is just 'whatever causes the state,' there can be no error. Teleosemantics introduces a normative standard (what the mechanism is supposed to detect) that makes error possible."

- question: "Naturalizing intentionality means arguing that intentionality — the 'aboutness' of mental states — does not really exist."
  type: true-false
  answer: false
  explanation: "Naturalizing intentionality is not eliminativist — it does not deny that intentionality exists. It accepts intentionality as a real phenomenon and attempts to explain it entirely within the resources of natural science (physics, biology, causal laws), without invoking irreducibly mental notions. The project is reductive, not eliminativist: it aims to show that aboutness is a natural property that physical systems can have."

- question: "What is the disjunction problem, and why does it challenge informational semantics specifically rather than teleosemantics?"
  type: short-answer
  answer: "The disjunction problem: any physical detector is triggered by multiple stimuli (fly, BB, shadow), so purely causal accounts cannot determine whether the state's content is 'fly,' 'BB,' or the disjunction 'fly-or-BB-or-shadow' — all are reliably causally connected to the firing. Informational semantics is vulnerable because it grounds content entirely in reliable causal connection and has no further resource to privilege one description over another. Teleosemantics escapes the problem by asking not 'what causes this state?' but 'what was this mechanism selected by evolution to detect?' — evolution selected the frog's detector for fly-catching, so the content is 'fly' regardless of what happens to trigger it on any given occasion."
  explanation: "The disjunction problem reveals that causal co-variation alone is insufficient to fix mental content — there are always too many possible descriptions of the cause. Any successful naturalization of intentionality needs a way to privilege one content description over others. Teleosemantics does this via evolutionary history; Fodor's asymmetric dependence theory does it via the logical structure of counterfactual dependencies. Both are attempts to find a natural fact that does the normative work of selecting content."
```

## Explainer

You know from your study of intentionality that mental states have the remarkable property of being **about** things — a belief is about the election, a desire is about coffee, a perception is about the red apple in front of you. You also know from physicalism that the brain is a physical system describable in terms of neurons, electrochemical signals, and causal mechanisms. The project of naturalizing intentionality is the attempt to bridge these two: to explain, in purely physical and biological terms, how it is possible for a physical state to be about anything at all.

The challenge is sharpest when you consider a simple case. A thermometer's reading tracks temperature — the mercury rises when temperature rises. In that sense, the thermometer's position carries **information** about temperature. Fred Dretske proposes building mental content on this foundation: a neural state means 'there is a fly' if it reliably carries information about flies — if it is caused by flies across a range of circumstances. This is **informational semantics**, and it captures the intuitive idea that representation is a kind of natural tracking. The thermostat tracks temperature; the frog's retinal state tracks flies.

But the **disjunction problem** immediately threatens this account. The frog's fly-detector also fires for small dark blobs moving on a light background — BBs, pellets, even optical illusions. So what does the detector state mean? 'Fly'? 'Small dark blob'? 'Fly or BB or shadow'? The information-theoretic account cannot cleanly select one content over the others, because the state is caused by all of them. Ruth Millikan's **teleosemantics** addresses this by invoking biological function. The question is not what the state is caused by, but what it was *selected for* over evolutionary history. The frog's detector was shaped by selection because it reliably triggered fly-catching behavior that caught flies — not BBs. So the content is 'fly,' because that is what the mechanism was designed by evolution to detect. This introduces a crucial distinction: a detector can be *triggered* by a non-fly while still *representing* a fly — because representing, on this view, is about function, not just causal history.

Jerry Fodor's **asymmetric dependence theory** takes a different route, staying closer to causal information while addressing the disjunction problem. The key insight is that the 'BB causes detector to fire' connection is not independent — it depends on and is asymmetrically parasitic on the 'fly causes detector to fire' connection. If there were no flies, BBs would not cause firings (because the detector would never have developed); but even if there were no BBs, flies would still cause firings. Genuine content is fixed by the basic, non-derivative causal connection. Each of these strategies tries to locate, in purely natural terms, the normativity that distinguishes correct from incorrect representation — what the state is supposed to represent, even when it misfires. Whether any of them fully succeeds remains one of the deepest open questions in philosophy of mind.
