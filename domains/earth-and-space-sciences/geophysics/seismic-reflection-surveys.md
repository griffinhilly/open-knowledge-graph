---
id: seismic-reflection-surveys
title: Seismic Reflection Surveys and Common Midpoint Processing
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-waves
  type: hard
- id: elastic-wave-propagation-in-solids
  type: hard
builds-toward:
- seismic-migration-techniques
- synthetic-seismogram-modeling
tags:
- seismic
- reflection
- survey
- cmp
- processing
stage: advanced
status: draft
---

# Seismic Reflection Surveys and Common Midpoint Processing

## Core Idea
Seismic reflection surveys use reflected waves to image subsurface structure. Common midpoint (CMP) processing groups traces by reflection point, allowing velocity estimation through normal moveout (NMO) analysis and coherent stacking to enhance signal.

## How It's Best Learned
Study real seismic datasets and process them step-by-step: sorting, NMO correction, velocity picking, and stacking. Compare stacked sections from different velocity models.

## Explainer

From your study of seismic waves and elastic wave propagation, you know that when a wave encounters a boundary between materials with different elastic properties, part of its energy reflects back toward the surface. Seismic reflection surveys exploit this principle to create detailed images of subsurface structure — essentially an ultrasound scan of the Earth. A controlled energy source (an explosive charge, vibroseis truck, or air gun) generates seismic waves at the surface, and an array of receivers (geophones on land, hydrophones at sea) records the reflected arrivals from each subsurface interface.

The raw data from a reflection survey is a collection of **seismograms** — wiggly traces showing amplitude versus time for each source-receiver pair. The challenge is that a single reflected event from one subsurface point appears on many different traces, recorded at different offsets (source-to-receiver distances), each with a slightly different travel time because of the longer path. **Common midpoint (CMP) gathering** organizes the data by grouping all traces that share the same reflection point, regardless of which source-receiver pair produced them. This is the fundamental organizational step that makes modern reflection processing possible.

Within a CMP gather, traces from the same reflector arrive at different times because of the offset-dependent path length. This time difference is called **normal moveout (NMO)** — for a flat reflector, it follows a hyperbolic curve. By measuring the curvature of the hyperbola, you estimate the seismic velocity above the reflector: steeper curvature means slower velocity, flatter means faster. This process of **velocity analysis** is done interactively by testing different velocity values and seeing which one best flattens the hyperbola. Once the correct velocity is applied, the NMO correction shifts each trace so that all offsets show the same arrival time — as if every trace were recorded at zero offset directly above the reflection point.

After NMO correction, the traces in each CMP gather are **stacked** — simply summed together. This is where the power of redundancy pays off. Coherent reflections add constructively, while random noise (which differs from trace to trace) partially cancels out. The signal-to-noise ratio improves roughly as the square root of the number of traces stacked, which is why surveys are designed with high **fold** (many traces per CMP). The result of stacking all CMPs across a survey line is a **stacked section** — an image that approximates a geological cross-section, with the horizontal axis showing surface position and the vertical axis showing two-way travel time. Converting from time to depth requires the velocity model estimated during NMO analysis, and further processing steps like migration correct for the geometric distortions that arise when reflectors are dipping or structures are complex.
