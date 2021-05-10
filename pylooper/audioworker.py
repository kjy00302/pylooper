import pyaudio

class AudioWorker:
    def __init__(self, samplerate, bufsize=1024):
        self._samplerate = samplerate
        self._bufsize = bufsize
        
        self._pa = pyaudio.PyAudio()
        self.stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=samplerate,
            output=True,
            input=True,
            frames_per_buffer=bufsize,
            stream_callback=self.aw_callback
        )
        self.chunk_latency = int((self.stream.get_input_latency() + self.stream.get_input_latency()) / bufsize)

    def aw_callback(self, in_data, frame_count, time_info, status_flags):
        raise NotImplementedError

    def aw_start(self):
        self.stream.start_stream()

    def aw_stop(self):
        self.stream.stop_stream()
