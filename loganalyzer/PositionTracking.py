# if(filename[-3:]=='.gz'):
#     print('filename=',myargs+'/'+filename[:-7])
#     gunzip(myargs+'/*.gz')
#     parser = Parser(myargs+'/'+filename[:-7])
# else:    

print('file number:', ctr)

print('filename= ',myargs+'/'+filename[:-4])
parser = Parser(myargs+'/'+filename[:-4])

game = Game(parser)
analyzer = Analyzer(game, myargs+'/'+filename[:-4])
analyzer.analyze()

analyzer.draw_heatmap()
analyzer.draw_heatmap(right_team=True)