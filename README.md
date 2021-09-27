# BeatTaser
A python program made for a raspberry PI that tazes you on a block miss or level fail.

## Get started!
### Raspberry PI configuration
Type ``sudo raspi-config`` go to ``3 Interface Options`` then ``P2 SSH`` and make sure
it's __ENABLED__.

### PIP Packages
Install with ``pip install`` or ``python3 -m pip install``
- ``websockets``
- ``RPi.GPIO``

### Initialize
Download this repository and edit ``hostComputerIP`` in main.py
if you have a static IP. You can also edit the taser ON time in this file.

### How to connect
My configuration has a relay connected to pin 2 and a "taser" 
(aka a high-voltage DC to DC converter) connected to that relay to a external
power supply.