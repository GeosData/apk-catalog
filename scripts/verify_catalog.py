import hashlib
import json
import sys
import urllib.request
from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "public" / "catalog.json"
CHUNK = 1024 * 1024
SIZE_TOLERANCE_MB = 1


def digest(url: str) -> tuple[str, float]:
    sha = hashlib.sha256()
    total = 0
    with urllib.request.urlopen(url, timeout=120) as response:
        while chunk := response.read(CHUNK):
            sha.update(chunk)
            total += len(chunk)
    return sha.hexdigest(), total / 1_048_576


def main() -> int:
    products = json.loads(CATALOG.read_text(encoding="utf-8"))["products"]
    errors = []
    for product in products:
        for release in product["releases"]:
            label = f"{product['id']} {release['version']} ({release['variant']})"
            try:
                sha, size_mb = digest(release["url"])
            except Exception as error:
                errors.append(f"{label}: download failed: {error}")
                continue
            found = []
            if sha != release["sha256"]:
                found.append(f"{label}: sha256 mismatch, catalog {release['sha256'][:12]} vs file {sha[:12]}")
            if abs(size_mb - release["size_mb"]) > SIZE_TOLERANCE_MB:
                found.append(f"{label}: size {size_mb:.1f} MB, catalog says {release['size_mb']} MB")
            if not found:
                print(f"ok: {label} ({size_mb:.1f} MB)")
            errors.extend(found)
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
