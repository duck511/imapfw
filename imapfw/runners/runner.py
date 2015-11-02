# The MIT License (MIT)
#
# Copyright (c) 2015, Nicolas Sebrecht & contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from imapfw import runtime

from imapfw.constants import WRK

# Annotations.
from imapfw.edmp import Emitter


class TwoSidesRunner(object):
    def __init__(self, referent: Emitter, left: Emitter, right: Emitter,
            engineName=None):

        self.referent = referent
        self.left = left
        self.rght = right
        self.engineName = engineName

        self.ui = runtime.ui

        self.workerName = None
        self.exitCode = -1 # Force the run to set a valid exit code.

    def debug(self, msg: str):
        runtime.ui.debugC(WRK, "%s: %s"% (self.workerName, msg))

    def setExitCode(self, exitCode):
        if exitCode > self.exitCode:
            self.exitCode = exitCode