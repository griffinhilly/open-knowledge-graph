---
id: plane-mirrors
title: Image Formation in Plane Mirrors
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-law
  type: hard
- id: reflection-and-law-of-reflection
  type: hard
builds-toward:
- spherical-mirrors
tags:
- plane mirror
- virtual image
- image distance
- laterally inverted
stage: formal-systems
status: validated
---

# Image Formation in Plane Mirrors

## Core Idea
A plane (flat) mirror forms a virtual, upright, laterally reversed image that appears to be located as far behind the mirror as the object is in front of it. The image is virtual because the reflected rays diverge — they only appear to originate from behind the mirror and cannot be projected onto a screen. Ray diagrams are constructed by applying the law of reflection to at least two rays from each object point.

## How It's Best Learned
Draw ray diagrams for an object at various positions in front of a flat mirror. Verify that image distance equals object distance using a candle and a piece of glass as a two-way mirror.

## Common Misconceptions
- Plane mirrors do not flip left-right; they flip front-back (swap object and image depth). The left-right reversal perception is a cognitive effect.
- The size of the mirror needed to see your whole body is half your height, regardless of your distance from it.

## Questions

```yaml
- question: "You hold a page of text up to a plane mirror and the writing appears reversed. What does the mirror actually invert?"
  type: multiple-choice
  options:
    - "Left and right — mirrors swap the horizontal axis"
    - "Up and down — mirrors invert the vertical axis"
    - "Front and back — mirrors swap depth, mapping each point to an equal distance behind the surface"
    - "Both left-right and up-down, which is why images appear strange"
  answer: 2
  explanation: "A plane mirror inverts only the axis perpendicular to its surface — the depth axis (front-back). Points in front of the mirror map to points equally far behind it; x (horizontal) and y (vertical) are unchanged. The perceived left-right reversal is a cognitive artifact: when you mentally 'turn around' to face your reflection as if it were another person, that imagined rotation is what swaps left and right in your perception. The mirror itself is indifferent to handedness in the horizontal plane. Hold text up to a window and look at it from outside — you see the same reversal, for the same reason."

- question: "An object is placed 30 cm in front of a plane mirror. Which statement correctly describes the image?"
  type: multiple-choice
  options:
    - "The image is 30 cm behind the mirror and can be projected onto a screen placed there"
    - "The image is 30 cm behind the mirror and cannot be projected onto a screen — it is virtual"
    - "The image is 60 cm behind the mirror because the light must travel to the mirror and back"
    - "The image is 30 cm in front of the mirror on the same side as the object"
  answer: 1
  explanation: "The image forms as far behind the mirror as the object is in front of it — 30 cm in this case. But the image is virtual: the reflected rays diverge as they leave the mirror's surface, and your eye traces them backward as if they originated from a point 30 cm behind the mirror. No light actually reaches that point. A screen placed there would catch nothing. This distinguishes a virtual image (apparent convergence of backward-traced rays) from a real image (actual convergence of forward-traveling rays, as produced by a concave mirror or converging lens)."

- question: "As you walk toward a plane mirror, the minimum mirror height needed to see your full reflection decreases, because you are closer to the image and it subtends a larger angle."
  type: true-false
  answer: false
  explanation: "The minimum mirror height needed to see your full reflection is always half your height, regardless of distance. This follows from the geometry: as you walk closer, your image also moves closer at the same rate (since image distance equals object distance). The rays from your head and feet to the mirror's edges subtend the same angle at your eyes whether you're near or far. The half-height rule is fixed by your own geometry — the distance from your eyes to your head, and from your eyes to your feet — not by how far you are from the mirror."

- question: "You can see a clear image of yourself in a plane mirror, which proves the image is real — if it weren't real, it couldn't be seen."
  type: true-false
  answer: false
  explanation: "This is the central misconception about virtual images. A virtual image can be seen clearly — your brain traces diverging reflected rays backward and perceives them as coming from behind the mirror. What makes an image virtual is not invisibility but the fact that no actual light rays converge at the image location. A real image (like that formed by a concave mirror) actually has light converging at the image point and can be caught on a screen. A virtual image cannot be projected onto a screen, but it is absolutely visible to an eye that receives the diverging rays."

- question: "Why is the image formed by a plane mirror described as 'virtual,' and what does this mean for where the light rays actually travel?"
  type: short-answer
  answer: "The image is virtual because the reflected rays diverge — they never actually meet at the image location. After reflecting off the mirror, the rays spread apart as they travel toward the observer's eye. The eye traces these rays backward along straight lines into the mirror, and those backward extensions converge at a point behind the mirror — the apparent image location. But no light physically reaches that point: the mirror surface blocks it. A 'real' image would require the reflected rays to actually converge in space, which only curved mirrors or lenses can achieve. The plane mirror's flat surface can only produce diverging reflected rays, hence a virtual image."
  explanation: "The virtual/real distinction is fundamentally about where the light actually goes. Real images can be caught on a screen because light physically passes through the image point. Virtual images cannot, because the light never reaches the image location — only the backward extrapolations of the reflected rays do. Understanding this distinction is essential for the next topic (spherical mirrors), where both virtual and real images can form depending on object position and mirror curvature."
```

## Explainer

The law of reflection — angle of incidence equals angle of reflection — is the only rule you need to construct a complete theory of plane mirrors. Start with a single point on an object, say the tip of an arrow. Draw two rays leaving that point and striking the mirror at different locations. Apply the law of reflection to each: the outgoing ray bounces away from the surface at the same angle it arrived, measured from the normal to the surface. The two reflected rays now travel away from the mirror in different directions. Your eye, receiving those two diverging rays, automatically traces them backward along straight lines into the mirror. Those backward-traced lines converge at a point *behind* the mirror — that convergence point is the **image**.

The geometry of this construction guarantees two things: the image is as far behind the mirror as the object is in front of it (image distance equals object distance), and the image is the same size as the object. The image is **virtual** because the rays do not actually pass through the image point — they only *appear* to diverge from it. A screen placed behind the mirror would catch no light there. This is the defining difference between a virtual image (apparent convergence of backward-traced rays) and a real image (actual convergence of forward-traveling rays).

The left-right reversal puzzle is worth resolving carefully. A plane mirror does not swap left and right; it swaps front and back — it maps the z-axis (depth) into its mirror while leaving x (horizontal) and y (vertical) unchanged. What you perceive as left-right reversal is actually a cognitive reinterpretation: you imagine *turning around* to face your image, and that mental rotation is what swaps left and right in your perception. Hold text up to a mirror and it appears reversed because you are mentally rotating it; hold it up to a window and look at the reflection from outside — same reversal, same reason. The mirror itself is indifferent to handedness in the horizontal sense.

Finally, the half-height rule: to see your full reflection you need a mirror of exactly half your height, mounted so its top is at halfway between your eyes and your head. This seems counterintuitive — surely walking closer would require a larger mirror? But because image distance equals object distance, both you and your image move closer together as you approach the mirror. The angle subtended stays constant. The minimum mirror size is fixed by your geometry, not your distance. This elegant result follows directly from the equal-angle reflection law applied to the extreme rays from your head and feet.
