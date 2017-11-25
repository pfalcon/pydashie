import datetime
import json
from repeated_timer import RepeatedTimer

class DashieSampler:
    def __init__(self, app, interval):
        self._app = app
        self._timer = RepeatedTimer(interval, self._sample)

    def stop(self):
        self._timer.stop()

    def name(self):
        '''
        Child class implements this function
        '''
        return 'UnknownSampler'

    def sample(self):
        '''
        Child class implements this function
        '''
        return {}

    def _send_event(self, widget_id, body):
        body['id'] = widget_id
        body['updatedAt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S +0000')
        await self._app.push_event(json.dumps(body))

    def _sample(self):
        data = self.sample()
        if data:
            await self._send_event(self.name(), data)
