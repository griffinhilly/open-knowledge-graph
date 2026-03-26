---
id: optic-flow-navigation-mst
title: Optic Flow and Navigation in Medial Superior Temporal Area
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: motion-perception-middle-temporal-area
  type: hard
- id: dorsal-stream-reaching-visuomotor-control
  type: hard
builds-toward:
- navigation-neural-basis
- motion-sickness-vestibular-visual-integration
tags:
- optic-flow
- MST
- navigation
- motion
- self-motion
stage: expert
status: validated
---

# Optic Flow and Navigation in Medial Superior Temporal Area

## Core Idea
Medial superior temporal area (MST), receiving input from MT, processes global optic flow patterns that signal self-motion during navigation. MST neurons integrate local motion signals to extract heading direction and self-motion parameters. This computation enables perception of heading and guides smooth pursuit eye movements and heading-directed behavior during self-motion.

## Questions

```yaml
- question: "A person walks forward down a hallway. How does MST compute their heading direction from the visual input?"
  type: multiple-choice
  options:
    - "It tracks the fastest-moving object in the visual field and uses its trajectory as a heading cue"
    - "It locates the focus of expansion — the central point from which all visual elements radiate outward — in the global optic flow field"
    - "It averages the individual motion vectors detected by MT neurons across the visual field"
    - "It relies primarily on vestibular signals from the inner ear, using visual input only as a cross-check"
  answer: 1
  explanation: "The geometric key to heading perception is the focus of expansion: when you move forward, the entire visual field expands outward from a single point that corresponds precisely to where you are heading. MST neurons have large receptive fields and respond selectively to global flow patterns (expansion, contraction, rotation), allowing them to locate this focus. Simply averaging MT vectors (option C) would not isolate the focus; tracking individual objects (option A) is a different strategy; vestibular input (option D) is supplementary, not primary."

- question: "A patient with damage to the right MST has impaired smooth pursuit eye movements. In which direction is pursuit most affected?"
  type: multiple-choice
  options:
    - "Leftward — contralateral to the lesion, consistent with crossed projections"
    - "Rightward — ipsilateral to the lesion, consistent with MST's role in monitoring visual motion during gaze"
    - "Both horizontal directions equally, since pursuit requires bilateral MST coordination"
    - "Vertical directions only, since horizontal pursuit relies on the frontal eye fields"
  answer: 1
  explanation: "MST lesion studies show that smooth pursuit is impaired specifically in the ipsilateral direction — rightward for a right MST lesion. This differs from many other visual cortical areas that show contralateral deficits, and reflects MST's role in processing ipsilateral motion during gaze. This finding confirms MST's dual role in both self-motion perception and gaze control."

- question: "MST neurons process mainly visual motion signals and receive no input from non-visual sensory systems."
  type: true-false
  answer: false
  explanation: "MST also receives vestibular input from the inner ear. This multisensory convergence is functionally significant: when you actually move through the world, optic flow and vestibular signals should agree. When they conflict — such as when watching a large-screen movie where your body is stationary but your visual field mimics forward motion — the mismatch between visual and vestibular signals can produce motion sickness. MST's integration of both modalities is central to coherent self-motion perception."

- question: "The focus of expansion in optic flow is located at the point in the visual field toward which the observer is heading."
  type: true-false
  answer: true
  explanation: "This is the core geometric relationship between optic flow and heading. When you move forward, visual elements in every direction stream away from a central point — this is the focus of expansion, and its location in the visual field directly specifies heading direction. MST neurons compute global optic flow patterns over large receptive fields to identify this focus, enabling the brain to derive heading without requiring knowledge of absolute speed or distance traveled."

- question: "Why can MT alone not provide information about the observer's heading direction, and what computation does MST add?"
  type: short-answer
  answer: "MT neurons respond to local motion — direction and speed in small patches of the visual field. Local motion signals cannot distinguish self-motion from world-motion, and do not reveal the global geometric structure of optic flow. MST integrates MT's local signals across large spatial scales, responding to global flow patterns like radial expansion and contraction. By identifying where the focus of expansion falls in the visual field, MST extracts heading direction — information that no local motion signal can provide on its own."
  explanation: "This is the core hierarchical computation: MT extracts local velocity; MST extracts global structure from those local signals. The analogy is how V1 edge detectors feed into higher areas that extract shapes — each stage derives increasingly abstract properties. Heading perception requires the global level because the diagnostic signal (focus of expansion) is a property of the entire flow field, not any single point in it."
```

## Explainer

From your prerequisites on motion perception in **MT** (middle temporal area) and the dorsal stream's role in visuomotor control, you have the components needed to understand **MST** (medial superior temporal area). MT neurons respond to local motion — small patches of the visual field moving in a particular direction at a particular speed. But local motion signals alone can't distinguish *you* moving through a stationary world from *the world* moving around a stationary you. MST solves this by integrating local motion signals across large visual field regions into global flow patterns that specifically signal **self-motion**.

Think about what your visual field looks like when you walk forward down a hallway. All visual elements expand outward from a single central point — the **focus of expansion** — located where you are heading. Items above that point move upward, items below move downward, items to the left move leftward, all streaming away from the center. This radially expanding pattern of motion vectors is **optic flow**, and its geometry is tightly linked to heading direction. MST neurons have very large receptive fields (sometimes covering entire hemifields) and respond selectively to global flow patterns: **expansion** (moving forward), **contraction** (moving backward), **rotation** (spinning), and **spiral** combinations of these. By computing where the focus of expansion falls in the visual field, the brain can derive heading direction without knowing absolute speed or distance traveled.

The integration across MT and MST exemplifies a **hierarchical processing** strategy that connects directly to your dorsal stream prerequisite. MT extracts local velocity — direction and speed at each point. MST integrates these local signals over large spatial scales to extract global structure. This parallels how primary visual cortex extracts oriented edges that higher areas combine into shapes: each processing stage derives increasingly abstract properties from the signals below. MST also receives **vestibular input** from the inner ear, which matters because when your body actually moves, both visual optic flow and vestibular motion signals should agree. When they conflict — as on a stationary flight simulator with moving visual displays, or while watching a large-screen film — the mismatch between visual and vestibular signals can produce **motion sickness**.

MST also contributes to **smooth pursuit eye movements** — tracking a moving target by smoothly rotating the eyes to keep it on the fovea. Lesions to MST impair pursuit specifically in the direction ipsilateral to the lesion, consistent with its role in monitoring visual motion during gaze. This dual function in both self-motion perception and eye movement control illustrates the broader mandate of the dorsal stream: providing the brain with real-time motion information needed to guide a moving body through a moving world.
