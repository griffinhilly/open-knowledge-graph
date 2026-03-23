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
status: validated
---

# Fischer Projections and Wedge-Dash Representation

## Core Idea
Fischer projections represent three-dimensional molecules on a two-dimensional plane, with horizontal bonds projecting forward and vertical bonds projecting backward. Wedge-dash notation uses wedges (forward) and dashes (backward) to indicate stereochemistry. Fischer projections and wedge-dash are interconvertible representations critical for communicating stereochemical structures.

## Questions

```yaml
- question: "In a Fischer projection of an amino acid, the amino group is drawn on the horizontal left and the hydrogen on the horizontal right at the alpha carbon. What is the spatial relationship of these groups relative to the viewer?"
  type: multiple-choice
  options:
    - "Both project away from the viewer into the page"
    - "Both project toward the viewer out of the page"
    - "The amino group is in the plane of the page; the hydrogen projects forward"
    - "The stereochemistry is ambiguous without wedge-dash notation"
  answer: 1
  explanation: "In a Fischer projection, ALL horizontal bonds at a stereocenter project toward the viewer (out of the page), and all vertical bonds project away. This convention is fixed and encodes the 3D structure without any explicit wedge or dash symbols. Both the amino group and the hydrogen (horizontal) therefore project forward. Option D is the core misconception: Fischer projections are not ambiguous — the horizontal = forward rule is exactly what makes them unambiguous."

- question: "A student has a Fischer projection and rotates it 90° in the plane of the page. What happens to the stereochemical configuration at each stereocenter?"
  type: multiple-choice
  options:
    - "Nothing changes — rotations in the plane preserve configuration"
    - "Every stereocenter is inverted — what was horizontal is now vertical and vice versa"
    - "The absolute configuration is preserved but the drawing looks different"
    - "Only the top and bottom stereocenters are affected; middle ones are unchanged"
  answer: 1
  explanation: "A 90° rotation in the plane swaps what was horizontal (toward viewer) with what was vertical (away from viewer) — inverting the spatial relationship at every stereocenter simultaneously. The rule is: rotating a Fischer projection 90° changes the configuration. Rotating 180° does not, because horizontal bonds rotate to become horizontal again and vertical to vertical again. Students who assume any in-plane rotation is safe will consistently assign incorrect configurations."

- question: "In a Fischer projection, vertical bonds at a stereocenter point toward the viewer."
  type: true-false
  answer: false
  explanation: "This is false — the opposite is true. In a Fischer projection, HORIZONTAL bonds point toward the viewer (out of the page), and VERTICAL bonds point away from the viewer (into the page). Confusing this convention is the most common error in Fischer projection problems. A helpful memory aid: the horizontal bonds 'reach out' toward you like arms extending forward."

- question: "Swapping any two groups at a stereocenter in a Fischer projection inverts the configuration at that center."
  type: true-false
  answer: true
  explanation: "True — each two-group swap at a single stereocenter inverts the configuration at that center, producing the mirror image at that position. This is directly analogous to Walden inversion: any permutation that changes the spatial arrangement results in the opposite R/S designation. Two swaps return you to the original. This rule lets you verify Fischer-to-wedge conversions: if you ended up with the wrong configuration, you can diagnose whether you made an odd number of swaps."

- question: "Why does a 90° rotation of a Fischer projection in the plane of the page change the stereochemical configuration, while a 180° rotation does not?"
  type: short-answer
  answer: "A Fischer projection encodes directionality: horizontal bonds point toward you, vertical bonds point away. A 90° rotation converts what was horizontal (toward viewer) into vertical (away from viewer) at each stereocenter — swapping the spatial direction of all bonds and inverting every stereocenter. A 180° rotation converts horizontal bonds back to horizontal and vertical back to vertical — preserving the toward/away assignments of every bond and leaving all configurations unchanged."
  explanation: "The key is that the Fischer projection's 3D meaning depends on which bonds are horizontal vs. vertical, not on their absolute orientation in the plane. 90° shuffles the horizontal/vertical category; 180° preserves it. This is why flipping the projection off the page (a forbidden operation) also inverts configurations — it reverses which direction 'horizontal' points in 3D space."
```

## Explainer

You already know from studying chirality that the three-dimensional arrangement of groups around a stereocenter matters — enantiomers have identical connectivity but different spatial arrangements, and this difference has real chemical and biological consequences. The challenge is representing these three-dimensional arrangements on a flat page. Two conventions dominate organic chemistry: **wedge-dash notation** and **Fischer projections**, and being fluent in both — and in converting between them — is essential for stereochemistry problems.

**Wedge-dash notation** is the more intuitive system. You draw the carbon skeleton in the plane of the page, then use a solid wedge (▸) to indicate a bond pointing toward you (out of the page) and a dashed wedge (╌) to indicate a bond pointing away from you (into the page). Plain lines represent bonds in the plane of the page. For a tetrahedral carbon with four different groups, two of those groups typically sit in the plane while one projects forward and one backward. This directly represents what you would see if you held a molecular model in front of you. Wedge-dash works well for individual stereocenters and small molecules, but it becomes cluttered for molecules with many stereocenters — like sugars with four or five chiral carbons.

**Fischer projections** solve this problem with a strict convention: the carbon chain is drawn vertically with the most oxidized carbon (or the carbon with the lowest number) at the top, and each stereocenter appears as a cross. The horizontal lines at each cross represent bonds coming toward you, and the vertical lines represent bonds going away from you. You never need to draw wedges or dashes because the projection rules encode the three-dimensional information. For a sugar like glucose with four stereocenters, a Fischer projection shows all the stereochemistry in a clean, compact format that would be nearly unreadable in wedge-dash.

The critical manipulation rules for Fischer projections are: (1) you may rotate the entire projection 180° in the plane without changing the configuration, but a 90° rotation inverts every stereocenter; (2) you may swap any two groups on a single stereocenter, but each swap inverts the configuration — two swaps return you to the original; (3) you must never lift the projection off the page and flip it, as this also inverts configuration. To convert a Fischer projection to wedge-dash, remember that horizontal groups point toward you and vertical groups point away, then redraw accordingly. To convert from wedge-dash to Fischer, orient the molecule so the chain is vertical with forward-pointing groups horizontal, then flatten into the cross notation. Practicing these conversions with a molecular model kit in hand builds the spatial reasoning that makes stereochemistry problems manageable.
