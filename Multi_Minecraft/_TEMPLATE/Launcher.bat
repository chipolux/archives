::Launcher.bat - Script to starte minecraft instance with current directory set as APPDATA -chipolux
@echo off
set APPDATA=%~dp0
start %~dp0Minecraft.exe