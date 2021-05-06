import pyaudio
import array
import audioop

"""
Proof of concept looper
TODO:
    Accurate 1 second
    Latency compensation
    And more...
"""

# chunk size
CHUNK = 1024
SAMPLERATE = 48000

# 16bit integer array
aud_buf = array.array('h')

pa = pyaudio.PyAudio()

# open stream
stream = pa.open(
    format=pa.get_format_from_width(2), # 16bit audio
    channels=1, # mono
    rate=SAMPLERATE, # 48k samplerate
    output=True, # writable stream
    input=True # readable stream
)

# divide 48k samples by 1024 chunk
for i in range(SAMPLERATE//CHUNK):
    d = stream.read(CHUNK)
    aud_buf.frombytes(d)
    stream.write(d)
try:
    # and loop forever! (until interrupt)
    while True:
        for i in range(SAMPLERATE//CHUNK):
            buf = aud_buf[i*CHUNK:(i+1)*CHUNK].tobytes()
            aud_in = stream.read(CHUNK)
            
            stream.write(
                audioop.add(buf, aud_in, 2) # mix input and output
            )
except InterruptedError:
    pass

# cleanup
stream.stop_stream()
stream.close()
pa.terminate()
