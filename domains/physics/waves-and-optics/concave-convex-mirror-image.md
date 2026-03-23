---
id: concave-convex-mirror-image
title: 'Spherical Mirrors: Focal Length and Image Formation'
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-angle-geometry
  type: hard
builds-toward:
- lens-equation-magnification-formula
tags:
- mirrors
- optics
stage: formal-systems
status: validated
---

# Spherical Mirrors: Focal Length and Image Formation

## Core Idea
A spherical mirror's focal length f = R/2 (R = radius of curvature) is the distance from the mirror where parallel rays converge (concave) or appear to diverge (convex). The mirror equation 1/s_o + 1/s_i = 1/f relates object and image distances. Magnification m = -s_i/s_o. Concave mirrors form real images (inverted) when s_o > f; convex mirrors form only virtual images (upright).

## How It's Best Learned
Trace rays for objects at different distances to understand when real vs. virtual images form and their orientation.

## Common Misconceptions
A convex mirror cannot form a real image—it always forms a virtual, upright, diminished image.

## Questions

```yaml
- question: "An object is placed 5 cm from a concave mirror with focal length 10 cm. Using the mirror equation, what type of image forms and where?"
  type: multiple-choice
  options:
    - "A real image 10 cm in front of the mirror — the focal point is the natural image location."
    - "A real image between the mirror and the focal point."
    - "A virtual image 10 cm behind the mirror — the negative image distance places it behind the surface."
    - "No image forms because the object is inside the focal length."
  answer: 2
  explanation: "Using 1/s_i = 1/f − 1/s_o = 1/10 − 1/5 = −1/10, so s_i = −10 cm. The negative value means the image is virtual and located 10 cm behind the mirror. When the object is closer than the focal length (s_o < f), reflected rays diverge and never converge in front of the mirror — tracing them backward places a virtual, upright, magnified image behind the surface. This is exactly how a makeup mirror works. Option D is a common misconception: an image always forms, its nature just changes."

- question: "Without calculating, can you determine whether a convex mirror will ever form a real image for an object placed in front of it?"
  type: multiple-choice
  options:
    - "Yes — if the object is far enough away, the image becomes real."
    - "Yes — if the object is placed between the mirror and its focal point, a real image forms."
    - "No — a convex mirror has a negative focal length, so s_i is always negative regardless of object distance."
    - "Only if the object is placed exactly at the center of curvature."
  answer: 2
  explanation: "A convex mirror has f < 0 (focal point behind the mirror). In the equation 1/s_i = 1/f − 1/s_o, with f < 0 and s_o > 0 (real object in front), 1/f is negative and 1/s_o is positive, so their difference is always negative — meaning s_i is always negative. A negative image distance always means a virtual image behind the mirror. No object position changes this. This is why convex mirrors always produce diminished, upright, wide-field virtual images used in security mirrors and car side mirrors."

- question: "A concave mirror can form either a real or a virtual image of the same object, depending on where the object is placed relative to the focal point."
  type: true-false
  answer: true
  explanation: "True. When the object is beyond the focal point (s_o > f), reflected rays converge in front of the mirror, forming a real, inverted image. When the object is inside the focal point (s_o < f), reflected rays diverge and the image is virtual, upright, and magnified — located behind the mirror. The focal point is the dividing line. A concave makeup mirror places your face inside the focal length; a concave solar concentrator places the target beyond it."

- question: "A convex mirror can form a real image if the object is placed far enough away from the mirror."
  type: true-false
  answer: false
  explanation: "False. A convex mirror has a negative focal length, which guarantees s_i < 0 for any real object (s_o > 0). No matter how far the object is, the mirror equation gives a negative image distance — always virtual, always behind the mirror. This is the misconception the Common Misconceptions section flags directly: convex mirrors form only virtual, upright, diminished images regardless of object position."

- question: "Using the mirror equation, explain why a concave mirror forms a virtual image when the object is placed closer than the focal length."
  type: short-answer
  answer: "When s_o < f, the term 1/s_o > 1/f, so 1/s_i = 1/f − 1/s_o is negative, giving s_i < 0. A negative image distance means the image is on the same side as the incoming light — behind the mirror surface — where no real reflected rays converge. Physically, when the object is inside the focal length, the concave surface cannot bend the reflected rays enough to make them converge in front of the mirror; they remain divergent. Tracing these diverging rays backward locates a virtual image from which they appear to originate, behind the mirror."
  explanation: "The sign of s_i is the key diagnostic: positive means real (light actually converges there in front of the mirror), negative means virtual (reflected rays only appear to come from that point behind the mirror). The mirror equation algebraically encodes the geometric transition that occurs when the object crosses the focal point."
```

## Explainer

You already know from reflection-angle geometry that the angle of incidence equals the angle of reflection. Spherical mirrors apply that law to a curved surface, and the curvature introduces something powerful: parallel incoming rays no longer reflect randomly — they all converge toward (or diverge away from) a single point called the **focal point**. For a concave mirror, parallel rays reflect inward and meet at the focal point in front of the mirror. For a convex mirror, they reflect outward and appear to come from a focal point behind the mirror. In both cases, the focal length f = R/2, where R is the radius of the sphere the mirror's surface belongs to — half the radius of curvature.

The **mirror equation** 1/s_o + 1/s_i = 1/f ties together three quantities: the object distance s_o (how far the object sits from the mirror), the image distance s_i (how far the resulting image sits from the mirror), and the focal length. When you solve for s_i, you immediately learn two things: where the image forms and whether it is real or virtual. Positive s_i means the image forms in front of the mirror — where light actually goes after reflecting — and is therefore a **real image**. Negative s_i means the image appears to be behind the mirror, where no light actually travels, making it a **virtual image**.

**Magnification** m = −s_i/s_o tells you both size and orientation. A negative m means the image is inverted; positive m means upright. A |m| > 1 means the image is larger than the object; |m| < 1 means smaller. For a concave mirror, the character of the image depends entirely on where the object sits relative to the focal point: when s_o > f, light has room to converge and a real, inverted image forms. Move the object inside the focal length (s_o < f), and the reflected rays diverge — they never cross in front of the mirror, so you trace them backward and find a virtual, upright, magnified image behind it. This is exactly how a makeup mirror works.

Convex mirrors have a negative focal length (the focal point is behind the mirror), so s_i always comes out negative regardless of where you place the object. The image is always virtual, upright, and smaller than the object — but it covers a wide field of view, which is why convex mirrors are used for security corners and vehicle side mirrors. The key discipline when working these problems is tracking sign conventions rigorously: front of the mirror is positive, back is negative, and the sign of s_i tells you immediately whether the image is real or virtual.
