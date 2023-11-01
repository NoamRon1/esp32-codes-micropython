class Motor:
    
    def __init__(self, pin1A, pin2A, enable_pinA, pin1B, pin2B, enable_pinB):
        self.pin1A = pin1A
        self.pin2A = pin2A
        self.enableA = enable_pinA
        self.pin1B = pin1B
        self.pin2B = pin2B
        self.enableB = enable_pinB
    
    def start(self, speed, motorA):
        speed = min(max(speed, -100), 100)
        if motorA:
            if speed > 0:
                self.pin1A.value(0)
                self.pin2A.value(1)
                self.enableA.duty(round(abs(speed)*10.23))
            elif speed < 0:
                self.pin1A.value(1)
                self.pin2A.value(0)
                self.enableA.duty(round(abs(speed)*10.23))
            else:
                self.pin1A.value(0)
                self.pin2A.value(0)
                self.enableA.duty(0)
        else:
            if speed > 0:
                self.pin1B.value(0)
                self.pin2B.value(1)
                self.enableB.duty(round(abs(speed)*10.23))
            elif speed < 0:
                self.pin1B.value(1)
                self.pin2B.value(0)
                self.enableB.duty(round(abs(speed)*10.23))
            else:
                self.pin1B.value(0)
                self.pin2B.value(0)
                self.enableB.duty(0)
    
    def timemove(self, Aspeed, Bspeed, during):
      start(Aspeed, True)
      start(Bspeed, False)
      time.sleep(during)
      start(0, True)
      start(0, False)  



    
    
