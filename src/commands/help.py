def main(msg):
    #return('James was too lazy to print all the info here. So take a look at the github page\nhttps://github.com/gpanda70/Jenkins')
    x=['-wiki {arg}',
       '-img {arg}',
       '-gif {arg}',
       '-gif -random {arg}',
       '-ask {arg}',
       '-help {arg}']
    y = ['returns the summary Wikipedia article of your arg.',
         'returns the first google image search result of your arg.',
         'returns a gif from giphy',
         'returns random gif from giphy.',
         'returns an answer for your question using wolframalpha.',
         'returns this help menu']
    h_menu = ('Source Code on https://github.com/gpanda70/Jenkins\n' + '-'*77)
    for i,j in zip(x,y):
        h_menu += ('\n{:<20} {:>12}'.format(i,j))
    return(h_menu)
main('')
