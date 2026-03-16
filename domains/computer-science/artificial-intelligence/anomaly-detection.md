---
id: anomaly-detection
title: Anomaly Detection Methods
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: probability-basics
  type: hard
tags:
- unsupervised-learning
- outlier-detection
- anomaly
stage: advanced
status: draft
---

# Anomaly Detection Methods

## Core Idea
Anomaly detection identifies rare or abnormal patterns. Methods include statistical (z-score, isolation forests), density-based (Local Outlier Factor), and reconstruction-based (autoencoders). Threshold selection trades precision for recall depending on application.

## Explainer

From probability basics, you understand distributions, expected values, and what it means for an observation to be unlikely under a given model. **Anomaly detection** applies this reasoning at scale: given a dataset of mostly "normal" examples, identify the rare instances that do not fit the pattern. The core challenge is that anomalies are, by definition, rare and diverse — you cannot simply train a classifier on labeled anomalies because you may never have seen the specific type of anomaly that will appear next. Instead, most approaches learn what "normal" looks like and flag anything that deviates significantly.

The simplest statistical approach extends ideas you already know. If a feature follows a roughly normal distribution, any observation more than 3 standard deviations from the mean (a **z-score** beyond ±3) is suspicious. But real data is multivariate and rarely Gaussian, so more sophisticated methods are needed. **Isolation forests** take a clever shortcut: they build random decision trees that recursively split the data on random features at random thresholds. Normal points, clustered together in dense regions, require many splits to isolate. Anomalies, sitting far from the crowd, get isolated in very few splits. The average number of splits needed to isolate a point becomes its anomaly score — elegant because it requires no distance calculations or density estimates.

**Density-based methods** like Local Outlier Factor (LOF) formalize the intuition that anomalies live in sparse regions. LOF compares the local density around each point to the density around its neighbors. A point in a sparse region surrounded by dense neighborhoods gets a high LOF score — it is an outlier relative to its local context. This local comparison is crucial because it handles datasets with clusters of varying density, where a global threshold would fail. A point that seems normal in a sparse cluster might be anomalous if it appeared in a dense one. **Reconstruction-based methods** take yet another approach: train an autoencoder to compress and reconstruct normal data. Since the autoencoder learns to represent typical patterns efficiently, anomalies — which differ structurally from the training data — produce high reconstruction error, flagging themselves.

The hardest practical decision in anomaly detection is **threshold selection**. Every method produces a continuous anomaly score, and you must choose a cutoff above which you declare "anomaly." Set it too low and you drown in false alarms; set it too high and you miss real anomalies. This is a precision-recall tradeoff shaped entirely by the application's cost structure. In credit card fraud detection, missing a true fraud (false negative) costs far more than investigating a legitimate transaction (false positive), so you set a low threshold and accept more alerts. In manufacturing quality control, false alarms that halt a production line are expensive, so you set a higher threshold and tolerate occasional escapes. There is no universally correct threshold — it encodes a business decision about the relative cost of errors.
