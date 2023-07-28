from transformers import pipeline
import cmd
import nltk
import sys
import torch

nltk.download('punkt')

class bcolors:
    GREEN = '\033[92m'
    END = '\033[0m'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(bcolors.GREEN + "Your program is running on " + device.type + "." + bcolors.END)

fix_spelling = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")

# get the max_length argument from the command line
max_length = int(sys.argv[1])

class SpellingFixer(cmd.Cmd):
    intro = bcolors.GREEN + "Welcome to the spelling fixer. Type a sentence to correct it or 'quit' to exit." + bcolors.END
    prompt = "> "

    def default(self, line):
        if line == "quit":
            return True
        else:
            # split the input into sentences
            sentences = nltk.sent_tokenize(line)
            # initialize an empty list to store the corrected sentences
            corrected_sentences = []
            # loop over each sentence and correct it
            for sentence in sentences:
                result = fix_spelling(sentence, max_length=max_length)
                corrected_sentences.append(result[0]["generated_text"])
            # join the corrected sentences with a space
            output = " ".join(corrected_sentences)
            print("===========================================")
            print("result: " + output)

if __name__ == "__main__":
    SpellingFixer().cmdloop()
