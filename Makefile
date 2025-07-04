install-dependency:
	@sudo apt-get install -y jq

generate-standalone-config:
	@< /dev/urandom tr -dc 'A-Za-z0-9' | head -c 16 | xargs ./scripts/generate_hash.sh

container-restart:
	@python3 ./scripts/generate.py
	@docker compose down && docker compose build && docker compose up -d

format:
	@uvx ruff format
