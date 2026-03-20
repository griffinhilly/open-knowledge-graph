---
id: spatial-representation-maps
title: Spatial Representation, Maps, and Cartography
domain: social-sciences
course: human-geography
prerequisites:
- id: spatial-scale-human-geography
  type: hard
builds-toward:
- political-territory-power
tags:
- representation
- cartography
- maps
- visualization
- power
stage: abstract-reasoning
status: draft
---

# Spatial Representation, Maps, and Cartography

## Core Idea
Maps are powerful tools for representing space, but they are never neutral—they necessarily select, simplify, and interpret reality. Map-making involves political choices about what to show, how to show it, and from whose perspective. Critical cartography examines how representations shape geographic understanding and serve particular interests.

## Questions

```yaml
- question: "The Mercator projection has been standard in Western classrooms for centuries. Which of the following best explains why critical cartographers consider this problematic?"
  type: multiple-choice
  options:
    - "The Mercator projection is mathematically incorrect and should be replaced with accurate ones"
    - "It exaggerates the size of high-latitude areas, making Europe and North America appear much larger than they are, encoding a Eurocentric worldview as objective fact"
    - "The Mercator projection is valid only for navigation and should never be used in educational contexts"
    - "Modern digital maps have corrected for Mercator distortion, so the historical problem no longer applies"
  answer: 1
  explanation: "The explainer notes that Greenland appears roughly equal in size to Africa on Mercator maps, while Africa is actually about 14 times larger. This isn't just a technical inaccuracy — Mercator preserves navigational angles correctly for its stated purpose. The problem is that it aligned conveniently with colonial powers who wanted the world organized around their perspective, and presenting it as the default 'objective' map encodes that perspective invisibly."

- question: "Colonial-era maps of densely populated indigenous territories frequently depicted them as 'terra nullius' (empty land). What does this illustrate about mapmaking?"
  type: multiple-choice
  options:
    - "Mapmakers lacked the technology to survey population density in distant territories accurately"
    - "Maps are political arguments about what exists and matters — inclusion and omission are never neutral choices"
    - "Indigenous peoples did not have established territorial boundaries that could be represented cartographically"
    - "Maps serve purely descriptive functions and cannot make claims about territory or ownership"
  answer: 1
  explanation: "The explainer states: 'What a map includes defines what exists and matters; what it omits is rendered invisible or marginal.' Terra nullius maps weren't neutral descriptions — they were arguments that provided cartographic justification for seizure and settlement. The populations were erased from the map before being displaced from the land. This is critical cartography's central insight: maps are instruments of power, not mirrors of reality."

- question: "Every map projection necessarily distorts at least one spatial property — area, shape, distance, or direction — because a sphere cannot be perfectly flattened."
  type: true-false
  answer: true
  explanation: "This is the fundamental geometric constraint of cartography. Flattening a sphere without tearing or compressing it is mathematically impossible — every projection must make tradeoffs. Mercator preserves angles (useful for navigation) but distorts area. Equal-area projections preserve area but distort shape. There is no perfect projection, only choices about which distortion to accept — and those choices encode values about what matters."

- question: "The choice of map scale is a purely technical decision with no political implications."
  type: true-false
  answer: false
  explanation: "The explainer explicitly addresses this: scale is 'simultaneously a technical parameter and a political choice.' Large-scale maps reveal granular detail — block-by-block demographic variation, informal settlements, fine-grained community structure — that vanishes at national scale. Decisions about scale shape what solutions become thinkable: urban renewal plans made from national-scale maps can miss community structure visible up close; global climate agreements made without local-scale maps can miss who is actually at risk."

- question: "Why is asking 'who made this map and for what purpose' just as important as asking 'is this map accurate'?"
  type: short-answer
  answer: "Because technical accuracy is only one dimension of how a map can mislead. A map can be geometrically accurate while still omitting populations, using politically loaded place names, applying a projection that inflates certain territories, or framing a scale that makes some problems visible while hiding others. The maker's purpose shapes all these choices — and a map made to justify colonial land seizure and a map made for indigenous rights advocacy might both use accurate coordinates while telling opposite stories about the same territory."
  explanation: "Critical cartography's central insight is that 'a map that appears objective is always an argument about what matters in space.' Geographic literacy therefore requires reading both the map and the conditions of its production — projection, scale, inclusion, omission, naming, and perspective. Treating a map as a neutral mirror rather than a situated argument is itself a political act."
```

## Explainer

You've already learned how the choice of spatial scale shapes what geographic patterns become visible. Maps are the technology that makes spatial representation shareable — but every technical decision in mapmaking is also an interpretive decision, and interpretation is never neutral. Understanding this is the gateway from reading maps to reading maps *critically*.

Start with the unavoidable technical constraint: **projection**. A projection is a method of representing Earth's curved surface on a flat plane, and every projection distorts something — area, shape, distance, or direction — because you cannot flatten a sphere without tearing or compressing it. The Mercator projection, standard in Western classrooms for centuries and still the default for many web maps, preserves navigational angles but dramatically exaggerates the size of high-latitude areas. Greenland appears roughly equal in size to Africa on a Mercator map; Africa is actually about fourteen times larger. This wasn't a neutral technical choice — it also placed Europe visually at the center and made it appear large, which aligned conveniently with colonial powers who were the map's primary users and who wanted the world organized around their perspective.

**Critical cartography** examines these choices as political acts rather than neutral conventions. What a map includes defines what exists and matters; what it omits is rendered invisible or marginal. Colonial-era maps of Africa and the Americas frequently depicted vast territories as "terra nullius" — empty land — even when densely populated, providing a cartographic justification for seizure and settlement. Contemporary maps encode political choices too: whether to show contested borders as settled, which place names to use (the colonizer's names or indigenous names), whose infrastructure appears (highways yes; informal settlements often no), and which hazards or resources are emphasized for whose benefit.

**Scale** is simultaneously a technical parameter and a political choice. Mapping a neighborhood at large scale reveals granular detail — individual streets, buildings, block-by-block demographic variation — that disappears at national scale. Decisions about which scale to use for which problem shape what solutions become thinkable: urban renewal decisions made from national-scale maps can miss the fine-grained community structure that would be visible up close; global climate agreements made without local-scale vulnerability maps can miss who is actually at risk. Geographic literacy therefore requires asking, of every map: who made this, for what purpose, using what projection and scale, and what has been left off? A map that appears objective is always an argument about what matters in space — and like all arguments, it can be contested.
