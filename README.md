Network Testing Application
===========================
Network Testing Application - a personal project (c) 2013 Nick Klose.

Developed for Ms. Naomi Hodge (ECE 491, University of Alberta).

This application was designed to provide functionality for testing 
mesh networks. It allows text to be sent between nodes and relayed 
if necessary.

Required Packages
=================
1. PyQT. PyQT is Copyright (c) 2013, Riverbank Computing Limited. Riverbank Computing Limited is a company registered in England and Wales with company number 4314904.
2. PySerial. PySerial is Copyright (c) 2001-2010, Chris Liechti. All rights reserved.

Compatibility
=============
## Windows
The application can be run by double-clicking on `network.exe` or by using the command `python network.py` if dependencies are installed.

To recompile `network.exe`, use the command `python setup.py py2exe`. The `py2exe` module is required for this.

Application has been tested most extensively on Windows.

## Linux
Application was built and tested using Ubuntu Linux 12.10. It can be run using the command `python network.py` if dependencies are installed.

## OSX
OSX has not been tested, but the command `python network.py` should work if all dependencies are installed.

## Other
Other operating systems are not supported, though if they have Python and the required packages installed they should work too.

Known Issues
============
* Program can become unstable if the port is selected twice.
* Serial parameters are not actually used to open the port.
* Sending images is not working.

License
=======
	Network Testing Application
	
	(c) 2013 Nick Klose

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	http://www.gnu.org/copyleft/gpl.html