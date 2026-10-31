# Limits

What SatDump cannot do, stated as plainly as what it can.

**It cannot receive.** Without a radio and an antenna there is no signal, and without a signal — or someone else's recording of one — there is nothing to process. Every miracle in this guide happened downstream of a receiver that already existed. The program's live mode narrows the gap (it can drive the radio itself) but does not close it: the physics of a weak signal from 850 km up, on its way through your roof, is entirely your side of the bargain.

**A recording's facts cap its products.** Chapter 8's lesson, generalised: no timestamp, no map; two channels, no five-channel composites; a dropout in the recording is a hole in the picture forever. SatDump will not invent the missing pieces, and its refusal to try is a feature — but it means the ceiling of any decode was set at the moment of reception, possibly years before you run the program.

**Not every pipeline is a promise.** 184 pipelines include research-grade, single-mission and barely-tested entries alongside the polished weather fleet. Some transmissions need dishes and tracking mounts; some satellites in the catalogue have gone silent since their pipeline was written; the catalogue records the format, not the satellite's current health. Budget your enthusiasm by the frequency list and the satellite's status, not by the pipeline's existence.

**Verification has edges the lab hit honestly.** The 1.2.2 release publishes no checksum file, so a download cannot be verified against the project (chapter 3). And this guide verified one pipeline end to end — NOAA APT, on audio — plus the catalogue by reading it. The other 183 pipelines are described from their own definitions and the project's documentation, not from lab decodes; treat their chapters as maps, as chapter 9 labels itself.

**It is a heavy program doing heavy work.** A minute of computing for fourteen minutes of audio, on a small machine, for the *simplest* pipeline in the catalogue; high-rate digital pipelines move gigabytes. On modest hardware, decoding is a batch job measured in minutes to hours, not a button you press idly.

**Pictures are data, with data's responsibilities.** A decoded weather image is public information broadcast for the public — but the habit SatDump teaches, treating recordings as evidence with a provenance, cuts both ways. Label what you share with when and where it was received and by whom, as this guide labelled its 2018 fixture. An unlabelled satellite picture, passed around, becomes misinformation with good production values.
