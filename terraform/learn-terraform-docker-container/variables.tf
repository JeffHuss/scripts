variable "docker_ports" {
  type = map(object({
    internal = number
    external = number
    protocol = string
  }))
  description = "Internal and external ports with protocol for Docker containers"
  default = {
    "http" = {
      internal = 80
      external = 8080
      protocol = "tcp"
    },
    "https" = {
      internal = 443
      external = 8443
      protocol = "tcp"
    }
  }
}