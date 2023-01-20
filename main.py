import collections
import string
import re
# import json


class WordCount:

    def question_one_word_count(self, file_path):
        """
        function for question one: read a line from the input file and replace the punctuations;
        iterate each word in each line, to check if the dictionary has the word or not. If not,
        put the word into the dictionary as the key, value is 1; if yes, increase the value by 1.
        For the best case, the complexity for time is O(n), space is O(n), when there is only one
        line in the text; worse case, the complexity for time if O(n^2), space is O(n), where each
        word takes a line.

        :param file_path: the path to read the text
        :return: a dictionary of all the words count. key is the word and value is the count.
        """
        dictionary = {}
        if not file_path:
            print("Error! Input path is empty!")
            return

        #  read the file:
        try:
            words_text = open(file_path, "r")
        except OSError:
            print("Error when opening the file!")
            return

        with words_text:
            lines = words_text.readlines()
            for l in lines:
                # 1. remove \t\n
                stripped_line = re.sub(r'\\t|\\n', '', l)
                # 2. remove punctuation
                str_no_punc = stripped_line.translate(str.maketrans('', '', string.punctuation))
                # 3. count the words
                words = str_no_punc.lower().split()
                for w in words:

                    if dictionary.get(w):
                        dictionary[w] += 1
                    else:
                        dictionary[w] = 1

        # write output to a file if needed
        # with open("output/question_one_result.txt", 'w') as result_file:
        #     result_file.write(json.dumps(dictionary))

        return dict(dictionary)


    def question_two_word_count(self, file_path):
        """
        This is an improved approach with O(n) for time and O(n) for space
        In this approach I read all the content from the file into a string
        and preprocess the string by replacing the punctuation.

        defaultdict is used in approach as it is a dictionary like data structure,
        plus it offers default value (in my case, set to 0) if the key (the word) doesn't exist.

        :param file_path: the path to read the text
        :return: return a dictionary of all the words count. key is the word and value is the count.
        """
        if not file_path:
            print("Error! Input path is empty!")
            return

        #  read the file:
        try:
            words_text = open(file_path, "r")
        except OSError:
            print("Error when opening the file!")
            return

        # remove /t /n and punctuation and put the word count into a defaultdict
        with words_text:
            words = words_text.read().lower().replace('\\t', '').replace('\\n', '').translate(
                str.maketrans('', '', string.punctuation)).split()
            dictionary = collections.defaultdict(int)

            for word in words:
                dictionary[word] += 1

            return dict(dictionary)

    def question_three_highest_count(self, dictionary):
        """ function for question three
        output for the highest word count, return a tuple, first element is the word, second element is the count
        In this question three, I use python sorted function to sort the dictionary output from question 1 and 2.
        Since Python dictionary is a hashmap, the complexity for sorting is O(nlogn) and space is O(n)
        """
        if not dictionary:
            return
        sorted_words_counts = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        return sorted_words_counts[0]


wc = WordCount()
dictionary_first_approach = wc.question_one_word_count("data/sample.txt")
dictionary_second_approach = wc.question_two_word_count("data/sample.txt")
print("word count from first approach: ", dictionary_first_approach)
print("word count from second approach: ", dictionary_second_approach)
highest_count_first_approach = wc.question_three_highest_count(dictionary_first_approach)
highest_count_second_approach = wc.question_three_highest_count(dictionary_second_approach)
print("Highest count from first approach: ", highest_count_first_approach)
print("Highest count from second approach: ", highest_count_second_approach)
