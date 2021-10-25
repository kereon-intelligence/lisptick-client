
class LispTickException(Exception):
    """Simple LispTick error message"""

    def __init__(self, msg):
        super(LispTickException, self).__init__(msg)
        self._msg = msg

    def _str_(self):
        return self._msg
