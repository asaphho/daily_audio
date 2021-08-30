# daily_audio

<h1>About</h1>

This project contains a simple Python script for running on a Raspberry Pi. It will play an audio file corresponding to the date when a button is pushed. This project was started for a highly specific use case.

<h1>Setting up the pi</h1>

**Start with a clean install of the Raspberry Pi OS.** 

First, the Pi needs to be configured with the correct location (e.g. Singapore) and connected to the Internet.

Once that is done, do the following on the Pi:

Configure the audio to output to the desired output (e.g. 3.5mm audio jack). This can be done by accessing the configuration menu through the terminal:

```sh
sudo raspi-config
```

The setting can be found under System Options > Audio. When the configuration is done, you do not need to reboot yet. If you did reboot, continue with the next step after booting up.

Make sure you are in the home directory, or navigate to it with 
```sh
cd /home/pi
```

Clone this repository:
```sh
git clone https://github.com/asaphho/daily_audio.git
```

Run the setup script to install the required packages for the Python script:
```sh
bash /home/pi/daily_audio/setup.sh
```

During the installation of packages, you may be prompted a few times on whether you wish to continue. Continue every time. 
This version will automatically download the audio files from a specified URL each day, if the file for the corresponding day is not found. Specify the URL of the directory to download from. For example, if the file for any given date is found at https://somedirectory/YYYY-MM-DD.mp3 (the date in the URL has to be in this format. It is hard-coded), then the URL to be entered is https://somedirectory (DO NOT include a trailing slash).
After the installation is done, the Pi will reboot. The Python script will run on boot. The Python script requires the Pi to be connected to the Internet in order to be able to get the date, so you must ensure that it will connect to the Internet upon booting up.
**It is not recommended to install any more programs or run anything else on the Pi after this is done.**
 
<h1>Usage</h1>
Once the Pi has completed booting up, the python script will run and a chime will sound to indicate that the program is ready. Pressing the button will play the file corresponding to the date if a file of the right format corresponding to the date has been placed in /home/pi/Downloads. If the file does not exist, it will download the file from the remote URL. In this current version I have implemented a bouncetime of 10 seconds after each button input. If the button is pressed a second time more than 10 seconds after pressing it the first time but the file is still playing, the file will play again immediately upon finishing.

<h1>Audio files cleanup and updating</h1>
Whenever the python script runs, all .mp3 files in /home/pi/Downloads will be removed. This is to allow the Pi to get the new version of an audio file if it is updated on the remote source (the one specified by the URL). If a file for the day was updated after the Pi had already pulled the old version, you must turn off the Pi and turn it on again in order to get the updated file.
