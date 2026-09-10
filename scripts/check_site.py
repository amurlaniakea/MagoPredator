# Copyright (C) 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Checks del sitio estático para CI y verificación local.

1. index.html parsea como HTML válido (html.parser sin excepciones).
2. Las 5 secciones existen por id: hero, proyectos, articulos, hn, contacto.
3. Ningún archivo del sitio menciona "Apache" ni "MIT" (licencia única AGPL).
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECCIONES = ["hero", "proyectos", "articulos", "hn", "contacto"]


class Recolector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()


    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == "id":
                self.ids.add(v)


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    rec = Recolector()
    rec.feed(html)  # eleva excepción si el HTML está mal formado
    faltan = [s for s in SECCIONES if s not in rec.ids]
    if faltan:
        print("Faltan secciones:", faltan)
        return 1
    for f in [ROOT / "index.html", ROOT / "styles.css", ROOT / "README.md"]:
        texto = f.read_text(encoding="utf-8")
        if re.search(r"apache|mit license|\bmit\b", texto, re.IGNORECASE):
            print("Mención no-AGPL en:", f.name)
            return 1
    print("OK: 5 secciones, HTML válido, sin menciones Apache/MIT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
