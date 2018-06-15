#Resize-Minecraft.ps1 - Script to resize minecraft client to 720p -chipolux

Add-Type @"
  using System;
  using System.Runtime.InteropServices;

  public class Win32 {
    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);

    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool GetClientRect(IntPtr hWnd, out RECT lpRect);

    [DllImport("user32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int nWidth, int nHeight, bool bRepaint);
  }

  public struct RECT
  {
    public int Left;        // x position of upper-left corner
    public int Top;         // y position of upper-left corner
    public int Right;       // x position of lower-right corner
    public int Bottom;      // y position of lower-right corner
  }

"@


$rcWindow = New-Object RECT
$rcClient = New-Object RECT

$h = (Get-Process | where {$_.MainWindowTitle -eq "Minecraft Launcher"}).MainWindowHandle

[Win32]::GetWindowRect($h,[ref]$rcWindow)
[Win32]::GetClientRect($h,[ref]$rcClient)

$width = 1280
$height = 720

$dx = ($rcWindow.Right - $rcWindow.Left) - $rcClient.Right
$dy = ($rcWindow.Bottom - $rcWindow.Top) - $rcClient.Bottom

[Win32]::MoveWindow($h, $rct.Left, $rct.Top, $width + $dx, $height + $dy, $true )