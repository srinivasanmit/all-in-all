namelist =[ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
output = ' '.join([name["name"] for name in namelist])
output = output.replace(output.split(' ')[-1], "& "+output.split(' ')[-1])
print output.replace(output.split(' ')[0], output.split(' ')[0] + ",")
