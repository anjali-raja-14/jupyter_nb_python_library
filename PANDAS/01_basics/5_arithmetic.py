import pandas as pd
var=pd.DataFrame({"A":[1,2,9,4],"B":[6,5,4,7]})
var["C"]=var["A"]+var["B"]
# print("Addition\n",var)

"""
Addition

   A  B   C
0  1  6   7
1  2  5   7
2  3  4   7
3  4  7  11

"""
var["python "]= var["C"]>=10
print(var)
"""
A  B   C  python 
0  1  6   7    False
1  2  5   7    False
2  9  4  13     True
3  4  7  11     True

"""