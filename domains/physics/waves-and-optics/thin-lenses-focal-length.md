---
id: thin-lenses-focal-length
title: Thin Lenses and Focal Length
domain: physics
course: waves-and-optics
prerequisites:
- id: geometric-optics-ray-approximation
  type: hard
- id: refraction-and-snells-law
  type: hard
builds-toward:
- thin-lens-equation
- lensmakers-equation
tags:
- thin-lens
- focal-length
- converging-diverging
stage: advanced
status: validated
---

# Thin Lenses and Focal Length

## Core Idea
A thin lens is a transparent optical element that refracts light at two surfaces. A converging lens (positive f) bends rays toward the focal point; a diverging lens (negative f) bends rays away. Focal length f is the distance from the lens where parallel rays converge (or appear to diverge). Lens power P = 1/f (in diopters) quantifies the strength of focusing.

## Questions

```yaml
- question: "A lens has focal length f = −20 cm. What type of lens is it, and what happens to parallel rays that pass through it?"
  type: multiple-choice
  options:
    - "Converging lens; parallel rays focus to a real point 20 cm behind the lens"
    - "Diverging lens; parallel rays spread outward and appear to diverge from a virtual point 20 cm in front of the lens"
    - "Converging lens; parallel rays bend toward the axis but never actually converge"
    - "Diverging lens; parallel rays are absorbed and no image is formed"
  answer: 1
  explanation: "Negative focal length is the defining property of a diverging (concave) lens. Parallel rays entering such a lens are bent away from the optical axis, never converging on the far side. Extending those diverging rays backward reveals they appear to originate from a virtual focal point on the same side as the incoming light, at a distance |f| = 20 cm from the lens. Option A is wrong because positive f is converging; negative f is always diverging."

- question: "An optometrist prescribes lenses of +2.5 diopters. What do you know about these lenses?"
  type: multiple-choice
  options:
    - "They are converging lenses with focal length 40 cm, used to correct farsightedness"
    - "They are converging lenses with focal length 2.5 cm, used to correct nearsightedness"
    - "They are diverging lenses with focal length 40 cm, used to correct farsightedness"
    - "They are diverging lenses with focal length 0.4 mm, used to correct astigmatism"
  answer: 0
  explanation: "Power P = 1/f, so f = 1/P = 1/2.5 = 0.4 m = 40 cm. Positive power means a converging lens, which adds focusing power to an eye that cannot converge parallel rays onto the retina — the definition of farsightedness (hyperopia). Nearsightedness requires a diverging (negative power) lens. The common error in option B is forgetting to convert diopters to meters before computing focal length."

- question: "A converging lens usually forms a real, inverted image of any object placed in front of it."
  type: true-false
  answer: false
  explanation: "When an object is placed inside the focal length of a converging lens (object distance < f), the lens acts as a magnifying glass and forms a virtual, upright, magnified image on the same side as the object. A real, inverted image is only formed when the object is beyond the focal point. This is one of the most important subtleties of converging lenses: the same lens can produce fundamentally different image types depending on object position."

- question: "Lens power is defined as P = 1/f (in diopters) rather than just using focal length because powers of lenses in contact add directly, making compound lens calculations simple."
  type: true-false
  answer: true
  explanation: "When two thin lenses are placed in contact, the combined focal length satisfies 1/f_total = 1/f₁ + 1/f₂, which means P_total = P₁ + P₂. This additive property makes diopters the natural unit for optometrists and optical engineers who combine multiple elements. If focal lengths were used directly, the combined focal length would require a more complex formula. The diopter system also makes it immediately obvious whether a combination is converging (net positive power) or diverging (net negative)."

- question: "Why is lens power defined as P = 1/f rather than simply using focal length f to describe a lens's strength? What physical relationship motivates this definition?"
  type: short-answer
  answer: "Power measures the bending strength of a lens per unit distance. A shorter focal length means light is bent more strongly — the lens converges (or diverges) parallel rays more sharply. Because bending strength is inversely proportional to focal length, P = 1/f captures this directly: doubling the bending strength halves the focal length and doubles the power. The diopter definition also enables simple addition of powers when lenses are combined in contact, reflecting the fact that refractive deflections from successive surfaces accumulate."
  explanation: "The underlying physics is that each lens surface deflects a ray by an angle proportional to the surface's curvature and the refractive index difference. Total deflection determines focal length. A 'stronger' lens deflects more, producing a shorter f and higher P = 1/f. This inverse relationship makes P the natural measure of lens strength, just as spring constant k (not 1/k) is the natural measure of spring stiffness because force is directly proportional to k."
```

## Explainer

You already know two things that are all you need to understand thin lenses: the geometric optics ray approximation (light travels in straight rays, bending only at interfaces) and Snell's law (rays bend toward the normal when entering a denser medium and away from it when exiting). A lens is simply two curved refracting surfaces in close succession. Each surface bends the ray a little according to Snell's law; the combined effect determines where parallel incoming rays end up.

Consider a **converging (convex) lens** with both surfaces curving outward. A ray entering near the top of the lens strikes the first surface tilted toward the normal, bends downward (toward the optical axis), crosses the lens, and bends downward again at the exit surface. A ray entering at the center passes through without bending because it hits both surfaces at normal incidence. The result: all rays entering the lens parallel to the axis converge to a single point on the other side — the **focal point**. The distance from the lens center to this point is the **focal length** *f*. The focal length is positive for a converging lens: parallel light comes to a real focus on the far side.

A **diverging (concave) lens** curves inward. The same analysis reverses: parallel rays entering the lens are bent *away* from the axis and emerge spreading outward. Tracing those diverging rays backward (just as you did with virtual images in plane mirrors) reveals that they appear to diverge from a point on the *same* side as the incoming light — a virtual focal point. The focal length is negative for a diverging lens. The sign convention is consistent: positive *f* means converging power, real focus on the transmission side; negative *f* means diverging power, virtual focus on the incoming side.

**Lens power** P = 1/f measured in diopters (m⁻¹) quantifies how strongly a lens bends light. A short focal length means strong bending — high power. A long focal length means gentle bending — low power. This is why your optometrist prescribes lenses in diopters: +2.0 D is a converging lens with f = 0.5 m used to correct farsightedness; −3.0 D is a diverging lens with f ≈ 0.33 m used to correct nearsightedness. Powers add when lenses are placed in contact, which is why compound lenses in cameras and telescopes combine multiple elements to achieve a desired total power with fewer aberrations than a single thick lens could provide.
