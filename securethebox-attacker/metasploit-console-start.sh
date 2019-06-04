#!/bin/bash
#  This is for MSFConsole
PASSWORD="changeme123"
msfconsole -q -x "load msgrpc [Pass=$PASSWORD]"
exit