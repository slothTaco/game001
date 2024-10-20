#!/usr/bin/env python3
# by Seth Kenlon

## GPLv3
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

'''
Variables
'''
# put variables here
worldx = 960
worldy = 720
fps = 40 # frame rate
ani = 4 # animation cycles

'''
Objects
'''

# put Python classes and functions here


'''
Setup
'''
# put run-once code here
clock = pygame.time.Clock ()
pygame.init()

'''
Main Loop
'''

# put game loop here
