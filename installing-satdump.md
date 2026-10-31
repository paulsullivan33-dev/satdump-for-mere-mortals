# Installing SatDump

SatDump is free and open source, published by its project on GitHub. The current stable release at the time of writing is **1.2.2** (29 November 2024), with a rolling "nightly" build for people who want the newest work. This is a case where the project's own release page is the only address worth trusting: satellite software attracts repackaged copies, and the genuine article is easy to get.

**On Linux**, the release offers `.deb` packages matched to Ubuntu versions (the lab used `satdump_1.2.2_ubuntu_24.04_amd64.deb`), plus an AppImage in the nightly builds. Install the `.deb` the ordinary way, with your package manager, and dependencies are handled for you. One caution the lab can pass on: **the 1.2.2 release publishes no checksum file**, so the usual "verify the download against the publisher's hash" step cannot be done against the project. The lab recorded the hash of its own download so readers can compare notes:

```
68672f0d1bb76d5646d02ad2cbbeaa7549bed5ecedf4ee27d0d8467e72cf3221  satdump_1.2.2_ubuntu_24.04_amd64.deb
```

A matching hash proves you downloaded the same bytes the lab did; it cannot prove the bytes are the project's, which is what the project's missing checksum file would have done. Download from the project's release page, and treat any other source with suspicion.

**On Windows and macOS**, the release offers installers and portable archives, and there is an Android app. This guide's lab ran on Linux, so those routes are documented-only here — the program itself, its pipelines and its products are the same, and every procedure after this chapter was written against the command-line program all platforms share.

However you installed it, prove the program runs before going further. The command-line program, given a job, begins by announcing itself:

```
$ satdump noaa_apt audio_wav recording.wav out/
[...] (I) Starting SatDump v1.2.2
[...] (I) Loading config /usr/share/satdump/satdump_cfg.json
[...] (I) Loading plugins from /usr/lib/satdump/plugins
```

Your paths will differ by platform; the version line is the check. If the program cannot find its configuration or its pipelines folder, it says so in plain words and stops — that message, word for word, is the first entry in the troubleshooting chapter, because the lab met it before it met anything else (its copy was unpacked by hand rather than installed, and the program looked in the standard system places until it was pointed at them).

The graphical program, `satdump-ui`, is the same installation. Chapter 10 describes it from the project's documentation: the lab's machine had no display worth using and no radio, so it was never honestly opened here, and this guide does not pretend otherwise.
