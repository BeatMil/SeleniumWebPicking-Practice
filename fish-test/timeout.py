import eventlet
from eventlet.timeout import Timeout
timeout = Timeout(0.2, False)
try:
    eventlet.sleep(0.3)
except:
    timeout.cancel()
    print("except")