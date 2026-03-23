#!/usr/bin/env python3
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/audit/biology.json', 'r', encoding='utf-8') as f:
    biology = json.load(f)

with open('tools/audit/physics.json', 'r', encoding='utf-8') as f:
    physics = json.load(f)

# ============================================================================
# BIOLOGY RECOMMENDATIONS
# ============================================================================

bio_recs = []

# 1. BIOCHEMISTRY: advanced -> formal-systems
biochem_downgrade = {
    'amino-acid-classification-and-properties': 'Fundamental protein building blocks taught in intro biochemistry',
    'amino-acid-structure-and-properties': 'Fundamental protein building blocks taught in intro biochemistry',
    'amino-acid-degradation-overview': 'Standard metabolic pathway in undergrad biochemistry',
    'aromatic-amino-acid-catabolism': 'Standard metabolic pathway in undergrad biochemistry',
    'atp-hydrolysis-and-free-energy': 'Fundamental bioenergetics in intro biochemistry courses',
    'atp-synthase-structure-mechanism': 'ATP synthesis taught in standard undergrad biochemistry',
    'branched-chain-amino-acid-catabolism': 'Standard metabolic pathway in undergrad biochemistry',
    'carbohydrate-homeostasis': 'Standard metabolic regulation in undergrad biochemistry',
    'carbohydrate-structure-and-classification': 'Fundamental biochemistry covered in intro courses',
    'citric-acid-cycle-mechanism': 'Fundamental pathway in standard undergrad biochemistry courses',
    'citric-acid-cycle-regulation': 'Central metabolism taught in standard undergrad biochemistry',
    'enzyme-cofactors-and-coenzymes': 'Fundamental enzyme biochemistry taught in intro courses',
    'fad-fadh2-and-other-redox-carriers': 'Basic cofactors in standard undergrad biochemistry',
    'fatty-acid-oxidation-beta-oxidation': 'Standard metabolic pathway in undergrad biochemistry',
    'fatty-acid-structure-and-classification': 'Fundamental biochemistry covered in intro courses',
    'fatty-acid-synthesis': 'Standard metabolic pathway in undergrad biochemistry',
    'gluconeogenesis': 'Standard metabolic pathway in undergrad biochemistry',
    'glycolysis-mechanism-and-regulation': 'Central pathway in standard undergrad biochemistry courses',
    'lipolysis-and-fatty-acid-mobilization': 'Standard metabolic regulation in undergrad biochemistry',
    'lipoproteins-structure-and-transport': 'Standard biochemistry topic in intro courses',
    'membrane-lipids-and-lipoproteins': 'Fundamental cell biology in standard undergrad courses',
    'michaelis-menten-enzyme-kinetics': 'Fundamental enzyme kinetics in intro biochemistry courses',
    'nad-nadh-structure-and-function': 'Basic cofactors in standard undergrad biochemistry',
    'nucleotide-salvage-pathways': 'Standard metabolic pathway in undergrad biochemistry',
    'nucleotide-structure-and-nomenclature': 'Fundamental biochemistry covered in intro courses',
    'nucleotide-synthesis': 'Standard metabolic pathway in undergrad biochemistry',
    'oxidative-phosphorylation-and-chemiosmosis': 'Central bioenergetics in standard undergrad courses',
    'peptide-bonds-and-polypeptide-formation': 'Fundamental protein chemistry in intro biochemistry',
    'phospholipid-biosynthesis': 'Standard metabolic pathway in undergrad biochemistry',
    'protein-folding-and-chaperones': 'Fundamental biochemistry covered in intro courses',
    'sulfur-amino-acid-metabolism': 'Standard metabolic pathway in undergrad biochemistry',
}

for topic_id, rationale in biochem_downgrade.items():
    bio_recs.append({
        'id': topic_id,
        'course': 'biochemistry',
        'current': 'advanced',
        'recommended': 'formal-systems',
        'confidence': 'high',
        'rationale': rationale
    })

# 2. MICROBIOLOGY: advanced -> formal-systems (intro content)
micro_downgrade = {
    'bacterial-anaerobic-respiration-and-fermentation': 'Fundamental bacterial metabolism in intro microbiology',
    'bacterial-cell-wall-architecture': 'Fundamental bacterial structure in intro microbiology courses',
    'bacterial-flagella-and-chemotaxis': 'Fundamental bacterial motility in intro microbiology courses',
    'bacterial-flagella-pili-motility-adhesion': 'Fundamental bacterial structures in intro microbiology',
    'bacterial-metabolism-overview': 'Fundamental bacterial metabolism in intro microbiology courses',
    'fermentation-pathways-and-end-products': 'Standard metabolic pathway in undergrad microbiology',
    'flagellar-motor-rotation': 'Detailed bacterial motility mechanism in intro microbiology',
    'fungal-spore-conidia-ascospores': 'Fungal reproduction in standard microbiology courses',
    'gram-staining-and-cell-wall-classification': 'Fundamental lab technique in intro microbiology courses',
    'industrial-fermentation-and-production-microbiology': 'Applied microbiology in standard undergrad courses',
    'microbial-fermentation': 'Fundamental metabolic pathway in intro microbiology courses',
    'viral-replication-dna-polymerase': 'Basic viral replication in standard microbiology courses',
    'viral-replication-rna-polymerase': 'Basic viral replication in standard microbiology courses',
    'yeast-fermentation-and-metabolic-pathways': 'Standard metabolic topic in undergrad microbiology',
}

for topic_id, rationale in micro_downgrade.items():
    bio_recs.append({
        'id': topic_id,
        'course': 'microbiology',
        'current': 'advanced',
        'recommended': 'formal-systems',
        'confidence': 'high',
        'rationale': rationale
    })

# ============================================================================
# PHYSICS RECOMMENDATIONS
# ============================================================================

phys_recs = []

# 1. MODERN PHYSICS: advanced -> formal-systems
modern_downgrade = {
    'blackbody-radiation': 'Intro-level modern physics covered in standard undergrad courses',
    'compton-scattering-analysis': 'Intro-level modern physics covered in standard undergrad courses',
    'compton-scattering': 'Intro-level modern physics covered in standard undergrad courses',
    'compton-wavelength-shift': 'Intro-level modern physics covered in standard undergrad courses',
    'gamma-decay-emission': 'Intro-level nuclear physics covered in standard undergrad courses',
    'lorentz-transformation': 'Special relativity foundations in standard undergrad physics',
    'mass-energy-equivalence-relativity': 'Fundamental special relativity in standard undergrad physics',
    'mass-energy-equivalence': 'Fundamental special relativity in standard undergrad physics',
    'nuclear-mass-binding-energy': 'Fundamental nuclear physics in standard undergrad courses',
    'photoelectric-effect': 'Canonical intro-level modern physics topic',
    'photon-absorption-emission': 'Standard topic in intro modern physics courses',
    'photon-concept-quanta': 'Fundamental photon concept in intro modern physics',
    'photon-model': 'Fundamental photon concept in intro modern physics',
    'photon-particle-properties': 'Fundamental photon properties in intro modern physics',
    'planck-einstein-relation': 'Fundamental relationship in intro modern physics',
    'planck-quantization-hypothesis': 'Foundational concept in intro modern physics',
    'special-relativity-postulates': 'Special relativity fundamentals in standard undergrad physics',
    'wave-particle-duality-observations': 'Fundamental concept covered in intro modern physics',
    'wave-particle-duality': 'Fundamental concept covered in intro modern physics',
}

for topic_id, rationale in modern_downgrade.items():
    phys_recs.append({
        'id': topic_id,
        'course': 'modern-physics',
        'current': 'advanced',
        'recommended': 'formal-systems',
        'confidence': 'high',
        'rationale': rationale
    })

# 2. QUANTUM MECHANICS: formal-systems -> advanced
qm_upgrade = {
    'bell-inequalities': 'Advanced quantum foundations requiring substantial QM background',
    'bell-theorem': 'Advanced quantum foundations requiring substantial QM background',
    'canonical-commutation-relations-quantum-mechanics': 'Formal QM mathematical structure in upper-division courses',
    'commutation-relations': 'Formal QM mathematical structure in upper-division courses',
    'dirac-notation': 'Formal QM notation introduced in upper-division quantum courses',
    'exchange-symmetry': 'Advanced many-body quantum mechanics in upper-division courses',
    'fermions-and-bosons': 'Advanced quantum statistics in upper-division courses',
    'hilbert-space-formalism': 'Formal mathematical structure in upper-division quantum courses',
    'identical-particles-quantum': 'Advanced many-body quantum mechanics in upper-division courses',
    'kets-and-bras': 'Formal QM notation in upper-division quantum courses',
    'slater-determinant': 'Advanced many-body quantum mechanics in upper-division courses',
}

for topic_id, rationale in qm_upgrade.items():
    phys_recs.append({
        'id': topic_id,
        'course': 'quantum-mechanics',
        'current': 'formal-systems',
        'recommended': 'advanced',
        'confidence': 'high',
        'rationale': rationale
    })

# Write to files
with open('tools/audit/biology_recommendations.json', 'w', encoding='utf-8') as f:
    json.dump(bio_recs, f, indent=2, ensure_ascii=False)

with open('tools/audit/physics_recommendations.json', 'w', encoding='utf-8') as f:
    json.dump(phys_recs, f, indent=2, ensure_ascii=False)

print(f"✓ Biology: {len(bio_recs)} recommendations written")
print(f"✓ Physics: {len(phys_recs)} recommendations written")
print()
print("Files:")
print("  tools/audit/biology_recommendations.json")
print("  tools/audit/physics_recommendations.json")
