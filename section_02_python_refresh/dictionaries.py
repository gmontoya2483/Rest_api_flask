
## dictinaries: key:value set and they represents things

my_set = {1, 2, 4}
my_dict ={ 'name':'jose', 'age': 90, 'grades': [13, 45, 66, 90] }
another_dict = {1: 15, 2: 75,3: 150}


# Examples

lottery_player = {
    'name': 'Rodolf',
    'numbers': (13, 45, 66, 23, 22)
}

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

another_dict_in_dict = {
    'key': {
        'name': 'Jose'
    }
}



print (sum(lottery_player['numbers']))
lottery_player['name'] = 'John'
print (lottery_player['name'])
print (lottery_player)


