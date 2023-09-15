import os
import librosa
import soundfile as sf
from pydub import AudioSegment


class AudioProcessor:
    processor = "librosa"

    @classmethod
    def edit_volume(cls, input_dir: str = "input", output_dir: str = "output",
                    factor=1, db_diff=0):
        """
        Increase or reduce .wav files volume.
        :param input_dir: directory with input files
        :param output_dir: directory with processed files
        :param factor: factor for librosa converter
        :param db_diff: dB difference for pydub converter
        """
        processed = 0
        skipped = 0

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        for file_name in os.listdir(input_dir):
            if not file_name.endswith(".wav"):
                skipped += 1
                print(f"File '{file_name}' is not in .wav format. Skipped.")
                continue

            if cls.processor == "librosa":
                # sr = None - don't reduce samplerate on load
                data, samplerate = librosa.load(
                    f"{input_dir}/{file_name}", sr=None
                )
                data *= factor
                sf.write(f"{output_dir}/{file_name}", data, samplerate)

            elif cls.processor == "pydub":
                track = AudioSegment.from_wav(f"{input_dir}/{file_name}")
                track += db_diff
                track.export(f"{output_dir}/{file_name}", format="wav")

            processed += 1

        print(f"Processed {processed} files. Skipped {skipped} files.")
