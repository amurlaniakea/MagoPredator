<!--
  Copyright (C) 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
  SPDX-License-Identifier: AGPL-3.0-or-later
-->

# MagoPredator

> **Portafolio público: herramientas de defensa para agentes de IA, artículos y presencia en HN.**

Por Pedro Sordo Martínez (Sil) — amurlaniakea@gmail.com

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.txt)

Sitio estático puro (HTML + CSS, sin frameworks, sin backend, sin build).
Estado: P3 — esqueleto con placeholders. El contenido real se rellena en P4.

## Estructura

- `index.html` — las 5 secciones: hero, proyectos, artículos, HN, contacto.
- `styles.css` — estilos. Sin JavaScript en el sitio.

## Vista previa local

```bash
python3 -m http.server 8000
```

Abrir `http://localhost:8000`.

## CI

Checks en `.github/workflows/ci.yml`: LICENSE verbatim (661 líneas + sha256
canónico), cabeceras SPDX y parse válido del HTML. Sin tests de red.

## Licencia

AGPL-3.0-or-later. Ver archivo `LICENSE`.

Copyright (C) 2026 Pedro Sordo Martínez — amurlaniakea@gmail.com

**Contacto:** Pedro Sordo Martínez — amurlaniakea@gmail.com
