# Recipes

Small, complete jobs. Every command here uses the machinery the earlier chapters verified; options are named exactly as the lab used them or as the pipeline files define them.

**Decode an APT recording someone gave you.**
You need to know only that it's APT audio:

```
satdump noaa_apt audio_wav recording.wav out/
```

Then check the output the chapter 6 way: lines ≈ 2 × the recording's seconds, `raw_sync.png` 2,080 pixels wide, channel pictures 909 wide. If the lines are wildly short, the file wasn't APT audio, whatever its name.

**Decode it again, properly, once you learn the facts.**
Found out later which satellite and when? Nothing about the decode changes, but the projected products switch on:

```
satdump noaa_apt audio_wav recording.wav out2/ \
    --satellite_number 19 --start_timestamp 1545511181
```

The timestamp is seconds since 1970 (Unix time), UTC. Keep both output folders; comparing their contents is the fastest way to learn what projection adds.

**Work from a baseband recording instead.**
Your receiver software saved IQ (the SDR++ and GQRX shape of life):

```
satdump noaa_apt baseband pass.cs16 out/ \
    --samplerate 1e6 --baseband_format cs16
```

The sample rate and format must be the recording's true ones — they are properties of the file, not preferences. (The lab verified the audio route end-to-end; the baseband route is the same pipeline entered one door earlier, and is labelled accordingly.)

**Rebuild products without re-decoding.**
SatDump wrote `product.cbor` for a reason: products can be re-derived from it with the processing tools the project ships, and composites re-rendered with different enhancements, without touching the original recording. Treat the `.cbor` as the negative and the PNGs as prints.

**Keep a pass diary.**
For each recording, keep a one-line note beside the file — satellite, date, start time in UTC, how the pass sounded. Future you, decoding it in seven years, is a stranger; the 2018 recording this guide used survived *because someone wrote its facts down* in a test script. Match that standard and your archive stays decodable forever.
