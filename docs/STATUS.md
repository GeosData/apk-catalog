# STATUS · apk-catalog

Índice estático de APKs en https://apks.geosdata.com (Cloudflare Pages, proyecto `apk-catalog`). Cada APK vive como asset de un GitHub Release de `GeosData/apk-catalog`; `public/catalog.json` guarda versión, variante, tamaño, sha256 y URL.

## T-001 · Verificar el catálogo antes de publicar
- status: done
- owner: claude
- verified: 2026-11-21
- evidence: `scripts/verify_catalog.py` descarga cada URL de `catalog.json` y compara sha256 y tamaño; `make deploy` depende de `make verify`. Primera corrida: mural 2026.09.23 (debug) ok, 61.1 MB.
- verify: `make verify`
