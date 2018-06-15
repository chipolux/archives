import servicemanager
import win32event
import win32service
import win32serviceutil

from server.config import CONFIG
from server.service import Service


class ButrManager(win32serviceutil.ServiceFramework):
    _svc_name_ = "ButrManager"
    _svc_display_name_ = "ButrManager - Minecraft Server Management"
    _svc_description_ = "Manages local Minecraft server instances."

    def __init__(self, args):
        super().__init__(args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ''),
        )
        self.main()

    def main(self):
        self.timeOut = 10  # milliseconds

        service = Service(CONFIG.mode, CONFIG.port, CONFIG.password, True)
        while True:
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeOut)
            if rc == win32event.WAIT_OBJECT_0:
                servicemanager.LogInfoMsg("ButrManager - STOPPED")
                break
            else:
                servicemanager.LogInfoMsg("ButrManager - RUNNING")
                service.run_once()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ButrManager)
