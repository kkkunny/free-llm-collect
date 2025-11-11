#!/usr/bin/env python3
from pathlib import Path
import json
import html

ROOT = Path(__file__).resolve().parents[1]
providers_dir = ROOT / 'providers'
readme_template = ROOT / 'README_template.md'
output_readme = ROOT / 'README.md'

def sanitize_cell(text: str) -> str:
    # Escape pipe and wrap HTML-escaped text
    if text is None:
        return ''
    text = str(text)
    text = text.replace('|', '\\|')
    return html.escape(text)

def format_desc(raw: str) -> str:
    if not raw:
        return ''
    lines = []
    for line in raw.splitlines():
        s = line.strip()
        # Remove leading + bullet marks
        if s.startswith('+'):
            s = s.lstrip('+').strip()
        # Remove leading dashes or bullets
        if s.startswith('-'):
            s = s.lstrip('-').strip()
        if s:
            lines.append(html.escape(s))
    # Join with <br> so markdown table preserves line breaks
    return '<br>'.join(lines)

rows = []
for p in sorted(providers_dir.glob('*.json')):
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"Skipping {p.name}: failed to parse JSON: {e}")
        continue
    name = data.get('name') or p.stem
    path = data.get('path') or ''
    free = data.get('config', {}).get('free', None)
    if free is True:
        free_str = 'Yes'
    elif free is False:
        free_str = 'No'
    else:
        free_str = ''
    desc_raw = data.get('desc', '')
    desc = format_desc(desc_raw)

    # Use markdown link for Path if present
    link_md = f"[{html.escape(name)}]({html.escape(path)})" if path else html.escape(name)

    rows.append((name, link_md, free_str, desc))

# Build markdown table
table_lines = []
table_lines.append('| Name | Free | Description |')
table_lines.append('|---|:---:|---|')
for name, link_md, free_str, desc in rows:
    # desc may contain HTML escapes and <br>
    table_lines.append(f'| {link_md} | {free_str} | {desc} |')

table_md = '\n'.join(table_lines) + '\n'

# Read template and replace placeholder
tpl = readme_template.read_text(encoding='utf-8')
if '{{ Providers }}' not in tpl:
    print('Placeholder "{{ Providers }}" not found in README_template.md')
    new_content = tpl + '\n' + table_md
else:
    new_content = tpl.replace('{{ Providers }}', table_md)

# Write README.md
output_readme.write_text(new_content, encoding='utf-8')
print('Generated README.md with providers table.')