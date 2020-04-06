#!/usr/bin/python3
import pyudev
import os

usb_info = {
        "idVendor": None,
        "idProduct": None,
        "path": None
    }

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    idProduct = device.get('ID_SERIAL')
    if device.action == 'add' and  idProduct is not None:
        usb_info["idVendor"] = device.get('ID_VENDOR_FROM_DATABASE')
        usb_info["idProduct"] = device.get('ID_MODEL')
        usb_info["path"] = device.device_node
        msg = "$(echo -e 'USB detected! \n Vendor: {0} \n Product: {1} \n Path: {2}')".format(usb_info["idVendor"], usb_info["idProduct"], usb_info["path"])
        os.system('notify-send ' + '\"' + msg + '\"')
        print()
    elif device.action == 'remove':
        os.system('notify-send ' + 'USB removed!')
