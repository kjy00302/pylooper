from . import audioworker
import array
import pyaudio
import audioop

LOOPER_STOP = 0
LOOPER_RECORD = 1
LOOPER_PLAY = 2
LOOPER_OVERDUB = 3

class Looper(audioworker.AudioWorker):
    def __init__(self):
        super().__init__(48000)
        self._state = LOOPER_STOP
        self._aud_buf = array.array('h')
        self._chunk_cnt = 0
        self._chunk_ptr = 0
        self._rms = 0

    def aw_callback(self, in_data, frame_count, time_info, status_flags):
        self._rms = self._rms * 0.7 + audioop.rms(in_data, 2)/32768 * 100 * 0.3
        if self._rms < 5:
            in_data = audioop.mul(in_data, 2, (self._rms/5) ** 8)

        if self._state & 2: # LOOPER_PLAY & LOOPER_OVERDUB
            offset = self._bufsize * self._chunk_ptr
            if self._state == LOOPER_OVERDUB:
                recoffset = self._bufsize * ((self._chunk_ptr - self.chunk_latency) % self._chunk_cnt)
                mixsrc = self._aud_buf[recoffset:recoffset+self._bufsize].tobytes()
                self._aud_buf[recoffset:recoffset+self._bufsize] = array.array('h', audioop.add(mixsrc,in_data,2))
            data = self._aud_buf[offset:offset+self._bufsize].tobytes()
            self._chunk_ptr = (self._chunk_ptr + 1) % self._chunk_cnt
        else: # LOOPER_STOP & LOOPER_RECORD
            if self._state == LOOPER_RECORD:
                self._aud_buf.frombytes(in_data)
                self._chunk_cnt += 1
            data = bytes(self._bufsize * 2)
        return (data, pyaudio.paContinue)

    def stop(self):
        self._state = LOOPER_STOP

    def record(self):
        self._aud_buf = array.array('h')
        self._chunk_cnt = 0
        self._chunk_ptr = 0
        self._state = LOOPER_RECORD

    def overrec(self):
        self._state = LOOPER_OVERDUB

    def play(self):
        self._state = LOOPER_PLAY
