%define name usb-notifier
%define version 0.1
%define unmangled_version 0.1
%define release 1

Summary: A small USB notification python program!
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv3+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mohit Bansal <philomath@disroot.org>
Requires: python3-devel, python3-pyudev, libnotify

%description

The program to send notification to system on USB events.
 
### Assignment 1
Assignment 1 includes the questions:
1. Write a program which shows a notification message whenever a new USD device plugged in or removed.
2. The notification message should show the "idVendor" and "idProduct" attributes of the USB device.
3. If possible, the notification message should also show "manufacturer" and "product" attributes of the USB devices.

Udev Module deals with the USB devices and their management, that includes the notification of the Plug in and removal of the device.

How to achieve the solution?
Either update a udev rule that notifies the required message when a usb device is plugged in or removed.
Or using `Pyudev` library in python script to notify the USB device and update the init script.

How to run the program, 

* Change the settings and udev rules.
* Copy the program.sh in the directory "/usr/bin/".
* Log out and login the system.
* Plug in the USB device.

### Assignment 2
1. Make your Assignment 1 program start whenever a user logged-in into a Desktop Environment.
2. Your program should keep on running and monitoring USB plug-in and plug-out till the user logout or shutdown or restart the OS.


### Assignment 3
1. Create a .deb or .rpm package for your program along with config files from assignment 2 to install in Linux distro.
2. Specify the installation process for packages for another distribution.

Requirements:
* notify-send
* pyudev

Installation:
* For RPM based distributions:
    Download the package available and use `sudo rpm -ivh <packagename.rpm>` to install the program.
* For Other Distributions:
    Download the repository, copy the file, usb_notifier.py to <path>, install the requirements and update the init.d as following to run it automatically on boot


%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/xdg/autostart
install -m 0755 $RPM_BUILD_DIR/usb-notifier-0.1/usb-notifier $RPM_BUILD_ROOT/usr/bin
install -m 0644 $RPM_BUILD_DIR/usb-notifier-0.1/usb-notifier_autostart.desktop $RPM_BUILD_ROOT/etc/xdg/autostart

 
%clean
rm -rf $RPM_BUILD_ROOT

%files 
/usr/bin/usb-notifier
/etc/xdg/autostart
