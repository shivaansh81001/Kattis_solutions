

# MADE A RECURSIVE FUNCTION TO CHECK FOR EVERY LAYER 
def pyramid(blocks,blocks_in_layer):
    # BREAKS THE RECURSION IF THE LAYER REQUIRES MORE BLOCKS THAN WHAT WE ARE LEFT WITH
    if blocks_in_layer**2>blocks:
        return 0
    
    else:
        # ELSE RECALLS THE FUNCTION AGAIN SUBTRACTING THE BLOCKS REQUIRED BY PREVIOUS LAYER AND GOING DOWN THE LAYER TOP TO BOTTOM: AS ONLY ODD NUMBERS ARE 
        # APPLICABLE IT JUMPS THE BLOCKS REQUIRED BY 2
        return 1+pyramid(blocks-(blocks_in_layer**2), blocks_in_layer+2)

def main():
    blocks=int(input())
    blocks_in_layer=1
    answer=pyramid(blocks, blocks_in_layer)
    print(answer)

if __name__=='__main__':
    main()