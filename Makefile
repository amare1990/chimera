IMAGE=chimera

setup:
	uv pip install -e .
	uv pip install pytest

test:
	docker build -t $(IMAGE) .
	docker run --rm $(IMAGE)

spec-check:
	@echo "Checking spec existence..."
	test -d specs
	test -f specs/technical.md
	test -d skills
	@echo "Spec structure OK"
