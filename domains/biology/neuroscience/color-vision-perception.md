---
id: color-vision-perception
title: 'Color Vision: Three Cone Types and Trichromatic Perception'
domain: biology
course: neuroscience
prerequisites:
- id: photoreceptors-phototransduction
  type: hard
tags:
- sensory-systems
- vision
- color-perception
stage: advanced
status: draft
---

# Color Vision: Three Cone Types and Trichromatic Perception

## Core Idea
Humans and many primates have three types of cone photoreceptors with peak sensitivities to short (blue), medium (green), and long (red) wavelengths. Color is computed by comparing responses across cone types; the brain infers color from relative activation patterns rather than from single-wavelength encoding.

## Explainer

From your study of photoreceptors and phototransduction, you know that light striking the retina activates photopigments in rod and cone cells, triggering a signaling cascade that ultimately changes the cell's membrane potential. Rods handle dim-light vision with a single photopigment, which is why nighttime vision is colorless. Color vision depends on **cones**, and specifically on having multiple cone types with different spectral sensitivities. Humans possess three: **S-cones** (short-wavelength, peaking around 420 nm in the blue range), **M-cones** (medium-wavelength, peaking around 530 nm in the green range), and **L-cones** (long-wavelength, peaking around 560 nm in the red range). This arrangement is called **trichromacy**.

The crucial insight is that no single cone "sees" a color. Each cone type responds to a broad range of wavelengths — their sensitivity curves overlap substantially. A photon of 550 nm light will strongly activate both M-cones and L-cones, and weakly activate S-cones. The brain determines color not from any one cone's output, but from the **ratio of activation across all three types**. Yellow light produces a particular M:L:S ratio; so does a mixture of red and green light that has no yellow wavelengths at all. If the ratios match, you perceive the same color — this is why your TV screen, which has only red, green, and blue pixels, can produce the full spectrum of perceived colors. Color is a computational inference, not a direct wavelength measurement.

This comparison begins in the retina itself through **opponent processing**. Retinal ganglion cells and neurons in the lateral geniculate nucleus do not simply relay cone signals — they compute differences. **Red-green opponent cells** compare L-cone and M-cone inputs: they are excited by one and inhibited by the other, creating a channel that signals "more red" or "more green." **Blue-yellow opponent cells** compare S-cone input against the combined L+M signal. A third channel computes overall luminance (light vs. dark) from the sum of cone responses. These three channels — red/green, blue/yellow, and light/dark — are the axes along which human color perception is organized, which is why you never perceive "reddish green" or "bluish yellow" as single colors.

**Color blindness** reveals this system's genetic basis. The genes for L-cone and M-cone photopigments sit next to each other on the X chromosome and are nearly identical in sequence, making them prone to deletion or recombination errors. The most common form, red-green color blindness (affecting ~8% of males), results from loss or alteration of either the L-cone or M-cone pigment, collapsing the red-green opponent channel. Affected individuals still see color — they retain the blue-yellow and luminance channels — but cannot distinguish colors that differ primarily in the red-green dimension. The fact that losing one cone type degrades color perception without eliminating it confirms that color vision is genuinely a comparison across channels, not a property of any single receptor.
