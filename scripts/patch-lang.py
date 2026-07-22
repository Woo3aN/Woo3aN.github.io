"""Patch Butterfly theme source to fix Archives title + Search button"""
import os

# Fix 1: Archives uses _p('page.archives') but zh-CN doesn't have it.
# Change to _p('nav.archives') which IS "归档"
f1 = 'node_modules/hexo-theme-butterfly/scripts/helpers/page.js'
with open(f1, 'r') as f: c = f.read()
c = c.replace("_p('page.archives')", "_p('nav.archives')")
with open(f1, 'w') as f: f.write(c)
print('OK: Archives title now uses nav.archives (=归档)')

# Fix 2: Search button text — hardcode 'Search' in nav.pug
f2 = 'node_modules/hexo-theme-butterfly/layout/includes/header/nav.pug'
with open(f2, 'r') as f: c = f.read()
c = c.replace("_p('search.title')", "'Search'")
with open(f2, 'w') as f: f.write(c)
print('OK: Search button hardcoded to Search')
