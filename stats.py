def get_book_text(filepath):

  with open(filepath) as f:
    contents = f.read()
    return contents

def num_words(text):
  list_of_words = text.split()
  return len(list_of_words)

def unique_chars(text):
  dict_count = {}

  for char in text:
    the_char = char.lower()
    if the_char not in dict_count:
      dict_count[the_char] = 1
      continue
    dict_count[the_char] += 1

  return dict_count

def sort_dict(char_dict):
  list_of_dicts = []
  for key in char_dict:
    a_dict = {}
    a_dict["char"] = key
    a_dict["num"] = char_dict[key]
    list_of_dicts.append(a_dict)


  list_of_dicts.sort(reverse=True, key=sort_on)
  return list_of_dicts

def sort_on(item):
  return item["num"]


