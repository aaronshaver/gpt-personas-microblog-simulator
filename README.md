# GPT Personas Microblog Simulator

## Why? What is this thing?

foo

## Setup

1. Install Python 3.7.1 or newer
1. Using a virtual environment is recommended to ensure project dependencies don't conflict with your global Python setup.
   1. python -m venv openai-env
   1. Activate the virtual environment:
      1. Windows: `openai-env\Scripts\activate`
      1. Unix or MacOS: `source openai-env/bin/activate`
   1. You should see the terminal / command line interface change slightly after you active the virtual environment, it should now show "openai-env" to the left of the cursor input section.
1. `pip install -r requirements.txt` (TODO: this will probably just be in Dockerfile(s))
1. Make sure you have an OpenAI API key on your system in some fashion: https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key
   1. Note that OpenAI billing can be confusing. You have to specifically add another payment method (even if you're already a Plus member) and generate a *new* API token if you had generated one before adding billing/API access. And even then, it can take a few minutes for usage stats to start showing up.
1. Finally, run `whatever_command.py` (TODO update this)