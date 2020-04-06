## USB-notifier

This is a python program that monitors any usb device plugin and notifies the user with its Vendor, Product Details and mount path.

### Assignment 1
1. Write a program which shows a notification message whenever a new USD device plugged in or removed.
2. The notification message should show the "idVendor" and "idProduct" attributes of the USB device.
3. If possible, the notification message should also show "manufacturer" and "product" attributes of the USB devices.

### Assignment 2
1. Make your Assignment 1 program start whenever a user logged-in into a Desktop Environment.
2. Your program should keep on running and monitoring USB plug-in and plug-out till the user logout or shutdown or restart the OS.

### Assignment 3
1. Create a .deb or .rpm package for your program along with config files from assignment 2 to install in Linux distro.
2. Specify the installation process for packages for another distribution.


### Approach to the solution
Udev Module deals with the USB devices and their management, that includes the notification of the Plug in and removal of the device.

Since it was required to notify the user about the USB plugin, the most simple solution would be to use, udev rules. Update the udev rules for monitoring any usb plugin or removal and call `notify-send` program to notify the user.

Or, using pyudev (a libudev library for python), we can achieve the same. To run the program automatically on the boot time, writing a systemd service unit or cronjob would do the job. Since using systemd service method requires to modify the program, we can also use the .desktop file to start the program automatically.


### Requirements:
* notify-send
* pyudev

### Installation:
* For RPM based distributions:
    - Download the package available and use `sudo rpm -ivh <packagename.rpm>` to install the program.
    - Then, enable the usb-notifier.service to run the program automatically on the next boot.
* For Other Distributions:
    Download the repository, copy the file, usb_notify.py to `/usr/bin/`, install the requirements and copy the `usb-notifier_autostart.desktop` file to `/etc/xdg/autostart`, log out and login to run the program.

To execute the program explicitly, type `usb-notifier` in the command shell.

NOTE: The program can be improved a lot, with creation of necessary functions to call the usb monitoring, adding a logger etc.
