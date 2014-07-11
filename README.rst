==========
introspect
==========

How do you spend your time?

This is very early days, but introspect can now successfully log OS X active
window. It polls every second.

Quickstart
==========
::
    pip install introspect
    introspect_logger

Log File Location
=================
introspect_logger writes to ~/.introspect. A new log file is written to every
hour. The format is: "~/.introspect/introspect_YYYY_MM_DD_HH.log"
