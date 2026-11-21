PAGES_PROJECT := apk-catalog

.PHONY: deploy

deploy:
	npx wrangler pages deploy public --project-name $(PAGES_PROJECT) --branch main
