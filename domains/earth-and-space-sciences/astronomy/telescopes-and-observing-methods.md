---
id: telescopes-and-observing-methods
title: Telescopes and Observing Methods
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: electromagnetic-spectrum-astronomy
  type: hard
- id: refraction-intro
  type: soft
- id: reflection-law
  type: soft
- id: electromagnetic-waves
  type: soft
- id: thin-lens-equation
  type: soft
- id: diffraction-gratings
  type: soft
- id: celestial-coordinates
  type: soft
builds-toward:
- stellar-spectral-classification
- stellar-properties-luminosity-temperature
tags:
- telescopes
- refractors
- reflectors
- radio-telescopes
- angular-resolution
- aperture
- interferometry
stage: concrete-operations
status: validated
---
# Telescopes and Observing Methods

## Core Idea
Telescopes gather and focus electromagnetic radiation to detect faint or distant objects. Refracting telescopes use lenses; reflecting telescopes use mirrors — most modern large telescopes are reflectors because large mirrors are cheaper to fabricate than equivalent lenses. Angular resolution, the ability to distinguish close objects, scales with aperture divided by wavelength, so radio telescopes require much larger dishes than optical telescopes for comparable resolution. Interferometric arrays like the VLA and Event Horizon Telescope combine signals from widely spaced antennas to achieve extraordinary resolution.

## How It's Best Learned
Compare the design tradeoffs between refractors and reflectors, then explore how interferometry achieves super-resolution. Calculate theoretical resolutions for telescopes of different apertures and wavelengths using the Rayleigh criterion.

## Common Misconceptions
- Magnification is not the primary purpose of an astronomical telescope — light-gathering power and angular resolution are far more important.
- The Hubble Space Telescope's advantage is not its mirror size but its location above Earth's turbulent, blurring atmosphere.

## Explainer

You already understand that electromagnetic radiation spans a vast spectrum — from radio waves with wavelengths of meters to gamma rays at fractions of a nanometer — and that astronomical objects emit across this entire range. A telescope is fundamentally a device for collecting as much of that radiation as possible and bringing it to a focus where it can be analyzed. The two core properties that determine a telescope's capability are its **light-gathering power** (proportional to the area of its aperture) and its **angular resolution** (the smallest angular separation it can distinguish between two sources). Magnification, despite popular belief, is secondary — making a faint, blurry image larger just gives you a larger faint, blurry image.

**Refracting telescopes** use lenses to bend light to a focus, applying the principle of refraction you studied in optics. The first astronomical telescopes, including Galileo's, were refractors. However, lenses have fundamental limitations at large sizes: they suffer from **chromatic aberration** (different wavelengths focus at different points), they can only be supported at their edges (causing sag under gravity), and glass must be optically perfect throughout its volume. For these reasons, the largest refractor ever built — the Yerkes 40-inch — dates from 1897, and no larger one has been attempted. **Reflecting telescopes** use curved mirrors instead, which reflect all wavelengths equally (eliminating chromatic aberration), can be supported across their entire back surface, and need only one optically perfect surface. Virtually all modern research telescopes are reflectors, with primary mirrors ranging from 1 meter to the 39-meter segmented mirror of the upcoming Extremely Large Telescope.

The theoretical angular resolution of any telescope is set by the **Rayleigh criterion**: θ ≈ 1.22 λ/D, where λ is the observing wavelength and D is the aperture diameter. This formula reveals why radio astronomy requires enormous structures. At a wavelength of 21 cm (the hydrogen line), a single dish would need to be kilometers across to match the resolution of a modest optical telescope operating at 500 nm. The solution is **interferometry**: combining signals from an array of widely separated antennas to synthesize the resolving power of a single dish as large as the maximum baseline between them. The **Very Large Array** (VLA) in New Mexico uses 27 antennas spread across 36 km, and the **Event Horizon Telescope** links dishes across the entire globe to achieve the angular resolution needed to image a black hole's shadow.

For ground-based optical and infrared telescopes, Earth's atmosphere imposes a practical resolution limit far worse than the Rayleigh criterion. Turbulent cells in the atmosphere refract starlight along constantly shifting paths, smearing point sources into blobs roughly 1 arcsecond across — a phenomenon called **seeing**. Two strategies address this. Space telescopes like Hubble and JWST avoid the atmosphere entirely, achieving diffraction-limited performance with relatively modest mirrors (2.4 m and 6.5 m respectively). Ground-based telescopes use **adaptive optics**: a deformable mirror whose surface is adjusted hundreds of times per second, guided by measurements of a natural or laser-generated guide star, to cancel atmospheric distortion in real time. With adaptive optics, 8–10 meter ground-based telescopes can match or exceed Hubble's resolution in the near-infrared.

Beyond imaging, telescopes serve as platforms for **spectroscopy** — dispersing collected light into its component wavelengths to reveal the chemical composition, temperature, velocity, and magnetic fields of astronomical sources. Diffraction gratings, which you encountered in wave optics, are the key dispersive element in most modern spectrographs. Multi-object spectrographs can observe hundreds of targets simultaneously by positioning optical fibers across the focal plane, enabling the massive surveys that map the structure and chemical history of the Milky Way and the large-scale distribution of galaxies.
