---
id: granular-synthesis-composition
title: Granular Synthesis and Composition
domain: music
course: advanced-music-theory
prerequisites:
- id: electroacoustic-morphology-analysis
  type: hard
- id: fourier-series-definition
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- algorithmic-composition-theory
- spectral-harmony-overtone-analysis
tags:
- synthesis
- electronic-music
- texture
stage: advanced
status: draft
---

# Granular Synthesis and Composition

## Core Idea
Granular synthesis divides sounds into microscopic particles (grains, typically 1-100ms) and recombines them. Compositional control of grain density, pitch, envelope, and spacing creates evolving textures. This technique enables unprecedented textural control and transforms source materials.

## How It's Best Learned
Use granular synthesis software to generate textures from recorded or synthetic material; manipulate grain parameters to hear their effect. Analyze Curtis Roads granular-music compositions to understand how grain-level control creates form.

## Common Misconceptions
- Assuming granular synthesis is purely textural; grain-level control enables precise pitch and melodic organization. - Confusing granular synthesis with simple time-stretching; granular composition is a creative tool. - Overlooking that granular textures exist on a continuum from recognizable sound to abstract texture.

## Explainer

From your study of electroacoustic morphology you know that sounds can be analyzed as shapes in time: their attack, sustain, and decay contours, their spectral motion, their texture. Granular synthesis takes this analytical lens and turns it into a compositional tool. The central idea is **temporal atomization**: any sound — a voice, a chord, a field recording — can be sliced into microscopic fragments called **grains**, typically 1 to 100 milliseconds long, and then reassembled according to compositional rules rather than the original time sequence. You are no longer manipulating the sound as a whole; you are operating one layer below, at the level of the individual grain.

Your soft prerequisite of Fourier series gives you an important reference point. Fourier decomposition analyzes sound by breaking it into frequency components — sine waves of different frequencies stacked together. Granular synthesis operates in the time domain instead: it breaks sound into time slices. These are complementary decompositions. Where Fourier thinking leads to additive synthesis (building up a sound from sine waves), granular thinking leads to **cloud synthesis** — assembling a sound from a dense stream of micro-events. The composer controls not which frequencies are present, but which moments, at what density, with what envelope shape and playback pitch applied to each grain.

The key parameters to understand are: **grain size** (shorter grains smear pitch, longer grains preserve more of the original timbre), **grain density** (grains per second — sparse for rhythmic textures, dense for smooth clouds), **grain envelope** (the amplitude shape of each grain; a soft bell curve avoids clicks at grain boundaries), **pitch transposition per grain** (can spread grains across a pitch range for chords or glissandi), and **scatter** (random variation in timing, pitch, or amplitude that introduces organic irregularity). By modulating these parameters over time, a composer can transform a single recorded sound into a slowly evolving texture, a rhythmic stutter, or an abstract cloud with no recognizable connection to the source.

The compositional significance is that granular synthesis shifts the unit of musical thought from the note or phrase down to the grain. A 50ms fragment of a piano attack, looped and densified at different pitch transpositions, can become a shimmering cloud. The source material becomes **plastic**: frozen (time-stretched by repeating grains), compressed, scattered, or reordered. Composers like Curtis Roads and Iannis Xenakis developed entire formal languages around this grain-level control, treating texture itself as structural material rather than surface decoration. Understanding granular synthesis means understanding that timbre and texture are not fixed properties of a sound but parameters you can sculpt with the same precision you apply to pitch and rhythm.
