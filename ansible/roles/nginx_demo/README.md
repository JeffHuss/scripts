# Nginx Demo Role

An Ansible role that deploys a customized Nginx web server as a Docker container.

## Description

This role sets up a Docker container running Nginx with a custom configuration and a dynamic web page. It demonstrates how to use Ansible templates, variables, and Docker configuration to create a reusable deployment pattern.

## Requirements

- Docker installed on the target host
- Ansible 2.9+
- The `community.docker` collection (`ansible-galaxy collection install community.docker`)

## Role Variables

The following variables are defined in `defaults/main.yml` and can be overridden:

| Variable | Default | Description |
|----------|---------|-------------|
| `container_name` | nginx-web | Name for the Docker container |
| `container_image` | nginx:latest | Docker image to use |
| `container_state` | started | Desired state of container (started, stopped, etc.) |
| `host_port` | 80 | Host port to map to container |
| `container_port` | 80 | Container port to expose |
| `nginx_worker_processes` | auto | Number of Nginx worker processes |
| `nginx_worker_connections` | 1024 | Maximum connections per worker |
| `nginx_error_log_level` | warn | Nginx error log level |
| `nginx_port` | 80 | Port Nginx listens on inside container |
| `nginx_server_name` | localhost | Server name for Nginx |
| `nginx_extra_config` | "" | Additional Nginx configuration |
| `web_content_dest` | /usr/share/nginx/html | Container path for web content |

## Dependencies

None. The role assumes Docker is already installed on the target host.

## Example Playbook

```yaml
---
- name: Deploy Nginx container
  hosts: docker_vm_hosts
  become: yes
  
  roles:
    - nginx_demo
```

## Directory Structure

```
nginx_demo/
├── defaults/
│   └── main.yml          # Default variables
├── templates/
│   ├── index.html.j2     # Template for the main web page
│   ├── site.js.j2        # JavaScript for dynamic page features
│   └── nginx.conf.j2     # Nginx configuration template
└── tasks/
    └── main.yml          # Tasks to deploy the container
```

## Role Tasks

1. Creates directories for web content and Nginx configuration
2. Processes templates and copies them to the host
3. Launches a Docker container with Nginx using the provided configuration

## Web Interface

The deployed web server provides:
- A responsive web page with dynamic content
- Current time display updated by JavaScript
- Server information including container name and Nginx version
- Interactive elements using JavaScript

## License

MIT

## Author Information

Created for Ansible role learning purposes.