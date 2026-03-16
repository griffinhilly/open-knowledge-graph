---
id: polyphase-filter-decomposition-multirate
title: Polyphase Filter Decomposition and Structure
domain: engineering
course: signals-and-systems
prerequisites:
- id: multirate-decimation-interpolation
  type: hard
builds-toward:
- decimation-anti-aliasing-and-downsampling
- interpolation-filtering-image-rejection
tags:
- polyphase
- multirate
- decomposition
- efficiency
stage: abstract-reasoning
status: draft
---

# Polyphase Filter Decomposition and Structure

## Core Idea
Polyphase decomposition factors a filter into M subfilters (for decimation by M) or K subfilters (for interpolation by K), each operating at the lower or higher rate. This reduces computation by moving downsampling/upsampling before filtering, avoiding computations discarded in decimation. Polyphase structures are computationally efficient for multirate signal processing and form the basis of practical audio codecs and multirate systems.

## How It's Best Learned
Decompose a 64-tap FIR filter for 4:1 decimation into 4 polyphase subfilters. Compare computational complexity of direct decimation vs polyphase form.

## Common Misconceptions
- Thinking polyphase changes the filtering operation (it's a reorganization, not modification).
- Confusing polyphase decomposition with parallel filter structures.
- Not recognizing that polyphase enables real-time multirate processing.

## Explainer

From multirate signal processing, you know that decimation by M means: apply a lowpass anti-aliasing filter to prevent aliasing, then keep every M-th output sample and discard the rest. This raises an immediate question about efficiency. If you filter first at the high sample rate and then throw away M−1 out of every M output samples, you have done M times more computation than necessary — the discarded outputs contributed nothing to the result. **Polyphase decomposition** is the reorganization that eliminates this waste by moving the downsampling to before the filtering.

The key insight starts with the filter's impulse response h[n]. For a length-N filter decimating by M, you can split h[n] into M interleaved subsequences called **polyphase components**: e₀[n] = h[nM], e₁[n] = h[nM + 1], ..., e_{M-1}[n] = h[nM + M−1]. Each polyphase component is a length-N/M filter that operates only on every M-th input sample. The original filter's output at the decimated rate can be computed by: downsample the input by M into M separate streams (each phase of the input), apply the corresponding polyphase filter to each stream, and sum the results. Since each polyphase filter operates at 1/M the original sample rate, the total computation is the same as running a single length-N/M filter at the original rate — an M-fold reduction in multiply-accumulate operations.

A concrete example makes this tangible. Suppose you have a 64-tap FIR lowpass filter used to decimate by 4. The naive approach: filter the input at full rate (64 multiplications per input sample), then output every 4th sample (75% wasted). The polyphase approach: split into 4 polyphase components of 16 taps each. For each output sample, compute 4 × 16 = 64 multiplications — but those 64 multiplications produce one output sample, not four. Wait: the savings come from the fact that you are now computing at the decimated rate, not the full rate. Per output sample the cost is 64 operations either way; but per unit time the polyphase structure produces output at 1/4 the input rate, so per input sample the cost is 64/4 = 16 multiplications, versus 64 in the naive case. The factor-of-M speedup is real and directly scales hardware resources and power consumption.

Polyphase structures extend symmetrically to interpolation: for interpolation by K, you decompose the interpolation filter into K polyphase components, compute each one at the input rate, and interleave the outputs to produce the higher-rate output. The same principle applies to arbitrary rational rate changes M/K — decimate by M in polyphase form, then interpolate by K in polyphase form, possibly combined into a single efficient structure. This efficiency is why polyphase filters are ubiquitous in real-world multirate systems: audio sample rate converters (44.1 kHz ↔ 48 kHz in professional audio), software-defined radio channelizers, OFDM baseband processing in wireless standards, and image resizing algorithms all rely on polyphase filter banks to achieve the required sample rate manipulations within tight power and latency budgets.
