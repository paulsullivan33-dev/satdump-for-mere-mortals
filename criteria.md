# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's one fixture is a published test recording from
   another open-source project, identified exactly.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: it cannot receive without a radio, a recording's
   facts cap its products, the catalogue's breadth is not a set
   of promises, the release publishes no checksum file, and
   only one of 184 pipelines was verified end to end here.
8. **The ethics rule is in the text, early.** Chapter 1 states
   the line plainly — these broadcasts are public by design;
   receive what is broadcast openly, never transmit on
   satellite frequencies without a licence, and never present
   a decoded picture as something it is not, which is why the
   guide states its one picture's provenance exactly.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a small shared Linux sandbox with no radio
receiver, no antenna and no usable display. SatDump **1.2.2**
(the project's current stable release, 29 November 2024) was
run unmodified: the official `satdump_1.2.2_ubuntu_24.04_amd64.deb`
was extracted, not installed, because the machine is shared —
the package's own two private libraries needed an
`LD_LIBRARY_PATH` entry, one further library (`libnng1`, Ubuntu
package 1.7.2-1build2) was extracted the same way, and two
temporary symlinks in `/usr/share` and `/usr/lib` pointed the
program at its unpacked files; the symlinks were removed when
the lab was deleted. **The 1.2.2 release publishes no checksum
file**, so the download could not be verified against the
project; the lab's own SHA-256 of the `.deb`
(`68672f0d…cf3221`) is recorded in chapter 3 and transcript
`t00` so readers can compare bytes. All transcripts live in
`satdump-lab/transcripts/`; the measuring script is
`satdump-lab/check-images.py`.

The one decoded recording is a real satellite reception with a
stated provenance: `test_11025hz.wav`, the integration-test
fixture of the open-source **noaa-apt** project (GitHub
repository `martinber/noaa-apt`, file `test/test_11025hz.wav`;
same recording as its `docs/examples/argentina.wav`; the
project's test script decodes it as **NOAA 19, 2018-12-22
20:39:41 UTC**). Verified from the file in the lab: mono,
11,025 Hz, 16-bit, 9,067,017 samples = 822.4 s; SHA-256
`50160851…d78691`. The lab did not receive this pass and never
claims to have; it decoded a recording, which is the program's
designed centre of use.

Run for real, with transcripts as evidence:

- Version and startup (the log's "Starting SatDump v1.2.2"),
  config and plugin loading, including the SDR plugins that
  fail on a radio-less machine and are skipped (t00, t02).
- The pipeline catalogue counted from the installed files:
  71 JSON files, 184 pipeline ids, with the NOAA, Meteor-M,
  GOES and Others families enumerated (t01). The pipeline
  files are not strict JSON (a literal newline sits inside one
  description string), so the count was taken by a tolerant
  scan of top-level keys — stated here so the number can be
  reproduced.
- A complete `noaa_apt` decode at the `audio_wav` input level
  of the 822-second recording: about 66 s wall time, full log
  kept (t02), twelve product files.
- Product verification without trusting the program: channel
  images 909 × 1,643 px, raw strip 2,080 × 1,643 px, against
  APT's guarantees (2 lines/s × 822.4 s ≈ 1,645 lines; 909 px
  per channel) — the two missing lines are the recording's
  partial end-seconds (t04, `check-images.py`). A downscaled
  normalisation of channel A was also *looked at* by the lab
  (`satdump-lab/apt-channel-a-preview.png`): South America,
  the Andes, weather systems, one static dropout band.
- Repeatability and knowledge layering (t03, t05): the same
  file decoded three times; base products byte-identical
  (matching MD5). Without a timestamp, three composites were
  refused with "This composite requires projection info" and a
  row of channel-starved composites were skipped; with
  `--satellite_number 19 --start_timestamp 1545511181` the
  projected thermal-IR product appeared.
- Orbital data: SatDump created `~/.config/satdump/satdump_tles.txt`
  itself at first launch (2,470,063 bytes; the log reports
  15,900 TLEs loaded) over the machine's ordinary HTTPS route
  (t05). An intermediate lab run used a timestamp one hour off
  (miscomputed by hand) and still projected — caught and
  corrected by recomputing the timestamp; the episode is kept
  in chapter 14 rather than tidied away.

Documented only — described from the project's documentation
and the pipeline files, not run, and the text does not claim
otherwise:

- Live reception and live mode, and the graphical program
  `satdump-ui` in any form: no radio and no display existed.
- The baseband input route of the same APT pipeline (the audio
  route was the verified door) and every other pipeline —
  enumerated and characterised from their own JSON definitions
  (frequencies, input levels, module chains), not decoded.
- Windows, macOS and Android installs, and the nightly builds.
- ISS SSTV: searched for in this build's pipeline files and
  libraries and **not found** — reported as an absence in
  chapter 5 rather than assumed from the project's reputation.

Fixtures are deliberately generic apart from the identified
test recording: no names, organisations or real events of the
author's appear anywhere in this guide.
