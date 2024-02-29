
'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -NONE

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''

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