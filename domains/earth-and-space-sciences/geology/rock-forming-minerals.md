---
id: rock-forming-minerals
title: Rock-Forming Minerals
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: minerals-and-crystal-structure
  type: hard
- id: ionic-bonding
  type: soft
- id: covalent-bonding
  type: soft
builds-toward:
- igneous-rocks
- sedimentary-rocks
- metamorphic-rocks
- weathering-and-erosion
- soil-formation
tags:
- silicates
- minerals
- feldspars
- quartz
- mafic
- felsic
stage: formal-systems
status: validated
---

# Rock-Forming Minerals

## Core Idea
The vast majority of Earth's crust is composed of a small subset of minerals called rock-forming minerals, dominated by silicates—minerals built around silicon-oxygen tetrahedra (SiO₄). The silicate framework structure (isolated, chain, sheet, and framework silicates) controls a mineral's melting temperature and resistance to weathering. Feldspars, quartz, micas, pyroxenes, amphiboles, and olivine together constitute over 90% of crustal rocks. Understanding which minerals form under which pressure-temperature conditions is the foundation for interpreting rock history.

## How It's Best Learned
Learning to identify the major rock-forming minerals by their diagnostic properties (cleavage angles for feldspars vs. pyroxenes, lack of cleavage in quartz) is more durable than memorizing chemical formulas. Classifying minerals as felsic (quartz, feldspar) vs. mafic (olivine, pyroxene) provides a quick framework for predicting rock composition.

## Common Misconceptions
- Quartz and feldspar look similar but are distinguished by cleavage: quartz has none, feldspar has two cleavage planes at ~90°.
- 'Silica' refers to SiO₂ (quartz or amorphous), not to the entire silicate mineral class.
- Mafic minerals are denser and darker than felsic minerals due to iron and magnesium content, not due to any property of silicon.

## Questions

```yaml
- question: "A geologist finds a well-sorted sandstone composed of over 95% quartz grains with almost no feldspar, pyroxene, or other minerals. What does this mineral composition tell her about the sediment's history?"
  type: multiple-choice
  options:
    - "The original rock was granite, which is naturally quartz-rich and would produce quartz-dominated sediment"
    - "The sediment underwent intense and prolonged weathering and transport, destroying all less-resistant minerals until only chemically durable quartz survived"
    - "The deposit formed quickly from a nearby source, as rapid burial preserves original mineralogy"
    - "The sediment came from an oceanic crust source, which is naturally quartz-rich"
  answer: 1
  explanation: "Mineralogical maturity — dominance by quartz — is a record of weathering history, not simply original source composition. Even granite (rich in both quartz and feldspar) would initially produce sediment containing both minerals. Prolonged weathering destroys feldspars, pyroxenes, and amphiboles (which decompose to clay minerals), while quartz — fully bonded in a three-dimensional SiO₂ framework with no weak cleavage planes — survives nearly indefinitely. A quartz-dominated sandstone is thus a 'mature' sediment reworked extensively over time. Option C is backwards: rapid burial actually preserves less-stable minerals (immature sediment)."

- question: "Mica flakes into perfect thin sheets along a single plane, while quartz fractures irregularly in all directions. Both are silicates — what best explains this difference?"
  type: multiple-choice
  options:
    - "Quartz is harder than mica (higher Mohs hardness), making it resistant to splitting"
    - "Mica's sheet silicate structure shares three of four oxygens in flat layers, creating planes of weak interlayer bonding; quartz shares all four oxygens three-dimensionally, leaving no preferential planes"
    - "Mica contains water molecules trapped between layers that act as a lubricant for splitting"
    - "Mica is an isolated silicate where tetrahedra do not connect, making it easy to split"
  answer: 1
  explanation: "This is directly determined by silicate framework structure. In sheet silicates (micas), each tetrahedron shares three of its four oxygens with neighbors in the same flat layer. The layers bond to each other only through weaker forces — these interlayer bonds define the perfect single-plane cleavage. In quartz, all four oxygens are shared three-dimensionally with equal strength in every direction, leaving no weak planes — it fractures conchoidally like glass. Option D is wrong: isolated silicates (like olivine) also lack cleavage for a different reason. The real contrast is the two-dimensional sheet structure versus the full three-dimensional network."

- question: "Quartz and feldspar are both framework silicates that share most four oxygens in a three-dimensional network, so neither mineral exhibits cleavage."
  type: true-false
  answer: false
  explanation: "Quartz (pure SiO₂) has no cleavage because every oxygen is shared equally in a uniform three-dimensional network, leaving no preferential weak planes. Feldspars, however, have two distinct cleavage planes at approximately 90° — one of their key diagnostic properties in the field. The cleavage in feldspars arises because aluminum substitutes for some silicon in the framework (Al³⁺ for Si⁴⁺), and the resulting structural distortions create planes of slightly weaker bonding. Both are framework silicates, but the aluminum substitution breaks the symmetry that would otherwise eliminate cleavage."

- question: "Mafic minerals like olivine and pyroxene are denser and darker than felsic minerals like quartz because they contain a higher proportion of silicon."
  type: true-false
  answer: false
  explanation: "Mafic minerals are denser and darker because they are rich in iron (Fe) and magnesium (Mg) — the word 'mafic' derives from Magnesium and Ferric (iron). Iron and magnesium atoms are heavier than the aluminum, potassium, and sodium found in felsic minerals, giving mafic minerals densities of ~3.0–3.5 g/cm³ versus ~2.6–2.7 g/cm³ for felsic minerals. The dark color also comes from iron. Felsic minerals actually have more silicon per formula unit — this is the opposite of the misconception."

- question: "Why does the way silicon-oxygen tetrahedra connect — the silicate framework type — control physical properties like cleavage, density, and weathering resistance?"
  type: short-answer
  answer: "The silicate framework type determines how many oxygen atoms each tetrahedron shares with neighbors and how bond strengths are distributed through the crystal. In isolated silicates (olivine), unshared oxygens bond to metal cations in all directions — no planes of weakness exist, producing dense, cleavage-free minerals. In sheet silicates (micas), three-of-four oxygens link tetrahedra within a flat layer, while the fourth oxygens connect layers through weaker bonds — this creates a preferential cleavage plane. Framework silicates (quartz) with all oxygens shared have no weak planes, hence no cleavage and high chemical stability. Greater oxygen sharing also produces lower density because the open three-dimensional network is less compact than densely-packed isolated units."
  explanation: "This structural logic is the key to reading rock history: the silicate structure of a mineral determines how long it survives weathering, how rocks break down, and what minerals appear in sediments far from their source."
```

## Explainer

From your understanding of mineral crystal structure — how atoms arrange themselves in repeating three-dimensional patterns held together by ionic and covalent bonds — you are ready to focus on the specific minerals that make up nearly all of Earth's crust. Despite thousands of known mineral species, fewer than a dozen **rock-forming minerals** account for over 90% of crustal rocks. They are almost all silicates, built around the same fundamental unit: the **silicon-oxygen tetrahedron** (SiO₄⁴⁻), in which one silicon atom sits at the center of four oxygen atoms arranged at the corners of a tetrahedron. The way these tetrahedra connect to each other — or don't — creates the major silicate structural classes and determines each mineral's physical properties.

In **isolated (island) silicates** like olivine, individual tetrahedra are not bonded to each other; they are linked instead through metal cations (Mg²⁺, Fe²⁺) between them. This produces a compact, dense structure with no cleavage planes — olivine fractures rather than splitting along flat surfaces. In **single-chain silicates** (pyroxenes), tetrahedra share oxygen atoms to form continuous chains, producing two cleavage planes at roughly 90°. **Double-chain silicates** (amphiboles like hornblende) link pairs of chains side by side, yielding two cleavage planes at about 60° and 120°. **Sheet silicates** (micas, clay minerals) share three of four oxygens to form continuous flat sheets, producing the perfect single-plane cleavage that lets you peel mica into paper-thin flakes. Finally, **framework silicates** (quartz, feldspars) share all four oxygens between adjacent tetrahedra, creating a fully three-dimensional network. Quartz, being pure SiO₂ with every oxygen shared, has no weak planes and therefore no cleavage — it fractures conchoidally like glass.

The practical classification that matters most in field geology divides these minerals into **felsic** and **mafic** groups. Felsic minerals — quartz, potassium feldspar (orthoclase), sodium-rich plagioclase, and muscovite mica — are light-colored, relatively low-density (~2.6–2.7 g/cm³), and silica-rich. They dominate continental crust and granitic rocks. Mafic minerals — olivine, pyroxene, amphibole, and biotite mica — are dark-colored, denser (~3.0–3.5 g/cm³), and rich in iron and magnesium. They dominate oceanic crust and basaltic rocks. This felsic-mafic spectrum is not arbitrary; it maps directly onto melting temperature (mafic minerals crystallize at higher temperatures), weathering resistance (quartz is nearly indestructible at the surface while olivine weathers rapidly), and tectonic setting (mafic rocks form at mid-ocean ridges, felsic rocks concentrate at convergent margins).

Knowing the rock-forming minerals gives you a decoder ring for reading Earth's history. When you see a rock made of olivine and calcium-rich plagioclase, you know it formed from high-temperature, silica-poor magma — probably from the upper mantle. A rock dominated by quartz and potassium feldspar formed from cooler, silica-rich magma typical of continental settings. A sandstone made entirely of quartz grains tells you the sediment was intensely weathered, because every less-resistant mineral was destroyed during transport — only quartz survived. Each mineral's presence, absence, or relative abundance constrains the conditions under which the rock formed and the journey it has taken since.
