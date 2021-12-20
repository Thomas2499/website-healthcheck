DOCKER_COMPOSE_TEMPLATE = {
    "version": '2.0',
    "services": {}
}

DOCKER_COMPOSE_SERVICE_TEMPLATE = {
    "image": "website-health-check:0.2",
    "ports": [],
    "environment": {
      "WEBSITE_URL": None,
      "PORT": None
    }
}

STARTING_PORT = 2499
IMAGE_TAG = "website-health-check:0.2"
