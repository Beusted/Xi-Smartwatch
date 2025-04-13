import idle
import threading

t = threading.Thread(target=idle.idle)
t.start()
