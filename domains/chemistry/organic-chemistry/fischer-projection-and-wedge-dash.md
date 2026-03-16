---
id: fischer-projection-and-wedge-dash
title: Fischer Projections and Wedge-Dash Representation
domain: chemistry
course: organic-chemistry
prerequisites:
- id: molecular-geometry-basics
  type: hard
- id: enantiomers-and-chirality
  type: hard
- id: newman-projection-and-conformations
  type: soft
builds-toward:
- r-s-nomenclature-cahn-ingold-prelog-rules
tags:
- fischer-projection
- wedge-dash
- stereochemistry
- 2d-representation
stage: formal-systems
status: draft
---

# Fischer Projections and Wedge-Dash Representation

## Core Idea
Fischer projections represent three-dimensional molecules on a two-dimensional plane, with horizontal bonds projecting forward and vertical bonds projecting backward. Wedge-dash notation uses wedges (forward) and dashes (backward) to indicate stereochemistry. Fischer projections and wedge-dash are interconvertible representations critical for communicating stereochemical structures.

## Explainer

You already know from studying chirality that the three-dimensional arrangement of groups around a stereocenter matters — enantiomers have identical connectivity but different spatial arrangements, and this difference has real chemical and biological consequences. The challenge is representing these three-dimensional arrangements on a flat page. Two conventions dominate organic chemistry: **wedge-dash notation** and **Fischer projections**, and being fluent in both — and in converting between them — is essential for stereochemistry problems.

**Wedge-dash notation** is the more intuitive system. You draw the carbon skeleton in the plane of the page, then use a solid wedge (▸) to indicate a bond pointing toward you (out of the page) and a dashed wedge (╌) to indicate a bond pointing away from you (into the page). Plain lines represent bonds in the plane of the page. For a tetrahedral carbon with four different groups, two of those groups typically sit in the plane while one projects forward and one backward. This directly represents what you would see if you held a molecular model in front of you. Wedge-dash works well for individual stereocenters and small molecules, but it becomes cluttered for molecules with many stereocenters — like sugars with four or five chiral carbons.

**Fischer projections** solve this problem with a strict convention: the carbon chain is drawn vertically with the most oxidized carbon (or the carbon with the lowest number) at the top, and each stereocenter appears as a cross. The horizontal lines at each cross represent bonds coming toward you, and the vertical lines represent bonds going away from you. You never need to draw wedges or dashes because the projection rules encode the three-dimensional information. For a sugar like glucose with four stereocenters, a Fischer projection shows all the stereochemistry in a clean, compact format that would be nearly unreadable in wedge-dash.

The critical manipulation rules for Fischer projections are: (1) you may rotate the entire projection 180° in the plane without changing the configuration, but a 90° rotation inverts every stereocenter; (2) you may swap any two groups on a single stereocenter, but each swap inverts the configuration — two swaps return you to the original; (3) you must never lift the projection off the page and flip it, as this also inverts configuration. To convert a Fischer projection to wedge-dash, remember that horizontal groups point toward you and vertical groups point away, then redraw accordingly. To convert from wedge-dash to Fischer, orient the molecule so the chain is vertical with forward-pointing groups horizontal, then flatten into the cross notation. Practicing these conversions with a molecular model kit in hand builds the spatial reasoning that makes stereochemistry problems manageable.
