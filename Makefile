.PHONY: install install-dev run dev clean lint format test help uninstall requirements

# Application name (will be available as terminal command)
APP_NAME = focis
SOURCE = app.py
INSTALL_DIR = /usr/local/bin
PYTHON = python3
PIP = pip3

# Dependencies file
REQUIREMENTS = requirements.txt

.DEFAULT_GOAL := help

help:
	@echo "Available commands:"
	@echo "  make install     - Install application as system utility"
	@echo "  make install-dev - Install for development"
	@echo "  make run         - Run application directly"
	@echo "  make dev         - Run in development mode"
	@echo "  make clean       - Clean temporary files"
	@echo "  make uninstall   - Remove application from system"
	@echo "  make lint        - Code style check"
	@echo "  make format      - Code formatting"
	@echo "  make requirements- Generate requirements.txt"

# Install dependencies
install-deps:
	$(PIP) install -r $(REQUIREMENTS)

# Install application as system utility
install: install-deps
	@echo "Installing $(APP_NAME) as system utility..."
	@echo "#!/bin/sh" > $(APP_NAME)
	@echo "$(PYTHON) $(PWD)/$(SOURCE) \"\$$@\"" >> $(APP_NAME)
	chmod +x $(APP_NAME)
	sudo mv $(APP_NAME) $(INSTALL_DIR)/
	@echo "Application installed! Run with: $(APP_NAME)"

# Install for development (without system installation)
install-dev: install-deps
	$(PIP) install black flake8 isort

# Run application directly
run:
	$(PYTHON) $(SOURCE)

# Run in development mode (with auto-reload if needed)
dev:
	$(PYTHON) $(SOURCE) --dev

# Remove application from system
uninstall:
	sudo rm -f $(INSTALL_DIR)/$(APP_NAME)
	@echo "Application removed from system"

# Clean temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache .coverage *.egg-info

# Code style check
lint:
	flake8 . --ignore=E501,E402
	black --check .
	isort --check-only .

# Code formatting
format:
	black .
	isort .

# Generate requirements.txt
requirements:
	$(PIP) freeze > $(REQUIREMENTS)
