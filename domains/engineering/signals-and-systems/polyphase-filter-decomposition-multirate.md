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
stage: expert
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

## Questions

```yaml
- question: "A 64-tap FIR lowpass filter is used to decimate by 4. In the naive approach, you apply the full filter at the input rate and keep every 4th output. Using a polyphase structure instead, how much is computation reduced per unit time?"
  type: multiple-choice
  options:
    - "No reduction — both approaches require 64 multiplications per output sample"
    - "4× reduction — the polyphase structure computes at 1/4 the rate, so the per-input-sample cost drops from 64 to 16 multiplications"
    - "64× reduction — the filter is split into 64 independent subfilters each of length 1"
    - "2× reduction — half the computations are avoided because every other sample is discarded"
  answer: 1
  explanation: "The key is 'per unit time,' not 'per output sample.' In the naive approach, the full 64-tap filter runs at the full input rate: 64 multiplications per input sample. In the polyphase approach, the filter is split into 4 subfilters of 16 taps each. Each subfilter operates at the decimated rate (1/4 the input rate). Per input sample, the cost is 4 × 16 / 4 = 16 multiplications — a factor-of-4 reduction. The factor equals M, the decimation ratio. This is the actual hardware and power savings that make polyphase structures practical in real systems."

- question: "Why does a polyphase decimation structure produce exactly the same output as naive decimation (filter first, then downsample)?"
  type: multiple-choice
  options:
    - "It uses a different set of optimized filter coefficients that happen to give the same frequency response"
    - "Both methods alias the same frequency components in the same way during downsampling"
    - "Polyphase decomposition is a mathematical reorganization of the same filter computation — it reorders operations without changing the result"
    - "The outputs are approximately equal, with the difference decreasing as the number of polyphase branches increases"
  answer: 2
  explanation: "Polyphase decomposition does not change the filtering operation — it is a reorganization that exploits the commutativity of linear, shift-invariant operations with downsampling. The polyphase components e₀, e₁, ..., e_{M-1} together contain exactly the same coefficients as the original filter h[n], just rearranged. The Noble Identity guarantees that downsampling before filtering each polyphase branch gives the same result as filtering then downsampling. This is the essential insight in option 'polyphase changes the filtering' misconception — it absolutely does not."

- question: "Polyphase decomposition works by splitting a single filter into multiple independent bandpass filters, each processing a different frequency range of the input signal."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Polyphase decomposition splits the filter by interleaving its time-domain coefficients into M branches — not by frequency. Each polyphase component e_k[n] = h[nM + k] contains coefficients at positions k, k+M, k+2M, ... from the original filter. These are not frequency-selective bandpass filters; they are all derived from the same lowpass prototype and together reconstruct the full lowpass filter behavior when combined. Splitting by frequency bands is what a filter bank does — polyphase is a computational reorganization of a single filter, not a parallel filter bank."

- question: "In a polyphase decimation-by-M structure, each polyphase subfilter operates at 1/M the original input sample rate, and this is the source of the computational efficiency gain."
  type: true-false
  answer: true
  explanation: "This is exactly the source of savings. Each polyphase branch only needs to compute one output for every M input samples, because it receives a downsampled version of the input. Since the subfilter runs at 1/M the rate, its contribution to per-input-sample computation is (length of subfilter) / M. Summed over all M branches: M × (N/M) / M = N/M multiply-accumulate operations per input sample, versus N in the naive approach. The efficiency comes entirely from operating at the lower rate — which is only possible by moving downsampling before the filtering step."

- question: "Explain in your own words why naive decimation is computationally wasteful, and how polyphase decomposition eliminates that waste without changing the filtering result."
  type: short-answer
  answer: "In naive decimation, you apply a full-rate filter to every input sample and then discard M-1 out of every M output samples. The discarded computations were wasted — they consumed power and time but contributed nothing to the output. Polyphase decomposition eliminates this waste by exploiting the Noble Identity: downsampling commutes with filtering in LTI systems. You decompose the filter's coefficients into M interleaved branches (polyphase components), downsample the input first into M parallel streams, filter each stream at the low rate with its short subfilter, and sum the results. Because each branch runs at 1/M the rate, no computations are ever discarded — every multiply-accumulate directly contributes to an output sample."
  explanation: "The key insight is that the output at the decimated rate contains all the information needed; computing intermediate high-rate samples that get thrown away is pure waste. Polyphase restructuring is a way to only compute what you actually need. The result is mathematically identical — the Noble Identity guarantees this — but requires M times fewer operations per unit time. This is why polyphase structures are ubiquitous in real-time multirate systems, from audio sample rate converters to software-defined radio receivers."
```

## Explainer

From multirate signal processing, you know that decimation by M means: apply a lowpass anti-aliasing filter to prevent aliasing, then keep every M-th output sample and discard the rest. This raises an immediate question about efficiency. If you filter first at the high sample rate and then throw away M−1 out of every M output samples, you have done M times more computation than necessary — the discarded outputs contributed nothing to the result. **Polyphase decomposition** is the reorganization that eliminates this waste by moving the downsampling to before the filtering.

The key insight starts with the filter's impulse response h[n]. For a length-N filter decimating by M, you can split h[n] into M interleaved subsequences called **polyphase components**: e₀[n] = h[nM], e₁[n] = h[nM + 1], ..., e_{M-1}[n] = h[nM + M−1]. Each polyphase component is a length-N/M filter that operates only on every M-th input sample. The original filter's output at the decimated rate can be computed by: downsample the input by M into M separate streams (each phase of the input), apply the corresponding polyphase filter to each stream, and sum the results. Since each polyphase filter operates at 1/M the original sample rate, the total computation is the same as running a single length-N/M filter at the original rate — an M-fold reduction in multiply-accumulate operations.

A concrete example makes this tangible. Suppose you have a 64-tap FIR lowpass filter used to decimate by 4. The naive approach: filter the input at full rate (64 multiplications per input sample), then output every 4th sample (75% wasted). The polyphase approach: split into 4 polyphase components of 16 taps each. For each output sample, compute 4 × 16 = 64 multiplications — but those 64 multiplications produce one output sample, not four. Wait: the savings come from the fact that you are now computing at the decimated rate, not the full rate. Per output sample the cost is 64 operations either way; but per unit time the polyphase structure produces output at 1/4 the input rate, so per input sample the cost is 64/4 = 16 multiplications, versus 64 in the naive case. The factor-of-M speedup is real and directly scales hardware resources and power consumption.

Polyphase structures extend symmetrically to interpolation: for interpolation by K, you decompose the interpolation filter into K polyphase components, compute each one at the input rate, and interleave the outputs to produce the higher-rate output. The same principle applies to arbitrary rational rate changes M/K — decimate by M in polyphase form, then interpolate by K in polyphase form, possibly combined into a single efficient structure. This efficiency is why polyphase filters are ubiquitous in real-world multirate systems: audio sample rate converters (44.1 kHz ↔ 48 kHz in professional audio), software-defined radio channelizers, OFDM baseband processing in wireless standards, and image resizing algorithms all rely on polyphase filter banks to achieve the required sample rate manipulations within tight power and latency budgets.
