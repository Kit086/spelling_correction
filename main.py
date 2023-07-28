from transformers import pipeline
import cmd

fix_spelling = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")

class SpellingFixer(cmd.Cmd):
    intro = "Welcome to the spelling fixer. Type a sentence to correct it or 'quit' to exit."
    prompt = "> "

    def default(self, line):
        if line == "quit":
            return True
        else:
            result = fix_spelling(line, max_length=2048)
            print(result[0]["generated_text"])

if __name__ == "__main__":
    SpellingFixer().cmdloop()
