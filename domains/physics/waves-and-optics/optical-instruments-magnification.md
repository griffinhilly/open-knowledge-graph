---
id: optical-instruments-magnification
title: 'Optical Instruments: Microscopes and Telescopes'
domain: physics
course: waves-and-optics
prerequisites:
- id: lens-image-formation-ray-diagrams
  type: hard
- id: lens-combinations
  type: hard
builds-toward:
- optical-instruments
tags:
- microscope
- telescope
- magnification
stage: formal-systems
status: validated
---

# Optical Instruments: Microscopes and Telescopes

## Core Idea
A compound microscope uses an objective lens (high magnification, small focal length) and eyepiece (acts as magnifying glass) with total magnification M = Mo × Me. A refracting telescope uses an objective lens (long focal length, creates real image) and eyepiece (magnifies this image) with angular magnification M = -fo/fe. Reflecting telescopes replace the objective with a curved mirror to avoid chromatic aberrations.

## Questions

```yaml
- question: "A refracting telescope has an objective focal length of 900 mm and an eyepiece focal length of 30 mm. If the eyepiece is replaced with one of focal length 45 mm, what happens to the angular magnification?"
  type: multiple-choice
  options:
    - "It increases from 30× to 45× because a longer eyepiece sees more"
    - "It decreases from 30× to 20× because magnification is fo/fe"
    - "It stays the same because only the objective determines magnification"
    - "It increases from 30× to 40× because the two focal lengths now share more overlap"
  answer: 1
  explanation: "Angular magnification for a telescope is M = fo/fe. With fe = 30 mm: M = 900/30 = 30×. With fe = 45 mm: M = 900/45 = 20×. Increasing the eyepiece focal length decreases magnification. The formula makes clear that magnification is the ratio — a longer eyepiece is a weaker magnifier, not a stronger one. A common intuition failure is to think a physically larger eyepiece provides more magnification."

- question: "Why does a microscope objective use a very short focal length while a telescope objective uses a very long focal length?"
  type: multiple-choice
  options:
    - "Microscopes must be compact, so short lenses save space; telescopes need long lenses for structural rigidity"
    - "Short objective focal length creates a large real intermediate image from a nearby specimen; long objective focal length gathers parallel rays from distant objects and brings them to a useful focus inside the tube"
    - "Both use short focal lengths — the difference is that telescopes use curved mirrors instead"
    - "The focal lengths are determined by manufacturing convenience, not optical function"
  answer: 1
  explanation: "The two instruments solve opposite problems. A microscope must form a large magnified real image of a nearby object — this requires placing the objective very close to the specimen (just beyond its focal point), which is only possible with a very short focal length. A telescope deals with objects that are extremely distant (rays arrive nearly parallel); a long focal length brings those parallel rays to a real focus far down the tube, which the eyepiece then magnifies. Short fo → strong bending power for nearby objects; long fo → gentle convergence of parallel rays from infinity."

- question: "A reflecting telescope avoids chromatic aberration because a mirror reflects all wavelengths of light at the same angle, unlike a glass lens which refracts different wavelengths by different amounts."
  type: true-false
  answer: true
  explanation: "Chromatic aberration arises because glass has different refractive indices for different wavelengths (dispersion), causing different colors to focus at different distances. A concave mirror focuses light by reflection, governed by the law of reflection (angle of incidence = angle of reflection), which does not depend on wavelength. All colors focus at the same point, eliminating chromatic aberration. This is why all major research telescopes use mirrors."

- question: "The total magnification of a compound microscope is found by adding the objective magnification and eyepiece magnification: M_total = M_o + M_e."
  type: true-false
  answer: false
  explanation: "Total magnification is the product, not the sum: M_total = M_o × M_e. This follows from the two-stage design — the eyepiece magnifies the intermediate image that the objective already magnified. If M_o = 40× and M_e = 10×, you get 400× total, not 50×. Addition would apply if the two lenses somehow shared a single magnification step, which they do not; each stage acts independently in series."

- question: "Explain why a compound microscope and a refracting telescope both use a two-stage lens design (objective + eyepiece), yet require opposite focal length strategies for the objective."
  type: short-answer
  answer: "Both instruments use stage one (objective) to create a real intermediate image, and stage two (eyepiece) to magnify that image for the eye. The difference is what stage one must accomplish: a microscope objective must create a highly magnified real image from a nearby specimen, which requires strong bending power and therefore a short focal length. A telescope objective must gather parallel light from a very distant object and bring it to a focus inside the tube — for distant objects, a longer focal length means the focal point is farther away, giving a more convenient tube length, and the angular magnification formula M = fo/fe directly rewards a large fo."
  explanation: "The unifying insight is the two-stage structure: the intermediate real image is always the bridge between stages. Where the intermediate image forms, how large it is, and what the eyepiece does with it all follow from the lens equation applied to each stage. The difference in focal length strategy is not arbitrary — it follows directly from the geometry of nearby vs. infinitely distant objects."
```

## Explainer

From your work with lens image formation and ray diagrams, you know that a single converging lens placed close to an object (within or near the focal length) acts as a magnifying glass, producing a virtual, upright, enlarged image. A **compound microscope** exploits this twice: the **objective lens** — with a very short focal length — is placed just beyond its focal point from the specimen, producing a highly magnified real image inside the tube. The **eyepiece** then treats that real image as its own object, acting as a simple magnifier to produce a final virtual image seen by the eye. Because the two lenses act in series, total magnification multiplies: M_total = M_objective × M_eyepiece. Small focal lengths in the objective are essential — shorter focal length means stronger bending power, which allows the lens to sit close to the specimen and produce a large real image.

A telescope solves the opposite problem: the objects are enormous but very far away, so their actual image on the retina is tiny. The **objective lens** of a telescope has a long focal length, meaning it collects light from a distant object and brings it to a real focus inside the tube. The eyepiece again acts as a magnifier, but here the result is described as **angular magnification** — the object appears to subtend a larger angle at your eye than it would without the telescope. The formula M = -fo/fe tells you that a long objective focal length and short eyepiece focal length maximize angular magnification; the negative sign indicates the image is inverted. You can combine lenses as you practiced in lens-combinations: adding an erecting lens system makes the image upright (as in binoculars), at the cost of some additional length.

Reflecting telescopes swap the objective lens for a concave mirror. The optical principle is identical — light from a distant source is brought to a real focus — but mirrors have two practical advantages. First, they do not refract different wavelengths by different amounts, avoiding **chromatic aberration** (the color fringing that plagues large refracting telescopes). Second, a mirror can be supported from behind, allowing arbitrarily large apertures without the sagging that afflicts large glass lenses. Nearly all modern research telescopes are reflectors for these reasons.

The unifying idea in both instruments is the **two-stage design**: stage one (objective) creates a real intermediate image; stage two (eyepiece) magnifies that image for the eye. Understanding where the intermediate image forms — using the lens equation from your ray diagram work — tells you everything about how to space the lenses and what total magnification to expect. If you move the eyepiece to view a real image formed slightly differently, the magnification changes accordingly. The instruments differ only in what kind of magnification they optimize: linear size (microscope) versus angular subtense (telescope).
