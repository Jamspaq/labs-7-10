"""Basic structure, nesting and local-link checks; not a full W3C validator."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.stack, self.ids, self.links = path, [], set(), []
        self.tags, self.charset, self.lang, self.title_text = [], False, False, ''
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == 'html':
            self.lang = bool(attrs.get('lang'))
        if tag == 'meta' and attrs.get('charset', '').lower() == 'utf-8':
            self.charset = True
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path.name}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            errors.append(f'{self.path.name}: unexpected closing tag {tag}')
        else:
            self.stack.pop()
    def handle_data(self, data):
        if self.stack and self.stack[-1] == 'title':
            self.title_text += data

pages = {}
for path in sorted(ROOT.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    page = Page(path)
    page.feed(text)
    page.close()
    pages[path.resolve()] = page
    if not text.lstrip().lower().startswith('<!doctype html>'):
        errors.append(f'{path.name}: missing doctype')
    for tag in ('html', 'head', 'body', 'main', 'h1', 'title'):
        if page.tags.count(tag) != 1:
            errors.append(f'{path.name}: expected exactly one {tag}')
    if page.stack or not page.charset or not page.lang or not page.title_text.strip():
        errors.append(f'{path.name}: unclosed tags or missing charset/lang/title')
if len(pages) != 3:
    errors.append('Expected three participant/project pages')
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_relative_to(ROOT) or not target.is_file():
            errors.append(f'{path.name}: invalid local target {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing fragment {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'HTML Check OK: {len(pages)} pages; nesting, metadata and local links checked')
