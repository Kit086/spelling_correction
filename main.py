from transformers import pipeline
import cmd
import nltk

nltk.download('punkt')

class bcolors:
    GREEN = '\033[92m'
    END = '\033[0m'

fix_spelling = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")

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
                result = fix_spelling(sentence, max_length=4096)
                corrected_sentences.append(result[0]["generated_text"])
            # join the corrected sentences with a space
            output = " ".join(corrected_sentences)
            print("===============================")
            print("# " + output)

if __name__ == "__main__":
    SpellingFixer().cmdloop()