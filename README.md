# apk-catalog

Indice estatico de APKs. Los archivos viven como assets de GitHub Releases (tag `{producto}-{version}`); `public/catalog.json` los lista y `public/index.html` lo renderiza.
Deploy: `wrangler pages deploy public --project-name apk-catalog --commit-dirty=true`.
Convencion completa: vault `Memory/ops/APK-Distribucion.md`.
