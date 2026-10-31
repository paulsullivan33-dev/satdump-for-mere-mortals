# Recordings First — Files In

Every SatDump job starts with a file and a statement of what kind of file it is. The command's shape never changes:

```
satdump <pipeline> <input level> <input file> <output folder> [options]
```

The **input level** is the idea to grasp, because it is where beginners' jobs fail. A satellite transmission exists at several stages of cookedness, and a recording can capture any of them:

- **Baseband** — the raw radio recording: the receiver's whole view of a slice of spectrum, stored as samples of the signal itself. Files are large (megabytes per second), formats have names like `cf32`, `cs16`, `cs8` and `cu8` (the shape and size of each sample), and the job needs the recording's **sample rate** — how many samples per second the radio took — passed with `--samplerate`. Get the rate wrong and every frequency inside shifts; the decode fails completely, and the log's failure to find any signal is your clue.
- **Soft symbols / framed data** — some pipelines accept the halfway stages too: the output of a demodulator, or of a decoder, so researchers can re-run just the later steps. Most readers will never record these directly, but the levels explain the pipeline diagrams you will meet.
- **Audio** — for the oldest and simplest transmissions, someone (a radio receiver, or another program) has already done the demodulating, and what remains is a sound file: a `.wav` whose "sound" is the satellite's data tone. NOAA's APT service, from chapter 6, is the famous case.

The NOAA APT pipeline shows the levels in its recipe. It offers two doors: start at `baseband` with an IQ recording of the 137 MHz signal, or start at `audio_wav` with a demodulated recording, in which case its first module is a demodulator for the *audio* — because APT is a picture encoded as a varying tone, and that tone still needs decoding into brightness values (the recipe, read in the lab, names the module `noaa_apt_demod` and fixes its internal audio rate at 50,000 samples per second; your `.wav` can be any reasonable rate and is converted on the way in).

Two practical consequences follow. First, **a recording is never just a file; it is a file plus its facts** — sample rate, centre frequency, which satellite, and when it began. SatDump takes these as command options (`--samplerate`, `--start_timestamp`, pipeline parameters such as `--satellite_number`) and can read the start time out of filenames in the formats recording programs commonly write. Lose the facts and the file still decodes, but everything that depends on knowing where and when — maps, overlays, correct satellite names — quietly switches off. Chapter 8 is the demonstration.

Second, **recordings are the hobby's library.** Because a baseband or audio file can be decoded by anyone, anywhere, test recordings circulate: projects keep them as regression tests, teachers keep them for classes, and beginners decode a known-good file to prove their setup before an antenna enters the story. The recording this guide decodes is exactly that — a test fixture kept by another open-source project, identified precisely in chapter 6. Learning SatDump from recordings first is not a shortcut around the hobby; it is how the hobby teaches itself.
