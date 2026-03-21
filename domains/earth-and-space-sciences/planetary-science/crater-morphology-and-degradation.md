---
id: crater-morphology-and-degradation
title: Crater Morphology and Degradation
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: impact-cratering-mechanics
  type: hard
- id: geomorphology
  type: soft
- id: rock-rheology-elastic-plastic-deformation
  type: soft
builds-toward:
- surface-geology-terrestrial-planets
tags:
- craters
- morphology
- degradation
stage: advanced
status: draft
---

# Crater Morphology and Degradation

## Core Idea
Crater morphology transitions from simple (raised rim, bowl-shaped) to complex (central peak, terraced walls) above a size threshold that depends on surface gravity. Craters degrade through slumping, isostatic adjustment, erosion, and volcanic infilling, with degradation rates varying by planetary environment.

## Questions

```yaml
- question: "A 5 km diameter crater on Earth has terraced walls and a central peak. An identical 5 km crater on the Moon is simple and bowl-shaped. What best explains this difference?"
  type: multiple-choice
  options:
    - "The Moon's crust is weaker than Earth's, so lunar impacts produce simpler craters"
    - "Earth's higher surface gravity causes crater walls to collapse at smaller diameters, producing complex morphology sooner"
    - "Lunar impacts are more energetic, excavating deeper simple craters"
    - "Earth's erosion gradually adds terracing and central peaks to older craters over time"
  answer: 1
  explanation: "The simple-to-complex transition diameter depends on surface gravity. On Earth (strong gravity), walls collapse inward and floors rebound at diameters as small as 2–4 km. On the Moon (weak gravity), the same collapse only occurs above ~15 km. So a 5 km crater can be complex on Earth but simple on the Moon — the same size, but different morphology because gravity differs. Option D is a classic misconception: erosion degrades craters, it does not create central peaks or terraces."

- question: "A planetary scientist observes a crater on Mars with fluvial channels carved into its walls and layered sediments on the floor. What does this primarily indicate?"
  type: multiple-choice
  options:
    - "The impact that formed it was unusually energetic, melting rock and depositing layered ejecta"
    - "The crater is geologically young and has not yet been modified by Martian processes"
    - "Past liquid water activity modified the crater after its formation"
    - "Volcanic intrusion beneath the crater deposited the layered sediments from below"
  answer: 2
  explanation: "Degradation style reveals environmental history. Fluvial channels on crater walls and layered interior sediments are diagnostic of past liquid water — water that carved channels and transported sediment into the basin after the impact event. This is exactly the reasoning behind selecting craters like Gale and Jezero as landing sites: their degradation style indicates ancient aqueous environments. Energetic impacts produce melt sheets, not fluvial channels."

- question: "On the Moon, a crater with sharp rims and bright ejecta rays is relatively young, because lunar degradation is extraordinarily slow compared to Earth."
  type: true-false
  answer: true
  explanation: "The Moon lacks atmosphere, running water, and plate tectonics, so craters degrade only through micrometeorite bombardment and occasional larger impacts. A fresh lunar crater can retain sharp rims and bright rays for hundreds of millions of years. This makes rim sharpness and ray preservation powerful relative age indicators on the lunar surface."

- question: "A larger crater is always more degraded than a smaller crater on the same planetary surface."
  type: true-false
  answer: false
  explanation: "Crater size and degradation state are independent variables. Size depends on impactor energy; degradation depends on time elapsed since formation and the intensity of surface processes. A large fresh crater can be sharper and less degraded than a tiny ancient crater that has been filled with regolith and battered by later impacts. Geologists assess degradation by rim sharpness, ejecta preservation, and superimposed crater density — not by diameter."

- question: "Why does the simple-to-complex transition occur at a smaller diameter on Earth than on the Moon, and what does this imply about using crater morphology to infer surface gravity on other planets?"
  type: short-answer
  answer: "The transition occurs when gravitational forces overwhelm the strength of crater walls, causing them to collapse inward (forming terraces) and allowing the compressed floor to rebound upward (forming a central peak). Higher surface gravity exerts stronger forces, so collapse happens at smaller diameters. On the Moon, where gravity is about one-sixth of Earth's, walls can support themselves up to ~15 km. This means that if you observe the transition diameter on an unknown planetary body, you can estimate surface gravity: a planet where complex craters begin at 5 km has higher gravity than one where the transition occurs at 20 km."
  explanation: "The key is that morphology encodes a balance between gravity and rock strength. Because rock strength is roughly similar across rocky bodies, gravity becomes the dominant variable. Planetary scientists use the transition diameter, measured from crater counts and morphological surveys, as one line of evidence for constraining a body's gravitational environment — which is especially useful for bodies where direct gravity measurements are sparse."
```

## Explainer

From your study of impact cratering mechanics, you know that a hypervelocity impact releases enormous energy, excavating a transient cavity that is much larger than the impactor itself. The **morphology** of the final crater — the shape that persists after the impact event — depends on how the target material responds to that excavation, and this response is governed by crater size, surface gravity, and the mechanical properties of the target rock.

**Simple craters** are the smallest category: clean, bowl-shaped depressions with raised rims and smooth interior walls. On the Moon, simple craters range up to about 15 kilometers in diameter. The transient cavity produced by the impact is roughly preserved because the crater walls are strong enough to support themselves. Above a critical diameter — the **simple-to-complex transition** — gravity overwhelms the strength of the crater walls. The rim collapses inward along concentric faults, forming **terraced walls**, and the crater floor rebounds upward as the compressed rock beneath the impact point relaxes, producing a **central peak**. This rebound is analogous to the central jet you see when you drop a stone into water, but in rock moving at geological timescales during the seconds to minutes of crater modification. On higher-gravity bodies, the transition occurs at smaller diameters: about 15 km on the Moon, but only 2–4 km on Earth, because stronger gravitational forces cause walls to collapse sooner. The very largest impacts produce **multi-ring basins** where concentric rings of mountains surround a broad, flat floor — structures like the Orientale Basin on the Moon that record impacts so energetic that the lithosphere itself flexed and fractured.

Once formed, craters begin to degrade immediately, and the rate and style of degradation depend entirely on the planetary environment. On the Moon, which lacks an atmosphere, running water, and plate tectonics, degradation is extraordinarily slow. Lunar craters degrade primarily through **micrometeorite bombardment** (which gradually rounds rims and fills interiors with regolith), occasional larger impacts that deposit ejecta across older craters, and slow **isostatic adjustment** as the lithosphere relaxes under the crater's mass deficit. A fresh lunar crater retains sharp rims and bright ejecta rays for hundreds of millions of years. On Mars, degradation is faster: wind erosion rounds rims, aeolian sediment fills floors, and ancient water erosion has carved channels into crater walls and deposited layered sediments inside craters like Gale and Jezero. On Earth, degradation is most rapid of all — weathering, erosion, vegetation, sedimentation, and plate tectonics can obliterate craters entirely within tens of millions of years, which is why only about 200 confirmed impact structures are known on Earth despite billions of years of bombardment.

The state of degradation of a crater is therefore a powerful diagnostic tool. On airless bodies, the degree of rim sharpness, ejecta preservation, and superimposed small crater density allows planetary scientists to assign **relative ages** — a fresh, sharp-rimmed crater overlying a degraded, filled one is unambiguously younger. This principle underlies crater counting, the primary method for dating planetary surfaces. On bodies with atmospheres and active geology, the style of degradation reveals the processes that have operated: fluvial channels on crater rims indicate past liquid water, volcanic fills record episodes of volcanism, and wind-sculpted features record atmospheric activity. Understanding crater morphology and degradation thus connects impact physics to surface geology, geochronology, and the environmental history of planetary bodies throughout the solar system.
