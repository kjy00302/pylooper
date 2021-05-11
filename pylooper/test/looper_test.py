from ..aw_looper import Looper
import time

looper = Looper()
print(looper.chunk_latency)
looper.aw_start()
print('rec..')
looper.record()
time.sleep(1)

print('play..')
looper.play()
time.sleep(5)

print('overrec..')
looper.overrec()
time.sleep(1)

looper.play()
print('play..')
time.sleep(5)
