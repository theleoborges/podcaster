# Podcaster

[NotebookLM](https://notebooklm.google.com/) is amazing. If you haven't tried it out, do it. But what if you would like to generate a podcast from some private or confidential document? This is where this script may come in handy.

The idea is that you generate a podcast script based on some material, such as a PDF file, using an LLM such as LLaMa. You can use LLaMa on your local laptop via [LMStudio](https://lmstudio.ai/) or [Ollama](https://ollama.com/). This script then uses [bark](https://github.com/suno-ai/bark) to convert text to speech.

There is a sample script in this repo that was created from the included PDF file — an HBR article about hybrid work. You can create the podcast script using the following prompts in LMStudio (or other similar tool):

1. <<Upload PDF>>
2. User: Please extract the text from the attached PDF while preserving context.
3. User: Now turn this into a podcast transcript from the perspective of hosts Jane and Matt, tech and business journalists and AI enthusiasts.

Once you have the script, save it to `script.txt` and generate the audio file:

    $ python main.py script.txt

This will run **slow** on your laptop but it will work. It took about 10-15min to generate a 2.5min podcast. 

Have fun!