COMPOSER=docker-compose
RELEASER=heroku
CONTAINER=api


up:
	$(COMPOSER) up

build:
	$(COMPOSER) build

down:
	$(COMPOSER) down

logs:
	$(COMPOSER) logs

bash:
	$(COMPOSER) run $(CONTAINER) bash

deploy:
	$(COMPOSER) down \
	&& $(RELEASER) login \
	&& $(RELEASER) container:login \
	&& $(RELEASER) container:push $(CONTAINER) \
	&& $(RELEASER) addons:create heroku-postgresql:hobby-dev \
	&& $(RELEASER) container:release $(CONTAINER) \
	&& $(RELEASER) logs --tail

