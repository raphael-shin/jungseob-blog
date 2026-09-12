"""Discover representative images without copying source article bodies or images."""
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen


def web_url(url):
    parts = urlsplit(url)
    return parts.scheme in ('https', 'http') and bool(parts.hostname) and not parts.username


class ImageMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = (attrs.get('property') or attrs.get('name') or '').lower()
        if tag == 'meta' and key in ('og:image', 'og:image:secure_url', 'twitter:image', 'twitter:image:src', 'thumbnail'):
            self.images.setdefault(key, attrs.get('content', ''))
        if tag == 'link' and attrs.get('rel') == 'image_src':
            self.images.setdefault('image_src', attrs.get('href', ''))

    def candidates(self, base):
        seen = set()
        for key in ('og:image:secure_url', 'og:image', 'twitter:image', 'twitter:image:src', 'image_src', 'thumbnail'):
            value = self.images.get(key)
            if not value:
                continue
            url = urljoin(base, value)
            if web_url(url) and url not in seen:
                seen.add(url)
                yield url


def discover(source):
    if not web_url(source):
        return None
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; KnowledgeBlog/1.0)'}
    with urlopen(Request(source, headers=headers), timeout=20) as response:
        parser = ImageMetadata()
        parser.feed(response.read(2_000_000).decode(response.headers.get_content_charset() or 'utf-8', errors='replace'))
        candidates = list(parser.candidates(response.url))
    for url in candidates:
        try:
            with urlopen(Request(url, headers=headers), timeout=15) as image:
                if image.headers.get_content_type().startswith('image/'):
                    return url
        except (OSError, ValueError):
            continue
    return None
