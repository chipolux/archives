ESP8266 Buildbox
================

A 'quick' and easy to setup build and dev environment for the ESP8266.

It's also on dockerhub as
[`chipolux/esp8266-buildbox`](https://registry.hub.docker.com/u/chipolux/esp8266-buildbox/).


Usage
=====

Once you've got [docker](https://docs.docker.com/installation/#installation)
installed and running on your system, you can either pull down this Dockerfile
and build it with:

`docker build -t chipolux/esp8266-buildbox ./path/to/Dockerfile`

Or simply do the following to pull it down from dockerhub:

`docker pull chipolux/esp8266-buildbox`

Then situate yourself in a project directory of choice and then run this:

`docker run --rm -ti -v $(pwd):/home/esp8266/project chipolux/esp8266-buildbox`

That will start a buildbox and put you in a terminal on it with your current
directory mounted at the working directory of the buildbox.

This will allow you to run build commands inside the buildbox but use your
regular dev environment from outside it!

Then to push your code to the chip, you can do the following:

`pip install -r requirements.txt`

And that will install esptool.py which is great for talking to the chip!


Common Issues
=============

* Sharing a volume with a container shares the volume from the host machine
    which means containers ran on a remote host (or boot2docker in Windows
    and OSX) won't get the volume you might think. Since boot2docker 1.3
    they share user folders by default so this takes care of a lot of use
    cases, but this still won't work if you're using a true remote host.
    * Unfortunately there really isn't a workaround to this, I've bashed
        my head on it for awhile and docker/boot2docker have issues open
        to look into methods of sharing volumes with true remote hosts so
        that may be fixed later.

* When using a remote host, most commonly boot2docker, you may get a time
    skew error when using make.
    * This happens when the b2d VM is running when the host computer goes to
        sleep and the VM experiences a time drift since it has no physical
        clock or automated NTP update process.
    * An easy fix is to close all your containers, run
        `boot2docker ssh sudo ntpclient -s -h pool.ntp.org` to update the
        b2d VM's time, and then bring your containers back up. If your host
        machine is in sync with NTP then it should all work fine!
    * If your using a true remote host, you just need to ensure that both
        it and your machine are in sync with NTP.
    * There are also issues open with b2d to figure out a way to have
        this happen automatically so it may be solved in the future.
