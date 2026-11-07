"""Parse each file's frontmatter + Questions YAML; print problems. Usage: yaml_check.py files..."""
import sys,re,yaml,pathlib
bad=0
for p in sys.argv[1:]:
    t=pathlib.Path(p).read_text(encoding='utf-8')
    try:
        yaml.safe_load(t.split('---')[1])
        m=re.search(r'^## Questions\s*\n(.*?)(?=^## |\Z)',t,re.M|re.S)
        f=re.search(r'```ya?ml[ \t]*\n(.*?)```',m.group(1),re.S) if m else None
        q=yaml.safe_load(f.group(1)) if f else None
        assert q is None or isinstance(q,list), 'questions not a list'
        for i,x in enumerate(q or []):
            for k in ('question','type','answer','explanation'):
                assert k in x, f'q{i} missing {k}'
            if x['type']=='multiple-choice': assert isinstance(x['answer'],int) and 0<=x['answer']<len(x['options']), f'q{i} bad mc answer'
    except Exception as e: bad+=1; print('BAD',p,str(e)[:100])
print('yaml ok' if not bad else f'{bad} bad')
