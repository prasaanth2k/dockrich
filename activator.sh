#!/bin/bash

# Get the path of monisys
MONISYS_PATH=$(which monisys)

# Check if monisys is in the user's local bin
if [[ "$MONISYS_PATH" != "/home/$USER/.local/bin/monisys" ]]; then
    echo "monisys not found in the expected location: /home/$USER/.local/bin/"
    exit 1
fi

# Get the Python site-packages path
PYTHON_SITE_PACKAGES=$(python3 -c "import site; print(site.USER_SITE)")

# Use the full path with sudo, ensuring the Python environment is set
echo "Using full path with sudo:"
sudo PYTHONPATH=$PYTHON_SITE_PACKAGES $MONISYS_PATH -h

# Add the local bin directory to sudo's PATH temporarily
echo "Adding /home/$USER/.local/bin to sudo's PATH temporarily:"
sudo PATH=$PATH:/home/$USER/.local/bin PYTHONPATH=$PYTHON_SITE_PACKAGES $MONISYS_PATH -h

# Modify the sudoers file to permanently add the path
echo "Adding /home/$USER/.local/bin to sudoers secure_path:"
sudo bash -c "echo 'Defaults secure_path=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/$USER/.local/bin\"' >> /etc/sudoers"

# Create a symlink in /usr/local/bin
echo "Creating symlink in /usr/local/bin:"
sudo ln -sf $MONISYS_PATH /usr/local/bin/monisys

echo "Done! You should now be able to run 'sudo monisys' without any issues."
