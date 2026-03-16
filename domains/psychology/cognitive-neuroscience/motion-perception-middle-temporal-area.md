---
id: motion-perception-middle-temporal-area
title: Motion Perception and Middle Temporal (MT) Area
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: visual-system-retina-cortex
  type: hard
- id: dorsal-stream-reaching-visuomotor-control
  type: hard
builds-toward:
- biological-motion-perception-stp
- optic-flow-navigation-mst
tags:
- motion-perception
- MT
- MST
- direction-selectivity
- speed-selectivity
- optical-flow
stage: advanced
status: draft
---

# Motion Perception and Middle Temporal (MT) Area

## Core Idea
Area MT (medial temporal cortex) and related dorsal stream regions extract motion direction and speed from visual input. MT neurons exhibit strong tuning for motion direction and are pooled to detect global motion patterns from local motion signals. Damage to MT impairs motion perception (akinetopsia) while sparing static form recognition, demonstrating domain-specificity. MT projects to medial superior temporal area (MST) for integration of optical flow in navigation.

## Explainer

From your prerequisites you know that the retina encodes static images and that V1 neurons respond to oriented edges at specific locations. But the visual world is dynamic — objects move, you move through environments, and distinguishing motion from stillness is fundamental to threat detection, object tracking, and navigation. Area MT (also called V5, located in the middle temporal cortex and strongly connected to the dorsal stream) is the region where motion is computed from the sequential static snapshots that V1 provides, and its properties reveal how the brain extracts a continuous dynamic percept from what is, at the retinal level, a series of stills.

MT neurons have a defining property: strong **direction selectivity**. Each MT neuron responds vigorously to motion in one preferred direction and weakly or not at all to the opposite direction. This tuning isn't directly inherited from V1 — V1 neurons detect oriented edges, and MT integrates signals across groups of V1 neurons to extract direction over a larger spatial scale. This integration solves the **aperture problem**: a single oriented edge seen through a small aperture (or by a small V1 neuron with a restricted receptive field) is ambiguous about direction — you can't determine whether a diagonal edge is moving left, up, or obliquely, because only the component perpendicular to the edge is visible. MT pools signals from V1 neurons with different orientations, computing the global motion direction consistent with all local signals. The result is unambiguous motion perception despite V1's local ambiguity.

When MT is damaged, the consequence is **akinetopsia** — a selective inability to perceive motion while form perception remains intact. The most documented case (LM) could not perceive pouring liquid as flowing; she perceived it as a series of frozen snapshots. Moving cars appeared to teleport between positions. She could navigate normally in a static world but was dangerously impaired in dynamic environments. This selective deficit confirms that motion perception is not simply derived by comparing a sequence of still images at a high level — it requires dedicated neural computation that MT provides. You can also observe MT's role in normal perception through **motion aftereffects**: staring at a waterfall for 30 seconds and then looking at a cliff creates the illusion of upward drift, because MT neurons tuned for downward motion have adapted (reduced firing) and their upward-preferring counterparts rebound, producing motion percept without actual motion.

MT projects forward to **MST** (medial superior temporal area), which integrates MT's local motion signals into complex global patterns. MST neurons are tuned for **optic flow** — the global pattern of visual motion generated when you move through a scene. Walking forward produces an expanding pattern radiating from a focal point straight ahead; turning left produces a rotation. MST neurons that respond to these expansion and rotation patterns are critical for estimating your heading and for stabilizing your gaze during self-motion. Together, MT and MST form a functional hierarchy: MT extracts local motion direction and speed from individual regions of the visual field; MST integrates these into the global flow patterns that tell you where you're going. This architecture mirrors the general organizing principle of visual cortex — simple features extracted early, progressively integrated into complex percepts by downstream areas.
