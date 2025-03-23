#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status
set -x  # Print commands and their arguments as they are executed

# Debug: Print current working directory and list files
echo "Current working directory: $(pwd)"
echo "Listing files in current directory:"
ls -l

# Update package list and install dependencies
apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libpango1.0-0 \
    libcups2 \
    libxss1 \
    libgbm1 \
    libasound2

# Debug: Check if dependencies were installed successfully
echo "Dependencies installed successfully."
dpkg -l | grep -E "wget|unzip|curl|gnupg|libglib2.0-0|libnss3|libgconf-2-4|libfontconfig1|libx11-xcb1|libxcomposite1|libxcursor1|libxdamage1|libxi6|libxtst6|libgdk-pixbuf2.0-0|libgtk-3-0|libpango1.0-0|libcups2|libxss1|libgbm1|libasound2"

# Create /drivers directory
mkdir -p /app/drivers

# Download and install Chrome
wget -O /app/drivers/chrome-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.165/linux64/chrome-linux64.zip
echo "Chrome downloaded successfully."
unzip -o /app/drivers/chrome-linux64.zip -d /drivers/
rm /app/drivers/chrome-linux64.zip


# Download and install Chromedriver
wget -O /app/drivers/chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.165/linux64/chromedriver-linux64.zip
echo "Chromedriver downloaded successfully."
unzip -o /app/drivers/chromedriver-linux64.zip -d /drivers/
rm /app/drivers/chromedriver-linux64.zip

# Ensure Chromedriver is moved to /drivers
if [ -f /drivers/chromedriver-linux64/chromedriver ]; then
    mv /drivers/chromedriver-linux64/chromedriver /drivers/
fi

# Make Chromedriver executable
chmod +x /drivers/chromedriver

# Verify installation
/drivers/chrome-linux64/chrome --version
/drivers/chromedriver --version

#find / -name chromedriver
#find / -name chrome