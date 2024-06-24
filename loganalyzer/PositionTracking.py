import sys
from loganalyzer.Parser import *
from loganalyzer.Game import *
from loganalyzer.Analyzer import *

parser = Parser(sys.argv[1])

game = Game(parser)
analyzer = Analyzer(game)
analyzer.analyze()

analyzer.draw_heatmap()
analyzer.draw_heatmap(right_team=True) 