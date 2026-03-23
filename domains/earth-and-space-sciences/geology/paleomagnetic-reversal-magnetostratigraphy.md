---
id: paleomagnetic-reversal-magnetostratigraphy
title: Paleomagnetic Reversals and Magnetostratigraphy
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: stratigraphy
  type: soft
tags:
- paleomagnetism
- dating
- stratigraphy
stage: formal-systems
status: draft
---

# Paleomagnetic Reversals and Magnetostratigraphy

## Core Idea
Paleomagnetic reversals create distinctive magnetic polarity zones in volcanic and sedimentary sequences. These zones can be correlated to the geomagnetic polarity time scale, providing precise dating without radiometric analysis. Magnetostratigraphy is particularly valuable for Neogene and younger sequences.

## Questions

```yaml
- question: "A geologist drills a core through a sedimentary sequence and identifies alternating zones of normal and reversed polarity. To assign absolute ages to the polarity boundaries, what additional resource is required?"
  type: multiple-choice
  options:
    - "Radiometric dates measured directly from every polarity boundary in the core"
    - "The geomagnetic polarity time scale (GPTS), which has been independently calibrated using radiometric dating of volcanic rocks"
    - "Fossil assemblages from every polarity zone to establish a biochronology"
    - "An independently measured sedimentation rate for the section to convert polarity zone thickness to time"
  answer: 1
  explanation: "The core provides the local sequence of polarity zones (the pattern of N and R), but polarity alone carries no inherent age. The GPTS provides the ages — it is a globally calibrated record of when each reversal occurred, built by radiometrically dating volcanic rocks of known polarity worldwide. Magnetostratigraphy works by pattern-matching: if the local polarity sequence matches a distinctive segment of the GPTS, those dates transfer to the section without requiring radiometric measurements from the sedimentary rock itself. Fossils and sedimentation rates can help narrow down which segment of the GPTS matches, but the GPTS is the necessary source of absolute ages."

- question: "Why is the pattern of geomagnetic polarity reversals useful for correlating rock sequences on different continents?"
  type: multiple-choice
  options:
    - "Reversals occur at regular intervals, providing a reliable periodic timekeeping signal"
    - "A reversal is a globally synchronous event recorded everywhere on Earth simultaneously, regardless of rock type or environment"
    - "Reversals preferentially occur at continental margins, where stratigraphic sections are most complete and accessible"
    - "Polarity zones have distinctive chemical signatures that can identify them independently of the GPTS"
  answer: 1
  explanation: "A geomagnetic reversal is instantaneous on geological timescales and simultaneous across the entire planet — the magnetic field flips globally, not locally. This means a reversal boundary in a deep-sea core from the Pacific is exactly the same age as the same reversal recorded in a terrestrial section in East Africa, even if those environments share no fossil species in common. This global synchrony is what makes magnetostratigraphy a powerful correlation tool: it bridges different depositional environments using a shared physical signal that operates everywhere at once."

- question: "In sedimentary rocks, magnetic minerals record the direction of Earth's field at the time of lithification (when the rock solidifies), not at the time of deposition."
  type: true-false
  answer: false
  explanation: "In sedimentary rocks, the relevant process is detrital remanent magnetization (DRM): tiny magnetic grains physically rotate to align with the ambient field as they settle through water or during compaction, before the sediment fully lithifies. The magnetization is acquired during deposition and early burial, not at lithification. This contrasts with volcanic rocks, where thermoremanent magnetization is locked in as the rock cools through the Curie temperature. The distinction matters because DRM can be affected by post-depositional bioturbation and chemical diagenesis, which are considerations in interpreting paleomagnetic records from sediments."

- question: "Magnetostratigraphy can assign absolute ages to a rock sequence without requiring any radiometric measurements from that specific section, by correlating its polarity pattern to the globally calibrated GPTS."
  type: true-false
  answer: true
  explanation: "This is the key practical power of magnetostratigraphy. The GPTS was built by radiometrically dating volcanic rocks worldwide and is maintained as a globally shared reference. A new section needs only its polarity sequence (obtainable from core samples with no radiometric measurements) and a successful pattern match to a GPTS segment to obtain dates for its reversal boundaries. This makes magnetostratigraphy especially valuable in sedimentary basins where volcanic layers are absent and biostratigraphy provides insufficient resolution — the section can be dated using the polarity record alone."

- question: "Explain how the geomagnetic polarity time scale functions as a 'barcode' for dating rock sequences, and why magnetostratigraphy is especially useful when rocks lack datable volcanic layers."
  type: short-answer
  answer: "The GPTS is a global record of when each polarity reversal occurred, built by combining radiometric dates from volcanic rocks with their measured polarities. The key feature is that reversal intervals are irregular — some chrons last millions of years, others only tens of thousands — creating a distinctive, non-repeating pattern analogous to a barcode. When you measure the polarity sequence of a new rock section and find, for example, three short reversals bracketed by two long normal intervals, that specific pattern matches a unique position in the GPTS. The ages of those reversals in the GPTS then transfer directly to your section. When volcanic layers are absent, other dating methods (biostratigraphy, radiometric dating of detrital minerals) cannot provide the continuous, high-resolution time control that polarity stratigraphy delivers for Neogene and Quaternary sequences."
  explanation: "The 'barcode' analogy captures the key insight: the value of the GPTS for dating is not just that reversals happened, but that the pattern of reversals is globally unique and irregular enough that matching a local sequence to the GPTS is unambiguous (with sufficient section length). Longer sections provide more context and reduce ambiguity in the pattern match."
```

## Explainer

From your study of geomagnetic reversal chronology, you know that Earth's magnetic field periodically flips polarity — magnetic north becomes magnetic south and vice versa — at irregular intervals ranging from tens of thousands to millions of years. From stratigraphy, you know that rock layers record time sequences. **Magnetostratigraphy** exploits the intersection of these two facts: when rocks form, they lock in the magnetic field direction of the time they formed, creating a sequence of normal and reversed polarity zones that can be matched to the global geomagnetic polarity time scale (GPTS) like a barcode.

The recording mechanism differs between rock types. In **volcanic rocks**, iron-bearing minerals like magnetite crystallize from cooling lava and align with the ambient magnetic field. Once the rock cools below the **Curie temperature** (about 580°C for magnetite), the magnetic alignment is locked in permanently — this is thermoremanent magnetization. In **sedimentary rocks**, tiny magnetic grains (detrital magnetite or hematite) physically rotate to align with the field as they settle through water and become trapped during compaction. This detrital remanent magnetization is weaker and can be affected by post-depositional processes, but in fine-grained sediments deposited in quiet water, it faithfully records the field direction at the time of deposition.

The practical technique works by drilling oriented core samples at closely spaced intervals through a stratigraphic section and measuring each sample's magnetic polarity in the laboratory. The result is a column of normal (N) and reversed (R) polarity zones — a **magnetic polarity stratigraphy** for that section. This local pattern is then compared to the GPTS, which has been independently calibrated using radiometric dating of volcanic rocks with known polarities. The GPTS has a distinctive, irregular pattern of long and short polarity intervals — the Brunhes normal chron (0–0.78 Ma), the Matuyama reversed chron (0.78–2.58 Ma), and so on — that functions like a unique fingerprint. When the pattern of polarity zones in your section matches a segment of the GPTS, you have dated those rocks without needing any radiometric measurements from the section itself.

Magnetostratigraphy is especially powerful for **Neogene and Quaternary sequences** (the last ~23 million years), where the GPTS is most precisely calibrated and polarity intervals are short enough to provide high temporal resolution. It excels in sedimentary environments like deep-sea cores and continental basins where datable volcanic layers are absent, making it complementary to biostratigraphy and radiometric dating. The technique also provides global correlation capability: a polarity reversal happens everywhere on Earth simultaneously, so a reversal boundary identified in a marine core from the Pacific can be correlated directly with one in a terrestrial section in East Africa, bridging environments that share no fossil species in common.
