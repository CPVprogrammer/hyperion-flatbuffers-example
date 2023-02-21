# Google flatbuffers example
This is a little example of Google flatbuffers with python3 and hyperion

## Documentation
Google flatbuffers:
- https://github.com/google/flatbuffers
- https://google.github.io/flatbuffers/flatbuffers_guide_tutorial.html

Hyperion docs:
- https://docs.hyperion-project.org/
- https://github.com/hyperion-project/hyperion.docs

## Requirements
Google flatbuffers (flatc):
- https://github.com/google/flatbuffers/releases

Hyperion ambilight project:
- https://github.com/hyperion-project/hyperion.ng

Hyperion flatbuffers schemas (*.fbs):
- https://github.com/hyperion-project/hyperion.ng/tree/master/libsrc/flatbufserver

python 3:
- https://www.python.org/

python Colour:
- https://github.com/vaab/colour
- `pip install colour`

python Pillow:
- https://github.com/python-pillow/Pillow
- `pip install pillow`

## Execution 
Execute the program and select an option of the menu:
- `python3 flatbuffers-hyperion.py`

If hyperion is not running you will get an error message.

## Results
There are a few lines in hyperion local website log with the code:
`[FLATBUFSERVER]`
and 2 files were created in the program folder:
- flatbuffers_send.bin
- flatbuffers_recv.bin

To transform those .bin into .json execute this:
- `flatc --json --raw-binary hyperion_request.fbs -- flatbuffers_send.bin`
- `flatc --json --raw-binary hyperion_reply.fbs -- flatbuffers_recv.bin`

## Other projects:
Google flatbuffers with Kodi and Hyperion:
- https://github.com/CPVprogrammer/kodi-hyperion-flatbuffers

Google protobuf with Kodi and Hyperion:
- https://github.com/CPVprogrammer/kodi-hyperion-protobuf
