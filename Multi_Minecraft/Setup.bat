::Setup.bat - Script to setup Multi_Minecraft with initial files ready for your .jar -nzwrigh
@echo off
echo Checking and Fetching Minecraft.exe...
if not exist %~dp0_TEMPLATE\Minecraft.exe echo Fetching Minecraft && call cscript.exe %~dp0Fetch_Minecraft.vbs
echo.
echo Creating initial minecraft install in folder "Default"...
xcopy /s /i /q /y %~dp0_TEMPLATE %~dp0Default > nul
echo.
echo Starting "Default" Minecraft for you! Enjoy!
%~dp0Default\Launcher.bat
pause