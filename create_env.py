from consts import DOCKER_COMPOSE_SERVICE_TEMPLATE, DOCKER_COMPOSE_TEMPLATE, STARTING_PORT
from copy import deepcopy
import socket
import yaml


def _check_port_availability(service_port):
    port_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("127.0.0.1", service_port)
    check_status = port_socket.connect_ex(location)
    port_socket.close()
    return check_status


def _build_service_compose(website, service_index, service_port):
    service_name = f"website-healthcheck0{service_index}"
    service_compose = {service_name: deepcopy(DOCKER_COMPOSE_SERVICE_TEMPLATE)}
    service_compose[service_name]["environment"]["WEBSITE_URL"] = website
    if _check_port_availability(service_port):
        service_compose[service_name]["ports"] = [f"{service_port}:{service_port}"]
        service_compose[service_name]["environment"]["PORT"] = service_port
        return service_compose
    return None


def _create_compose_file(content):
    with open("docker-compose.yml", "w") as file:
        yaml.safe_dump(content, file)


def create_env(websites):
    addresses = {}
    service_port = STARTING_PORT
    service_index = 1
    compose_file_content = deepcopy(DOCKER_COMPOSE_TEMPLATE)
    for website in websites:
        service_config = _build_service_compose(website, service_index, service_port)
        if not service_config:
            # Checks if the next port is available
            while service_config is None:
                service_port += 1
                service_config = _build_service_compose(website, service_index, service_port)

        addresses[website] = f"http://localhost:{service_port}/status"
        compose_file_content["services"].append(service_config)
        service_index += 1
        service_port += 1

    _create_compose_file(compose_file_content)
    _build_docker()
    _run_docker()
    return addresses
