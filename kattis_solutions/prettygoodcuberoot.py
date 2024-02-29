
'''
  
  -https://socratic.org/questions/how-do-you-use-newton-s-method-to-approximate-the-value-of-cube-root

'''


def check(least, most,number):
    
    half=(most+least)//2
    # print(half)
    cube=(half)**3
    cube2=(half+1)**3
    if cube==number:
        print(str(half))
        return 0
        # exit()
    
    # print('+',cube)
    # print('-',cube2)
    
    # print('-',half)
    # print('+',half+1) 
    
    if number>cube and number <cube2 :
        
        if abs(cube-number)>abs(cube2-number):
            print(str(int(half)+1))
            return 0
            # exit()
        elif abs(cube-number)<abs(cube2-number):
            print(str(int(half)))
            return 0
            # exit()
        #     # print('hi')
        #     print(str(half+1))
        #     return
        # print(((cube-number),(cube2-number)))
        # if abs(cube-number)<2:
            
        # print(str(round(half+((number-cube))/(3*(half**2)))))
       
        
        # elif cube2-number==0:
        #     # print('hi')
        #     print(str(half+1))
        #     return
    
        # print('hello')
        #     print(str(round((half+1)+((cube2-number))/(3*((half+1)**2)))))
        #     return
        
    
    if cube>number:
        check(least, half, number)
        
    
    
    elif cube<=number:
        check(half,most,number)
    
    

def main():
    
    while(1):
        try:
            inp=input()
        except:
            break
        # inp=input()
        # inp=input()
        len_of_cbrt=0
        # inp=input()
        l=len(inp)
        if l%3==0:
            len_of_cbrt+=(l//3)
        else:
            len_of_cbrt+=((l//3)+1)
        
        least=int('1'+(len_of_cbrt-1)*'0')
        
        
        most=int(len_of_cbrt*'9')
        
        # print(least,most)
        check(least,most,int(inp))
        
        # print('least',least_cube)
    

        
        most=int(len_of_cbrt*'9')
        
        # print(least,most)
        # check(least,most,int(inp))
        # print(x)
        # print('least',least_cube)
    
main()
