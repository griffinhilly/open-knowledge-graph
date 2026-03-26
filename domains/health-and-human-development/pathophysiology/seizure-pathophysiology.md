---
id: seizure-pathophysiology
title: Seizures and Epilepsy
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: neuronal-excitability-and-action-potentials
  type: hard
- id: gabaergic-inhibition
  type: hard
- id: glutamatergic-excitation
  type: hard
builds-toward:
- status-epilepticus
- post-ictal-state
tags:
- seizure
- epilepsy
- neuronal-synchronization
stage: expert
status: validated
---

# Seizures and Epilepsy

## Core Idea
Seizures result from excessive synchronized neuronal firing caused by imbalance between excitation (glutamate, AMPA/NMDA receptors) and inhibition (GABA). Epilepsy is a predisposition to recurrent seizures. Hyperexcitability stems from altered ion channels, reduced GABAergic tone, or excessive excitatory input.

## How It's Best Learned
Classify seizures by EEG pattern (generalized vs focal) and phenomenology (tonic-clonic, absence, focal motor). Understand status epilepticus as a medical emergency with risk of neuronal death.

## Common Misconceptions
Febrile seizures in childhood do not cause epilepsy in most cases—the risk is low. Photosensitivity is present in only ~3% of patients with epilepsy; it is not a universal trigger.

## Questions

```yaml
- question: "A patient experiences déjà vu, then performs repetitive hand movements without awareness, then suddenly loses consciousness and convulses with full-body rhythmic jerking. This best represents:"
  type: multiple-choice
  options:
    - "A primary generalized tonic-clonic seizure from onset"
    - "An absence seizure with secondary motor features"
    - "A focal seizure originating in the temporal lobe with secondary generalization"
    - "A provoked seizure caused by metabolic derangement"
  answer: 2
  explanation: "The sequence — déjà vu (temporal lobe aura), automatisms (complex partial phase), then loss of consciousness with convulsions — is the classic pattern of a focal seizure with secondary generalization. Déjà vu and automatisms are hallmark temporal lobe manifestations; the subsequent bilateral convulsion means the discharge spread to involve both hemispheres. A primary generalized seizure (option A) involves both hemispheres from onset with no focal aura. Absence seizures (option B) are brief lapses without aura or post-ictal state."

- question: "Benzodiazepine withdrawal lowers the seizure threshold primarily because:"
  type: multiple-choice
  options:
    - "Withdrawal causes a surge in glutamate synthesis that overwhelms inhibitory circuits"
    - "Removing benzodiazepine potentiation suddenly reduces GABAergic inhibitory tone, tipping the excitation-inhibition balance"
    - "Benzodiazepines normally prevent voltage-gated sodium channel activation, and withdrawal unmasks these channels"
    - "Withdrawal causes hypoglycemia, depriving neurons of energy needed to maintain resting potential"
  answer: 1
  explanation: "Benzodiazepines work by potentiating GABA-A receptor function, enhancing Cl⁻ influx and inhibitory tone. Abrupt withdrawal removes this potentiation, suddenly reducing the brain's inhibitory brake. The excitation-inhibition balance tips toward excitation, lowering seizure threshold. Option A is plausible but wrong — it is not a glutamate surge but a loss of inhibition. Options C and D describe different mechanisms not central to benzodiazepine pharmacology."

- question: "Epilepsy is defined as any seizure, whether provoked or unprovoked, because seizure threshold is intrinsically lowered in most cases."
  type: true-false
  answer: false
  explanation: "Epilepsy is specifically a predisposition to *unprovoked* recurrent seizures — diagnosed after two unprovoked seizures or one with high recurrence risk. A provoked seizure (during meningitis, severe hypoglycemia, alcohol withdrawal) indicates the brain is reacting to an acute insult, not that it has an intrinsic predisposition. This distinction matters clinically: a provoked seizure may resolve when the underlying cause is treated, whereas epilepsy requires long-term antiepileptic management."

- question: "Status epilepticus is a medical emergency partly because prolonged seizure activity causes excitotoxic neuronal death via calcium overload through NMDA receptors."
  type: true-false
  answer: true
  explanation: "During status epilepticus (seizure >5 minutes or recurrent without recovery), sustained glutamatergic excitation keeps NMDA receptors open. NMDA receptors are highly permeable to Ca²⁺, and calcium overload in neurons triggers apoptotic and necrotic cell death pathways — excitotoxicity. This is not merely a theoretical risk; prolonged status causes measurable hippocampal and cortical injury. This is why terminating status epilepticus rapidly with benzodiazepines is an emergency priority."

- question: "Explain why the same underlying mechanism — excessive synchronized neuronal firing — can produce such clinically different seizure types (e.g., a 10-second lapse of awareness vs. full-body convulsions)."
  type: short-answer
  answer: "The clinical manifestation depends on WHERE in the brain abnormal discharge begins and how far it spreads. A discharge confined to thalamocortical circuits produces absence seizures — brief lapses with 3-Hz spike-wave patterns — because the thalamus gates consciousness. A discharge starting in the motor cortex produces focal jerking of the contralateral body part. If the discharge spreads to involve both hemispheres (secondary generalization), it produces the full tonic-clonic convulsion. Primary generalized seizures engage both hemispheres from onset. The underlying biology — excitation overwhelming inhibition — is the same; the geography determines what you see."
  explanation: "This is the core clinical principle of seizure semiology: location and spread, not just mechanism, determines presentation. Understanding this is what allows clinicians to localize seizure onset from clinical observation, which is essential for surgical planning in drug-resistant epilepsy."
```

## Explainer

You already understand that neurons fire action potentials when sufficient excitatory input depolarizes them past threshold, and that **GABAergic inhibition** (via Cl⁻ influx through GABA-A receptors) counters **glutamatergic excitation** (via cation influx through AMPA and NMDA receptors). Normal brain function depends on keeping excitation and inhibition in dynamic balance. A seizure is what happens when that balance fails at scale — a population of neurons becomes abnormally synchronized and fires collectively in an uncontrolled burst, spreading electrical activity through connected circuits.

The threshold for this runaway excitation depends on several interacting mechanisms. **Ion channel mutations** are a major cause: altered voltage-gated sodium channels (as in SCN1A mutations causing Dravet syndrome) can either increase persistent sodium currents (more depolarization) or impair inhibitory interneuron function (less GABAergic brake). **Reduced GABAergic tone** can result from GABA receptor mutations, benzodiazepine withdrawal (which suddenly removes potentiation of GABA-A receptors), or alcohol withdrawal — all lower the threshold for synchronized firing. **Metabolic derangements** (hypoglycemia, hyponatremia, hypoxia) deprive neurons of the energy and ion gradients needed to maintain resting membrane potential, making the entire network more susceptible to runaway depolarization.

Not all seizures look or behave alike, because the location and spread of the abnormal discharge determines the clinical manifestation. **Focal (partial) seizures** begin in a discrete cortical region: a seizure starting in the primary motor cortex produces focal motor activity; one starting in the temporal lobe may produce déjà vu, complex automatisms, or altered awareness. If the discharge spreads to involve both hemispheres, the focal seizure **secondarily generalizes**, producing the characteristic tonic-clonic convulsion. **Primary generalized seizures** involve both hemispheres from onset — absence seizures show brief lapses of consciousness with 3-Hz spike-wave discharges on EEG; generalized tonic-clonic seizures involve a tonic phase (sustained muscular contraction, often with apnea) followed by a clonic phase (rhythmic jerking) followed by the **postictal state** (confusion, fatigue, often headache) as neurons recover from the metabolic exhaustion of the discharge.

**Epilepsy** is not a single disease but a predisposition to recurrent unprovoked seizures — it is diagnosed after at least two unprovoked seizures or one seizure with high recurrence risk. The word "unprovoked" matters: a seizure during meningitis, severe hypoglycemia, or alcohol withdrawal is a provoked seizure (the brain is reacting to an acute insult, not showing an intrinsic predisposition). Antiepileptic drugs work by stabilizing the excitation-inhibition balance through various mechanisms: sodium channel blockers (valproate, phenytoin) reduce repetitive firing; GABA potentiators (benzodiazepines, barbiturates) enhance inhibition; calcium channel modulators (ethosuximide) reduce thalamic burst firing in absence epilepsy. **Status epilepticus** — a prolonged seizure exceeding 5 minutes or recurrent seizures without recovery — is a medical emergency because sustained excitation exhausts neuronal energy metabolism, leading to excitotoxic cell death via calcium overload through NMDA receptors.
