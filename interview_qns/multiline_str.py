## Best way to handle multi line strings. the second and third approach lag in indentation"
multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age") 
print(multiStr)

multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)

multiStr = """select * from multi_row 
where row_id < 5"""
print(multiStr)
