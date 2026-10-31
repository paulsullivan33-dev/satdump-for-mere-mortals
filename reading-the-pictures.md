# Reading the Pictures

Twelve files from one decode is a lot until you sort them into their four kinds. This chapter is the field guide to a SatDump output folder, using the lab's APT decode as the specimen.

**The raw strip.** `raw_unsync.png` is the picture exactly as it fell out of the audio — lines stacked in arrival order, slanting or torn where the decoder hadn't yet found the rhythm. `raw_sync.png` is the same strip after line synchronisation: each line shifted so the synchronisation patterns align, which straightens the picture. Both are 2,080 pixels wide, the full APT line: **909 pixels of channel A image, the telemetry wedges** (the staircase of grey blocks along the edges — the satellite's own calibration scale, sent with every frame), **909 pixels of channel B**, and the minute markers between. Keeping the unsynchronised version is not clutter; when a decode goes wrong, comparing the two tells you whether the failure was synchronisation or signal.

**The channels.** APT broadcasts two of the AVHRR instrument's five channels — typically a visible-light channel by day and a thermal infrared channel always. SatDump writes them as `APT-A.png`, `APT-B.png`, and under their instrument names, `AVHRR-2.png` and `AVHRR-4.png` for this pass (same pictures; the APT pair and the numbered pair were byte-identical in size and content in the lab's run). The versions named `avhrr_3_APT_channel_A.png` and its `_corrected` sibling are the same data equalised — stretched so the calibration wedges span their proper range, which is the version a meteorologist would start from.

**The composites that aren't there.** The log of the lab's decode spends a cheerful paragraph *not* making pictures:

```
(D) Skipping AVHRR 221 False Color as it can't be made!
(D) Skipping AVHRR 3a21 False Color as it can't be made!
...
(E) This composite requires projection info
```

Both refusals are the program being correct. False-colour recipes combine three channels; APT only ever carries two, so any recipe needing channel 1, 3 or 5 is impossible *from this transmission* — the same recipe works fine on the five-channel HRPT downlink. And several products need to know where the picture belongs on the Earth, which a bare audio file doesn't say. Nothing failed; the folder simply holds everything the recording could honestly support, and the log enumerates the rest as a list of things a better recording — five channels, a known time — would unlock. Read your own logs this way: in SatDump, "skipping" is information, not error.

**The data files.** `dataset.json` is the label: which satellite family, what time (`"timestamp": -1.0` in the lab's first run — minus one is the program's way of saying *unknown*, and chapter 8 is about fixing exactly that). `product.cbor` is the pictures in data form — the calibrated numbers behind the PNGs, kept so that composites and projections can be rebuilt later without decoding the audio again. If you keep only one thing from a decode besides the pictures, keep this pair: they are what make the folder a dataset instead of a pile of images.
