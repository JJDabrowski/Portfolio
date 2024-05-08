# 1.0 Hello and welcome to Calackey's back-end prototype #
Calackey is an app with which you will be able to tell an app that you want to create an appointment. The back-end's task is to capture the keyphrases from the input and schedule an appointment based on them.

# 2.0 Installation and Configuration #
## 2.1 Installation ##
Install requirements.txt. On some machines, the libraries might need updating to the version that is in the requirements even though you asked to install it beforehand. Just check with `pip freeze` if you have the right version installed. If not, please run for example: `pip install openai --upgrade`
## 2.2 Configuration ##
## 2.2.1 Configuring Google OAuth ##
To let Calackey use your calendar, you need to configure OAuth 2.0 first. Please follow the guide: https://developers.google.com/workspace/guides/configure-oauth-consent
Then please configure and download your `credentials.json` file and put it in this project's root. Please follow this guide: https://developers.google.com/workspace/guides/create-credentials
## 2.2.2 Get your OpenAI key ##
Next get your OpenAI key and put it in `calackey_starter.py` file on line 13: `openai.api_key="<your-openai-key-here>"`

You should be all set to test the Calackey backend prototype. I hope you will enjoy it!