# Write your sum_values function here:
def sum_values(my_dictionary):
  sum_val = 0
  for val in my_dictionary.values():
    sum_val += val
  return sum_val
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  key_sum = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      key_sum += my_dictionary[key]
  return key_sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  found_vals = []
  for keyval in my_dictionary.values():
    if keyval in my_dictionary:
      found_vals.append(keyval)
  return found_vals
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_key =  key
      largest_value = value
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_l = {}
  for word in words:
    word_l[word] = len(word)
  return word_l
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  dict_ = {}
  for word in words:
    if word not in dict_:
      dict_[word] = 0
    dict_[word] += 1
  return dict_
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Write your unique_values function here:
def unique_values(my_dictionary):
  lst = []
  for val in my_dictionary.values():
    if val not in lst:
      lst.append(val)
  return len(lst)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names.keys():
    first_letter =  key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}