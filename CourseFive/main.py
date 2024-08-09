import pandas as pd

# create two dataframes
data1 =  pd.DataFrame({
    'key':['A','B','C','D','E','F','G'],
    'value1':[1,2,3,4,5,6,7]
})

data2 =  pd.DataFrame({
    'key':['C','D','E','F','G','H'],
    'value1':[8,9,10,11,12,13]
})

print(data1)
print(data2)

# Inner join
print("-----Inner Join-----")
merge_inner_join = pd.merge(data1,data2, on='key', how='inner')
print(merge_inner_join)

# left join
print("-----Left Join-----")
merge_left_join = pd.merge(data1,data2, on='key', how='left')
print(merge_left_join)

# right join
print("-----Right Join-----")
merge_right_join = pd.merge(data1,data2, on='key', how='right')
print(merge_right_join)

# Left anti join 
print("-----Left Anti Join-----")
merge_left_join = pd.merge(data1,data2, on='key', how='left', indicator=True)
print(merge_left_join)
left_anti_join = merge_left_join[merge_left_join["_merge"] == 'left_only']
left_anti_join = left_anti_join.drop('_merge',axis=1)
print(left_anti_join)

# Right anti join 
print("-----Right Anti Join-----")
right_join =  pd.merge(data1,data2, on='key', how='right', indicator=True)
print(right_join)
anti_right_join = right_join[right_join['_merge'] == 'right_only']
anti_right_join =  anti_right_join.drop('_merge', axis=1)
print(anti_right_join)