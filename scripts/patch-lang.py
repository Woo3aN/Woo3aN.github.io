"""Patch Butterfly theme source - must succeed or fail loudly"""
import sys

errors = []

# Fix 1: Archives hero title
f1 = 'node_modules/hexo-theme-butterfly/scripts/helpers/page.js'
with open(f1, 'r') as f:
    c = f.read()
if "this._p('page.archives')" not in c:
    errors.append('FATAL: page.archives pattern not found in page.js')
else:
    c = c.replace("this._p('page.archives')", "'归档'")
    c = c.replace('return loop(menu) || defaultTitle', 'return defaultTitle || loop(menu)')
    with open(f1, 'w') as f:
        f.write(c)
    print('OK: Archives -> hardcoded 归档 + defaultTitle first')

# Fix 2: Search button text
f2 = 'node_modules/hexo-theme-butterfly/layout/includes/header/nav.pug'
with open(f2, 'r') as f:
    c = f.read()
if "_p('search.title')" not in c:
    errors.append('FATAL: search.title pattern not found in nav.pug')
else:
    c = c.replace("_p('search.title')", "'Search'")
    with open(f2, 'w') as f:
        f.write(c)
    print('OK: Search button -> Search')

# Fix 3: Archive monthly grouping
f3 = 'node_modules/hexo-theme-butterfly/layout/includes/mixins/article-sort.pug'
with open(f3, 'r') as f:
    c = f.read()
# Normalize line endings to LF
c = c.replace('\r\n', '\n')
old3 = "    - let year\n    - posts.forEach(article => {\n      - const tempYear = date(article.date, 'YYYY')"
new3 = "    - let year\n    - let month\n    - posts.forEach(article => {\n      - const tempYear = date(article.date, 'YYYY')\n      - const tempMonth = date(article.date, 'YYYY年MM月')"
if old3 in c:
    c = c.replace(old3, new3)
    old4 = "      if tempYear !== year\n        - year = tempYear\n        .article-sort-item.year= year"
    new4 = "      if tempYear !== year\n        - year = tempYear\n        - month = tempMonth\n        .article-sort-item.year= year\n        .article-sort-item.month= tempMonth\n      else if tempMonth !== month\n        - month = tempMonth\n        .article-sort-item.month= tempMonth"
    c = c.replace(old4, new4)
    with open(f3, 'w') as f:
        f.write(c)
    print('OK: Archive now groups by month')
else:
    errors.append('FATAL: article-sort.pug pattern not found')

if errors:
    for e in errors:
        print(e, file=sys.stderr)
    sys.exit(1)
