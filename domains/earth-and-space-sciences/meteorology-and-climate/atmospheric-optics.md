---
id: atmospheric-optics
title: 'Atmospheric Optics: Sky Color, Rainbows, Halos, and Mirages'
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: dispersion-and-prisms
  type: hard
- id: cloud-formation-and-types
  type: soft
- id: refraction-interface-snell-relation
  type: soft
- id: atmospheric-inversion-temperature
  type: soft
builds-toward: []
tags:
- optics
- scattering
- rainbow
- halo
- mirage
- rayleigh-scattering
stage: formal-systems
status: validated
---

# Atmospheric Optics: Sky Color, Rainbows, Halos, and Mirages

## Core Idea
Many sights in the sky come from three things light can do in the atmosphere: scatter off molecules and particles, refract and reflect inside water drops and ice crystals, and bend through layers of air at different temperatures. Air molecules scatter short (blue) wavelengths much more strongly than long (red) ones, which makes the sky blue and sunsets red. Raindrops refract and reflect sunlight into rainbows, and six-sided ice crystals refract it into halos and sun dogs. Air layers of different density bend light into mirages.

## How It's Best Learned
Use a glass of water or a glass sphere and a flashlight to show light bending and reflecting inside a "drop." Then go outside: stand with your back to the Sun and spray a fine mist to make a rainbow, and measure its angle with an outstretched hand. Have students sketch the path of light for each effect and name the process involved: scattering, refraction, reflection, or diffraction.

## Common Misconceptions
- The sky is blue because it reflects the ocean. (The sky is blue over deserts and land too; air molecules scatter blue light more than red light.)
- A rainbow is an object at a fixed place, so you could walk to its end. (A rainbow is a set of directions about 42° from the point directly opposite the Sun; each observer sees light from different drops, and the bow moves as you move.)
- Clouds are white because they contain no water. (Cloud droplets are large compared with the wavelength of light and scatter all colors about equally, so the scattered light looks white.)
- A mirage on a hot road is water on the road. (It is an image of the sky, bent upward by the hot, less dense air just above the road surface.)

## Questions

```yaml
- question: "Why is the Sun reddish at sunset?"
  type: multiple-choice
  options:
    - "The Sun gives off more red light in the evening"
    - "Sunlight passes through a much longer path of air, and scattering removes much of the blue light before it reaches you"
    - "Red light is reflected off the ground into the sky"
    - "The Sun is closer to Earth at sunset"
  answer: 1
  explanation: "Scattering by air molecules increases sharply at shorter wavelengths (about as 1/λ⁴). Near the horizon, sunlight crosses many times more air than at noon, so most of the blue is scattered out of the direct beam and the light that remains looks orange or red."

- question: "To see a rainbow, where must the Sun be relative to you and the rain?"
  type: short-answer
  answer: "The Sun must be behind you, and the rain must be in front of you. The primary bow appears as a circle of about 42° radius centered on the antisolar point, the point directly opposite the Sun."
  explanation: "Light enters each drop, reflects once off the back, and exits toward the observer at about 42° from the direction opposite the Sun. If the Sun is higher than about 42° above the horizon, the primary bow is below the horizon for a ground observer."

- question: "In a secondary rainbow, the order of colors is the reverse of the primary rainbow, with red on the inside."
  type: true-false
  answer: true
  explanation: "The secondary bow forms from two internal reflections in each drop, which reverses the color order. It appears at about 51° from the antisolar point and is fainter. The sky between the two bows is darker and is called Alexander's dark band."

- question: "A bright ring of radius about 22° appears around the Sun when thin, high cirrostratus clouds cover the sky. What causes it?"
  type: multiple-choice
  options:
    - "Diffraction of light by small water droplets"
    - "Refraction of sunlight through six-sided ice crystals"
    - "Reflection of sunlight off the ocean"
    - "Scattering by air molecules"
  answer: 1
  explanation: "Hexagonal ice crystals act like prisms with a 60° angle between alternate faces. Light passing through them is bent by a minimum of about 22°, so light piles up at that angle and forms the 22° halo. Diffraction by small droplets makes coronas, which are much smaller rings close to the Sun or Moon."
```

## Explainer
You already know that light bends, or refracts, when it passes from one medium to another, and that the amount of bending depends slightly on wavelength. That is why a prism spreads white light into colors. The atmosphere is full of natural prisms, mirrors, and scatterers, and the results are some of the most familiar sights in the sky.

**Scattering** explains sky color. Air molecules are far smaller than the wavelength of visible light. This kind of scattering, called Rayleigh scattering, is much stronger for short wavelengths, varying roughly as one over the wavelength to the fourth power. Blue light is therefore scattered across the sky far more than red light, and the sky looks blue from every direction. At sunset, sunlight travels through a much longer path of air. So much blue is scattered out of the direct beam that the Sun and nearby clouds look orange and red. Cloud droplets are much larger than light waves. They scatter all colors about equally, so clouds look white, or gray when they are thick enough to block light.

**Rainbows** need sunlight behind you and falling drops in front of you. Light enters a drop, refracts, reflects off the back, and refracts again as it leaves. The light comes back most strongly at about 42° from the antisolar point, the point directly opposite the Sun. Red bends least and appears on the outside of the bow. Some light reflects twice inside the drop and forms a fainter secondary bow at about 51°, with colors reversed.

**Halos** come from ice. In thin cirrostratus clouds, six-sided ice crystals bend light by at least about 22°, so a bright ring appears 22° from the Sun or Moon. When flat plate crystals float with their faces horizontal, bright spots called sun dogs appear about 22° to each side of the Sun.

**Mirages** come from air layers of different temperature. Over a hot road, the air near the surface is hot and less dense. Light from the sky bends upward as it passes through this layer, so you see an image of the sky on the road that looks like water. Over very cold surfaces, the bending goes the other way, and distant objects can appear raised above the horizon.
