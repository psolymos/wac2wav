# WAC to WAV Converter

WAC is a compressed audio format developed by Wildlife Acoustics, Inc. and used in older recording units.

- [WAC to WAV Converter](#wac-to-wav-converter)
  - [Current release](#current-release)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Original release](#original-release)
  - [License](#license)

## Current release

This version of the WAC-to-WAV command line converter
is a slightly more user friendly version of the
original program (see original release notes below).

## Installation

Run the makefile (assuming that compilers are available).
Make sure that the file is added to the path.

## Usage

```
wac2wav <input_file_name> <output_file_name>
```

## Original release

The original source files can be found on [SourceForge](https://sourceforge.net/projects/wac2wavcmd/files/). The SourceForge version is copied into the [`original-release`](original-release) folder.

> Wildlife Acoustics, Inc. is pleased to offer source code for decoding our
> proprietary WAC audio files produced by some of our bioacoustics recorders
> including our SM1, SM2, SM2+, SM2BAT192x2, SM2BAT384, SM2BAT+, SM3, SM3BAT,
> EM3, and EM3+.
>
> Our objective is to give our customers and third-party developers the ability
> to decode WAC files and create value-added solutions.  Details about the file
> format can be found in the comments in wac2wavcmd.c.  A Makefile is provided
> for convenience and should work on most Unix systems including Linux.

## License

The original and the current versions are released under the [GPLv3](http://www.gnu.org/licenses/gpl-3.0.html) license.
