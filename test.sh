#!/bin/bash

#to disconnect by id
#disconnect special key
xinput float 18
#disconnect main keyboard
xinput float 19
#disconnect special key
xinput float 21
#disconnect touch pad
xinput float 15

sleep 10s # Waits 10 seconds. 
#Check if your keyboard and touchpad is disabled

#to reconnecct by id to parent
xinput reattach 18 3
xinput reattach 19 3
xinput reattach 21 3
xinput reattach 15 2
