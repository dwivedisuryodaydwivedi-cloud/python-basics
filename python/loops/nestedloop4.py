"""
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
        """
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(end= "  ")
    for k in range(1,i+1,1):
        print(k,end= " ")
    print()
    
"""
* * * * *
  * * * *
    * * *
      * *
        *
        """
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(end= "  ")
    for k in range(1,i+1,1):
        print("*",end= " ")
    print()
    
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print("*" ,end= " ")
    print()
    
"""
      * * * * * * * * * *
      * * * *     * * * *
      * * *         * * *
      * *             * *
      *                 *
      *                 *              
      * *             * *
      * * *         * * *
      * * * *     * * * * 
      * * * * * * * * * *
      
"""
for i in range(5,0,-1):
    # left upper 
    for j in range(1,i+1,1):
         print(j,end= " ")
    # middle space
    for k in range(5,i,-1):
        print("  ",end= "  ")
    # right upper
    for l in range(i,0,-1):
        print(l,end= " ")
        
    print()
    
for m in range(1,6,1):
    # left lower 
    for n in range(1,m+1,1):
         print(n,end= " ")
    # middle space     
    for o in range(5,m,-1):
        print("  ",end= "  ")
     # lower right    
    for p in range(m,0,-1):
        print(p,end= " ")
        
    print()