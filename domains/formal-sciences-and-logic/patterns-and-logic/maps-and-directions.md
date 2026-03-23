---
id: maps-and-directions
title: Maps and Directions
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: ordinal-reasoning
  type: hard
builds-toward:
- visual-puzzles
tags:
- spatial-reasoning
- maps
- directions
- navigation
stage: concrete-operations
status: validated
---

# Maps and Directions

## Core Idea
Maps represent real-world spaces in a simplified, bird's-eye view. Reading a map requires translating between the map's abstract representation and the real space it depicts. Giving and following directions requires precise spatial language: left, right, north, south, forward, backward, how far, which turn. Maps and directions combine spatial reasoning with logical precision — every direction must be clear and unambiguous, and every step must be in the correct order. This is spatial thinking meets algorithmic thinking.

## How It's Best Learned
Start with maps of familiar spaces: the classroom, the school, the neighborhood. Have students give directions from one location to another and follow each other's directions to verify accuracy. Introduce grid maps where locations are at intersections and directions involve "go 3 blocks east, then 2 blocks north." Include compass directions (north, south, east, west) alongside relative directions (left, right, forward). Have students create maps of imaginary places and write directions between landmarks.

## Common Misconceptions
- Confusing left and right when facing different directions — "turn left" depends on which way you are facing, not a fixed direction on the map.
- Thinking maps show everything — maps are selective representations that simplify reality.
- Confusing compass directions with relative directions — north is always the same direction regardless of which way you face, but left and right change.
- Not giving distances or step counts — "go forward" is ambiguous without specifying how far.

## Questions

```yaml
- question: "You are facing north. Someone tells you to turn right. Which direction are you now facing?"
  type: multiple-choice
  options:
    - "South"
    - "East"
    - "West"
    - "Still north"
  answer: 1
  explanation: "If you face north and turn right (clockwise), you face east. This is because the compass directions go clockwise: north → east → south → west. Relative directions (left/right) depend on which way you face. Compass directions (north/south/east/west) do not. Understanding the relationship between these two systems is central to map reading."

- question: "Two people give directions to the same place. Person A says 'Go 3 blocks north, then 2 blocks east.' Person B says 'Go 2 blocks east, then 3 blocks north.' Do they arrive at the same place?"
  type: true-false
  answer: true
  explanation: "On a grid, going 3 north then 2 east reaches the same point as going 2 east then 3 north — the total displacement is the same. However, the PATHS are different (they walk different routes). This is an important distinction: the order of perpendicular movements does not change the destination, but it does change the route. For non-perpendicular movements or one-way streets, order might matter more."

- question: "Why are compass directions (north, south, east, west) more reliable than relative directions (left, right) for giving directions?"
  type: multiple-choice
  options:
    - "Compass directions are shorter words"
    - "Compass directions are fixed regardless of which way you face, while left and right change depending on your orientation"
    - "Left and right are not real directions"
    - "Compass directions are only used on maps, not in real life"
  answer: 1
  explanation: "If you face north, 'east' is to your right. If you turn around and face south, 'east' is now to your left — but east is still east. Compass directions are absolute (fixed relative to the Earth), while left/right are relative (depend on which way you face). This is why maps use compass directions — they are unambiguous regardless of the reader's orientation."

- question: "How is giving clear directions similar to writing a good algorithm?"
  type: short-answer
  answer: "Both require precise, ordered, complete instructions that someone can follow without guessing. A good algorithm says exactly what to do at each step, in what order, with no ambiguity. Good directions do the same: 'Walk 2 blocks north, turn right, walk 1 block east, the building is on your left.' Each step is specific (2 blocks, not 'a little way'), ordered (north first, then turn, then east), and complete (includes when to stop). Vague directions ('go that way for a while') fail for the same reason vague algorithms fail — they require guessing."
  explanation: "This connection reinforces the algorithmic thinking thread running through the course. Directions are a spatial algorithm — a step-by-step procedure for navigating space. Students who see this connection understand that algorithmic thinking is not limited to math or computers; it applies to any task that requires sequential, precise instructions."
```

## Explainer

You have been learning about sequences and ordinal reasoning — the idea that order matters. Now you are going to apply that to the physical world: **maps and directions**. Giving directions is like writing an algorithm for movement through space.

A **map** is a simplified picture of a real place, seen from above (a bird's-eye view). It shows where things are relative to each other: the school is north of the park, the library is east of the school. Maps use symbols, colors, and labels to represent real-world features. The key skill is **translation**: converting between the map (a flat picture) and the real space (where you actually walk around).

**Directions** are the algorithm for getting from one place to another. Like any algorithm, they must be ordered, specific, and complete. "Walk two blocks north, turn right on Oak Street, walk one block, the library is on your left" — each step tells you exactly what to do, in what order. Miss a step or do them out of order, and you end up in the wrong place.

There are two kinds of directional language, and understanding both is important. **Relative directions** — left, right, forward, backward — depend on which way you are facing. If you face north, right is east. If you turn around and face south, right is west. Same word, different directions. **Compass directions** — north, south, east, west — are fixed. East is always east, no matter which way you face. Compass directions are more reliable for giving directions because they do not change with orientation.

Maps and directions combine spatial reasoning with logical precision. Every direction is an instruction that must be clear and unambiguous. Every step must come in the right order. Every landmark or turn must be correctly placed. This is the same discipline required for algorithms and logical arguments — the difference is that here, the "steps" happen in physical space rather than on paper.
