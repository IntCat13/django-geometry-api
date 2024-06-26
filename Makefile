.PHONY: init dev test deploy

GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
BLUE := \033[0;34m
NO_COLOR := \033[0m
DOCKER_COMPOSE := docker-compose
MANAGE_PY := $(DOCKER_COMPOSE) exec web python manage.py

init: ## Initialize the environment
	@echo "$(GREEN)Stopping and removing containers...$(NO_COLOR)"
	@$(DOCKER_COMPOSE) down -v
	@echo "$(GREEN)Building and starting containers...$(NO_COLOR)"
	@$(DOCKER_COMPOSE) up --build -d
	@echo "$(GREEN)Running makemigrations...$(NO_COLOR)"
	@$(MANAGE_PY) makemigrations geo_core
	@echo "$(GREEN)Running migrations...$(NO_COLOR)"
	@$(MANAGE_PY) migrate
	@echo "$(GREEN)Running tests...$(NO_COLOR)"
	@$(MANAGE_PY) test
	@echo "$(GREEN)Api is running in background (use docker-compose logs -f to see logs)$(NO_COLOR)"

dev: ## Start the development environment
	@echo "$(GREEN)Starting development environment...$(NO_COLOR)"
	@$(DOCKER_COMPOSE) down
	@$(DOCKER_COMPOSE) up --build -d
	@echo "$(GREEN)Running tests...$(NO_COLOR)"
	@$(MANAGE_PY) test
	@echo "$(GREEN)Showing logs...$(NO_COLOR)"
	@$(DOCKER_COMPOSE) logs -f

test: ## Run tests
	@echo "$(YELLOW)Running tests...$(NO_COLOR)"
	@$(MANAGE_PY) test

deploy: ## Deploy the application
	@echo "$(RED)Deploying application...$(NO_COLOR)"
	@$(DOCKER_COMPOSE) up --build -d

help: ## Show this help
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*##"; printf "\n"} /^[a-zA-Z_-]+:.*?##/ { printf "\033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)