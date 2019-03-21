import sublime
import sublime_plugin
import re
from smiles.emojis import EMOJIS

class SmileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        region = sublime.Region(0, self.view.size())
        file_contents = self.view.substr(region)
        self.view.replace(edit, region, self.emojify(file_contents))

    def emojify(self, file_contents):
        return self.multiple_replace(EMOJIS, file_contents)

    def multiple_replace(self, adict, text):
        regex = re.compile("|".join(map(re.escape, adict.keys(  ))))
        # For each match, look up the value in the emojis
        return regex.sub(lambda match: adict[match.group(0)], text)
