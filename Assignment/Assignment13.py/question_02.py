dict1 = {
    'Name':'Sanjay Patil',
    'Age': 55,
}

dict2 = {
    'Address':'Jalgaon',
    'occupation':'Business'
}

result = {**dict1, **dict2}
print(result)