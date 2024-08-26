import asyncio

from src.schemas.post import PostSchema
from src.schemas.comment import CommentCreateSchema, CommentSchema
from src.utils.openai_moderator import created_related_comment


async def create_auto_reply(comment: CommentSchema, post: PostSchema) -> CommentCreateSchema:
    await asyncio.sleep(post.auto_response_delay * 60)
    content = created_related_comment(comment.content, post.content)
    return CommentCreateSchema(
        content=content,
        author_id=post.author_id,
        parent_comment_id=comment.id,
        post_id=post.id,
    )
