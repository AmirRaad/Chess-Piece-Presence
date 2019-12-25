# The Bishop

The Bishop is a project that can help in playing chess, it's entirely open source, based on OpenCV and Python.

### Introduction

The Bishop uses computer vision to recognize where the chess pieces are on the board before deciding what move to make.

### Camera

Vision is done by using a Raspberry Pi camera module attached with an HDMI cable to a fixture directly above the chessboard.

The camera is controlled via Python OpenCV running on the Raspberry Pi. The raw image is converted to a 480x480px image by warping the perspective so the chessboard squares are equal size and the non-chessboard part of the image is cropped.

![]images\r1.png