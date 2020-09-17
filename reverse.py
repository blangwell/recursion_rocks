# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(string):
    # start with base case
    if len(string) == 0: 
        return ''
    # then recursive step
    return string[-1] + reverse(string[:-1])

    # split_string = list(ss)
    # # print(split_str ing)
    # if len(split_string) >= len(result):
    #     result.append(split_string[index])
    #     index += 1
    #     print(result)
    #     return reverse(ss, result, split_string, index)


    # if len(split_string) >= len(result):
    #     pop_letter = split_string.pop()
    #     result.append(pop_letter)
    #     # print(result, "THIS IS THE RESULT")
    #     # print(split_string, "THIS IS THE SPLIT STRING")
    #     return reverse(ss, result, split_string)


    # pop the last letter off the ss string
    # add to beginning of result string

# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"
reverse('hello')