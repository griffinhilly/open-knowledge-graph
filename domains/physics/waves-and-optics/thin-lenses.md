---
id: thin-lenses
title: 'Thin Lenses: Converging and Diverging'
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-intro
  type: hard
- id: snells-law
  type: soft
builds-toward:
- thin-lens-equation
- lens-combinations
- optical-instruments
tags:
- thin lens
- converging lens
- diverging lens
- focal point
- principal axis
stage: formal-systems
status: validated
---

# Thin Lenses: Converging and Diverging

## Core Idea
A thin lens refracts light at two surfaces such that parallel rays converge to (or diverge from) a focal point. Converging (convex) lenses have positive focal length and can form real or virtual images; diverging (concave) lenses have negative focal length and always form virtual, upright, reduced images. The three principal rays for lenses parallel the rays used for mirrors: parallel ray, focal ray, and central ray through the optical center.

## How It's Best Learned
Use a converging lens to project an image of a distant window onto a sheet of paper and measure f. Then draw ray diagrams for objects at dₒ > 2f, dₒ = 2f, f < dₒ < 2f, and dₒ < f, tabulating image properties systematically.

## Common Misconceptions
- The 'thin lens' approximation assumes lens thickness is negligible compared to focal length; thick lenses require a more complex model.
- Diverging lenses cannot form real images, ever — a common exam trap.

## Questions

```yaml
- question: "A movie projector needs to cast a large, sharp image onto a screen several meters away. Which lens configuration achieves this?"
  type: multiple-choice
  options:
    - "A diverging lens with the film slide placed inside the focal length"
    - "A converging lens with the film slide placed between f and 2f"
    - "A converging lens with the film slide placed beyond 2f"
    - "Either lens type can project an image with the right screen distance"
  answer: 1
  explanation: "A projector needs a real, inverted, magnified image — which requires a converging lens with the object (slide) placed between f and 2f. In that configuration, the image forms beyond 2f on the far side, is real (it can be projected onto a screen), inverted, and magnified. If the slide were beyond 2f, the image would be real and inverted but reduced. Diverging lenses can never project a real image under any circumstances."

- question: "An object is placed 8 cm in front of a converging lens with focal length 12 cm. Where does the image form and what are its properties?"
  type: multiple-choice
  options:
    - "Beyond the lens — real, inverted, and reduced"
    - "Beyond the lens — real, inverted, and magnified"
    - "On the same side as the object — virtual, upright, and magnified"
    - "At the focal point on the far side of the lens"
  answer: 2
  explanation: "The object is at 8 cm, inside the focal length of 12 cm (d_o < f). When an object is inside f for a converging lens, the refracted rays still diverge after the lens — they cannot converge to a real image on the far side. Their backward extensions meet on the same side as the object, producing a virtual, upright, magnified image. This is exactly how a magnifying glass works."

- question: "A diverging lens can form a real image if the object is placed far enough away from the lens."
  type: true-false
  answer: false
  explanation: "Diverging lenses always produce virtual images — this is a firm rule with no exceptions based on object distance. A diverging lens spreads rays outward; no matter how far the object, parallel incoming rays are still bent to diverge, appearing to come from a virtual focal point on the incoming side. Real images require rays that actually converge on the far side, which a diverging lens cannot produce regardless of object placement."

- question: "When an object is placed between the focal point and a converging lens, the lens acts as a magnifying glass, producing a virtual, upright, enlarged image."
  type: true-false
  answer: true
  explanation: "With the object inside the focal length (d_o < f), a converging lens cannot converge the rays to a point on the far side — they still diverge after refraction. Looking through the lens from the far side, you trace these diverging rays backward and find they appear to originate from a point on the same side as the object — further away and larger. This virtual, upright, magnified image is the defining behavior of a magnifying glass."

- question: "Explain why the character of the image formed by a converging lens changes so dramatically when the object crosses the focal point."
  type: short-answer
  answer: "When the object is outside the focal length, rays from each object point arrive at the lens at angles that allow the lens's bending to converge them to a real meeting point on the far side. When the object moves inside f, those rays arrive at steeper angles — the lens still bends them, but not enough to make them cross on the far side. They continue to diverge after the lens, and only their backward extensions appear to converge on the same side as the object. The focal point is exactly the transition: at d_o = f, the emerging rays are parallel and converge 'at infinity.'"
  explanation: "The focal point marks the boundary between the converging and diverging output regimes. Beyond f, emerging rays converge (real image on the far side). Inside f, they diverge (virtual image traced back to the near side). At exactly f, they emerge parallel — the image distance becomes infinite. Understanding this transition is key to predicting image type and location for any object distance."
```

## Explainer

You already know from refraction that light bends when it crosses from one medium into another, with the bending angle determined by Snell's law and the refractive indices involved. A lens is simply two curved refracting surfaces working together to redirect light in a controlled and predictable way. The **thin lens approximation** treats both surfaces as coincident — valid when lens thickness is much smaller than its focal length — which lets us ignore the small displacement between entry and exit refractions and treat the whole lens as a single, instantaneous bending element.

The defining concept is the **focal point**. For a **converging lens** (thicker at center, like a magnifying glass), all rays arriving parallel to the **optical axis** are refracted and meet at a single point on the other side — the focal point F. The distance from the lens center to F is the **focal length** f, which is positive for converging lenses. A **diverging lens** (thinner at center) bends rays outward, so parallel incoming rays appear to *come from* a focal point on the same side they entered — a virtual focal point, giving a negative focal length.

Ray diagrams give you an exact geometric method for finding image location and properties. Three principal rays are sufficient: (1) a ray entering parallel to the optical axis exits through F on the far side; (2) a ray entering through F on the near side exits parallel to the axis; (3) a ray passing through the optical center is undeviated. Where any two of these rays meet is where the image forms. If they diverge after the lens and only their backward extensions meet, the image is virtual — located on the same side as the object.

For a converging lens, image character depends sharply on object distance relative to f. With the object beyond 2f, the image is real, inverted, and reduced. Between f and 2f, it's real, inverted, and magnified — the configuration used in projectors. Inside f, rays diverge after the lens, and you see a virtual, upright, magnified image on the same side as the object — exactly how a magnifying glass works. A diverging lens, by contrast, always produces virtual, upright, reduced images regardless of object distance; since it never converges rays to a point, it can never form a real image. This is a firm rule worth memorizing: diverging lens → virtual image, always.
