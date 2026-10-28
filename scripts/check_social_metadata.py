"""Check the rendered sharing metadata for every published post."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            key = attrs.get('property') or attrs.get('name')
            self.values.setdefault(key, []).append(attrs.get('content', ''))


def check_site(root):
    posts = sorted(root.glob('**/posts/*/index.html'))
    if not posts:
        raise ValueError(f'No rendered posts found in {root}')
    errors = []
    for post in posts:
        metadata = Metadata()
        metadata.feed(post.read_text())
        values = metadata.values
        for key in ('og:title', 'og:description', 'og:type', 'og:url', 'og:image',
                    'twitter:card', 'twitter:image'):
            if len(values.get(key, [])) != 1 or not values[key][0].strip():
                errors.append(f'{post}: missing, empty, or duplicate {key}')
        image = values.get('og:image', [''])[0]
        image_url = urlsplit(image)
        page_url = urlsplit(values.get('og:url', [''])[0])
        if image_url.scheme != 'https' or not image_url.netloc:
            errors.append(f'{post}: og:image must be an absolute HTTPS URL')
        if values.get('twitter:image', [''])[0] != image:
            errors.append(f'{post}: OG and Twitter images differ')
        if values.get('twitter:card', [''])[0] != 'summary_large_image':
            errors.append(f'{post}: expected a large-image sharing card')
        if image_url.netloc and image_url.netloc == page_url.netloc:
            image_file = root / unquote(image_url.path).lstrip('/')
            if not image_file.is_file():
                errors.append(f'{post}: local sharing image does not exist: {image}')
    if errors:
        raise ValueError('\n'.join(errors))
    return len(posts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site_root', type=Path)
    args = parser.parse_args()
    try:
        print(f'Sharing metadata verified for {check_site(args.site_root)} posts.')
    except ValueError as error:
        parser.exit(1, f'{error}\n')
