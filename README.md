
# pipevcr

Record and play back pipes. Similar to what `script` does with the terminal but for pipes.

This can be used for debugging or testing where timing matters.

## Installation

```
pip3 install --user pipevcr

# or if you have pipx
pipx install pipevcr
```

## Usage

```
usage: pipevcr [-h] [-r] [-s SPEED] [-m MAX_PAUSE] FILE

pipevcr - the linux pipe recorder

positional arguments:
  FILE                  data file

options:
  -h, --help            show this help message and exit
  -r, --record          record pipe
  -s SPEED, --speed SPEED
                        playback speed, <1 to slow down, >1 to speed up
  -m MAX_PAUSE, --max-pause MAX_PAUSE
                        max pause time between outputs in seconds
```

## Record

You record a pipe with `-r`, e.g.:

```
(echo wait 1; sleep 1; echo wait 2; sleep 2; echo end) | pipevcr -r test.vcr
```

## Playback

And play it back with:

```
pipevcr test.vcr
```

## Faster

To speed it up (2=double):

```
pipevcr -s 2 test.vcr
```

## Slower

To slow it down (.5=half):

```
pipevcr -s .5 test.vcr
```

You can also set the maximum pause time separately:

```
pipevcr -m 1 test.vcr
```
