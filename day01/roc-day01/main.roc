app [main] { pf: platform "https://github.com/roc-lang/basic-cli/releases/download/0.17.0/lZFLstMUCUvd5bjnnpYromZJXkQUrdhbva4xdBInicE.tar.br" }

import pf.Stdout
import pf.File

main =
    # Get input data
    fileName = "../input.txt"
    contents = File.readUtf8! fileName
    lines = Str.split contents "\n"

    # Split it into lines
    left = []
    right = []
    List.map lines splitInput

splitInput = \line->
    Str.split line "   "
