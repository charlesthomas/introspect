from os import path, uname

class UnsupportedOSError(Exception): pass

def get_osx_window_title():
    from sh import osascript
    script_path = path.join(path.dirname(__file__), 'scripts',
                            'osx_active_window_title.osascript')
    return osascript(script_path).stdout.strip()

def get_windows_window_title():
    from win32gui import GetForgroundWindow, GetWindowText
    return GetWindowText(GetForegroundWindow())

def get_linux_window_title():
    raise UnsupportedOSError("linux doesn't work yet, please submit pull "
                             "request")

def get_window_title():
    this_os = uname()[0]
    if this_os == 'Darwin':
        return get_osx_window_title()
    else:
        raise UnsupportedOSError("OS X only supported. windows function is "
                                 "untested, and linux is unknown")
