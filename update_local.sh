#!/bin/bash

sudo pip uninstall pryzm
sudo python setup.py install
pip list | grep pryzm
