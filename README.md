# SatDump for Mere Mortals

Weather satellites cross your sky every
hour or so, broadcasting pictures of the
Earth in the open — no encryption, no
account, free for anyone with a receiver.
**SatDump** is the program that turns
those broadcasts into pictures and data:
a **recording of radio signals** goes in,
and a folder of **weather images** comes
out. One program, startlingly many
satellites: the copy this guide's lab
installed ships **184 pipelines** —
recipes for 184 kinds of transmission,
from the NOAA weather fleet to Russia's
Meteor-M, the geostationary GOES
satellites, deep-space probes and
university cubesats.

The idea at SatDump's centre is that the
**recording** is the starting point. A
recording can be decoded today, next
year, on another computer, with better
settings — so the hobby shares recordings
the way it shares photographs, and
learners prove their setup on a known-good
file before an antenna enters the story.

So this guide's lab decoded one. The
recording is a **real pass**: NOAA 19 over
Argentina, received by an amateur station
in **December 2018** and kept ever since
as the test fixture of another open-source
project, which is how its satellite, date
and start time are known exactly. The lab
ran the genuine **SatDump 1.2.2** on it
and got the picture — South America from
orbit, the Andes down one side, one band
of honest static where the signal faded —
then checked the picture the way this
series checks everything: by arithmetic.
APT sends exactly two lines per second;
the recording runs 822 seconds; the
picture holds 1,643 lines. It decoded the
same file three times, watched knowledge
switch products on (a timestamp plus the
orbital data SatDump downloads by itself
unlocked the projected thermal product),
and counted what the program ships from
its own files rather than its reputation.

What the lab could not do, it did not
fake. It has no radio and no antenna, so
nothing was received live and the
graphical program was never opened;
reception, live mode and the other 183
pipelines are taught from the pipelines'
own definitions and the project's
documentation, and labelled as such
wherever they appear. `criteria.md` keeps
the full ledger of what was run and what
was only read.

## What this guide covers

- [**What SatDump is**](what-satdump-is.md) —
  recording in, products out, for a whole
  sky of satellites — and why the recording
  being the starting point matters
- [**The moving parts**](the-moving-parts.md) —
  the two programs, pipelines as recipes,
  modules and plugins, products, and the
  orbital data file that appears by itself
- [**Installing SatDump**](installing-satdump.md) —
  the official release, the missing
  checksum file stated plainly, and the
  version lines that prove it runs
- [**Recordings first — files in**](recordings-first.md) —
  baseband, halfway stages and audio: the
  input levels, and why a recording is a
  file plus its facts
- [**The pipeline catalogue**](the-pipeline-catalogue.md) —
  184 pipelines in 71 files, counted in
  the lab: the weather fleets, the long
  tail, and one honest absence
- [**Your first decode**](your-first-decode.md) —
  a real 2018 NOAA 19 pass decoded end to
  end, its provenance stated exactly, and
  the picture checked by arithmetic
- [**Reading the pictures**](reading-the-pictures.md) —
  raw strips, channels, equalised versions,
  the composites that aren't there, and
  the data files that make a folder a
  dataset
- [**Projections, timestamps and orbital data**](projections-and-orbital-data.md) —
  what a start time and 15,900 downloaded
  orbits unlock, and what quietly refuses
  without them
- [**Beyond NOAA — other satellites**](beyond-noaa.md) —
  Meteor LRPT, the HRPT step up, the
  geostationary bargain, and the long
  tail — a labelled map, not a lab report
- [**Live mode and the graphical interface**](live-mode-and-the-gui.md) —
  the radio-driven mode and the windowed
  program, from the project's
  documentation, flagged as unrun here
- [**Recipes**](recipes.md) — decode a
  found recording, rerun it with its facts,
  enter from baseband, rebuild products,
  and keep a pass diary that future
  decoders will thank you for
- [**The neighbours**](the-neighbours.md) —
  the radios, the recorder programs, the
  other decoders (including the one whose
  fixture chapter 6 borrowed), and the
  presentation layer
- [**Limits**](limits.md) — no reception
  without a radio, products capped by the
  recording's facts, pipelines that are
  not promises, and honest verification
  edges
- [**Troubleshooting**](troubleshooting.md) —
  the config file that wasn't found, the
  plugin failures that don't matter, the
  garbage that means a wrong level or
  rate, and the missing products the log
  explains
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Receiving itself: antennas, amplifiers,
tracking mounts and the geometry of
passes belong to the radio side of the
fence, and to this series' radio guides.
Building receiver chains from components
is likewise another guide's craft.
Transmitting is out entirely — SatDump
only listens, and this guide only teaches
listening. And the 183 pipelines the lab
did not run get maps, not lab reports;
the one pipeline verified end to end here
is NOAA APT.

## How to use this guide

Read chapters 1 and 2 first — the
recording-first model and the five moving
parts turn every later confusion into a
named problem. Chapter 4's input levels
decide whether a decode works at all, so
don't skip it for chapter 6's picture.
Chapter 6 is the centre: follow it with
the same recording (its hash is given, so
you can be sure you have the same file)
and your setup is proven. Chapter 8 is
the one to read twice — the layered way
knowledge switches products on is the key
to every SatDump run you will ever debug.
The lab's transcripts live in
`satdump-lab/transcripts/`; its measuring
script is `satdump-lab/check-images.py`,
and a downscaled look at the decoded
picture is `satdump-lab/apt-channel-a-preview.png`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [RTL-SDR for Mere Mortals](https://paulsullivan33-dev.github.io/rtl-sdr-for-mere-mortals/)
- [GNU Radio for Mere Mortals](https://paulsullivan33-dev.github.io/gnu-radio-for-mere-mortals/)
- [Ham Radio for Mere Mortals](https://paulsullivan33-dev.github.io/ham-radio-for-mere-mortals/)
- [Raspberry Pi for Mere Mortals](https://paulsullivan33-dev.github.io/raspberry-pi-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/satdump-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/satdump-for-mere-mortals/blob/main/LICENSE-CODE).
