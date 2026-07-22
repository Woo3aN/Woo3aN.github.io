"""Patch Butterfly theme source - must succeed or fail loudly"""
import sys

errors = []

# Fix 1: Archives uses _p('page.archives') -> _p('nav.archives')
f1 = 'node_modules/hexo-theme-butterfly/scripts/helpers/page.js'
with open(f1, 'r') as f: c = f.read()
if "_p('page.archives')" not in c:
    errors.append('FATAL: page.archives pattern not found in page.js')
else:
    c = c.replace("this._p('page.archives')", "'归档'")
    with open(f1, 'w') as f: f.write(c)
    print('OK: Archives -> nav.archives')

# Fix 2: Search button hardcode 'Search'
f2 = 'node_modules/hexo-theme-butterfly/layout/includes/header/nav.pug'
with open(f2, 'r') as f: c = f.read()
if "_p('search.title')" not in c:
    errors.append('FATAL: search.title pattern not found in nav.pug')
else:
    c = c.replace("_p('search.title')", "'Search'")
    with open(f2, 'w') as f: f.write(c)
    print('OK: Search button -> Search')

if errors:
    for e in errors:
        print(e, file=sys.stderr)
    sys.exit(1)
