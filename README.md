A simple gnome panel plugin which can enable or disable the touchpad and keyboard of your convertible laptop.

Some laptops dont have this happening automatically in Linux.

In this case we want to disable the keyboard with a script and renable als with script
We use Xinput to do this.

The main python file has a dependency (along with Python 3 of course) 
sudo apt-get install gir1.2-appindicator3-0.1 

The 2 scripts are for enabling and disabling the laptop keyboard and touchpad.

my xinput list is below, i had to experiment with the test script to get the right ids etc

ray@pop-os:~/TabletButton$ xinput list 
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Asus Keyboard                           	id=9	[slave  pointer  (2)]
⎜   ↳ Asus Keyboard                           	id=11	[slave  pointer  (2)]
⎜   ↳ ELAN9008:00 04F3:2FC2                   	id=12	[slave  pointer  (2)]
⎜   ↳ ASUE120D:00 04F3:31FB Mouse             	id=14	[slave  pointer  (2)]
⎜   ↳ ASUE120D:00 04F3:31FB Touchpad          	id=15	[slave  pointer  (2)]
⎜   ↳ input-remapper Asus Keyboard forwarded  	id=20	[slave  pointer  (2)]
⎜   ↳ ERGO M575 Mouse                         	id=22	[slave  pointer  (2)]
⎜   ↳ input-remapper ERGO M575 Mouse forwarded	id=23	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Video Bus                               	id=6	[slave  keyboard (3)]
    ↳ Power Button                            	id=7	[slave  keyboard (3)]
    ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
    ↳ Asus Keyboard                           	id=10	[slave  keyboard (3)]
    ↳ ELAN9008:00 04F3:2FC2 Stylus            	id=13	[slave  keyboard (3)]
    ↳ Asus WMI hotkeys                        	id=16	[slave  keyboard (3)]
    ↳ Asus Keyboard                           	id=17	[slave  keyboard (3)]
    ↳ input-remapper keyboard                 	id=18	[slave  keyboard (3)]
    ↳ input-remapper Asus Keyboard forwarded  	id=19	[slave  keyboard (3)]
    ↳ input-remapper Asus Keyboard forwarded  	id=21	[slave  keyboard (3)]

I finally zeroed on 

⎜   ↳ ASUE120D:00 04F3:31FB Touchpad          	id=15	[slave  pointer  (2)]
    ↳ input-remapper keyboard                 	id=18	[slave  keyboard (3)]
    ↳ input-remapper Asus Keyboard forwarded  	id=19	[slave  keyboard (3)]
    ↳ input-remapper Asus Keyboard forwarded  	id=21	[slave  keyboard (3)]
