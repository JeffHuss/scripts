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