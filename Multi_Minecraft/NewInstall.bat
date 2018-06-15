::Setup.bat - Script to setup Multi_Minecraft with initial files ready for your .jar -nzwrigh
@echo off
set /p newDir="Provide name for new install: "
echo.
echo Checking and Fetching Minecraft.exe...
if not exist %~dp0_TEMPLATE\Minecraft.exe call cscript.exe %~dp0Fetch_Minecraft.vbs > nul
echo.
echo Creating new Minecraft install in folder %newDir%...
xcopy /s /i /q /y %~dp0_TEMPLATE %~dp0%newDir% > nul
echo.
pause