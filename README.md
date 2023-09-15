##### Script to batch edit volume of .wav files.
Supported libraries: `librosa`, `pydub`.
___
##### CLI Usage:
`python main.py`

##### CLI Arguments:
`-p`, `--processor` - `librosa` or `pydub` (default: `librosa`).

`-i`, `--input` - input directory (default: `input`).

`-o`, `--output` - output directory (default: `output`).

`-f`, `--factor` - volume factor for `librosa` (default: `1`)

`-d`, `--db_diff` - dB difference for `pydub` (default: `0`)

___
##### Example:
1. Set volume to 90% of its default value using `librosa`:

`python main.py -p librosa -f 0.9`

2. Reduce volume by 5 dB using `pydub`:

`python main.py -p pydub -d -5`