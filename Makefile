PAGES_PROJECT := apk-catalog

.PHONY: deploy verify

verify:
	python scripts/verify_catalog.py

deploy: verify
	npx wrangler pages deploy public --project-name $(PAGES_PROJECT) --branch main
