from openai import OpenAI

from src.config import get_settings

settings = get_settings()

client = OpenAI(api_key=settings.openai.API_KEY)


def check_for_swearing(text: str) -> bool:
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {
    #             "role": "user",
    #             "content": "Does the following text contain any swear words or offensive language?"
    #                        f"Respond with 'Yes' or 'No', no more letters or symbols.\n\nText: {text}\n\nAnswer:"
    #         }
    #     ]
    # )
    # return completion.choices[0].message.content == "Yes"
    return True


def created_related_comment(comment_content: str, post_content: str) -> str:
    return "related comment"
