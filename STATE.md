# State

## Current Phase
Phase 9: Learning Platform — IN PROGRESS (9A complete, 9B built + iterated)
Phase 8: Community Launch — nearly complete (cleanup pass + announcement remaining)

## Last Worked On (Mar 21, 2026)
- **Phase 9B: Quiz engine built + iterated through several rounds of feedback**
  - `tools/generate_assessment_questions.py` — extracts questions, selects quiz pool (228 warmup + 506 exploration), builds topic index (13,518 topics by domain+stage) for post-assessment inference
  - `tools/generate_quiz_page.py` — generates self-contained `output/quiz.html` (1.4 MB with embedded fluency.js + question data + topic index)
  - Adaptive tier-based warmup: 3 questions per stage tier × 5 tiers = ~15 questions, always escalates (doesn't stop on easy misses)
  - Phase 2 exploration: per-domain adaptive, "Something Different" / "Skip Domain" / "I'm Done" controls
  - Results with post-assessment inference, tier estimation, confidence tracking
- **Fluency model extended** (`lib/fluency.js`):
  - Confidence tracking: `okg-fluency-conf` localStorage key, 0-1 per topic
  - `postAssessmentInference()`: overall academic tier estimation + tier-based universal floors on general-ed domains + per-domain ceiling inference
  - General-ed vs specialized domain categorization (music, arts, engineering, philosophy, formal-sciences are specialized — only infer with direct evidence)
  - Single wrong answer confidence = 0.45 (inference CAN override); two answers = 0.70 (locked in)
- **Fixed 11 mis-staged physics topics** (electrodynamics abstract-reasoning → advanced, thermodynamics ideal-gas-law → formal-systems)
- **Stage audit completed**: ~274 potentially mis-staged topics across 23 courses (~2% of graph). See MEMORY.md for details.
- **Index page updated**: Quiz + Assessment links added

## Known Issues / Blockers
- **~274 mis-staged topics** across 23 courses need fixing (120 high-confidence, 60 medium, 90 debatable). Priority: theory-of-computation (32), cell-biology (26), research-methods-psychology (23), oceanography (17), thermodynamics (4), 1st-grade math (5)
- ~294 topics still missing questions (from earlier Q5 swarm failures)
- ~229 topics may still be missing explainers (shard 22 partial completion)
- ~11,035 expansion topics still at status: draft (content validated, promotion deferred by choice)
- Phase 9A deferred items: hub topic labels at moderate zoom, directional edge rendering
- Quiz not yet tested on GitHub Pages (local file:// only)
- Quiz UX still being refined — Griffin wants the assessment to more accurately estimate "brain tier" without relying on domain-specific trivia at lower stages

## Next Steps (in priority order)
1. Fix ~120 high-confidence mis-staged topics (6 priority courses)
2. Push all new/changed files to GitHub
3. Test quiz end-to-end on GitHub Pages
4. Phase 9C: Assessment Phase 3 (deep dive, short-answer) + Results screen redesign
5. Phase 9D: Landing page redesign + domain toggle + progress bars + polish
6. Remaining Phase 8 items (draft→validated promotion decision, announcement)
