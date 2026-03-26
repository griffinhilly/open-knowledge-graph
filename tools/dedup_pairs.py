#!/usr/bin/env python3
"""Merge duplicate topic pairs: delete the weaker file, redirect references.

Usage:
    python tools/dedup_pairs.py --dry-run
    python tools/dedup_pairs.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

# (delete_id, keep_id) — from duplicate analysis
# Round 4: non-math dedup sweep (149 pairs across 18 non-math domains)
DEDUP_PAIRS = [
    # --- biology ---
    ("adult-neurogenesis", "neurogenesis-adult"),
    ("oxygen-hemoglobin-binding-cooperativity", "hemoglobin-cooperativity-oxygen-binding"),
    ("collecting-duct-water-reabsorption-adh", "collecting-duct-water-reabsorption"),
    ("antibiotic-resistance-genetic-mechanisms", "antibiotic-resistance-mechanisms"),
    ("gap-junctions-direct-communication", "gap-junctions-communication"),
    ("serotonin-systems", "serotonin-system"),
    ("dopamine-systems", "dopamine-system"),
    # --- chemistry ---
    ("fluorescence-spectroscopy-analysis", "fluorescence-spectroscopy"),
    ("titrimetric-analysis-methods", "titrimetric-analysis-intro"),
    ("electrochemistry-intro", "electrochemistry-basics"),
    ("electron-configuration-principles", "electron-configuration"),
    ("intermolecular-forces-overview", "intermolecular-forces"),
    ("kinetic-molecular-theory-overview", "kinetic-molecular-theory"),
    ("lewis-structures-basics", "lewis-structures"),
    ("periodic-trends-and-properties", "periodic-trends"),
    ("chemical-equations-balancing", "chemical-equations-and-balancing"),
    ("complexometric-titration-edta-methods", "complexometric-titration"),
    ("molecular-partition-functions-theory", "molecular-partition-functions"),
    ("variational-principle-quantum-chemistry", "variational-principle-chemistry"),
    # --- computer-science ---
    # --- economics ---
    ("new-keynesian-framework-overview", "new-keynesian-framework"),
    ("kuznets-curve-inequality", "inequality-kuznets-curve"),
    ("inflation-expectations-formation-macro", "inflation-expectations-formation"),
    # --- engineering ---
    ("binary-phase-diagrams", "phase-diagrams-binary"),
    ("fracture-mechanics-analysis", "fracture-mechanics"),
    ("fracture-mechanics-concepts", "fracture-mechanics"),
    ("polymer-structure-properties", "polymer-structure-and-properties"),
    ("vapor-compression-refrigeration-cycles", "vapor-compression-refrigeration-cycle"),
    ("parallel-RLC-resonance-characteristics", "parallel-resonance-characteristics"),
    ("series-RLC-resonance-characteristics", "series-resonance-characteristics"),
    ("frequency-response-magnitude-and-phase", "frequency-response-magnitude-phase-basics"),
    ("frequency-response-Bode-plot-basics", "frequency-response-and-bode-plots"),
    ("sinusoidal-AC-steady-state-fundamentals", "sinusoidal-steady-state-analysis"),
    ("atomic-bonding-materials", "atomic-bonding-in-materials"),
    ("heat-treatment-steels", "heat-treatment-of-steels"),
    ("absorption-refrigeration-systems", "absorption-refrigeration-cycles"),
    ("minor-loss-coefficients-fittings-elbows", "minor-loss-coefficients-fittings"),
    # --- formal-sciences-and-logic ---
    ("kolmogorov-complexity-properties", "kolmogorov-complexity"),
    ("quantifier-elimination-and-decidability", "quantifier-elimination-decidability"),
    ("cumulative-hierarchy-and-ranks", "cumulative-hierarchy-ranks"),
    ("logical-equivalence-formula-classes", "logical-equivalence-formulas"),
    ("parameterized-complexity-fpt", "parameterized-complexity-fundamentals"),
    ("elementary-equivalence-and-logical-indistinguishability", "elementary-equivalence-indistinguishability"),
    # --- health-and-human-development ---
    ("health-disparities-and-equity-frameworks", "health-disparities-equity-frameworks"),
    ("sensory-system-integration-and-perceptual-development", "sensory-integration-and-perceptual-development"),
    ("peer-relationships-and-social-competence-children", "peer-relationships-and-social-competence"),
    ("bone-remodeling-mineral-homeostasis", "bone-remodeling-and-homeostasis"),
    # --- history ---
    ("anachronism-and-presentism", "anachronism-presentism"),
    ("shang-oracle-bones-divination-writing", "oracle-bones-divination-writing"),
    ("quantitative-historical-analysis", "quantitative-history-methods"),
    # --- language-and-communication ---
    ("sentence-structure-overview", "sentence-structure-basics"),
    ("subject-verb-agreement-rules", "subject-verb-agreement"),
    ("dependent-clause-types", "dependent-clauses"),
    ("first-language-acquisition", "language-acquisition"),
    ("derivational-morphology-formal", "derivational-morphology"),
    ("inflectional-morphology-formal", "inflectional-morphology"),
    # --- literature ---
    ("dialogism-bakhtin", "bakhtin-dialogism"),
    ("comparative-literary-method", "comparative-literary-analysis"),
    ("intertextuality-kristeva", "kristeva-intertextuality"),
    ("blocking-stage-movement", "stage-blocking-movement"),
    ("figurative-language-analysis", "figurative-language"),
    ("unreliable-narrator-analysis", "unreliable-narrator"),
    ("setting-mood-atmosphere", "setting-and-atmosphere"),
    ("literary-cosmopolitanism-ethics", "literary-cosmopolitanism"),
    # --- music ---
    ("electronic-composition-fundamentals", "electronic-composition-basics"),
    ("seventh-chord-resolution-voice-leading", "seventh-chord-voice-leading-resolution"),
    ("early-20th-century-modernism", "early-modernism-20th-century"),
    ("music-history-introduction", "music-history-overview"),
    ("cadence-function-and-types", "cadence-types-and-function"),
    ("diatonic-chord-construction-fundamentals", "diatonic-chord-construction"),
    ("interval-inversion-basics", "interval-inversion"),
    ("interval-quality-basics", "interval-quality"),
    ("major-scale-construction-fundamentals", "major-scale-construction"),
    ("seventh-chord-construction-fundamentals", "seventh-chord-construction"),
    ("chord-inversion-recognition-by-ear", "chord-inversion-recognition-ear"),
    ("harmonic-function-voice-leading-analysis", "harmonic-function-and-voice-leading-analysis"),
    ("scale-degree-naming-and-function", "scale-degree-names-and-function"),
    ("bass-line-dictation-ear", "bass-line-dictation"),
    ("jazz-chord-substitution-and-voice-leading", "jazz-chord-substitution-voice-leading"),
    ("secondary-dominant-voice-leading", "secondary-dominant-extended-voice-leading"),
    ("romantic-nationalism-in-music", "romantic-nationalism-and-folk-music"),
    ("chromatic-approach-notes-voice-leading", "chromatic-approach-voice-leading"),
    # --- philosophy ---
    ("conditional-reasoning-basics", "conditional-reasoning"),
    ("language-games-wittgenstein", "wittgenstein-language-games"),
    ("original-position-rawls", "rawls-original-position"),
    ("rawlsian-justice-principles", "rawlsian-justice"),
    ("hard-problem-consciousness-definition", "hard-problem-of-consciousness"),
    ("nietzsche-apollonian-and-dionysian", "nietzsche-apollonian-dionysian"),
    ("moral-education-and-development", "moral-education-development"),
    ("argument-premise-and-conclusion", "arguments-premises-and-conclusions"),
    ("imre-lakatos-research-programs", "lakatos-research-programs"),
    ("problem-of-induction-hume", "problem-of-induction"),
    ("karl-popper-falsificationism", "popper-falsificationism"),
    ("deductive-nomological-model-of-explanation", "deductive-nomological-explanation"),
    ("egalitarian-principles", "egalitarianism"),
    ("hobbes-and-absolutism", "hobbesian-absolutism"),
    ("reference-determination-theory", "reference-determination"),
    # --- physics ---
    ("capacitance-definition", "capacitance"),
    ("electric-potential-definition", "electric-potential"),
    ("magnetic-field-definition", "magnetic-field-intro"),
    ("compton-scattering-analysis", "compton-scattering"),
    ("quantum-entanglement", "entanglement-quantum"),
    ("harmonic-oscillator-quantum", "quantum-harmonic-oscillator"),
    ("quantum-measurement-problem", "measurement-problem-quantum"),
    ("operators-and-observables", "observables-and-operators"),
    ("partition-function-fundamentals", "partition-function-definition"),
    ("renormalization-group-methods", "renormalization-group-intro"),
    ("wavelength-frequency-speed-relationship", "wavelength-frequency-speed-relation"),
    ("interference-constructive-destructive-interference", "constructive-destructive-interference"),
    ("maxwell-equations-overview", "maxwells-equations-overview"),
    ("magnetic-force-on-moving-charges", "magnetic-force-moving-charges"),
    ("lenz-law", "lenzs-law"),
    ("radiation-reaction-and-self-force", "radiation-reaction-force"),
    ("radiation-reaction-self-force", "radiation-reaction-force"),
    ("two-sources-interference-pattern", "two-source-interference-patterns"),
    ("first-order-perturbation-energy", "first-order-perturbation-theory"),
    ("scalar-and-vector-potentials", "scalar-vector-potentials"),
    ("magnetic-force-on-current-carrying-conductors", "force-on-current-carrying-conductor"),
    ("electric-dipole-moment-field", "electric-dipole-moment"),
    ("fluctuation-dissipation-theorem-general", "fluctuation-dissipation-theorem"),
    # --- practical-life-skills ---
    ("electrical-system-fundamentals", "electrical-system-basics"),
    ("seasonal-home-maintenance-tasks", "seasonal-home-maintenance"),
    ("computer-hardware-components-basics", "computer-hardware-basics"),
    ("stock-market-investing-fundamentals", "stock-market-fundamentals"),
    ("inflation-and-purchasing-power-planning", "inflation-and-purchasing-power"),
    ("tasting-evaluating-food-flavor", "tasting-evaluating-food"),
    # --- psychology ---
    ("eating-disorders-overview", "eating-disorders"),
    ("substance-use-disorder-overview", "substance-use-disorder"),
    ("substance-use-disorders-overview", "substance-use-disorder"),
    ("differential-item-functioning-analysis", "differential-item-functioning"),
    ("post-traumatic-stress-disorder", "posttraumatic-stress-disorder"),
    ("obsessive-compulsive-disorder-ocd", "obsessive-compulsive-disorder"),
    ("generalized-anxiety-disorder-gad", "generalized-anxiety-disorder"),
    ("cognitive-behavioral-therapy-clinical", "cognitive-behavioral-therapy"),
    ("cognitive-behavioral-therapy-cbt", "cognitive-behavioral-therapy"),
    ("major-depressive-disorder-mdd", "major-depressive-disorder"),
    ("antidepressant-medications-ssris", "antidepressant-medications"),
    ("receptor-subtypes-and-signaling", "receptor-types-and-signaling"),
    ("mirror-neuron-system-action-understanding", "mirror-neurons-action-understanding"),
    ("panic-disorder-and-agoraphobia", "panic-disorder-agoraphobia"),
    ("interference-and-decay-forgetting", "forgetting-and-interference"),
    ("internal-consistency-reliability", "alpha-reliability-internal-consistency"),
    ("just-world-hypothesis-belief", "just-world-belief"),
    # --- arts-and-aesthetics ---
    ("aesthetic-interpretation-and-criticism", "aesthetic-interpretation-and-critical-methods"),
    ("expression-theory-of-art", "expression-theory-art"),
    ("clive-bell-significant-form", "bell-significant-form"),
    ("art-historical-periodization", "art-history-periodization"),
    ("integrating-elements-and-principles-in-design", "integrating-elements-principles-visual-design"),
    ("accessibility-inclusive-design-principles", "accessibility-in-design"),
    # --- earth-and-space-sciences (none confirmed) ---
    # --- social-sciences (none confirmed) ---
    # --- dietary/nutrition ---
    ("dietary-fiber-types-gut-health-and-microbiota", "dietary-fiber-and-gut-health"),
]


def find_topic_file(topic_id):
    """Find the .md file for a topic ID."""
    for f in DOMAINS_DIR.rglob(f"{topic_id}.md"):
        return f
    return None


def find_references(topic_id):
    """Find all files that reference a topic ID in their frontmatter."""
    refs = []
    for f in DOMAINS_DIR.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        # Check prerequisites and builds-toward for the ID
        if topic_id in text:
            refs.append(f)
    return refs


def redirect_references(delete_id, keep_id, dry_run=True):
    """Replace all references to delete_id with keep_id in other files."""
    refs = find_references(delete_id)
    modified = 0
    for f in refs:
        # Skip the file being deleted
        if f.stem == delete_id:
            continue
        text = f.read_text(encoding="utf-8")
        # Replace the ID in prerequisites (- id: X format)
        new_text = re.sub(
            r'(?<=\bid: )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, text)
        # Also replace in builds-toward lists (- X format)
        new_text = re.sub(
            r'(?<=- )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, new_text)
        if new_text != text:
            if not dry_run:
                f.write_text(new_text, encoding="utf-8")
            modified += 1
            print(f"    {'Would update' if dry_run else 'Updated'}: {f.relative_to(ROOT)}")
    return modified


def main():
    parser = argparse.ArgumentParser(description="Deduplicate topic pairs")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()
    dry_run = not args.apply

    print(f"Deduplicating {len(DEDUP_PAIRS)} pairs ({'DRY RUN' if dry_run else 'APPLYING'})\n")

    total_deleted = 0
    total_redirected = 0

    for delete_id, keep_id in DEDUP_PAIRS:
        delete_file = find_topic_file(delete_id)
        keep_file = find_topic_file(keep_id)

        if not delete_file:
            print(f"  SKIP {delete_id}: file not found")
            continue
        if not keep_file:
            print(f"  SKIP {delete_id}: keeper {keep_id} not found")
            continue

        print(f"  {delete_id} → {keep_id}")

        # Redirect references
        redirected = redirect_references(delete_id, keep_id, dry_run)
        total_redirected += redirected

        # Delete the file
        if not dry_run:
            delete_file.unlink()
        total_deleted += 1
        print(f"    {'Would delete' if dry_run else 'Deleted'}: {delete_file.relative_to(ROOT)}")

    print(f"\nSummary: {total_deleted} files {'to delete' if dry_run else 'deleted'}, "
          f"{total_redirected} files {'to update' if dry_run else 'updated'}")

    if dry_run:
        print("\nUse --apply to execute.")


if __name__ == "__main__":
    main()
