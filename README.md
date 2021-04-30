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
bash setup.sh
```

During the installation of packages, you may be prompted a few times on whether you wish to continue. Continue every time. After the installation is done, the Pi will reboot. The Python script will run on boot. The Python script requires the Pi to be connected to the Internet in order to be able to get the date, so you must ensure that it will connect to the Internet upon booting up.

**IMPORTANT: Do not run the setup script a second time. This is because the script adds a line to the ~/.bashrc file. 
It is also not recommended to install any more programs or run anything else on the Pi after this is done.**

<h1>Adding audio files</h1>
All audio files for playing should be placed in /home/pi/Downloads. Do not place the files in subfolders inside Downloads. The filenames are to be according to the format of YYYY-MM-DD.mp3. Examples:
<ul>
  <li>2021-04-29.mp3</li>
  <li>2021-05-02.mp3</li>
  <li>2022-10-01.mp3</li>
 </ul>
 
<h1>Usage</h1>
Once the Pi has completed booting up, pressing the button will play the file corresponding to the date if a file of the right format corresponding to the date has been placed in /home/pi/Downloads. In this current version, to prevent the file from playing again immediately after finishing if the button is pressed again while the file is still playing the first time, upon a button push, the Python script stops detecting button pushes and sleeps for a while before detecting button pushes again. The sleep period can be configured in the main.py file.