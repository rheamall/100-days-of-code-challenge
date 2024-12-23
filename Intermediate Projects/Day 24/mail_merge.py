with open('friend_names.txt') as names:
    for name in names:
        with open('template.txt') as my_template:
            with open(f'hi_{name.strip()}.txt', 'w') as file:
                content = my_template.read().replace('[name],', f'{name.strip()},')
                file.write(content)
