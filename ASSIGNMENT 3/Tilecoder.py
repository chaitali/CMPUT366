numTilings = 4
numTiles = 4 * 9 * 9

tile_width = 0.2125
tile_height = 0.0175
    
def tilecode(in1, in2, tileIndices):
    # write your tilecoder here (5 lines or so)
    
    for i in range(numTilings):
        p = ( (in1 + 1.2) + (i * tile_width) / numTilings) / tile_width
        v = ( (in2 + 0.07) + (i * tile_height)/ numTilings)/ tile_height
        tile_num = int(p) + (int(v) * 9)
        tileIndices[i] = i * 81 + tile_num     
    
    
def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    #print('Tile indices for input (', in1, ',', in2,') are : ', tileIndices)

if __name__ == '__main__':
    printTileCoderIndices(-1.2, -0.07)
    printTileCoderIndices(-1.2, 0.07)    
    printTileCoderIndices(0.5, -0.07)    
    printTileCoderIndices(0.5, 0.07)
    printTileCoderIndices(-0.35, 0.0)
    printTileCoderIndices(0.0, 0.0)
    