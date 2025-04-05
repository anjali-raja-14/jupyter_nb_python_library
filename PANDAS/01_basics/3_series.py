import pandas as pd
v=pd.Series(12,index=[1,2,3,4,])
print(v)


""""
1    12
2    12
3    12
4    12
dtype: int64
"""

import pandas as pd
v1=pd.Series(12,index=[1,2,3,4,])
v2=pd.Series(12,index=[1,2,])
print(v1+v2)

"""
1    24.0
2    24.0
3     NaN(not a no.)
4     NaN
dtype: float64"""