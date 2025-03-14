#!/bin/bash
# sync.sh

# Set your configuration variables
REMOTE_USER="Administrator"
REMOTE_HOST="192.168.50.167"
REMOTE_PATH="C:/Users/Administrator/PowerShellScripts"  # No trailing slash
LOCAL_PATH="$PWD"  # Current directory

# Ensure local directory exists (already taken care of)
# mkdir -p "$LOCAL_PATH"  # Not needed if you're already in the directory

# Perform synchronization
echo "Synchronizing files from Windows to Ubuntu..."

# Method 1: Using double quotes around the entire remote specification
scp -r "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}/*" "$LOCAL_PATH/"

# If Method 1 fails, try Method 2 (uncomment):
# scp -r ${REMOTE_USER}@${REMOTE_HOST}:"${REMOTE_PATH}/*" "$LOCAL_PATH/"

echo "Synchronization complete!"

# Show what's been synced
echo "Files in destination directory:"
ls -la "$LOCAL_PATH"