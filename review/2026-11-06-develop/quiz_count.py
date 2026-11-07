"""Count quizzable questions with the site's own extractor + filter."""
import sys,pathlib; sys.path.insert(0,'tools')
from parse_topic import parse_topic, extract_questions
from generate_assessment_questions import is_quizzable
n=q=t=0
for f in pathlib.Path('domains').rglob('*.md'):
    if f.name.startswith('_'): continue
    r=parse_topic(f)
    if not r or not r[0]: continue
    qs=extract_questions(r[1]) or []; n+=len(qs); k=sum(1 for x in qs if is_quizzable(x)); q+=k; t+= k>0
print(f"questions extracted {n}, quizzable {q}, topics with >=1 quizzable {t}")
