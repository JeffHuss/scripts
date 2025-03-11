# Windows Server SSH Key Authentication Setup Guide

This guide provides detailed, step-by-step instructions for configuring SSH key authentication on Windows Server. These steps have been tested and verified to work on Windows Server 2025. I'm including it here for my own reference. I don't recommend anyone run through this process on any important machine and I'm not responsible for any issues caused by running destructive commands!

## Prerequisites

- A running Windows Server (tested on Windows Server 2025)
- Administrator access to the Windows Server
- An SSH key pair on your client machine
- Your client machine running a Linux-based OS (tested with Ubuntu)

## Step 1: Install OpenSSH Server on Windows

First, install the OpenSSH Server on your Windows Server using PowerShell with Administrator privileges:

```powershell
# Check if OpenSSH is available
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start the service
Start-Service sshd

# Set it to start automatically
Set-Service -Name sshd -StartupType Automatic
```

## Step 2: Configure Windows Firewall to Allow SSH

Create a firewall rule to allow SSH traffic:

```powershell
# Create a rule for SSH (port 22)
New-NetFirewallRule -Name "SSH-Server" `
                   -DisplayName "OpenSSH Server (sshd)" `
                   -Description "Allow incoming SSH connections" `
                   -Protocol TCP `
                   -LocalPort 22 `
                   -Direction Inbound `
                   -Action Allow `
                   -Profile Domain,Private,Public
```

## Step 3: Configure SSH for Key Authentication

Create a special configuration file for the SSH server that will recognize administrator keys in a specific location:

```powershell
# Create a custom configuration file for the SSH server
$configContent = @"
# This file configures a specific location for administrator keys
AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
"@

# Write this content to a file that will be read by the SSH server
Set-Content -Path "C:\ProgramData\ssh\sshd_config_additional" -Value $configContent

# Update the main SSH config to include this file
$mainConfig = Get-Content "C:\ProgramData\ssh\sshd_config"
if (!($mainConfig -match "Include sshd_config_additional")) {
    Add-Content -Path "C:\ProgramData\ssh\sshd_config" -Value "Include sshd_config_additional"
}
```

## Step 4: Add Your Public Key to the Authorized Keys File

Set up the authorized_keys file with your public key:

```powershell
# Create the administrators_authorized_keys file with your public key
# Replace the public key below with yours
$publicKey = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDwBzqbYYLYQNtmvYJVgAnMhGWp0gBPlxrZr98Wytwbs your@email.com"
Set-Content -Path "C:\ProgramData\ssh\administrators_authorized_keys" -Value $publicKey

# Set required permissions on the file - these permissions are critical for SSH security
icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r
icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /grant "Administrators:R" /grant "SYSTEM:R"
```

## Step 5: Restart the SSH Service

Restart the SSH service to apply all changes:

```powershell
Restart-Service sshd
```

## Step 6: Test the Connection

From your Linux client machine, test the SSH connection:

```bash
# Basic SSH connection
ssh Administrator@your-windows-server-ip

# Or with verbose output for troubleshooting
ssh -v Administrator@your-windows-server-ip
```

You should now be able to connect without being prompted for a password.

## Step 7: Configure Ansible Inventory

Add this host to your Ansible inventory file. For an INI-style inventory:

```ini
[windows]
win-server ansible_host=your-windows-server-ip

[windows:vars]
ansible_user=Administrator
ansible_connection=ssh
ansible_shell_type=powershell
ansible_ssh_private_key_file=~/.ssh/id_ed25519
```

For a YAML-style inventory:

```yaml
all:
  children:
    windows:
      hosts:
        win-server:
          ansible_host: your-windows-server-ip
          ansible_user: Administrator
          ansible_connection: ssh
          ansible_shell_type: powershell
          ansible_ssh_private_key_file: ~/.ssh/id_ed25519
```

## Troubleshooting

If you encounter issues:

1. **Verify SSH Service is Running**
   ```powershell
   Get-Service sshd
   ```

2. **Check Firewall Rules**
   ```powershell
   Get-NetFirewallRule -Name "SSH-Server"
   ```

3. **Verify Key File Permissions**
   ```powershell
   icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys"
   ```
   The output should show only Administrators and SYSTEM with Read permissions.

4. **Verify SSH Configuration**
   ```powershell
   Get-Content C:\ProgramData\ssh\sshd_config
   Get-Content C:\ProgramData\ssh\sshd_config_additional
   ```

5. **Test SSH Connection with Verbose Output**
   ```bash
   ssh -vvv Administrator@your-windows-server-ip
   ```

## Security Best Practices

1. **Disable Password Authentication** (After confirming key authentication works):
   ```powershell
   $config = Get-Content "C:\ProgramData\ssh\sshd_config"
   $config = $config -replace "#PasswordAuthentication yes", "PasswordAuthentication no"
   Set-Content -Path "C:\ProgramData\ssh\sshd_config" -Value $config
   Restart-Service sshd
   ```

2. **Use a Non-Administrator Account** for day-to-day operations, setting up separate authorized keys for that account.

3. **Regularly Update SSH** to ensure you have the latest security patches.

## References

- [Microsoft OpenSSH Documentation](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)
- [Ansible Windows Documentation](https://docs.ansible.com/ansible/latest/os_guide/windows_setup.html)
- [OpenSSH for Windows GitHub](https://github.com/PowerShell/Win32-OpenSSH)