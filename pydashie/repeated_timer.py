import uasyncio

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        while 1:
            await self.function(*self.args, **self.kwargs)
            await uasyncio.sleep(self.interval)

    def start(self):
        if not self.is_running:
            uasyncio.get_event_loop().create_task(self._run())
            self.is_running = True

    def stop(self):
        # TODO
        self.is_running = False
