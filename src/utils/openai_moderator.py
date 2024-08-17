from openai import OpenAI

API_KEY = "sk--kjyma1pmZmAZCVoJA-n1YqIT9stCZ7_r4HGE67xGDT3BlbkFJDn-rlRGEDCEXsuCCDxJrfb4bOmwxGEh-fVmao-HksA"


client = OpenAI(api_key=API_KEY)


def check_for_swearing(text: str) -> bool:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Does the following text contain any swear words or offensive language?"
                           f"Respond with 'Yes' or 'No', no more letters or symbols.\n\nText: {text}\n\nAnswer:"
            }
        ]
    )
    return completion.choices[0].message.content == "Yes"
