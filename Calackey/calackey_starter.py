import openai
from Google import Create_Service


#Google prep
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

openai.api_key="<your-openai-key-here>"

input = input()

def generate_prompt(input):
    return """Przygotuj dla wydarzenia odpowiedź taką jak w przykładach.

Przykłady:
Wymiana opon przyszła środa od 8 dwie godziny: Wymiana opon, 2023-08-02T08:00:00, 2023-08-02T10:00:00

Spotkanie o pracę 13.05 13-14: Spotkanie o pracę, 2024-05-13T13:00:00, 2024-05-13T14:00:00

Odebrać kwiaty targowa 14 jutro rano: Odebrać kwiaty targowa 14, 2023-07-31T09:30:00, 2023-07-31T10:30:00

Trener 31 X o 18:00: Trener, 2024-10-31T18:00:00, 2024-10-31T19:00:00

HackYeah 30 września 8: HackYeah, 2023-09-30T08:00:00, 2023-09-30T09:00:00

""" + f'Prompt: {input}:'

response = openai.Completion.create(
            model="text-davinci-003",
            prompt= generate_prompt(input),
            max_tokens = 75,
            temperature = 0
        )

data = response["choices"][0]["text"]

split_data = data.split(',')
event_name = split_data[0].strip()
start_time = split_data[1].strip() +"%s"
end_time = split_data[2].strip() + "%s"

GMT_OFF = "+02:00"

google_request = {
    "summary": event_name,
    "start": {"dateTime": start_time % GMT_OFF},
    "end": {"dateTime": end_time % GMT_OFF}
}

e = service.events().insert(calendarId='primary', body=google_request).execute()