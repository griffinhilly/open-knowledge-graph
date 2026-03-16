---
id: variational-autoencoders
title: Variational Autoencoders (VAE)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: autoencoders-unsupervised
  type: hard
- id: generative-adversarial-networks
  type: soft
- id: probability-distributions
  type: soft
- id: probability-density-functions
  type: hard
- id: expected-value
  type: soft
- id: probability-density-functions-theory
  type: soft
- id: kullback-leibler-divergence
  type: soft
tags:
- generative-models
- probabilistic-models
- representation-learning
- latent-variables
stage: advanced
status: draft
---

# Variational Autoencoders (VAE)

## Core Idea
Variational autoencoders add probabilistic structure by encoding inputs into latent distributions (usually Gaussian) and decoding samples from these distributions. The ELBO (evidence lower bound) loss combines reconstruction error and KL divergence regularization that encourages the latent distribution to match a standard prior, enabling generative sampling and learning interpretable latent representations.

## How It's Best Learned
Implement VAE on image data and observe how the latent space enables interpolation between examples and how the KL term affects representation quality and generativeness.

## Explainer

A standard autoencoder, which you have already studied, compresses an input into a low-dimensional code and reconstructs the original from that code. It learns useful representations, but it has a fundamental limitation as a generative model: the latent space has no structure. If you pick a random point in the latent space, the decoder may produce garbage, because nothing during training forced nearby points to decode into similar or meaningful outputs. **Variational autoencoders** fix this by imposing probabilistic structure on the latent space, turning the autoencoder from a compression tool into a principled generative model.

The key idea is that instead of encoding an input x into a single latent vector z, the encoder outputs the **parameters of a probability distribution** — typically the mean μ and variance σ² of a Gaussian. To get a latent code, you sample z from this distribution: z ~ N(μ, σ²). The decoder then reconstructs x from the sampled z. This means the decoder must handle a range of z values near μ, not just one point, which forces the latent space to be smooth: nearby points in latent space decode to similar outputs. The sampling step creates a technical challenge — you cannot backpropagate gradients through a random sampling operation. The **reparameterization trick** solves this by rewriting z = μ + σ · ε where ε ~ N(0, 1). Now μ and σ are deterministic outputs of the encoder, ε is an external random input, and gradients flow cleanly through the computation.

The VAE training objective is the **evidence lower bound (ELBO)**, which combines two terms. The **reconstruction loss** measures how well the decoder reproduces the input from the sampled z — this is the same idea as in a standard autoencoder. The **KL divergence term** measures how far the encoder's distribution N(μ, σ²) deviates from a standard normal prior N(0, 1). You know from your study of KL divergence that it quantifies the "distance" between two distributions. By penalizing deviation from the prior, the KL term prevents the encoder from collapsing each input to a narrow spike at a unique point — it forces the latent distributions to overlap and organize into a coherent structure. The full loss is: L = reconstruction loss + KL(q(z|x) ‖ p(z)), and training minimizes this jointly.

The payoff is a latent space you can actually use for generation. Because the KL term pushes all encoder distributions toward the same standard normal, you can sample z ~ N(0, 1) at test time and decode it to generate new data — no input required. The latent space also supports **interpolation**: linearly blending the latent codes of two inputs and decoding intermediate points produces smooth transitions between them (for example, one face morphing into another). The tradeoff is that VAE outputs tend to be blurrier than those from GANs, because the reconstruction loss averages over the stochastic samples, which smooths out fine details. More sophisticated VAEs address this with richer priors, more expressive decoders, or hierarchical latent structures, but the fundamental architecture — encode to a distribution, sample, decode, regularize with KL — remains the foundation.
