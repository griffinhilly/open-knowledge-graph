#!/usr/bin/env python3
"""Comprehensive fix for all dangling prerequisite references.

Applies two operations:
1. FIXES: Replace dangling prereq IDs with correct existing topic IDs
2. REMOVES: Delete prereq entries that reference non-existent topics with no valid match

Run with --dry-run first, then without to apply.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

# ---- MAPPING: dangling_id -> correct_id ----
FIXES = {
    # Tier 1: Clear ID renames (high confidence)
    "2d-shapes-attributes-3rd": "shapes-2d-attributes-3rd",
    "abstract-objects-platonism": "abstract-entities-platonism",
    "alveolar-gas-exchange-diffusion": "gas-exchange-alveoli-and-diffusion",
    "art-and-political-intervention": "art-political-intervention",
    "autoimmune-disease-mechanisms": "autoimmunity-mechanisms",
    "autonomic-nervous-system-physiology": "autonomic-nervous-system",
    "bayesian-inference": "bayesian-inference-intro",
    "boolean-functions": "boolean-functions-and-circuits",
    "buffer-chemistry": "buffer-chemistry-le-chatelier-application",
    "buoyancy": "buoyancy-and-archimedes",
    "calculus-of-variations": "calculus-of-variations-euler-lagrange",
    "catholic-church-power": "medieval-church-power",
    "cell-junctions-adhesion-tissue": "cell-junctions-adhesion-communication",
    "chi-square-distribution": "chi-square-distribution-theory",
    "coagulation-cascade-and-pathways": "hemostasis-coagulation-cascade",
    "compactness": "compactness-hausdorff-spaces",
    "complement-cascade-and-pathways": "complement-activation-pathways",
    "connectedness": "connectedness-definition-examples",
    "consumer-theory": "consumer-theory-utility",
    "coronary-circulation-anatomy": "coronary-circulation-physiology",
    "cost-benefit-analysis-epidemiology": "cost-effectiveness-analysis-epidemiology",
    "dependent-clause-types": "dependent-clauses",
    "descriptive-statistics": "descriptive-statistics-overview",
    "differential-equations": "differential-equations-intro",
    "distance-formula": "distance-and-distance-formula-3d",
    "dynamic-optimization-lagrange": "dynamic-optimization-macro",
    "electron-transfer": "electron-transfer-reactions",
    "endothelial-dysfunction": "endothelial-dysfunction-pathophysiology",
    "energy-conservation": "energy-conservation-applications",
    "energy-conservation-mechanical-systems": "conservation-of-energy-mechanical-systems",
    "expected-value-and-variance-of-assets": "expected-return-and-variance-of-assets",
    "exponential-decay": "exponential-growth-and-decay",
    "f-distribution": "f-distribution-theory",
    "fed-fasted-metabolic-state": "fed-fasted-metabolic-state-and-hormonal-signaling",
    "fourier-series-intro": "fourier-series-definition",
    "frequency-response-magnitude-phase-plots": "frequency-response-magnitude-phase",
    "function-composition": "function-composition-and-inverses",
    "function-properties": "functions-and-function-properties",
    "glomerular-filtration-barrier": "glomerular-filtration-barrier-and-proteinuria",
    "glomerular-filtration-rate": "glomerular-filtration-rate-autoregulation",
    "gravitation": "newtons-law-of-gravitation",
    "homeomorphisms": "homeomorphisms-definition-properties",
    "hypothalamic-pituitary-axis": "hypothalamus-pituitary-axis",
    "hypothesis-testing-intro": "hypothesis-testing-fundamentals",
    "immune-memory-and-secondary-immune-response": "immunological-memory-secondary-response",
    "inflectional-morphology-formal": "inflectional-morphology",
    "information-asymmetry-markets": "information-asymmetry",
    "inner-products": "inner-product-spaces",
    "intracellular-signaling": "intracellular-signaling-and-second-messengers",
    "inverse-square-law-point-interactions": "coulomb-law-point-interactions",
    "jacobian-matrix": "jacobian-change-of-variables",
    "kinematics-rigid-body-rotation": "rigid-body-kinematics-rotation",
    "kinetic-molecular-theory-basics": "kinetic-molecular-theory",
    "language-ideology": "language-attitudes-and-ideology",
    "logarithms": "logarithms-intro",
    "maximum-likelihood-estimation": "maximum-likelihood-estimation-theory",
    "maxwells-equations": "maxwells-equations-overview",
    "measurement-in-psychology": "measurement-scales-psychology",
    "measurement-with-standard-units-length": "measuring-with-standard-units-length",
    "memory-consolidation": "memory-consolidation-systems",
    "metabolic-syndrome-pathophysiology": "obesity-metabolic-syndrome-and-nutritional-pathophysiology",
    "metric-spaces-introduction": "metric-spaces-definition",
    "mineral-properties-and-identification": "mineral-properties-and-testing",
    "minimalism-iteration-structures": "minimalism-phase-structures",
    "neuronal-excitability-and-action-potentials": "action-potential",
    "noethers-theorem": "noethers-theorem-fields",
    "nondeterministic-polynomial-time": "nondeterministic-polynomial-time-computability-and-complexity",
    "ocean-heat-content-and-thermal-inertia": "marine-heat-content-and-thermal-inertia",
    "open-and-closed-sets-real-line": "open-closed-sets-real-line",
    "pancreatic-beta-cell-function": "pancreatic-beta-cell-insulin-secretion",
    "parathyroid-hormone-function": "parathyroid-hormone-calcium-regulation",
    "permutations-and-combinations": "permutations-and-arrangements",
    "plate-boundaries-convergent": "plate-boundaries-intro",
    "plate-boundary-convergent": "plate-boundary-forces",
    "platelet-activation-and-aggregation": "platelet-activation-and-aggregation-pathophysiology",
    "pragmatics": "pragmatics-and-argumentation",
    "predicate-logic": "predicate-logic-introduction",
    "pressure-and-forces": "pressure-and-forces-in-fluids",
    "principle-of-virtual-work-method": "virtual-work-method",
    "propositional-logic": "propositional-logic-introduction",
    "prose-poetry-hybrid-form-hybrid-form": "prose-poetry-hybrid-form",
    "protein-protein-interactions": "protein-protein-interactions-structural",
    "reactive-oxygen-metabolism": "peroxisomes-and-reactive-oxygen-metabolism",
    "recursively-enumerable-languages": "recursively-enumerable-languages-properties",
    "regulatory-t-cells-immune-tolerance-immune-tolerance": "regulatory-t-cells-immune-tolerance",
    "rings-and-ideals": "subrings-and-ideals",
    "sat-boolean-satisfiability": "sat-boolean-satisfiability-computability-and-complexity",
    "sensory-transduction": "sensory-transduction-and-encoding",
    "speaker-voice-development": "authentic-speaker-voice-development",
    "spacetime-diagrams-minkowski": "spacetime-diagrams",
    "standard-deviation": "variance-standard-deviation",
    "statistical-inference": "statistical-inference-significance-testing",
    "supply-and-demand": "supply-and-demand-basics",
    "survey-sampling-methods": "sampling-methods",
    "systems-of-equations": "systems-of-linear-equations",
    "t-cell-receptor-structure-and-function-and-function": "t-cell-receptor-structure-and-function",
    "t-distribution": "t-distribution-theory",
    "tangent-spaces": "tangent-vectors-and-tangent-spaces",
    "thermostat-structure-of-atmosphere": "thermal-structure-of-atmosphere",
    "thyroid-hormone-synthesis": "thyroid-hormone-synthesis-regulation",
    "trigonometric-identities": "trigonometric-identities-pythagorean",
    "type-i-type-ii-errors": "type-i-and-type-ii-errors",
    "uv-vis-spectroscopy-quantitative": "ultraviolet-visible-spectroscopy-quantitative",

    # Tier 2: Course-name / broad-subject refs → best foundational topic
    "calculus": "fundamental-theorem-of-calculus-part-1",
    "fractions": "intro-to-fractions",
    "linear-algebra": "linear-transformations",
    "probability-distributions": "probability-density-functions",
    "probability-theory": "probability-axioms",
    "protein-folding-and-stability": "protein-folding-and-chaperones",
    "protein-structure-and-function": "protein-tertiary-structure",
    "type-systems-type-checking": "type-systems-overview",
    "utility-maximization": "consumer-theory-utility",
    "research-methods-psychology-intro": "scientific-method-psychology",
    "research-methods-psychology": "scientific-method-psychology",
    "sequences-and-series": "arithmetic-sequences-and-series",
    "special-relativity": "special-relativity-postulates",
    "spin": "spin-quantum-number",
    "recursion": "recursion-on-finite-structures",
    "ordinary-differential-equations": "differential-equations-intro",

    # Tier 3: Semantic matches requiring judgment
    "acids-and-bases": "everyday-acids-and-bases",
    "combinatorics": "probability-with-combinatorics",
    "redox-reactions-organic": "reduction-reactions-organic",
    "protein-synthesis": "ribosomes-and-protein-synthesis-intro",
    "protein-synthesis-overview": "ribosomes-and-protein-synthesis-intro",
    "protein-biosynthesis-intro": "ribosomes-and-protein-synthesis-intro",
    "random-variables": "continuous-random-variables",
    "ratios-and-proportions": "proportions",
    "steady-state-error-system-type": "steady-state-error-analysis",
    "tensor-products-vector-spaces": "tensor-products-universal",
    "symmetric-group": "representations-of-symmetric-groups",
    "quotient-spaces": "quotient-groups",
    "lcm-gcd": "divisibility-and-gcd",
    "least-common-multiple": "divisibility-and-gcd",
    "probability-distributions-theory": "probability-density-functions",
    "stochastic-processes": "stationary-processes",
}

# ---- REMOVE: dangling IDs with no valid match ----
REMOVES = {
    "abnormal-psychology",
    "absorption-and-emission-spectroscopy",
    "airway-smooth-muscle-contraction",
    "alveolar-capillary-barrier",
    "analytic-functions",
    "analytical-thesis-development",
    "apoptosis-pathways",
    "auditory-system-overview",
    "bacterial-fermentation-and-anaerobic-pathways",
    "basal-metabolic-rate-thyroid",
    "boussinesq-approximation",
    "buoyancy-forces",
    "calcium-phosphate-homeostasis",
    "carbon-chemistry",
    "cardiac-output-and-perfusion",
    "cell-adhesion-molecules",
    "cerebral-circulation-and-autoregulation",
    "chromatic-harmony",
    "classical-mechanics",
    "complex-analysis",
    "consumer-choice-theory",
    "convergence-rigorous-series",
    "cytochrome-p450-metabolism",
    "data-structures-and-algorithms-basics",
    "density-and-buoyancy-fluids",
    "density-driven-flow",
    "differential-geometry",
    "disturbance-and-ecosystem-recovery",
    "dna-recombination",
    "elastic-recoil-and-compliance",
    "endocannabinoid-signaling-and-modulation",
    "enzyme-specificity-and-selectivity",
    "equilibrium-chemical",
    "exponential-decay-growth",
    "first-law-energy-conservation",
    "four-vectors",
    "general-relativity-intro",
    "glucose-metabolism-and-homeostasis",
    "greatest-common-divisor",
    "hepatic-stellate-cell-activation",
    "hepatocellular-injury-mechanisms",
    "historical-context-and-influence",
    "home-safety-checklist",
    "hydrostatic-equilibrium",
    "implicit-function-theorem",
    "inequalities",
    "inequalities-intro",
    "infinite-series",
    "inflammation-innate-response",
    "insulin-signaling-pathways",
    "integral-calculus",
    "integrals",
    "international-capital-flows",
    "introspection-and-phenomenal-knowledge",
    "inverse-function-theorem",
    "iron-metabolism-and-storage",
    "light-bending-gravitational-fields",
    "light-deflection",
    "linear-algebra-basics",
    "linear-algebra-foundations",
    "linear-algebra applications",
    "liver-function-overview",
    "logistic-function",
    "loss-of-central-tolerance",
    "macroeconomics",
    "magnetohydrodynamics",
    "market-structure-overview",
    "measurement-units-standard",
    "mechanical-ventilation",
    "metabolic-acidosis-and-alkalosis-pathophysiology",
    "minor-scale-construction",
    "myofibroblast-differentiation",
    "neural-energy-metabolism",
    "neurotransmitter-reuptake",
    "nominalism-about-universals",
    "numerical-methods",
    "partial-differential-equations",
    "partial-differential-equations-intro",
    "periodic-functions",
    "periodicity",
    "philosophy-intro",
    "platelet-structure-function",
    "potential-theory-and-methods",
    "pressure-gradient-force",
    "probability",
    "probability-and-statistics",
    "production-theory",
    "proof-by-induction",
    "pyruvate-metabolism-overview",
    "quadratic-programming",
    "quantum-transitions",
    "radiative-transfer-equation",
    "rayleigh-benard-convection",
    "real-analysis-basics",
    "recursive-definitions",
    "red-blood-cell-structure-and-function",
    "redox-chemistry-intro",
    "renin-angiotensin-aldosterone-system",
    "sensory-system-overview",
    "series-convergence-tests",
    "skip-counting-patterns-skip-counting",
    "spectroscopy-fundamentals",
    "starling-forces-microcirculation",
    "statistics",
    "statistics-rigorous",
    "steroid-hormone-synthesis",
    "symmetry-matrices-properties",
    "task-switching-cognitive-flexibility",
    "thermodynamics-intro",
    "thyroid-gland-anatomy-and-function",
    "trigonometric-functions",
    "trigonometric-functions-and-graphs",
    "trigonometric-functions-review",
    "trigonometry",
    "tubular-function-and-reabsorption",
    "vascular-permeability-control",
    "visual-ethnography-theory",
    "vitamin-b12-and-folate-metabolism",
    "word-choice-diction-effect",
    "youngs-modulus-elasticity",
}


def load_all_topic_ids():
    ids = set()
    for md in DOMAINS_DIR.rglob("*.md"):
        if not md.name.startswith("_"):
            ids.add(md.stem)
    return ids


def verify_targets(all_ids):
    """Check that all FIX targets actually exist."""
    errors = []
    for old_id, new_id in FIXES.items():
        if new_id not in all_ids:
            errors.append(f"  FIX target missing: {old_id} -> {new_id}")
    return errors


def apply_all(dry_run=True):
    all_ids = load_all_topic_ids()

    # Verify targets exist
    errors = verify_targets(all_ids)
    if errors:
        print("ERROR: Some fix targets don't exist as topics:")
        for e in errors:
            print(e)
        print("\nFix these before applying.")
        return

    # Pre-compile all patterns
    fix_patterns = []
    for old_id, new_id in FIXES.items():
        fix_patterns.append((
            old_id,
            new_id,
            re.compile(rf'((?:- )?id: ){re.escape(old_id)}(\s)'),
            re.compile(rf'(  - ){re.escape(old_id)}(\s)'),
        ))
    remove_patterns = []
    for rid in REMOVES:
        remove_patterns.append((
            rid,
            re.compile(rf'- id: {re.escape(rid)}\n  type: (?:hard|soft)\n'),
            re.compile(rf'  - {re.escape(rid)}\n'),
        ))

    fix_count = 0
    remove_count = 0
    files_modified = 0

    for md in sorted(DOMAINS_DIR.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue

        if not text.startswith("---"):
            continue

        new_text = text
        file_fixes = 0
        file_removes = 0

        # Apply FIXES: replace IDs (skip if old_id not in text at all)
        for old_id, new_id, pat1, pat2 in fix_patterns:
            if old_id not in new_text:
                continue
            if pat1.search(new_text):
                new_text = pat1.sub(rf'\g<1>{new_id}\2', new_text)
                file_fixes += 1
            if pat2.search(new_text):
                new_text = pat2.sub(rf'\g<1>{new_id}\2', new_text)
                file_fixes += 1

        # Apply REMOVES: delete prereq entries (skip if rid not in text)
        for rid, rpat1, rpat2 in remove_patterns:
            if rid not in new_text:
                continue
            if rpat1.search(new_text):
                new_text = rpat1.sub('', new_text)
                file_removes += 1
            if rpat2.search(new_text):
                new_text = rpat2.sub('', new_text)

        if new_text != text:
            fix_count += file_fixes
            remove_count += file_removes
            files_modified += 1
            if not dry_run:
                md.write_text(new_text, encoding="utf-8")
            else:
                if file_fixes:
                    print(f"  FIX ({file_fixes}): {md.relative_to(ROOT)}")
                if file_removes:
                    print(f"  REMOVE ({file_removes}): {md.relative_to(ROOT)}")

    print(f"\n{'DRY RUN' if dry_run else 'APPLIED'}:")
    print(f"  Files modified: {files_modified}")
    print(f"  ID replacements: {fix_count}")
    print(f"  Prereqs removed: {remove_count}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply fixes (default is dry run)")
    args = parser.parse_args()
    apply_all(dry_run=not args.apply)
