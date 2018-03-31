#!/bin/bash

sudo pip uninstall prysm
sudo python setup.py install
pip list | grep prysm
