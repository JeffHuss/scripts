# Ubuntu VM Launcher with Cloud-Init

## Overview

This script automates the creation and deployment of Ubuntu virtual machines using KVM, cloud-init, and libvirt. It simplifies the process of setting up VMs by handling disk management, network configuration, user setup, and hostname registration in a single command.

The script generates a properly configured VM that is:
- Accessible via SSH using either hostname.local or IP address
- Correctly registered on the network with its hostname
- Pre-configured with necessary packages and user accounts
- Ready to use immediately after provisioning

## Requirements

Before using this script, ensure you have the following installed on your Ubuntu host system:

- QEMU/KVM
- libvirt-daemon
- virtinst
- cloud-utils
- A base Ubuntu cloud image (jammy-server-cloudimg-amd64.img)
- A configured network bridge (br0)

You can install most requirements with:

```bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system virtinst cloud-utils bridge-utils
```

## Basic Usage

```bash
./launch_vm.sh VM_NAME MEMORY_MB DISK_SIZE_GB
```

Example:
```bash
./launch_vm.sh testvm 2048 20
```

This will create a VM named "testvm" with 2GB of RAM and a 20GB disk.

## How It Works

The script performs the following operations:

1. Validates command-line arguments
2. Generates a cloud-init configuration
3. Creates a cloud-init ISO file
4. Copies and resizes the base disk image
5. Launches the VM using libvirt
6. Performs cleanup of temporary files

## Detailed Explanation

### Command-Line Arguments

The script accepts three required arguments:

1. `VM_NAME`: The hostname for the VM (used for network identification)
2. `MEMORY_MB`: RAM allocation in megabytes
3. `DISK_SIZE_GB`: Disk size in gigabytes

### Cloud-Init Configuration

Cloud-init is used to configure the VM on first boot. The configuration in this script handles:

#### Hostname Configuration

```yaml
hostname: ${VM_NAME}
preserve_hostname: true
fqdn: ${VM_NAME}.local
```

We use `preserve_hostname: true` to prevent cloud-init from changing the hostname after it's set. This is important because cloud-init might otherwise reset the hostname based on metadata from DHCP or other sources.

#### User Setup

```yaml
users:
  - name: ubuntu
    ssh_authorized_keys:
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDwBzqbYYLYQNtmvYJVgAnMhGWp0gBPlxrZr98Wytwbs jeff.huss@comcast.net
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: sudo
    shell: /bin/bash
    plain_text_passwd: ubuntuisawesome
```

The script creates an 'ubuntu' user with sudo access and configures SSH for both key-based and password authentication. This provides flexibility in how you connect to the VM.

#### Password Authentication

```yaml
ssh_pwauth: true
chpasswd:
  expire: false
  list: |
    ubuntu:ubuntuisawesome
```

Password authentication is enabled and the password is set to never expire. This is convenient for development environments, though in production environments you might want to use only key-based authentication.

#### Package Installation

```yaml
package_update: true
package_upgrade: true
packages:
  - net-tools
  - htop
  - vim
  - python3-pip
  - python3-venv
  - python3-dev
  - avahi-daemon
  - libnss-mdns
```

The script updates the package repository and installs useful packages:
- `net-tools`: For network debugging
- `htop`: For system monitoring
- `vim`: For text editing
- Python development tools
- `avahi-daemon` and `libnss-mdns`: For .local domain resolution

### Network Configuration

#### Custom Netplan Configuration

```yaml
- path: /etc/netplan/60-dhcp-hostname.yaml
  content: |
    network:
      version: 2
      ethernets:
        enp1s0:  # Typical interface name for QEMU VMs
          dhcp4: true
          dhcp4-overrides:
            hostname: ${VM_NAME}
          dhcp6: false
```

This is one of the most critical parts of the script. It:

1. Creates a netplan configuration file with a higher number (60) to override any default configurations
2. Explicitly sets the DHCP client to send the hostname with DHCP requests
3. Disables IPv6 to simplify the network setup

This approach ensures that when the VM requests an IP address from the DHCP server, it also registers its hostname. This solves the issue of hostname visibility in network scans.

#### Hostname Registration Script

```bash
- path: /usr/local/bin/ensure-hostname.sh
  content: |
    #!/bin/bash
    # Ensure hostname is set and registered with the network
    
    # Set hostname explicitly and persistently
    hostnamectl set-hostname ${VM_NAME} --static
    
    # Update /etc/hosts to include our hostname
    if ! grep -q "${VM_NAME}" /etc/hosts; then
      echo "127.0.1.1 ${VM_NAME} ${VM_NAME}.local" >> /etc/hosts
    fi
    
    # Apply netplan configuration
    netplan apply
    
    # Restart avahi for mDNS (.local) resolution
    systemctl restart avahi-daemon
```

This script ensures the hostname is properly set and registered. It:

1. Sets the hostname using systemd's `hostnamectl` with the `--static` flag to make it persistent
2. Updates `/etc/hosts` to associate the hostname with the loopback address (127.0.1.1)
3. Applies the netplan configuration explicitly
4. Restarts avahi-daemon to enable .local domain resolution

Adding the hostname to `/etc/hosts` is critical for some applications that look up the local hostname.

### First Boot Commands

```yaml
runcmd:
  # Set hostname immediately
  - hostnamectl set-hostname ${VM_NAME} --static
  
  # Make network aware of our hostname by running our script
  - /usr/local/bin/ensure-hostname.sh
  
  # Configure services
  - systemctl enable avahi-daemon
  - systemctl restart avahi-daemon
  - systemctl restart systemd-networkd
  - systemctl restart ssh
```

These commands run on the first boot to ensure everything is properly configured:

1. Set the hostname immediately
2. Run the hostname registration script
3. Enable and restart key services

This multi-layered approach provides redundancy in hostname configuration - even if one method fails, the others should succeed.

### VM Creation

```bash
# Create cloud-init disk
cloud-localds cloud-init-${VM_NAME}.iso cloud-init-${VM_NAME}.yml

# Copy the base image and resize it
cp jammy-server-cloudimg-amd64.img ${VM_NAME}.qcow2
qemu-img resize ${VM_NAME}.qcow2 ${DISK_SIZE}G

# Create the VM
virt-install --name ${VM_NAME} \
  --memory ${MEMORY} \
  --vcpus 2 \
  --disk ${VM_NAME}.qcow2,format=qcow2 \
  --disk cloud-init-${VM_NAME}.iso,device=cdrom \
  --os-variant ubuntu22.04 \
  --virt-type kvm \
  --graphics vnc \
  --network bridge=br0,model=virtio \
  --noautoconsole \
  --import
```

This section:

1. Converts the cloud-init YAML to an ISO image
2. Creates a copy of the base Ubuntu image and resizes it
3. Launches the VM using `virt-install`

Notable options:
- `--network bridge=br0,model=virtio`: Uses virtio networking for better performance and connects to the bridge network
- `--noautoconsole`: Prevents the console from automatically opening
- `--import`: Tells virt-install that we're using an existing disk image

### File Cleanup

```bash
# Cleanup temporary files
echo ""
echo "Cleaning up temporary files..."
rm cloud-init-${VM_NAME}.iso
echo "Note: Keeping cloud-init-${VM_NAME}.yml for reference and ${VM_NAME}.qcow2 which is needed for the VM to run."
```

The script automatically cleans up some temporary files after VM creation:

1. **Removed automatically**:
   - `cloud-init-${VM_NAME}.iso`: The cloud-init ISO file is removed as it's no longer needed after VM boot

2. **Kept intentionally**:
   - `cloud-init-${VM_NAME}.yml`: The configuration file is kept for reference and debugging purposes. It contains all the settings used to create this specific VM.
   - `${VM_NAME}.qcow2`: The VM disk image is essential for the VM to continue running and must not be deleted while the VM is active.

This selective cleanup approach balances disk space conservation with maintaining necessary files for VM operation and troubleshooting. The script also provides guidance on how to manually remove the remaining files when they're no longer needed.

## Why This Approach Works

### Hostname Visibility

The original script had issues with hostname visibility on the network. This optimized script fixes that by:

1. **Multiple Hostname Configuration Points**: Setting the hostname through several methods ensures at least one works
2. **Explicit DHCP Hostname Advertisement**: The custom netplan configuration explicitly tells the DHCP client to send the hostname
3. **Proper /etc/hosts Configuration**: Adding the hostname to /etc/hosts prevents applications from failing hostname lookups
4. **Avahi Integration**: Properly configuring avahi-daemon enables .local domain resolution

### Efficiency Improvements

The script was optimized by:

1. **Removing Redundant Password Settings**: Consolidating password configuration in one place
2. **Eliminating Unnecessary Reboot**: The original script scheduled a reboot, which added complexity without solving the issue
3. **Streamlining Service Restarts**: Only restarting the necessary services in the correct order
4. **Using virtio Network Model**: This provides better performance than the default network model

## Troubleshooting

### VM Not Appearing in Network Scans

If the VM doesn't appear with its hostname in network scans, you can:

1. SSH into the VM using its IP address
2. Check the hostname with `hostname`
3. Manually run the `/usr/local/bin/ensure-hostname.sh` script
4. Check if avahi-daemon is running with `systemctl status avahi-daemon`

### Cannot Connect via SSH

If you can't connect to the VM via SSH:

1. Ensure the VM is running with `virsh list --all`
2. Check if the VM has an IP address with `virsh domifaddr VM_NAME`
3. Try connecting using the IP address instead of the hostname
4. Check if the firewall on the host is blocking connections

### VM Takes Too Long to Start

If the VM takes more than 5 minutes to start:

1. Check the VM's console with `virt-viewer VM_NAME`
2. Look for any error messages
3. Check if the VM can reach the internet (required for package installation)

## Best Practices

### Security Considerations

This script is designed for development environments. For production use, consider:

1. Using only key-based authentication (`ssh_pwauth: false`)
2. Removing the password or using a stronger one
3. Adding more restricted sudo access
4. Enabling the firewall (`ufw`) in the cloud-init configuration

### Network Optimization

The script uses a bridge network (br0) which allows the VM to appear as a first-class citizen on your network. This is ideal for:

1. Servers that need to be accessible from other machines
2. VMs that need to communicate with devices on your LAN
3. Testing network services

### Resource Allocation

When deciding on memory and disk allocations:

1. **Memory**: Ubuntu Server can run with as little as 512MB, but 2GB or more is recommended for comfortable operation
2. **Disk**: 10GB is the minimum for Ubuntu Server, but allocate more if you plan to install additional packages or store data

## Conclusion

This script provides a streamlined, reliable way to create Ubuntu VMs with proper network integration. By handling the complexities of hostname registration and network configuration, it ensures that VMs are immediately accessible and identifiable on your network.