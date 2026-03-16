---
id: spherical-mirror-formula
title: Spherical Mirror Formula and Sign Conventions
domain: physics
course: waves-and-optics
prerequisites:
- id: mirror-equation
  type: soft
- id: paraxial-ray-approximation
  type: hard
builds-toward:
- mirror-image-formation-ray-diagrams
tags:
- spherical-mirrors
- mirror-equation
- focal-length
stage: formal-systems
status: draft
---

# Spherical Mirror Formula and Sign Conventions

## Core Idea
The mirror equation 1/f = 1/o + 1/i applies to spherical mirrors with focal length f = R/2 (R is radius of curvature). Sign conventions matter: concave mirrors have positive f; convex mirrors have negative f. Real objects have positive o; virtual objects (uncommon) have negative o.

## Explainer

You already know from the paraxial approximation that when rays travel at small angles to the optical axis, the geometry of reflection becomes linear. The **spherical mirror formula** is the direct payoff: a single equation, 1/f = 1/o + 1/i, that tells you where an image forms given the object distance and the mirror's focal length. The derivation follows from the paraxial geometry of a spherical mirror — tracing two paraxial rays from an off-axis object point and finding where they cross after reflection.

The key geometric fact is that a spherical mirror has a **center of curvature** C at distance R from the mirror surface, and a **focal point** F at distance R/2. Any ray parallel to the optical axis reflects through F; any ray directed toward C reflects straight back. These are the two standard construction rays for ray diagrams. The focal length f = R/2 is not a coincidence — it follows from the paraxial approximation applied to the law of reflection on a spherical surface. Without the paraxial assumption, rays from different heights would focus at slightly different points (spherical aberration), and a single focal length would not exist.

The **sign convention** is the part that trips students up most. The convention is defined by the physics: distances measured in the direction light travels from the object are positive; distances measured against that direction are negative. For a real object in front of a concave mirror, both o and f are positive, and the equation predicts where the real image forms on the same side as the object. For a convex mirror, f is negative (the focal point is behind the mirror, on the non-reflecting side), and the image distance i comes out negative too — indicating a **virtual image** behind the mirror that light rays never actually pass through, but that your eye perceives by tracing the diverging reflected rays backward. This is the image you see when looking into a car's convex rear-view mirror: always upright, always smaller than the object, always virtual.

The **magnification** m = −i/o ties the formula to what you actually observe. When m is negative, the image is inverted (real images from concave mirrors); when m is positive, the image is upright (virtual images). When |m| > 1, the image is enlarged; when |m| < 1, it is reduced. These four combinations — inverted/upright, real/virtual, enlarged/reduced — map cleanly onto the different regions of object distance relative to f and R, and understanding which combination applies in a given configuration is the practical skill the formula enables.
