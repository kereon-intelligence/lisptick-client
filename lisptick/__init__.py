"""
LispTick TimeSerie Streaming Server module
To work on an Onion Omega2 needs:
opkg update
opkg install python-codecs
"""

__version__ = "0.1.0"
__author__ = 'Cedric Joulain'
__credits__ = 'Kereon Intelligence'

import datetime
import json
import socket

from lisptick.reader import LisptickReader
from lisptick.exceptions import LispTickException


class Socket():
    """Request LispTick by socket"""

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def get_result(self, request):
        """Send resquest to server and return result"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.__host, self.__port))

        # Send request
        send_message(sock, request)
        res = LisptickReader(sock).get_result(-1)

        sock.close()
        return res

    def walk_result(self, request, func):
        """Call func on each part of result"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.__host, self.__port))

        # Send request
        send_message(sock, request)
        err_msg = LisptickReader(sock).walk_result(func)

        sock.close()
        if err_msg != "":
            raise LispTickException(err_msg)


def send_message(sock: socket, request: str):
    """Send request to LispTick

    Args:
        sock (socket): Socket
        request (str): LispTick request

    Raises:
        RuntimeError: message for LispTick is >64KB
        RuntimeError: socket connection broken
    """
    msg = json.dumps({"code": request}).encode()
    if len(msg) > 65536:
        raise RuntimeError("message for LispTick is >64KB")
    bsize = bytearray()
    bsize.append(len(msg) % 256)
    bsize.append(int(len(msg)/256))
    sock.send(bsize)
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
