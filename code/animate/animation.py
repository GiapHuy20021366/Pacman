import time

               
class Animation:

    def __init__(self, para = (2.0, 2), action = None) -> None:
        self.duration, self.repeat= para
        self.action = action
        self.process = 0.0
        self._time = time.time()
        self.running = False    
        self.prev_index = 0
        
    def next_image(self):
        if self.repeat == 0:
            return self.action.get_index(0)
        time_ = time.time()
        delta_time = time_ - self._time
        delta_time = (delta_time - int(delta_time/self.duration)*self.duration)
        self.process = delta_time / self.duration
        new_index = round(self.process * len(self.action.images)) % self.action.length()
        if self.prev_index == self.action.length() - 1 and new_index == 0:
            self.repeat = self.repeat - 1
        self.prev_index = new_index
        return self.action.get_index(new_index)
    
    def update(self):
        if self.repeat == 0:
            self._time = time.time()
            self.action.index = 0
            self.prev_index = 0
            return
        time_ = time.time()
        delta_time = time_ - self._time
        delta_time = (delta_time - int(delta_time/self.duration)*self.duration)
        self.process = delta_time / self.duration
        new_index = round(self.process * self.action.length()) % self.action.length()
        if self.prev_index == self.action.length() - 1 and new_index == 0:
            self.repeat = self.repeat - 1
        self.prev_index = new_index
        self.action.index = new_index
    
    def stop(self):
        self.repeat = 0
        

        