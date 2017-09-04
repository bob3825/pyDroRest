import serial
import multiprocessing

arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)


class PyArduino:

    def __init__(self):
        self.test = 'test'
        receiver = multiprocessing.Process(name='arduino_receiver', target=self.__receive)
        receiver.start()
        receiver.join()

    def __receive(self):
        while True:
            if arduinoSerialData.inWaiting:
                my_data = arduinoSerialData.readline
                print my_data
                self.handle_message(my_data)

    def front(self):
        self.is_not_used()
        print 'front'

    def back(self):
        self.is_not_used()
        print 'back'

    def right(self):
        self.is_not_used()
        print 'right'

    def left(self):
        self.is_not_used()
        print 'left'

    def front_right(self):
        self.is_not_used()
        print 'frontRight'

    def front_left(self):
        self.is_not_used()
        print 'frontLeft'

    def back_right(self):
        self.is_not_used()
        print 'backRight'

    def back_left(self):
        self.is_not_used()
        print 'backLeft'

    def up(self):
        self.is_not_used()
        print 'up'

    def down(self):
        self.is_not_used()
        print 'down'

    def land(self):
        self.is_not_used()
        print 'land'

    def test(self):
        self.is_not_used()
        print 'test'

    def is_not_used(self):
        pass

    def handle_message(self):
        pass
