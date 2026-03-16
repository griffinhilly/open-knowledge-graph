---
id: autoencoders-unsupervised
title: Autoencoders for Unsupervised Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: backpropagation
  type: hard
- id: dimensionality-reduction
  type: soft
builds-toward:
- variational-autoencoders
tags:
- unsupervised-learning
- representation-learning
- dimensionality-reduction
- reconstruction
stage: advanced
status: draft
---

# Autoencoders for Unsupervised Learning

## Core Idea
Autoencoders are neural networks trained to reconstruct their input through a bottleneck layer, learning a compressed representation unsupervised. Denoising autoencoders learn robust features by reconstructing clean data from corrupted inputs; sparse autoencoders enforce sparsity in the bottleneck layer; they enable nonlinear dimensionality reduction and anomaly detection.

## How It's Best Learned
Implement a denoising autoencoder on image data and visualize the learned representations and reconstructions to understand what features the bottleneck captures.

## Explainer

From your work with neural networks and backpropagation, you know how to train a network to map inputs to desired outputs by minimizing a loss function. An autoencoder applies this same machinery to a surprising objective: the desired output *is* the input itself. The network must learn to reconstruct its own input, which sounds trivial until you introduce the key constraint — a **bottleneck layer** in the middle that has far fewer neurons than the input. The network is forced to compress the input into a small representation and then expand it back out, and the only way to minimize reconstruction error is to learn the most important patterns and structure in the data.

The architecture has two halves. The **encoder** maps the high-dimensional input down to the low-dimensional bottleneck (also called the **latent representation** or **code**). The **decoder** maps the code back up to the original dimensionality. If the bottleneck has, say, 32 neurons and the input has 784 pixels (a 28×28 image), the encoder must learn to distill each image into just 32 numbers that capture enough information for the decoder to reconstruct it. This is nonlinear dimensionality reduction — similar in spirit to PCA, which you may know from dimensionality reduction, but capable of capturing curved and complex manifolds in the data rather than just linear subspaces.

What makes autoencoders powerful is their variants. A **denoising autoencoder** receives a corrupted version of the input (pixels randomly zeroed out, Gaussian noise added) but is trained to reconstruct the *clean* original. This forces the network to learn robust features rather than memorizing pixel values — it must understand the underlying structure well enough to fill in what is missing. A **sparse autoencoder** adds a penalty that encourages most bottleneck neurons to be inactive for any given input, producing representations where each neuron corresponds to a distinct, interpretable feature. Both variants improve the quality of learned representations and make autoencoders useful as feature extractors for downstream tasks.

The latent space of a trained autoencoder has practical applications beyond compression. Points near each other in the bottleneck space correspond to inputs that share important features, so the latent representation can be used for **anomaly detection**: encode a new input, decode it, and measure reconstruction error — anomalies that differ from training data will reconstruct poorly. The latent space also enables interpolation: blend two latent codes and decode the result to generate plausible intermediates between two inputs. These ideas lay the groundwork for variational autoencoders, which add probabilistic structure to the latent space and enable principled generation of entirely new data.
