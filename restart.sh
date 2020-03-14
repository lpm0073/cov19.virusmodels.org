#!/bin/bash
#---------------------------------------------------------
# written by: Lawrence McDaniel
#             lpm0073@gmail.com
#             lawrencemcdaniel.com
#
# date:       mar-2020
#
# usage:      re-start the Django platform
#
#---------------------------------------------------------
sudo systemctl restart gunicorn
sudo service nginx restart

sudo systemctl status gunicorn