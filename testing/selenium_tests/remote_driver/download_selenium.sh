#!/bin/bash
# Install Selenium

SEL_FILE='selenium-server-standalone-3.4.0.jar'
URL="http://selenium-release.storage.googleapis.com/3.4/$SEL_FILE"

CHROME_DRIVER_FILE='chromedriver_win32.zip'
CHROME_DRIVER_URL="http://chromedriver.storage.googleapis.com/2.30/$CHROME_DRIVER_FILE"

FIREFOX_DRIVER_FILE="geckodriver-v0.17.0-win64.zip"
FIREFOX_DRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/v0.17.0/$FIREFOX_DRIVER_FILE"

echo "downloading Selenium from $URL"
curl -O $URL
ln -s "$SEL_FILE" "selenium-server-standalone.jar"

echo "downloading Chromedriver from $CHROME_DRIVER_URL"
curl -LOk $CHROME_DRIVER_URL
unzip $CHROME_DRIVER_FILE
rm $CHROME_DRIVER_FILE

echo "downloading Geckodriver from $FIREFOX_DRIVER_URL"
curl -LOk $FIREFOX_DRIVER_URL
unzip $FIREFOX_DRIVER_FILE
rm $FIREFOX_DRIVER_FILE
