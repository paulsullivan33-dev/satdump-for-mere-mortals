# Your First Decode

This chapter runs one complete decode, end to end, on a recording whose origin can be stated exactly. By the end you will have a real weather picture, taken from orbit, and you will know precisely which claims about it are earned.

**The recording.** The file is `test_11025hz.wav`, kept in the public code repository of **noaa-apt**, another open-source APT decoder, as the fixture for its own automated tests. Its sibling file in that repository is named `argentina.wav`; the project's test script decodes this recording as a **NOAA 19** pass beginning **2018-12-22 at 20:39:41 UTC**. In numbers the lab verified from the file itself: mono audio, 16-bit samples, 11,025 samples per second, 9,067,017 samples — **822 seconds, thirteen minutes and forty-two seconds**, a full satellite pass, horizon to horizon. The lab's copy hashed to `50160851becd599796c0603a67c4d6b865cd70a096dca8ae7807dc3d3bd78691` (SHA-256), so any reader can confirm they have the same recording. It is a genuine reception — real radio noise, real dropouts, a real coastline — made by an amateur receiver in Argentina in December 2018. It did not come from this guide's lab, and nothing in this chapter pretends otherwise.

**The command.** APT audio enters at the `audio_wav` level (chapter 4), so the whole job is:

```
satdump noaa_apt audio_wav test_11025hz.wav out/
```

Run it and the program works for about a minute — 66 seconds on the lab's small shared machine, almost all of it drawing pictures after the decode itself finished in the first seconds. The log (kept in full as transcript `t02`) shows the shape of the work: the announcement and plugin loading from chapter 2; the demodulator taking the audio apart; the decoder finding the picture's rhythm — APT sends its lines at exactly two per second, with a synchronisation pattern at the start of each, and the decoder's first job is locking onto it; then the products, saved one by one.

**What comes out.** The output folder holds twelve files; chapter 7 reads them properly. The headline ones:

- `APT-A.png` and `APT-B.png` — the two picture channels APT carries, side by side in the broadcast, separated here into two images, each **909 pixels wide and 1,643 lines tall**.
- `raw_sync.png` — the whole received strip as broadcast, both channels and their calibration wedges together, **2,080 pixels wide** — the width is the APT format's own number, and meeting it exactly is a first sign the decode is honest.
- `product.cbor` and `dataset.json` — the data form of the products and their label, for programs that come later.

**Checking the picture without believing it.** A decode program that failed would still write files, so check the arithmetic the format guarantees. APT sends exactly 2 lines per second; the recording runs 822.4 seconds; the pictures should hold about 1,645 lines. They hold **1,643** — the two missing lines are the partial seconds at the recording's start and end, exactly as expected (the lab's measuring script and its full output are `satdump-lab/check-images.py` and transcript `t04`). The pixel values are 16-bit and spread widely (channel A runs from near 0 to the full 65,535, with the bulk of the picture between its 1st and 99th percentiles at 177 and 42,899) — a real image with shadows and bright cloud tops, not a blank frame or a saturated one. And the lab *looked*: a downscaled copy is kept at `satdump-lab/apt-channel-a-preview.png`. It shows South America from orbit — the Andes as a pale spine down the right side, ocean to the left, weather systems over Argentina, and one horizontal band of pure static partway down where the signal faded for a few seconds, as real passes do. (APT pictures come out as the satellite saw them, north at whichever end the satellite was travelling; turning the picture "upright" is a job for the projection step in chapter 8, not something wrong with the decode.)

Deterministic, too: the lab decoded the same file three times with different options, and the base picture came out **byte-for-byte identical** (same MD5 hash) every time. What changed with the options is the subject of chapter 8.
