
<p align="center">
  <img alt="" src="./public/assets/img/maxresdefault (2).png" width="400px" />
</p>

# <img alt="" src="./public/assets/img/pngegg.png" width="25px" /> audio-to-midi
<img alt="" src="./public/assets/img/logo.2506b88a52d750fce903.png" width="100px" />`audio-to-midi` takes in a sound file and converts it to a multichannel MIDI file. It accomplishes this by performing FFT's on all channels of the audio data at user specified time steps. It then separates the resulting frequency analysis into equivalence classes which correspond to the twelve tone scale; the volume of each class being the average volume of its constituent frequencies. It then formats this data for MIDI and writes it out to a user specified file. It has the ability to convert whichever audio file formats are supported by the [soundfile](https://pypi.org/project/SoundFile/) module. libsndfile must be installed before running `audio-to-midi`


## <img alt="" src="./public/assets/img/pngegg.png" width="25px" /> Installation

- backend
```
> python ./setup.py install
> python main.py
```
- frontend
```
> npm install
> npx http-server
```

## <img alt="" src="./public/assets/img/pngegg.png" width="25px" /> Usage

```shell
> audio-to-midi --help
usage: audio-to-midi [-h] [--output OUTPUT] [--time-window TIME_WINDOW] [--activation-level ACTIVATION_LEVEL] [--condense] [--condense-max] [--single-note]
                     [--note-count NOTE_COUNT] [--bpm BPM] [--transpose TRANSPOSE] [--key KEY [KEY ...]] [--no-progress]
                     infile

positional arguments:
  infile                The sound file to process.

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        The MIDI file to output. Default: <infile>.mid
  --time-window TIME_WINDOW, -t TIME_WINDOW
                        The time span over which to compute the individual FFTs in milliseconds.
  --activation-level ACTIVATION_LEVEL, -a ACTIVATION_LEVEL
                        The amplitude threshold for notes to be added to the MIDI file. Must be between 0 and 1.
  --condense, -c        Combine contiguous notes at their average amplitude.
  --condense-max, -m    Write the maximum velocity for a condensed note segment rather than the rolling average.
  --single-note, -s     Only add the loudest note to the MIDI file for a given time window.
  --note-count NOTE_COUNT, -C NOTE_COUNT
                        Only add the loudest n notes to the MIDI file for a given time window.
  --bpm BPM, -b BPM     Beats per minute. Defaults: 60
  --transpose TRANSPOSE, -T TRANSPOSE
                        Transpose the MIDI pitches by a constant offset.
  --key KEY [KEY ...], -k KEY [KEY ...]
                        Map to a pitch set.
  --no-progress, -n     Don't print the progress bar.
```

  <img alt="" src="./public/assets/img/pngegg (4).png"/>
  <img alt="" src="./public/assets/img/maxresdefault.jpg"/>
