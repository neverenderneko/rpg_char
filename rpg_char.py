full_dot = '●'
empty_dot = '○'

def create_character(character_name, STR, INT, CHA):
    # Tests against character_name
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif character_name == '':
        return 'The character should have a name'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif ' ' in character_name:
        return 'The character name should not contain spaces'
    # Tests against stats STR, INT, CHA
    elif not isinstance(STR, int) or not isinstance(INT, int) or not isinstance(CHA, int):
        return 'All stats should be integers'
    elif STR < 1 or INT < 1 or CHA < 1:
        return 'All stats should be no less than 1'
    elif STR > 4 or INT > 4 or CHA > 4:
        return 'All stats should be no more than 4'
    elif STR + INT + CHA != 7:
        return 'The character should start with 7 points'
    # Return below stat block if meets all criteria
    else:
        return f'''{character_name}
STR {full_dot * STR + empty_dot * (10 - STR)}
INT {full_dot * INT + empty_dot * (10 - INT)}
CHA {full_dot * CHA + empty_dot * (10 - CHA)}'''

print(create_character('ren', 4, 2, 1))
