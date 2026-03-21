---
id: visual-processing-pathway
title: Visual Processing Pathway
domain: psychology
course: biological-psychology
prerequisites:
- id: sensory-pathways-overview
  type: hard
- id: nervous-system-overview
  type: soft
- id: cerebral-cortex-organization
  type: soft
tags:
- retina
- lateral-geniculate
- V1
- dorsal-stream
- ventral-stream
- vision
stage: advanced
status: validated
---
# Visual Processing Pathway

## Core Idea
Visual processing begins in the retina with photoreceptors (rods and cones), passes through retinal ganglion cells whose axons form the optic nerve, crosses at the optic chiasm (nasal fibers decussate), and projects to the lateral geniculate nucleus of the thalamus before reaching primary visual cortex (V1). From V1, processing bifurcates: the dorsal 'where/how' stream (to parietal cortex) handles spatial location and visually guided action; the ventral 'what' stream (to temporal cortex) supports object recognition and face processing. This hierarchical organization means damage at any stage produces predictable, localized deficits.

## How It's Best Learned
Draw the full pathway from eye to cortex, including the chiasm crossing and what this means for visual field representation. Then work through specific deficits — hemianopia, prosopagnosia (ventral stream), optic ataxia (dorsal stream) — to test understanding.

## Common Misconceptions
- The left hemisphere does not process the left visual field; each hemisphere processes the contralateral visual field (right hemisphere → left visual field).
- V1 'sees' edges and orientations, not objects — the percept of a coherent object emerges from higher cortical processing.

## Questions

```yaml
- question: "A patient has a pituitary tumor that compresses the optic chiasm, selectively severing only the fibers that cross (the nasal retinal fibers). What visual deficit would you predict?"
  type: multiple-choice
  options:
    - "Monocular blindness in whichever eye the tumor presses on more strongly"
    - "Bitemporal hemianopia — loss of the peripheral (temporal) visual field in both eyes, while the central visual field is preserved"
    - "Homonymous hemianopia — loss of the same half of the visual field (e.g., left side) in both eyes"
    - "Complete blindness in both eyes, since the optic chiasm is a bottleneck for all visual fibers"
  answer: 1
  explanation: "The nasal retinal fibers are the ones that cross at the chiasm; they carry information from the temporal (peripheral) visual field of each eye. Severing only the crossing fibers leaves the temporal retinal fibers (carrying information from the nasal visual fields) intact. The result is loss of the temporal visual field in both eyes — bitemporal hemianopia, sometimes called 'tunnel vision.' This is the classic presentation of a pituitary tumor and is a direct consequence of the chiasm's anatomy: only the crossing fibers are vulnerable to compression from below."

- question: "A patient with otherwise intact visual acuity cannot recognize familiar faces or identify objects by sight, though they can accurately describe the color and basic features of what they see. Which finding best localizes the damage?"
  type: multiple-choice
  options:
    - "Damage to V1 — primary visual cortex cannot process object features without normal retinal input"
    - "Damage to the ventral 'what' stream (inferotemporal cortex) — prosopagnosia and object agnosia result from impaired object recognition, not loss of basic visual processing"
    - "Damage to the dorsal 'where/how' stream — spatial processing is required to identify objects in context"
    - "Damage to the lateral geniculate nucleus — the thalamic relay station cannot gate object-identity information"
  answer: 1
  explanation: "The ability to describe color and features while failing to recognize objects or faces is the signature of prosopagnosia and visual agnosia — syndromes resulting from ventral stream damage. The ventral 'what' stream projects from V1 toward inferotemporal cortex and supports object identity, face recognition, and visual memory. The patient's intact basic visual processing (acuity, color, feature description) confirms V1 and early visual areas are working; it is the higher-level integration in the ventral stream that is disrupted."

- question: "The right hemisphere of the brain primarily processes visual information from the right eye."
  type: true-false
  answer: false
  explanation: "The visual system is organized by visual field location, not by eye of origin. The right hemisphere processes the LEFT visual field of BOTH eyes. Nasal retinal fibers (which view the temporal visual field) cross at the optic chiasm to the opposite hemisphere; temporal retinal fibers (viewing the nasal visual field) stay ipsilateral. The result: all visual input from your left visual field — regardless of whether it entered via the left eye, the right eye, or both — is processed in the right hemisphere. 'Left eye → left hemisphere' is a persistent misconception that the chiasm crossing disproves."

- question: "Primary visual cortex (V1) responds to local features like edge orientation and spatial frequency, and the perception of a coherent object emerges from processing in higher cortical areas beyond V1."
  type: true-false
  answer: true
  explanation: "V1 neurons are tuned to specific local properties: orientation of edges, spatial frequency, direction of motion, and binocular disparity for depth. V1 does not 'see' objects — it extracts oriented contrast patches from the visual image. The perception of a face, a chair, or a word requires the integration of V1 outputs across many higher cortical areas: V2, V4 (color and form), and inferotemporal cortex for object identity (ventral stream). Patients with selective damage to these higher areas can have perfectly intact V1 and still be unable to recognize objects (agnosia), confirming that object perception is assembled downstream of V1."

- question: "The optic chiasm reorganizes visual information by visual field location rather than by which eye it came from. Explain why this organization is functionally advantageous."
  type: short-answer
  answer: "Organizing by visual field location means that each cortical hemisphere receives a complete map of one half of space — all information about the left visual field goes to the right hemisphere, regardless of eye of origin. This arrangement allows each hemisphere to integrate binocular information about the same spatial region, which is necessary for depth perception (stereopsis) and for coherent perception of visual space. If fibers were instead organized by eye, each hemisphere would receive information from only one eye, making binocular integration for depth difficult and creating an awkward arrangement where each hemisphere would need to coordinate across the corpus callosum just to perceive a single spatial location."
  explanation: "The chiasm crossing is also diagnostically valuable: the predictable reorganization means lesion location can be precisely inferred from the pattern of visual field loss. Monocular loss → optic nerve; bitemporal loss → chiasm; homonymous loss → optic tract or cortex. The anatomy makes predictions, and clinicians use visual field testing as a non-invasive window into the location of neurological damage."
```

## Explainer

You already know that sensory systems convert physical energy into neural signals and route them through hierarchical pathways to cortex. Vision follows this logic, but with an unusual detour: the routing is organized by location in visual space, not by which eye is looking. The process begins in the **retina** — a sheet of neural tissue at the back of the eye. **Photoreceptors** (rods for low-light/peripheral vision, cones for color and acuity) transduce light into graded potentials, which are processed locally by bipolar and amacrine cells before converging on **retinal ganglion cells (RGCs)**. The axons of RGCs collect into the **optic nerve** — the only output channel from the eye to the brain.

The two optic nerves meet at the **optic chiasm** beneath the hypothalamus, where a partial crossing occurs. Fibers from the *nasal* half of each retina (which see the temporal visual field) cross to the opposite hemisphere; fibers from the *temporal* retina stay ipsilateral. The result is that all visual information from your left visual field — regardless of which eye it entered — ends up in your right hemisphere, and vice versa. This is the key organizational principle: the brain maps visual *space*, not visual *organs*. After the chiasm, the optic tracts continue to the **lateral geniculate nucleus (LGN)** of the thalamus — the relay station that gates and preprocesses signals before passing them to cortex.

From the LGN, projections reach **primary visual cortex (V1)** in the occipital lobe. V1 neurons are tuned to local features: edge orientation, spatial frequency, direction of motion, and binocular disparity for depth. V1 does not "see" objects — it extracts oriented contrasts. Object perception is assembled across many subsequent cortical areas. From V1, processing bifurcates into two streams. The **dorsal "where/how" stream** projects toward parietal cortex, handling spatial localization, depth, motion, and visually guided action. The **ventral "what" stream** projects toward inferotemporal cortex, supporting object recognition, face perception, and visual memory. These two streams are computationally distinct: one answers "where is it and how do I act on it?" while the other answers "what is it?"

Because the pathway is anatomically well-mapped and hierarchical, damage at any stage produces a predictable, localizable deficit. Cutting the optic nerve before the chiasm causes monocular blindness. Cutting the chiasm itself (a classic consequence of pituitary tumors pressing upward) severs the crossing nasal fibers, causing **bitemporal hemianopia** — loss of the peripheral visual field in both eyes. Damage to one optic tract causes **homonymous hemianopia** — loss of the same visual field half in both eyes. Selective damage to the ventral stream causes **prosopagnosia** (intact acuity, but inability to recognize faces) without blindness, while dorsal stream damage causes **optic ataxia** (inaccurate reaching) despite normal object recognition. This lesion logic is not just a memorization exercise — it is the pathway's anatomy making predictions, and the predictions are confirmed by the clinical record.
