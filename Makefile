.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"

	@echo "  copy_env        Copies the 'env.example.ini' file to 'env.ini'."

.PHONY: copy_env
copy_env:
	@cp env.example.ini env.ini
