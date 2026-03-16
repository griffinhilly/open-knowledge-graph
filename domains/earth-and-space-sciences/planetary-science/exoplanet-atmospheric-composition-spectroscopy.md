---
id: exoplanet-atmospheric-composition-spectroscopy
title: Exoplanet Atmospheric Composition from Transmission Spectroscopy
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: exoplanet-transmission-spectroscopy
  type: hard
- id: atmospheric-photochemistry
  type: hard
- id: uv-vis-spectroscopy-quantitative
  type: soft
builds-toward:
- biosignatures-exoplanet-atmospheres
tags:
- spectroscopy
- atmospheres
- composition
- transmission-spectra
- molecules
stage: advanced
status: draft
---

# Exoplanet Atmospheric Composition from Transmission Spectroscopy

## Core Idea
Transmission and emission spectra reveal exoplanet atmospheric composition by measuring wavelength-dependent absorption from molecular features. Hydrogen-dominated atmospheres show Rayleigh scattering; secondary atmospheres show molecular bands (H₂O, CO₂, CH₄). Combined with photochemistry models and general circulation models, spectra constrain composition, temperature structure, habitability, and potential biosignatures.

## Explainer

From your work on transmission spectroscopy, you know the basic technique: when an exoplanet transits its star, some starlight filters through the planet's atmosphere, and molecules in that atmosphere absorb specific wavelengths. By comparing the star's spectrum with and without the planet in front of it, you can extract a **transmission spectrum** — a plot showing how much extra light the atmosphere blocks at each wavelength. Each dip in this spectrum is a fingerprint. The challenge and excitement of atmospheric composition work is reading those fingerprints to determine what the atmosphere is actually made of.

Different molecules absorb at characteristic wavelengths determined by their vibrational and rotational energy levels. **Water vapor** (H₂O) produces broad absorption features in the near-infrared around 1.4 and 1.9 μm. **Carbon dioxide** (CO₂) has a strong signature near 4.3 μm and 15 μm. **Methane** (CH₄) absorbs near 3.3 μm. **Sodium** and **potassium** produce narrow lines in visible wavelengths. By matching observed spectral features against laboratory-measured or computationally modeled absorption profiles, astronomers can identify which molecules are present and estimate their abundances. This is the same underlying physics as UV-Vis spectroscopy in a chemistry lab — Beer-Lambert absorption — but applied across interstellar distances to atmospheres you can never sample directly.

The type of atmosphere determines what you see. A **hydrogen-dominated atmosphere** (like those of hot Jupiters and sub-Neptunes) has a large scale height — meaning the atmosphere is puffy and extended, producing deep, easily measured absorption features. These atmospheres also show a characteristic slope in the visible spectrum from **Rayleigh scattering**, where shorter (bluer) wavelengths are scattered more than longer ones. A **secondary atmosphere** dominated by heavier molecules (CO₂, N₂, H₂O) has a much smaller scale height, producing weaker spectral features that require extremely precise instruments to detect. This is why characterizing Earth-like atmospheres is so much harder than characterizing gas giant atmospheres — the signals are 10–100 times smaller.

Interpreting spectra also requires understanding atmospheric photochemistry — your other prerequisite. Ultraviolet radiation from the host star drives chemical reactions that can produce or destroy molecules, creating a vertical composition profile that differs from what simple chemical equilibrium would predict. Methane, for example, is destroyed by UV photolysis in the upper atmosphere, so detecting it implies a continuous source (biological or geological). Ozone (O₃) is produced photochemically from oxygen. Disequilibrium combinations — such as methane and oxygen coexisting — are especially significant because they suggest an active source of replenishment, potentially biological. This is why atmospheric composition spectroscopy is the most promising near-term pathway to detecting **biosignatures** on exoplanets: not by imaging alien life directly, but by identifying atmospheric chemistry that is difficult to explain without it.
