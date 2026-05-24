#!/bin/bash 

#State refers to the current connection status, whether it is active and established, or waiting or if it has ended.
#Local address refers to your system/machine's IP address and connection port.
#Remote address refers to the IP address and port of the destination machine or remote system that yoour machine is interacting with.
#Process tells us which program is using which connection. It matches or links them together basically

echo "Monitoring Active Internet Connections on this Machine"
echo ""
ss -tunp
echo ""
echo "The End"
