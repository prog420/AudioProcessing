import argparse
from audio_processor import AudioProcessor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--processor', help='Audio Processor',
                        default="librosa")
    parser.add_argument('-i', '--input', help='Input Directory',
                        default="input")
    parser.add_argument('-o', '--output', help='Output Directory',
                        default="output")
    parser.add_argument('-f', '--factor', help='Volume factor (librosa)',
                        default=1, type=float)
    parser.add_argument('-d', '--db_diff', help='dB diff (pydub)',
                        default=0, type=int)

    args = vars(parser.parse_args())

    AudioProcessor.processor = args["processor"].lower()

    AudioProcessor.edit_volume(
        input_dir=args["input"],
        output_dir=args["output"],
        factor=args["factor"],
        db_diff=args["db_diff"]
    )
