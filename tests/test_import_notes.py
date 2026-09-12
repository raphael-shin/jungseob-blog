import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('import_notes', Path(__file__).resolve().parents[1] / 'scripts/import_notes.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
NOTE = '''---
title: 제목
date: 2026-09-09
published: 2026-08-26
author: 원문 저자
publish: true
---

# 제목

## Source
[원문](https://example.com)

{{ literal }}
'''

class ImportTests(unittest.TestCase):
    def test_dates_author_and_body(self):
        name, result = module.convert(NOTE, 'stable-slug')
        self.assertEqual(name, '2026-09-09-stable-slug.md')
        self.assertIn('author: jungseob', result)
        self.assertIn('source_author: 원문 저자', result)
        self.assertIn("source_published: '2026-08-26'", result)
        self.assertIn('render_with_liquid: false', result)
        self.assertNotIn('\n# 제목\n', result)
        self.assertIn('{{ literal }}', result)
    def test_unpublished_and_unresolved(self):
        for text in [NOTE.replace('publish: true', 'publish: false'), NOTE + '[[Private]]', NOTE + '![img](photo.png)']:
            with self.assertRaises(ValueError):
                module.convert(text, 'slug')
    def test_preflight_and_idempotence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'note.md').write_text(NOTE)
            dest = root / 'output'
            selection = [{'file': 'note.md', 'slug': 'slug'}]
            first = module.import_notes(root, selection, dest)
            self.assertEqual(first, module.import_notes(root, selection, dest))
            for bad in [selection * 2, selection + [{'file': '../secret.md', 'slug': 'secret'}]]:
                with self.assertRaises(ValueError):
                    module.import_notes(root, bad, root / 'untouched')
                self.assertFalse((root / 'untouched').exists())

if __name__ == '__main__':
    unittest.main()
