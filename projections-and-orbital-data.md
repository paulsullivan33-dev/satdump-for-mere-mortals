# Projections, Timestamps and Orbital Data

A decoded APT strip is a picture of the Earth taken along a line — the satellite's path — but it doesn't know where that line lies, how the ground curved away at the edges, or which way is north. **Projection** is the step that answers those questions: warping the strip onto a map, so coastlines land where an atlas says they should, and the picture can be drawn *on* a map, with borders and place markers overlaid. It needs three facts: which satellite, **when the recording started**, and where the satellite was at that moment. The first two you supply; the third comes from orbital data.

**The TLE file.** SatDump keeps its orbital data in `~/.config/satdump/satdump_tles.txt` — two-line elements for everything tracked, refreshed automatically. The lab's copy appeared by itself at first launch, downloaded by the program through the machine's ordinary internet connection: 2.4 megabytes, and the decode log reports **"15900 TLEs loaded!"** (transcript `t05`). Nobody configures this, and on a machine with no internet it would simply grow stale — orbits drift slowly, so a weeks-old file still projects well; a years-old one puts the satellite in the wrong place and the map lands in the ocean. If your projections are subtly wrong rather than absent, a stale TLE file is the first suspect.

**The same decode, with the facts.** The lab ran its recording a second time, adding what chapter 6's provenance research had established:

```
satdump noaa_apt audio_wav test_11025hz.wav out2/ \
    --satellite_number 19 --start_timestamp 1545511181
```

(`1545511181` is 2018-12-22 20:39:41 UTC, the pass's documented start.) Two things changed, and one important thing didn't. The base pictures came out **byte-for-byte identical** — timestamp knowledge doesn't touch the decode itself. But the folder gained a product the first run refused: `avhrr_3_rgb_10.8um_Thermal_IR.png` and its `_corrected` twin, the thermal channel rendered as a proper projected product, now that "this composite requires projection info" could be satisfied. Products that need still more — map overlays proper, with the satellite's ground track computed across the whole pass — belong to the same mechanism and appear when the pipeline's requirements are met.

The lesson generalises beyond APT. **SatDump's outputs are layered by knowledge.** Signal alone gives you the strip. Signal plus channels gives you the calibrated pictures. Signal plus *time* plus *orbits* gives you geography. When a product you expected is missing, the question is never "why did it fail" but "which fact didn't the job have" — the log almost always names it, as it did here three times in the first run. And the corollary for your own receiving: the single most valuable habit is naming your recordings with their start times, in the formats SatDump reads automatically, because a recording whose time is lost can never be fully projected afterwards. The 2018 recording survived with its facts intact because another project's test script wrote them down — be that person for your own files.
