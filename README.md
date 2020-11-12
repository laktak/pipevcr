
# pipevcr

Record and play back pipes. Similar to what `script` does with the terminal but for pipes.

This can be used for debugging or testing where timing matters.

## Usage

```
usage: pipevcr.py [-h] [-r] [-m MAX_PAUSE] FILE

pipevcr - the linux pipe recorder

positional arguments:
  FILE                  data file

optional arguments:
  -h, --help            show this help message and exit
  -r, --record          record pipe
  -m MAX_PAUSE, --max-pause MAX_PAUSE
                        max pause time between outputs in ms
```

You record a pipe with `-r`, e.g.:

```
(echo start; sleep 1; echo continue; sleep 1; echo end) | pipevcr -r test.vcr
```

And play it back with:

```
pipevcr test.vcr
```

If you want to speed it up you may set the max wait time for pauses:

```
pipevcr -m 300 test.vcr
```
