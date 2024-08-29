from openai import OpenAI

from src.config import get_settings

settings = get_settings()

client = OpenAI(api_key=settings.openai.API_KEY)


def check_for_swearing(text: str) -> bool:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional moderator"},
            {
                "role": "user",
                "content": "Does the following text contain any swear words or offensive language?"
                           f"Respond with 'Yes' or 'No', no more letters or symbols.\n\nText: {text}\n\nAnswer:"
            }
        ]
    )
    return completion.choices[0].message.content == "Yes"


def created_related_comment(comment_content: str, post_content: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an insightful commenter"},
            {
                "role": "user",
                "content": "Create your own comment in response to the comment, "
                           "ensuring it relates to the context of both the comment and the post."
                           "Your reply should be 1-3 sentences long."
                           f"Post: {post_content}, Comment: {comment_content}"
            }
        ]
    )
    return completion.choices[0].message.content
