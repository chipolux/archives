#Windows Service Install

###Requirements
* [Python 3.4+](http://www.python.org/download/)
* [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
* Everything else as normal in requirements.txt

###Install
1. Place this project wherever you'd like it to run from and set up your `server/config.json`
    and associated server files.
2. Open a command prompt in this projects directory at the same folder as `win_service.py`.
    * You will need to open the command prompt as an administrator.
3. Install the service by running `python win_service.py --startup auto install`.
    * You don't have to use `--startup auto` if you always want start the service manually.
4. Start the service by running `python win_service.py start`

###Uninstall
1. Open a command prompt in this project directory, in the same folder as `win_service.py`.
    * You will need to open the command prompt as an administrator.
2. Run `python win_service.py stop` to stop the service.
3. Run `python win_service.py remove` to uninstall the service.
