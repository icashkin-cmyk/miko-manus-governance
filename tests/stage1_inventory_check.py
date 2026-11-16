#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, subprocess, sys, time

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
EXPECTED = 21
errors = []
records = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing frontmatter opener"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "missing frontmatter closer"
    data = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if ':' not in line:
            return None, f"invalid frontmatter line: {line}"
        key, value = line.split(':', 1)
        key, value = key.strip(), value.strip()
        if key in data:
            return None, f"duplicate key: {key}"
        if value.startswith(('"', "'")) and value.endswith(value[0]):
            value = value[1:-1]
        data[key] = value
    return data, None

names = []
for path in SKILLS:
    text = path.read_text(encoding='utf-8')
    fm, err = parse_frontmatter(text)
    name = path.parent.name
    desc = ''
    if err:
        errors.append(f"{path}: {err}")
    else:
        if not fm.get('name'):
            errors.append(f"{path}: missing name")
        else:
            names.append(fm['name'])
        desc = fm.get('description', '')
        if not desc or len(desc.strip()) < 20:
            errors.append(f"{path}: description missing or too short")
    if len(text.strip()) == 0:
        errors.append(f"{path}: empty file")
    records.append({
        'path': str(path.relative_to(ROOT)),
        'directory_name': name,
        'name': fm.get('name') if fm else 'UNKNOWN',
        'description_present': bool(desc.strip()),
        'sha256': sha(path),
        'source_archive_present': (ROOT / 'source-archive' / name).exists(),
        'status': 'PASS' if not err and bool(desc.strip()) else 'FAIL'
    })

if len(SKILLS) != EXPECTED:
    errors.append(f"skill count {len(SKILLS)} != expected {EXPECTED}")
if len(set(names)) != len(names):
    errors.append('duplicate frontmatter skill names')
if sorted(names) != sorted([r['directory_name'] for r in records if r['name'] != 'UNKNOWN']):
    errors.append('frontmatter names do not match skill directory names')

out = ROOT / 'evidence/stage-01'
out.mkdir(parents=True, exist_ok=True)
(out / 'skill-inventory-current.json').write_text(json.dumps({
    'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
    'repository': str(ROOT),
    'commit': subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'], text=True).strip(),
    'expected_count': EXPECTED,
    'actual_count': len(SKILLS),
    'records': records,
    'errors': errors,
    'result': 'PASS' if not errors else 'FAIL'
}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

print(f"EXPECTED_SKILLS={EXPECTED}")
print(f"ACTUAL_SKILLS={len(SKILLS)}")
print(f"UNIQUE_NAMES={len(set(names))}")
print(f"ERROR_COUNT={len(errors)}")
for e in errors:
    print(f"ERROR: {e}")
print(f"RESULT={'PASS' if not errors else 'FAIL'}")
sys.exit(0 if not errors else 1)
