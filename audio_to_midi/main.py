#!/usr/bin/env python3

import argparse
import os
import sys
import logging

from audio_to_midi import converter, progress_bar


def _convert_beat_to_time(bpm, beat):
    try:
        parts = beat.split("/")
        if len(parts) > 2:
            raise Exception()

        beat = [int(part) for part in parts]
        fraction = beat[0] / beat[1]
        bps = bpm / 60
        ms_per_beat = bps * 1000
        return fraction * ms_per_beat
    except Exception:
        raise RuntimeError("Invalid beat format: {}".format(beat))

def parse_params(infile="./uploads/Untitled.wav", output=None, time_window=5.0, activation_level=0.0, condense=False,
               condense_max=False, single_note=False, note_count=0, bpm=60, beat=None,
               transpose=0, key=None, no_progress=False):
    args = {
        'infile': infile,
        'output': output if output else f"{os.path.basename(infile)}.mid",
        'time_window': time_window,
        'activation_level': activation_level,
        'condense': condense,
        'condense_max': condense_max,
        'single_note': single_note,
        'note_count': note_count,
        'bpm': bpm,
        'beat': beat,
        'transpose': transpose,
        'key': key if key else [],
        'no_progress': no_progress
    }

    if args['single_note']:
        args['note_count'] = 1

    if args['key']:
        for k in args['key']:
            if k not in range(12):
                raise RuntimeError("Key values must be in the range: [0, 12)")

    if args['beat']:
        args['time_window'] = _convert_beat_to_time(args['bpm'], args['beat'])
        print(args['time_window'])

    return args

def MIDIConverter(params):
    try:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")

        process = converter.Converter(
            infile=params["infile"],
            outfile=params["output"],
            time_window=params["time_window"],
            activation_level=params["activation_level"],
            condense=params["condense"],
            condense_max=params["condense_max"],
            note_count=params["note_count"],
            transpose=params["transpose"],
            key=params["key"],
            bpm=params["bpm"],
            progress=None if params["no_progress"] else progress_bar.ProgressBar(),
        )
        process.convert()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        logging.exception(e)
        sys.exit(1)


# if __name__ == "__main__":
#     main()
