# Troubleshooting

The failures this guide's lab actually met, and the ones the log taught it to read. SatDump logs generously, in plain words, with timestamps — nearly every answer below is "the log already told you."

**"Couldn't load config file! Was trying: /usr/share/satdump/satdump_cfg.json"**
The program cannot find its own installation. On a normal install this means the install is broken or partial; on a hand-unpacked copy (the lab's situation) it means the program is looking in the system places and its files live elsewhere. The lesson isn't the lab's workaround — it's that SatDump expects its `pipelines`, `resources` and config to live in the standard paths for your platform, so install it the standard way and this message never appears. A close sibling complains about the plugins folder in the same style.

**Plugins fail to load, in a long list at startup**
Mostly harmless. Each SDR plugin needs its radio's own libraries; a machine without an Airspy will watch the Airspy plugin fail with `cannot open shared object file` and should carry on. Worry only if the plugin that fails is the one your pipeline needs — the satellite-support plugins load the same way, and those matter.

**The decode runs, but the picture is static, torn, or half the expected length**
Wrong input level, wrong sample rate, or wrong file — in that order of likelihood. An APT job fed a baseband file at the `audio_wav` door (or the reverse) produces confident garbage. A baseband job with a guessed `--samplerate` produces nothing recognisable at all. Check the file's actual properties against your command before blaming the signal; chapter 6's arithmetic (lines ≈ 2 × seconds, widths 909/2080) separates "decoding happened" from "decoding worked."

**Products you expected are missing from the folder**
Read the log for `Skipping` and `requires projection info`. The first means the transmission never carried what the recipe needs (two-channel APT versus a three-channel composite) — permanent, and correct. The second means the job lacked a fact, usually the start timestamp — fixable: rerun with `--start_timestamp` set, exactly as chapter 8 does, and keep both folders.

**The projected map is in the wrong place**
Stale orbital data or a wrong timestamp. Check the age of `~/.config/satdump/satdump_tles.txt` (SatDump refreshes it when it can reach the internet), and check your timestamp arithmetic in UTC — an hour's error in the start time moves the projected satellite hundreds of kilometres along its track, which is far enough to look plausible and be wrong. The lab made precisely this slip in an intermediate run and caught it by recomputing the timestamp rather than trusting memory.

**Everything is slow**
That's the workload being honest. High-rate pipelines move gigabytes and the image products dominate the clock (in the lab's APT run, a minute of wall time held a few seconds of decode and the rest product rendering). Decode overnight, keep the `.cbor`, and re-render products instead of re-decoding.
