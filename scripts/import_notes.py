#!/usr/bin/env python3
"""Import only explicitly selected, publishable knowledge notes."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def convert(text, slug):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Invalid slug')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z', text, re.S)
    if not match:
        raise ValueError('Missing front matter')
    meta = yaml.safe_load(match[1])
    if meta.get('publish') is not True:
        raise ValueError('Note is not explicitly publishable')
    day = dt.date.fromisoformat(str(meta['date'])[:10]).isoformat()
    body = match[2].lstrip('\n')
    lines = body.splitlines()
    if lines and lines[0] == '# ' + meta['title']:
        body = '\n'.join(lines[1:]).lstrip('\n') + '\n'
    if '[[' in body or re.search(r'!?\[[^\]]*\]\((?!https?://|mailto:|#)[^)]+\)', body):
        raise ValueError('Resolve wiki links and local attachments before importing')
    out = {
        'layout': 'post', 'title': meta['title'], 'date': day,
        'last_modified_at': str(meta.get('updated', meta.get('created', day))),
        'author': 'jungseob', 'categories': ['지식 노트'],
        'tags': [t for t in meta.get('tags', []) if t not in ('knowledge', 'blog')],
        'description': meta.get('description', ''), 'source': meta.get('source', ''),
        'source_title': meta.get('source_title', ''), 'source_author': meta.get('author', ''),
        'source_published': str(meta.get('published', '')),
        'published': True, 'render_with_liquid': False,
    }
    return f'{day}-{slug}.md', '---\n' + yaml.safe_dump(out, allow_unicode=True, sort_keys=False) + '---\n\n' + body


def import_notes(source_dir, selection, destination):
    source_dir = Path(source_dir).resolve()
    pending = {}
    manifest = []
    for entry in selection:
        filename = entry['file']
        source = (source_dir / filename).resolve()
        if Path(filename).name != filename or source.parent != source_dir:
            raise ValueError('Source must be a direct child of the selected directory')
        original = source.read_text(encoding='utf-8')
        name, content = convert(original, entry['slug'])
        if name in pending:
            raise ValueError('Duplicate destination')
        pending[name] = content
        manifest.append({'source_file': filename, 'post': name, 'sha256': hashlib.sha256(original.encode()).hexdigest()})
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for name, content in pending.items():
        (destination / name).write_text(content, encoding='utf-8')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', required=True, type=Path)
    parser.add_argument('--selection', type=Path, default=ROOT / 'publishing/selection.json')
    args = parser.parse_args()
    manifest = import_notes(args.source_dir, json.loads(args.selection.read_text()), ROOT / '_posts')
    (ROOT / 'publishing/import-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(f'Imported {len(manifest)} notes')
