---
id: optical-instruments
title: Optical Instruments
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lens-equation
  type: hard
- id: lens-combinations
  type: hard
- id: mirror-equation
  type: soft
tags:
- camera
- microscope
- telescope
- angular magnification
- resolving power
stage: formal-systems
status: validated
---

# Optical Instruments

## Core Idea
Optical instruments use lens combinations to magnify or focus images. A simple magnifier uses a converging lens to produce a magnified virtual image at the near point. A compound microscope uses an objective (short focal length) to form a real magnified intermediate image, then an eyepiece to magnify that image again: M_total = M_obj × M_eye. A refracting telescope uses a large-aperture objective for light-gathering and an eyepiece for angular magnification M = −f_obj/f_eye. Resolution is ultimately limited by diffraction.

## How It's Best Learned
Build a simple telescope using two lenses in a cardboard tube; measure the angular magnification by comparing the apparent size of a distant ruler with and without the telescope. Derive the formula from the two-lens analysis.

## Common Misconceptions
- Magnification and resolution are distinct; a telescope can magnify greatly but still not resolve two close stars if the aperture is too small.
- The eyepiece of a microscope does not form a real image on the retina directly; it acts as a magnifier of the intermediate real image.

## Explainer

You've worked through the thin lens equation and lens combinations — the geometry of how a single lens bends rays and where images form. Optical instruments take that foundation and engineer multi-lens systems for specific purposes: magnifying small nearby objects, resolving fine detail, or gathering light from astronomical distances. In each case, the design logic follows directly from the ray optics you already know.

The simplest instrument is the **magnifying glass**: a single converging lens positioned so the object lies inside its focal length. The lens intercepts the diverging rays from the object and bends them into a less-diverging bundle reaching your eye. Because the bundle is less diverging than it would be without the lens, your eye perceives the light as coming from a larger virtual image farther away. The **angular magnification** M = 25 cm / f measures the benefit: a 5 cm focal length lens magnifies 5×, meaning the object appears to subtend 5 times the angle it would at the standard near point of 25 cm.

A **compound microscope** stacks two magnifying stages to reach much higher magnifications than any single lens can provide. The **objective lens** — very short focal length, placed just beyond its focal point from the specimen — creates a real, inverted, greatly magnified intermediate image inside the tube. That intermediate image then becomes the object for the **eyepiece**, which acts as a simple magnifier to produce the final virtual image your eye observes. Total magnification is multiplicative: M_total = M_objective × M_eyepiece. This staged design explains the physical layout of a microscope: the long tube separates the two lenses to allow the objective to form its real intermediate image at the correct location for the eyepiece.

A **refracting telescope** has the opposite challenge: the objects are already far away, so the goal is not photographic magnification but **angular magnification** — making the small apparent angle between two stars seem larger. The large-aperture objective gathers parallel incoming rays from a distant point and brings them to focus at its focal point. The eyepiece then re-collimates those rays so your eye receives them as a parallel bundle from a wider angle. The magnification formula M = −f_objective / f_eyepiece shows why astronomical telescopes have long tubes: a long-focal-length objective yields high magnification, but it must be physically separated from the eyepiece by roughly f_obj + f_eye. Critically, **magnification and resolution are independent**: a small-aperture telescope can magnify a star enormously yet still cannot resolve whether it is a binary, because angular resolution is diffraction-limited by aperture diameter — the larger the objective, the finer the detail it can distinguish.
