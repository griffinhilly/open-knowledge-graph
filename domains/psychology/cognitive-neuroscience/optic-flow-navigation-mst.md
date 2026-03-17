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
stage: advanced
status: draft
---

# Optic Flow and Navigation in Medial Superior Temporal Area

## Core Idea
Medial superior temporal area (MST), receiving input from MT, processes global optic flow patterns that signal self-motion during navigation. MST neurons integrate local motion signals to extract heading direction and self-motion parameters. This computation enables perception of heading and guides smooth pursuit eye movements and heading-directed behavior during self-motion.

## Explainer

From your prerequisites on motion perception in **MT** (middle temporal area) and the dorsal stream's role in visuomotor control, you have the components needed to understand **MST** (medial superior temporal area). MT neurons respond to local motion — small patches of the visual field moving in a particular direction at a particular speed. But local motion signals alone can't distinguish *you* moving through a stationary world from *the world* moving around a stationary you. MST solves this by integrating local motion signals across large visual field regions into global flow patterns that specifically signal **self-motion**.

Think about what your visual field looks like when you walk forward down a hallway. All visual elements expand outward from a single central point — the **focus of expansion** — located where you are heading. Items above that point move upward, items below move downward, items to the left move leftward, all streaming away from the center. This radially expanding pattern of motion vectors is **optic flow**, and its geometry is tightly linked to heading direction. MST neurons have very large receptive fields (sometimes covering entire hemifields) and respond selectively to global flow patterns: **expansion** (moving forward), **contraction** (moving backward), **rotation** (spinning), and **spiral** combinations of these. By computing where the focus of expansion falls in the visual field, the brain can derive heading direction without knowing absolute speed or distance traveled.

The integration across MT and MST exemplifies a **hierarchical processing** strategy that connects directly to your dorsal stream prerequisite. MT extracts local velocity — direction and speed at each point. MST integrates these local signals over large spatial scales to extract global structure. This parallels how primary visual cortex extracts oriented edges that higher areas combine into shapes: each processing stage derives increasingly abstract properties from the signals below. MST also receives **vestibular input** from the inner ear, which matters because when your body actually moves, both visual optic flow and vestibular motion signals should agree. When they conflict — as on a stationary flight simulator with moving visual displays, or while watching a large-screen film — the mismatch between visual and vestibular signals can produce **motion sickness**.

MST also contributes to **smooth pursuit eye movements** — tracking a moving target by smoothly rotating the eyes to keep it on the fovea. Lesions to MST impair pursuit specifically in the direction ipsilateral to the lesion, consistent with its role in monitoring visual motion during gaze. This dual function in both self-motion perception and eye movement control illustrates the broader mandate of the dorsal stream: providing the brain with real-time motion information needed to guide a moving body through a moving world.
