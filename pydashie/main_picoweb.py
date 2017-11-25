#
# This is a picoweb example showing a Server Side Events (SSE) aka
# EventSource handling,
#
import ure
import uasyncio
import picoweb

event_sinks = []

#
# Webapp part
#

def events(req, resp):
    global event_sinks
    print("Event source connected")
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/event-stream\r\n")
    yield from resp.awrite("\r\n")
    event_sinks_add(resp)
    return False


def widget_html(req, resp):
    name = req.url_match.group(1)
    fname = "widgets/%s/%s.html" % (name, name)
    await app.sendfile(resp, fname)


ROUTES = [
    ("/", lambda req, resp: (yield from app.sendfile(resp, "templates/main.html"))),
    ("/events", events),
    (ure.compile("/views/([^/]+)\.html"), widget_html),
]

#
# Background service part
#

def event_sinks_add(sink):
    global event_sinks
    for i in range(len(event_sinks)):
        if event_sinks[i] is None:
            event_sinks[i] = sink
            return
    event_sinks.append(sink)


def push_event(val):
    global event_sinks
    for i in range(len(event_sinks)):
        resp = event_sinks[i]
        if resp is None:
            continue
        try:
            await resp.awrite("data: %s\n\n" % val)
        except OSError as e:
            await resp.aclose()
            print("Event source %r disconnected (%r)" % (resp, e))
            event_sinks[i] = None


class EventQueue:

    def push_event(self, val):
        await push_event(val)


import logging
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

app = picoweb.WebApp(__name__, ROUTES)

import example_app
example_app.run(EventQueue())

app.run(debug=True, host="0.0.0.0")
