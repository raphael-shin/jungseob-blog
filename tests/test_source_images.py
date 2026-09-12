import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_images import ImageMetadata
from import_notes import convert
from test_import_notes import NOTE

class ImageTests(unittest.TestCase):
    def test_priority_and_relative_paths(self):
        parser = ImageMetadata()
        parser.feed('<meta name="twitter:image" content="/twitter.jpg"><meta property="og:image" content="../og.png?a=1&amp;b=2">')
        self.assertEqual(list(parser.candidates('https://example.com/blog/post')), ['https://example.com/og.png?a=1&b=2', 'https://example.com/twitter.jpg'])
    def test_invalid_and_missing_images(self):
        parser = ImageMetadata()
        parser.feed('<meta property="og:image" content="data:image/png;base64,aaa"><meta name="thumbnail" content="https://example.com/thumb.jpg">')
        self.assertEqual(list(parser.candidates('https://example.com')), ['https://example.com/thumb.jpg'])
        self.assertEqual(list(ImageMetadata().candidates('https://example.com')), [])
    def test_image_optional_and_body_unchanged(self):
        _, plain = convert(NOTE, 'slug')
        _, illustrated = convert(NOTE, 'slug', 'https://example.com/cover.png')
        self.assertEqual(plain.split('---', 2)[2], illustrated.split('---', 2)[2])
        self.assertIn('path: https://example.com/cover.png', illustrated)
        self.assertNotIn('\nimage:', plain)
