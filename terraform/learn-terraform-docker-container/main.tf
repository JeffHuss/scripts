terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///home/jhuss/.docker/desktop/docker.sock"
}

variable "docker_ports" {
  type = list(object({
    internal = number
    external = number
    protocol = string
  }))
  description = "Internal and external ports with protocol for Docker containers"
  default = [
  { # [0] HTTP
    internal = 80
    external = 8080
    protocol = "tcp"
  },
  { # [1] HTTPS
    internal = 443
    external = 8443
    protocol = "tcp"
  }
]
}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"
  ports {
    internal = var.docker_ports[0].internal
    external = var.docker_ports[0].external
    protocol = var.docker_ports[0].protocol
  }
}
