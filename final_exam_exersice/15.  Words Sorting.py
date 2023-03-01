def words_sorting(*args):
    result = ''
    my_dict = {}
    total_counter = 0
    for word in args:
        counter = 0
        for ch in word:
            counter += ord(ch)
        my_dict[word] = counter
        total_counter += counter

    if total_counter % 2 == 0:
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
    else:
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: -x[1]))

    for k, v in sorted_dict.items():
        result += f"{k} - {v}" + '\n'

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

