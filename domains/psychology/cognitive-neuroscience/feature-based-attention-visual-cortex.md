---
id: feature-based-attention-visual-cortex
title: Feature-Based Attention in Visual Cortex
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: visual-attention-mechanisms
  type: hard
- id: visual-cortex-hierarchical-organization
  type: hard
builds-toward:
- search-asymmetries-feature-dimensions
- selective-attention-mechanisms
tags:
- attention
- feature-attention
- gain-modulation
- color
- motion
- orientation
stage: advanced
status: draft
---

# Feature-Based Attention in Visual Cortex

## Core Idea
Visual attention operates not only at spatial locations but also on features across the entire visual field. Attending to a color, motion direction, or orientation enhances neural responses to that feature throughout visual cortex, even in spatially unattended locations. This feature-based attention likely reflects a global gain mechanism where attending to a feature enhances its representation across retinotopic space, improving discrimination and memory for that feature dimension.

## Explainer

From your study of visual attention mechanisms, you learned that attention can be directed to locations in space — the spotlight metaphor — boosting processing of everything at an attended location. From your study of visual cortex hierarchical organization, you know that different properties of visual input are processed in distinct cortical regions: motion in MT/V5, color in V4, orientation in early visual cortex. Feature-based attention exploits that architecture. Rather than selecting a location, it selects a feature value — say, "red" or "moving left" — and enhances the responses of neurons tuned to that feature throughout the entire visual field simultaneously.

The key experiment illustrating this involves directing a person's attention to a particular feature while their eyes remain fixed on a central point. If you attend to "red" while viewing a display with colored stimuli at many locations, the neural responses to red items increase in visual cortex *at all locations*, including locations where you're not currently looking and where spatial attention is explicitly directed elsewhere. This **global gain** effect is the defining signature of feature-based attention: it doesn't have the narrow spatial profile of spotlight attention. It operates like adjusting the gain on a specific channel — turning up the signal from all neurons tuned to the attended feature value, regardless of where those stimuli appear in the visual field.

The functional logic is straightforward. If you are searching a cluttered scene for a red object, it would be inefficient to move your spotlight of attention sequentially across every location. Feature-based attention pre-filters the entire field: it makes red stand out everywhere at once, guiding subsequent spatial attention toward likely target locations. This is why visual search for a distinctive feature (pop-out search) is so fast — the feature-based gain mechanism highlights targets automatically before deliberate spatial attention has to work. Feature-based and spatial attention interact: when both converge on the same stimulus (you attend to its feature *and* its location), the effects are roughly multiplicative, not merely additive.

At the neural level, feature-based attention modulates responses as early as V1 and V2, but the source of the top-down modulation signal is thought to lie in frontoparietal regions — the same networks that coordinate spatial attention. This points to a general-purpose attentional control system that can direct gain to either locations or features depending on the task. Neurons in feature-selective regions don't change their tuning under feature-based attention — a cell that prefers leftward motion still responds most to leftward motion — but their overall responsiveness increases for the attended feature value, effectively increasing the signal-to-noise ratio for that dimension. The practical consequence for perception is that attending to a feature dimension (color, motion, orientation) not only speeds detection but also improves fine discrimination and enhances the durability of subsequent memory encoding for items sharing that feature.
