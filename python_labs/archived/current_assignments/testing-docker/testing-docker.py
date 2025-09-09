import docker

def launch_nginx_container():
    # Initialize the Docker client
    client = docker.DockerClient(base_url="unix:///home/jhuss/.docker/desktop/docker.sock")
    
    # Pull the latest nginx image
    print("Pulling nginx image...")
    client.images.pull('nginx:latest')
    
    # Create and start an nginx container
    print("Creating and starting nginx container...")
    container = client.containers.run(
        'nginx:latest',
        name='my-nginx-container',
        ports={'80/tcp': 8080},  # Map container port 80 to host port 8080
        detach=True,  # Run in background
        restart_policy={"Name": "always"}  # Automatically restart the container
    )
    
    print(f"Container ID: {container.id}")
    print(f"Container Status: {container.status}")
    print(f"Nginx is now running at http://localhost:8080")
    
    # Return the container object for further operations if needed
    return container

if __name__ == "__main__":
    container = launch_nginx_container()
    
    # Optional: Demonstrate some container operations
    print("\nContainer Info:")
    print(f"Name: {container.name}")
    print(f"Image: {container.image.tags}")
    print(f"Logs: {container.logs(tail=5).decode('utf-8')}")
    
    # Uncomment to stop/remove container after testing
    print(f"Stopping {container.name}...")
    container.stop()
    print(f"Removing {container.name}...")
    container.remove()