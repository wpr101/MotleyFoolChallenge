#!/bin/bash
INSTALL_DIR=/opt/fool

#mkdir "$INSTALL_DIR"
git clone https://github.com/wpr101/MotleyFoolChallenge.git "$INSTALL_DIR"
cd "$INSTALL_DIR"
pyvenv .
source bin/activate
pip3 install Django==2.0.2
cd "$INSTALL_DIR"/fool 
python3 manage.py runserver
