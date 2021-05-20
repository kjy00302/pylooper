import pyaudio

class AudioWorker:
    def __init__(self, samplerate, bufsize=1024):
        self._samplerate = samplerate
        self._bufsize = bufsize
        self._pa = pyaudio.PyAudio()

    def aw_init(self):
        try:
            self.stream = self._pa.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self._samplerate,
                output=True,
                input=True,
                frames_per_buffer=self._bufsize,
                stream_callback=self.aw_callback
            )
        except Exception as e:
            print("Failed to open audio stream")
            print("Error:",type(e), e)
            if e.errno == -9996:
                print("Check your audio device")
            return False
        self.chunk_latency = int(
            self._samplerate * (
                self.stream.get_input_latency()
                + self.stream.get_input_latency()
            ) / self._bufsize
        )
        return True

    def aw_callback(self, in_data, frame_count, time_info, status_flags):
        raise NotImplementedError

    def aw_start(self):
        self.stream.start_stream()

    def aw_stop(self):
        self.stream.stop_stream()
