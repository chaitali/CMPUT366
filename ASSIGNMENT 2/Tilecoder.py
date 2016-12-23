numTilings = 8
    
def tilecode(in1, in2, tileIndices):
    # write your tilecoder here (5 lines or so)
    for index in range(numTilings):
        x = (in1 + index*0.6/numTilings)/0.6
        y = (in2 + index*0.6/numTilings)/0.6
        tile_num = int(x) + int(y)*11
        tileIndices[index] = index*(pow(11,2)) + tile_num    
    
    
def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    #print('Tile indices for input (', in1, ',', in2,') are : ', tileIndices)

#printTileCoderIndices(0.1, 0.1)
#printTileCoderIndices(4.0, 2.0)
#printTileCoderIndices(5.99, 5.99)
#printTileCoderIndices(4.0, 2.1)
    
