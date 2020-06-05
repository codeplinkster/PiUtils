# PiUtils
Whatsmyip.py is a python3 script that provides a simple way to immediately determine the private and public IP of the Raspberry Pi (pi) upon boot up into the pi desktop by launching a dialog window that identifies the host name, the public and private IP address of the network connected device.  This can aid in first-time setup of a pi on an unknown network without requiring network admin privileges or complicated network access to determine the IP of the pi.  The only things needed prior to booting the pi once it has been setup is to connect it to a monitor and connect it to the network using an ethernet cable.
# Pi Python Software Setup
The "whatsmyip.py" script uses the Python tkinter GUI package to display the ip addresses.
# Pi Boot Script setup
Use the "autostart" boot provision of Linux to launch an xterminal-emulator window that runs the python script.

Steps:
1. Copy "whatsmyip.py" onto your pi.  You may want to create a new folder like "~/rpiutils"
2. In your ~/.config/autostart folder, create a new file called “whatsmyip.desktop”

  >cd ~/.config/autostart
  
  >sudo nano whatsmyip.desktop
  
3. Enter the following into the "whatsmyip.desktop" file where {your path} is replaced by the path to your whatsmyip.py script from step 1 above:

    [Desktop Entry]

    Type=Application

    Name=WhatsMyIp

    Exec=xterm -hold -e '/usr/bin/python3 {your path}/whatsmyip.py'
  
4. Save and reboot. Once the desktop opens, a dialog will launch displaying the hostname, private and public IP's of the pi.

