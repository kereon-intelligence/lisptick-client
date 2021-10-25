import datetime


class Sentinel(int):
    """Sentinel object indicating end of a grid flow"""
    Null = 0
    End = 1
    Marker = 2


class InArray():
    """UID and position in an array"""

    def __init__(self, init_uid, init_pos):
        self.uid = init_uid
        self.pos = init_pos

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get_uid(self):
        """Element uniq id"""
        return self.uid

    def get_pos(self):
        """Element position in array"""
        return self.pos


class Duration():
    """LispTick duration time handling Year, Month, Day and microseconds (from nano)"""

    def __init__(self, init_year=0, init_month=0, init_day=0, init_epoch=0):
        self.year = init_year
        self.month = init_month
        self.timedelta = datetime.timedelta(init_day, 0, init_epoch / 1000)

    def __str__(self):
        return str(self.year) + "Y" + str(self.month) + "M" + str(self.timedelta)

    def get_year(self):
        """Number of years duration part"""
        return self.year

    def get_month(self):
        """Number of month duration part"""
        return self.month

    def get_timedelta(self):
        """micro seconds and days duration part as a timedelta"""
        return self.timedelta


class Point():
    """A point is a value at a time"""

    def __init__(self, init_time, init_value):
        self.time = init_time
        self.i = init_value

    def __str__(self):
        return str(self.time) + " " + str(self.i)

    def __len__(self):
        return 2


class HeartBeat():
    """An HeartBeat is an information value that can be forgotten"""

    def __init__(self, init_value):
        self.value = init_value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get_value(self):
        """HeartBeat value"""
        return self.value


class Tensor():
    """Tensor  n-dimensional arrays"""

    def __init__(self, shape, values=None):
        self.shape = shape
        if values is None:
            values = [0] * self.get_size()
        self.values = values

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get_size(self):
        """tensor size in number of values"""
        size = 1
        for i in self.shape:
            size *= i
        return size
