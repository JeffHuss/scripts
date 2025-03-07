#!/bin/bash
# Usage: ./launch_vm.sh vm_name memory_mb disk_size_gb
# Example: ./launch_vm.sh vm1 2048 20

# Check for required environment variable
if [ -z "${SSH_PUBLIC_KEY}" ]; then
    echo "Error: SSH_PUBLIC_KEY environment variable is not set."
    echo "Please set this variable with your SSH public key. For example:"
    echo "export SSH_PUBLIC_KEY=\"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDwBzqbYYLYQNtmvYJVgAnMhGWp0gBPlxrZr98Wytwbs your@email.com\""
    echo "You can add this to your .bashrc or .zshrc to make it permanent."
    exit 1
fi

if [ $# -lt 3 ]; then
    echo "Usage: $0 vm_name memory_mb disk_size_gb"
    echo "Example: $0 vm1 2048 20"
    exit 1
fi

VM_NAME=$1
MEMORY=$2
DISK_SIZE=$3

echo "Creating VM ${VM_NAME} with DHCP networking"

# Create cloud-init configuration
cat > cloud-init-${VM_NAME}.yml << EOF
#cloud-config

# Set hostname
hostname: ${VM_NAME}
preserve_hostname: true
fqdn: ${VM_NAME}.local

# User configuration
users:
  - name: ubuntu
    ssh_authorized_keys:
      - ${SSH_PUBLIC_KEY}
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: sudo
    shell: /bin/bash
    plain_text_passwd: ubuntuisawesome

# Password authentication for SSH
ssh_pwauth: true
chpasswd:
  expire: false
  list: |
    ubuntu:ubuntuisawesome

# Update and install packages
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

# Configure networking and hostname
write_files:
  # SSH configuration
  - path: /etc/ssh/sshd_config.d/99-cloud-init.conf
    content: |
      PasswordAuthentication yes
      PermitRootLogin no
      
  # Create network interface configuration with explicit hostname
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
  
  # Override cloud-init hostname handling
  - path: /etc/cloud/cloud.cfg.d/99-hostname-preserve.cfg
    content: |
      preserve_hostname: true
      
  # Create a script to ensure hostname is registered properly
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
      
      # Store network information
      ip addr > /home/ubuntu/network_info.txt
      chmod 644 /home/ubuntu/network_info.txt
      chown ubuntu:ubuntu /home/ubuntu/network_info.txt
      
      # Create VM info file
      echo "VM NAME: ${VM_NAME}" > /home/ubuntu/vm_info.txt
      echo "To connect to this VM:" >> /home/ubuntu/vm_info.txt
      echo "  ssh ubuntu@${VM_NAME}.local" >> /home/ubuntu/vm_info.txt
      echo "  or" >> /home/ubuntu/vm_info.txt
      echo "  ssh ubuntu@$(hostname -I | awk '{print $1}')" >> /home/ubuntu/vm_info.txt
      echo "Password: ubuntuisawesome" >> /home/ubuntu/vm_info.txt
      chmod 644 /home/ubuntu/vm_info.txt
      chown ubuntu:ubuntu /home/ubuntu/vm_info.txt
      
      echo "Hostname configuration completed at \$(date)" >> /var/log/hostname-setup.log
    permissions: '0755'

# Commands to run on first boot
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

# Final message
final_message: "Cloud-init has finished initialization. VM setup complete."
EOF

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

echo "VM creation completed!"
echo "The VM is now starting up. Full initialization may take 1-2 minutes."
echo ""
echo "To find the VM's IP address, you can run:"
echo "  sudo nmap -sn 192.168.50.0/24 | grep -A 1 ${VM_NAME}"
echo "  or look for QEMU virtual NICs:"
echo "  sudo nmap -sn 192.168.50.0/24 | grep -B 1 'QEMU virtual NIC'"
echo ""
echo "You can connect using:"
echo "  ssh ubuntu@${VM_NAME}.local"
echo "  or"
echo "  ssh ubuntu@IP_ADDRESS"
echo ""
echo "The password is: ubuntuisawesome"
echo ""
echo "To access the VM console use:"
echo "  virt-viewer ${VM_NAME}"

# Cleanup temporary files
echo ""
echo "Cleaning up temporary files..."
rm -f cloud-init-${VM_NAME}.iso
echo "Note: Keeping cloud-init-${VM_NAME}.yml for reference and ${VM_NAME}.qcow2 which is needed for the VM to run."
echo "If you want to remove these files later, use:"
echo "  rm cloud-init-${VM_NAME}.yml # Remove configuration file"
echo "  # Don't remove ${VM_NAME}.qcow2 while the VM is running"