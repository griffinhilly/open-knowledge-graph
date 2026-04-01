---
id: proteomics-data-analysis
title: Proteomics Data Analysis
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: translation
  type: hard
- id: amino-acid-structure-and-properties
  type: hard
- id: protein-structure-prediction-basics
  type: soft
- id: probability-density-functions
  type: soft
builds-toward:
- multi-omics-integration
- systems-biology-data-integration
tags:
- mass-spectrometry
- proteomics
- peptide-identification
- protein-quantification
- post-translational-modifications
stage: expert
status: validated
---
# Proteomics Data Analysis

## Core Idea
Proteomics measures the full complement of proteins in a biological sample using mass spectrometry (MS). In a typical bottom-up workflow, proteins are digested into peptides, separated by liquid chromatography, and analyzed by tandem mass spectrometry (LC-MS/MS). Computational analysis matches observed spectra to theoretical spectra from protein databases to identify peptides, then infers protein identities and quantities. Label-free quantification compares peptide intensities across runs, while labeling approaches (TMT, SILAC) enable multiplexed comparison. Proteomics captures information that transcriptomics cannot: protein abundance, post-translational modifications, protein-protein interactions, and protein turnover.

## How It's Best Learned
Analyze a published proteomics dataset using MaxQuant: load raw MS files, search against a protein database, filter by false discovery rate, and examine the identified proteins and their quantification. Compare the protein abundance rankings to RNA-seq expression data from the same tissue and observe the imperfect correlation.

## Common Misconceptions
- mRNA levels do not reliably predict protein levels — post-transcriptional regulation, translation efficiency, and protein degradation create a correlation of only ~0.4-0.6 between transcript and protein abundance.
- Identifying a peptide in a mass spectrum is a statistical inference, not a certain identification; false discovery rate control is essential.

## Questions

```yaml
- question: "In a bottom-up proteomics experiment, what is the database search step doing?"
  type: multiple-choice
  options: ["Aligning protein sequences to a reference genome", "Matching observed peptide mass spectra to theoretical spectra generated from a protein sequence database", "Searching for homologous proteins in other species", "Identifying post-translational modifications by comparing to a known modification database"]
  answer: 1
  explanation: "After LC-MS/MS, each peptide produces a fragmentation spectrum — a pattern of fragment ion masses. The database search engine (Mascot, Sequest, Andromeda) takes every protein in the database, computationally digests it into peptides, generates theoretical fragmentation spectra for each peptide, and compares these to the observed spectra. The best-matching peptide-spectrum match is scored and evaluated for statistical significance. This is fundamentally a pattern-matching problem between observed data and a theoretical reference."

- question: "Protein abundance in a cell can be accurately predicted from mRNA expression levels alone."
  type: true-false
  answer: false
  explanation: "The correlation between mRNA and protein levels is typically only 0.4-0.6, meaning transcript abundance explains less than half of the variance in protein abundance. Post-transcriptional regulation (miRNAs, RNA-binding proteins), differences in translation efficiency (codon usage, ribosome availability, mRNA structure), and differences in protein stability and degradation rates all contribute to the discrepancy. This is precisely why proteomics is necessary alongside transcriptomics — RNA-seq tells you what could be made, but proteomics tells you what is actually present."

- question: "Explain the concept of false discovery rate (FDR) in peptide identification and how the target-decoy approach controls it."
  type: short-answer
  answer: "In proteomics, every observed spectrum is matched to the best peptide in the database, but some matches will be incorrect — the spectrum came from a peptide not in the database, or noise produced a spurious match. The target-decoy approach controls FDR by searching against both the real (target) protein database and a shuffled or reversed (decoy) database. Any match to the decoy database is by definition a false positive. The FDR is estimated as: (2 x decoy hits) / (total hits above threshold). By adjusting the score threshold until the FDR reaches the desired level (typically 1%), the analysis controls the proportion of false identifications in the final results."
  explanation: "This is analogous to the Benjamini-Hochberg correction in genomics but uses the decoy database as an empirical null distribution rather than a theoretical one. The target-decoy approach has become the standard in proteomics because it accounts for the specific characteristics of each dataset's noise rather than relying on distributional assumptions."
```

## Explainer

Genomics tells you what genes an organism has. Transcriptomics tells you which genes are being transcribed. Proteomics tells you which proteins are actually present, at what levels, and in what modified forms — and since proteins are the primary functional molecules in cells, this is often the most biologically relevant layer of information.

The dominant technology is **liquid chromatography-tandem mass spectrometry (LC-MS/MS)**. In the bottom-up workflow, proteins are extracted from a sample and digested into peptides using trypsin (which cuts at lysine and arginine residues). The peptide mixture is separated by liquid chromatography (typically reversed-phase HPLC), which reduces complexity by spreading peptides out over time. As peptides elute from the column, they are ionized (electrospray ionization) and enter the mass spectrometer, which measures their mass-to-charge ratio. Selected peptides are then fragmented (by collision with gas molecules), and the fragment masses are recorded. This fragmentation pattern is the peptide's "fingerprint" — it encodes the amino acid sequence.

**Peptide identification** matches these experimental fragmentation spectra to a database. For each spectrum, the search engine generates theoretical fragment spectra for all peptides in the database within the mass tolerance of the observed precursor, scores each match, and reports the best. This is a massive search problem — a human proteome database contains hundreds of thousands of possible peptide sequences. Statistical evaluation using the target-decoy approach ensures that the reported identifications have a controlled false discovery rate. Protein inference then groups identified peptides into protein groups, handling the complication that some peptides are shared between multiple proteins (the protein inference problem).

**Quantification** measures how much of each protein is present. Label-free quantification compares the intensity or spectral count of each peptide across runs, but requires careful normalization for run-to-run variability. Labeling approaches tag peptides from different conditions with different mass labels: TMT (tandem mass tags) allows up to 18 samples to be multiplexed in a single run, and SILAC (stable isotope labeling) incorporates heavy amino acids during cell growth for in vivo comparison. Each approach has tradeoffs in throughput, accuracy, and dynamic range. Beyond abundance, proteomics can map post-translational modifications (phosphorylation, ubiquitination, acetylation) that regulate protein activity, identify protein-protein interactions (co-immunoprecipitation MS), and measure protein turnover rates (pulsed SILAC) — information layers that no other technology provides.
