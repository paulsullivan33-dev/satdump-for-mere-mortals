# Glossary

**APT (Automatic Picture Transmission)** — NOAA's analogue picture service on 137 MHz: two image channels sent as a varying audio tone, two lines per second. The oldest satellite picture format still flying, and the friendliest to receive.

**AVHRR** — The imaging instrument aboard NOAA and Metop polar satellites. It sees five channels; APT broadcasts two of them, HRPT all five.

**Baseband** — A recording of the raw radio signal itself, as samples, before any demodulation. Large, complete, and reprocessable forever — the negative from which all prints are made.

**CBOR** — A compact binary data format. SatDump's `product.cbor` stores a decode's underlying data so products can be rebuilt without re-decoding.

**Composite** — A picture made by combining channels — false-colour views, temperature renderings, merges. A composite is possible only if the transmission carried the channels it needs.

**Demodulation** — Turning a radio waveform into the data it carries. In APT's case, two stages of it: the receiver demodulates the FM broadcast into audio; SatDump demodulates the audio tone into brightness.

**HRPT** — The high-rate digital downlink (around 1.7 GHz) of the polar weather satellites: all channels, full resolution, and an antenna problem to match.

**Input level** — The stage of cookedness at which a recording enters a pipeline: `baseband`, halfway stages, or `audio_wav`. Matching the level to the file is the beginner's whole game.

**LRPT** — Meteor-M's digital picture service on 137 MHz: three channels, colour pictures, and digital's all-or-nothing manners.

**Pipeline** — SatDump's recipe for one transmission: input level, module chain, and products, stored as a JSON file. The installed program ships 184 of them in 71 files.

**Product** — Anything a pipeline writes: channel images, composites, projections, and the `dataset.json` / `product.cbor` data pair.

**Projection** — Warping a decoded strip onto a map using the satellite's position, which requires the recording's start time and current **TLEs**.

**Sample rate** — How many samples per second a baseband recording holds. A property of the file; a job told the wrong rate decodes nothing.

**SDR (software-defined radio)** — A radio whose tuning and demodulation are done by software — the class of receiver, from thirty-dollar USB sticks upward, that makes all of this possible.

**TLE (two-line elements)** — The standard compact description of an orbit, published for tracked objects and kept by SatDump in `satdump_tles.txt`, refreshed automatically.

**Telemetry wedges** — The staircase of grey calibration blocks sent beside every APT image, against which the picture's brightness is measured.
