---
id: compound-optical-systems
title: 'Compound Optical Systems: Lenses and Mirrors in Combination'
domain: physics
course: waves-and-optics
prerequisites:
- id: lens-combinations
  type: hard
builds-toward:
- optical-instruments
tags:
- compound-systems
- lens-combinations
- system-design
stage: formal-systems
status: draft
---

# Compound Optical Systems: Lenses and Mirrors in Combination

## Core Idea
In compound systems, the image from one lens/mirror serves as the object for the next. Overall magnification is the product of individual magnifications: M_total = M₁ × M₂ × ... Effective focal length can be calculated from component powers: 1/f_eff = 1/f₁ + 1/f₂ - d/(f₁f₂) with separation d.

## Questions

```yaml
- question: "A two-lens system has magnifications M₁ = −3 and M₂ = −2. What is the total magnification of the system?"
  type: multiple-choice
  options:
    - "−5 (magnifications add)"
    - "+6 (product, two sign flips)"
    - "−6 (product, sign retained)"
    - "+1 (they cancel)"
  answer: 1
  explanation: "Total magnification in a compound system is the *product* of individual magnifications: M_total = M₁ × M₂ = (−3)(−2) = +6. The positive sign means the final image is upright relative to the original object — two inversions cancel. A common error is to add the magnifications (−3 + −2 = −5), but magnifications multiply because each lens applies its transformation to the output of the previous one."

- question: "Two thin lenses with focal lengths f₁ and f₂ are placed in contact (separation d = 0). What is the effective focal length of the combined system?"
  type: multiple-choice
  options:
    - "f_eff = f₁ + f₂"
    - "f_eff = (f₁ + f₂) / 2"
    - "1/f_eff = 1/f₁ + 1/f₂"
    - "1/f_eff = 1/f₁ − 1/f₂"
  answer: 2
  explanation: "The general formula is 1/f_eff = 1/f₁ + 1/f₂ − d/(f₁f₂). When d = 0, the last term vanishes, giving 1/f_eff = 1/f₁ + 1/f₂. This is the optical power additive rule: powers (P = 1/f, measured in diopters) add directly when lenses are in contact. Note that focal lengths do NOT add directly — it is the reciprocals (powers) that add."

- question: "In a compound microscope, the intermediate image formed by the objective lens is a real, magnified image that serves as the object for the eyepiece."
  type: true-false
  answer: true
  explanation: "This is exactly the chain rule of compound optics: the objective forms a real, inverted, magnified image of the specimen somewhere inside the instrument body. The eyepiece then acts as a magnifying glass viewing that intermediate image. If the intermediate image were virtual, the eyepiece could not form a final real image. The two lenses multiply their magnifications precisely because one's output is the other's input."

- question: "In a compound microscope, the total magnification equals the sum of the objective magnification and the eyepiece magnification."
  type: true-false
  answer: false
  explanation: "Magnifications in a compound optical system *multiply*, not add. A 10× objective combined with a 10× eyepiece gives 100× total, not 20×. This multiplicative behavior is the whole point of compound systems — it is why a microscope can achieve magnifications that a single lens of any practical focal length could not."

- question: "Why does a compound microscope achieve much greater magnification than a single lens with the same objective focal length?"
  type: short-answer
  answer: "The objective forms a magnified real intermediate image, which the eyepiece then re-magnifies. Because total magnification is the product of the two individual magnifications, the system multiplies the gains rather than adding them. A single lens producing the same total magnification would require either an impractically short focal length or an impractically large image distance."
  explanation: "The key is that each lens's output becomes the next lens's input, so magnifications compound multiplicatively. The intermediate image also allows each lens to operate in a regime where it performs well — the objective at high magnification over short distances, the eyepiece as a comfortable magnifying glass — rather than asking one lens to do everything at once."
```

## Explainer

From your study of lens combinations, you know the thin-lens equation (1/f = 1/dₒ + 1/dᵢ) and how to calculate where a lens forms an image and how magnified it is. A compound optical system is just the logical extension: instead of stopping after one lens, you take the image that first lens produces and treat it as the object for the next lens. The chain rule of optics — each element's output becomes the next element's input — is the foundational idea.

Here is the procedure concretely. For a two-lens system, first apply the thin-lens equation to lens 1 alone: given the object distance dₒ₁, find image distance dᵢ₁ and magnification M₁ = −dᵢ₁/dₒ₁. Now that image becomes the object for lens 2. If the lenses are separated by distance d, then the object distance for lens 2 is dₒ₂ = d − dᵢ₁. Apply the thin-lens equation again to find dᵢ₂ and M₂. The **total magnification** is M_total = M₁ × M₂ — the magnifications multiply. If M₁ = −3 and M₂ = −2, the system magnifies by 6 and produces an upright image (two sign flips cancel).

The compound microscope is the canonical example. An **objective lens** with short focal length sits close to the specimen, forming a greatly magnified real intermediate image somewhere inside the instrument body. An **eyepiece lens** then acts like a magnifying glass, re-magnifying that intermediate image as you look through it. Neither lens alone could achieve the combined magnification without requiring physically impractical distances. The telescope works similarly but in reverse priority — the objective collects distant parallel light, the eyepiece magnifies the intermediate image — and here angular magnification (ratio of apparent size with vs. without the instrument) is more useful than lateral magnification.

The **effective focal length** formula 1/f_eff = 1/f₁ + 1/f₂ − d/(f₁f₂) handles the general case with arbitrary separation d. Notice the limiting case: when d = 0 (lenses in contact), the last term vanishes and 1/f_eff = 1/f₁ + 1/f₂. This is the **optical power** (in diopters, P = 1/f) additive rule — powers add when elements are in contact. Optometrists use this directly when combining corrective lens prescriptions. Increasing d from zero reduces the effective focal length (for two converging lenses), which is why long-focal-length objectives combined with eyepieces in a telescope tube achieve better magnification than either element alone.
