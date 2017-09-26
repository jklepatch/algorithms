def find_anagram(results, current_word, letters_to_permute):
    if len(letters_to_permute) == 1: 
        my_current_word = list(current_word)
        my_current_word.append(letters_to_permute[0])
        results.append(my_current_word)
        return

    for (i, letter) in enumerate(letters_to_permute):
        my_current_word = list(current_word)
        my_current_word.append(letter)

        my_letters_to_permute = list(letters_to_permute)
        del my_letters_to_permute[i]

        find_anagram(results, my_current_word[:], my_letters_to_permute)

    return

def main():
    results = []
    current_word = []
    letters_to_permute = list("abcd")

    find_anagram(results, current_word, letters_to_permute)

    per_row = len(results) / len(letters_to_permute)
   
    print("")
    for i in range(len(results)):
        if (i) % per_row == 0:
            print("Permutations for pivot: {}".format(results[i][0]))

        print(results[i])

        if i != 0 and (i + 1) % per_row == 0:
            print("")
    
    print("Total permutations: {}\n".format(len(results)))

main()
