Multi_Minecraft
===============

My setup for having multiple seperate installs of minecraft on one machine with minimal overhead. For Win XP and above only.

Setup
=====

You can download the current package by simply clicking the ZIP button up above next to the Clone in Windows button.

Once you have that you can go ahead and unzip it wherever you like on your HDD or on an external or a flash drive, whatever you'd like! That's the best part, it can run from anywhere (as far as my testing shows)!

Once extracted simply run the Setup.bat file either by doubleclicking or you can run it from command line with no args and it will setup a Default Minecraft install and put everything in place from the _TEMPLATE folder.

It'll start Minecraft up for you automatically the first time, but after that you'll need to go into the Default directory and run Launcher.bat to start it up. Simple as that!

Also, if you have Powershell v2 (If you've got XP SP3+ you do ;]) then you can run the Launcher_720p.bat script to start Minecraft and then it'll automatically wait 2 seconds and then try to resize the window to 720p for your big screened view pleasure!

Creating Another Install
========================

To create a new minecraft install simply run the NewInstall.bat file. It will ask you what to name the new install and put everything where it needs to be!

Modifying Your Installs
=======================

One of the largest benefits to this method is that you can run any multiple mods and versions and switch between them by simply double clicking the other Launcher.bat

As far as installing mods or different versions we'll use the Default install as an example, you treat the Default folder as your %APPDATA% folder, so you will find .minecraft and everything inside there including your saves and texturepacks, everything.

So if I downloaded the latest snapshot I'd do the following:
* Run NewInstall.bat and specify the name 12w17a for the latest snapshot.
* Navigate to the new 12w17a subdirectory it just created for me!
* Run Launcher.bat and login to Minecraft so that it generates all the necessary files in .minecraft.
* Close out of Minecraft and navigate to .minecraft\bin and replace minecraft.jar with new snapshot jar like normal.

It's as simple as that. I personally use a Snapshot directory that I contantly keep updated with the latest snapshot as well as Default directory for the current release install as well as other misc mods and versions.