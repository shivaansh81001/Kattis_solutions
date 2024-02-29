'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/kmp.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])
    #print(pi)
    return pi

def string_find(s, pat):
    pi = partial(pat)
    #print(pi)
    g = 0
    for i in range(len(s)):
        #print(g)
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            return True

    return False
    
def main():
    l=int(input())
    s1=input().split()
    s2=input().split()
    
    s1=list(map(int,s1))
    s2=list(map(int,s2))
    
    s1=sorted(s1)
    s2=sorted(s2)
    #print(s1,s2)
    
    s1_rel=[]
    s2_rel=[]
    for i in range(l):
        s1_rel.append((s1[(i+1)%l]-s1[i]+360000)%360000)
        s2_rel.append((s2[(i+1)%l]-s2[i]+360000)%360000)
    '''
    
    s1_rel=sorted(s1_rel)
    s2_rel=sorted(s2_rel)
    #print(s1_rel,s2_rel)
    #print(s1_rel,s2_rel)
    #print(partial(s1_rel))
    #print(partial(s2_rel))
    #print(match(s1_rel,s2_rel))
    #print(string_find(s1_rel*2,s2_rel))'''
    
    print('possible' if string_find(s1_rel+s1_rel,s2_rel) else 'impossible')
    
    
main()