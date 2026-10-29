#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""fix-seo-canonical-ga.py
- Sua toan bo canonical URL tu /cyberb/ sang /cyberb-facebook/
- Them canonical cho file thieu
- Chen Google Analytics (G-QW3TSMDH34) vao head cua tat ca file HTML
- Loai trang quan tri (noindex) van nhan duoc GA de do luu luong
"""
import glob
import os
import re

BASE = "https://emtenlamua.github.io/cyberb-facebook/"
OLD_BASE = "https://emtenlamua.github.io/cyberb/"
GA_ID = "G-QW3TSMDH34"

GA_SNIPPET = (
    '  <!-- Google Analytics (GA4) -->\n'
    '  <script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>\n'
    '  <script>\n'
    '    window.dataLayer = window.dataLayer || [];\n'
    '    function gtag(){dataLayer.push(arguments);}\n'
    '    gtag(\'js\', new Date());\n'
    '    gtag(\'config\', \'%s\');\n'
    '  </script>\n'
) % (GA_ID, GA_ID)

NO_INDEX_FILES = {"admin.html", "admin-seo.html", "login.html"}

stats = {"canonical_fixed": 0, "canonical_added": 0, "ga_added": 0, "skipped": 0}

for path in sorted(glob.glob("*.html")):
    with open(path, "r", encoding="utf-8") as f:
        t = f.read()
    orig = t

    # --- 1. Canonical ---
    m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    if m:
        old = m.group(1)
        new = old.replace(OLD_BASE, BASE)
        if new != old:
            t = t.replace(f'<link rel="canonical" href="{old}"',
                          f'<link rel="canonical" href="{new}"')
            stats["canonical_fixed"] += 1
    else:
        # File chua co canonical -> them vao truoc </head>
        slug = os.path.basename(path)
        if slug == "index.html":
            url = BASE
        else:
            url = BASE + slug
        t = t.replace("</head>", f'  <link rel="canonical" href="{url}">\n</head>', 1)
        stats["canonical_added"] += 1

    # --- 2. Google Analytics ---
    if "googletagmanager.com/gtag/js?id=" not in t:
        if "</head>" in t:
            t = t.replace("</head>", GA_SNIPPET + "</head>", 1)
            stats["ga_added"] += 1
        else:
            stats["skipped"] += 1

    if t != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(t)

print("=== Ket qua ===")
print(f"Canonical sua sai URL : {stats['canonical_fixed']}")
print(f"Canonical them moi     : {stats['canonical_added']}")
print(f"Chen Google Analytics  : {stats['ga_added']}")
print(f"Bo qua                : {stats['skipped']}")
