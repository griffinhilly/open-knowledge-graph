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
status: draft
---

# Optical Instruments: Microscopes and Telescopes

## Core Idea
A compound microscope uses an objective lens (high magnification, small focal length) and eyepiece (acts as magnifying glass) with total magnification M = Mo × Me. A refracting telescope uses an objective lens (long focal length, creates real image) and eyepiece (magnifies this image) with angular magnification M = -fo/fe. Reflecting telescopes replace the objective with a curved mirror to avoid chromatic aberrations.

## Explainer

From your work with lens image formation and ray diagrams, you know that a single converging lens placed close to an object (within or near the focal length) acts as a magnifying glass, producing a virtual, upright, enlarged image. A **compound microscope** exploits this twice: the **objective lens** — with a very short focal length — is placed just beyond its focal point from the specimen, producing a highly magnified real image inside the tube. The **eyepiece** then treats that real image as its own object, acting as a simple magnifier to produce a final virtual image seen by the eye. Because the two lenses act in series, total magnification multiplies: M_total = M_objective × M_eyepiece. Small focal lengths in the objective are essential — shorter focal length means stronger bending power, which allows the lens to sit close to the specimen and produce a large real image.

A telescope solves the opposite problem: the objects are enormous but very far away, so their actual image on the retina is tiny. The **objective lens** of a telescope has a long focal length, meaning it collects light from a distant object and brings it to a real focus inside the tube. The eyepiece again acts as a magnifier, but here the result is described as **angular magnification** — the object appears to subtend a larger angle at your eye than it would without the telescope. The formula M = -fo/fe tells you that a long objective focal length and short eyepiece focal length maximize angular magnification; the negative sign indicates the image is inverted. You can combine lenses as you practiced in lens-combinations: adding an erecting lens system makes the image upright (as in binoculars), at the cost of some additional length.

Reflecting telescopes swap the objective lens for a concave mirror. The optical principle is identical — light from a distant source is brought to a real focus — but mirrors have two practical advantages. First, they do not refract different wavelengths by different amounts, avoiding **chromatic aberration** (the color fringing that plagues large refracting telescopes). Second, a mirror can be supported from behind, allowing arbitrarily large apertures without the sagging that afflicts large glass lenses. Nearly all modern research telescopes are reflectors for these reasons.

The unifying idea in both instruments is the **two-stage design**: stage one (objective) creates a real intermediate image; stage two (eyepiece) magnifies that image for the eye. Understanding where the intermediate image forms — using the lens equation from your ray diagram work — tells you everything about how to space the lenses and what total magnification to expect. If you move the eyepiece to view a real image formed slightly differently, the magnification changes accordingly. The instruments differ only in what kind of magnification they optimize: linear size (microscope) versus angular subtense (telescope).
