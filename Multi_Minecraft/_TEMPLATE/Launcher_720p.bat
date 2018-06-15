::Launcher.bat - Script to starte minecraft instance with current directory set as APPDATA and resize to 720p -chipolux
@echo off
set APPDATA=%~dp0
start %~dp0Minecraft.exe
ping 999.999.999.999 -n 1 -w 2000 >nul
powershell.exe -NoProfile -ExecutionPolicy Bypass -File %~dp0Resize-Minecraft.ps1