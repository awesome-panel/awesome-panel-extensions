import param
from .base_model import BaseModel

class Author(BaseModel):
    name = param.String(doc="The name of the author or owner of the application.")
    url = param.String(doc="A link to a page about the author.")
    avatar_url = param.String(doc="A link to a thumbnail image of the author.")

    twitter_url = param.String(doc="A link to the Twitter page of the Author")
    linkedin_url = param.String(doc="A link to the Linked In page of the Author")
    github_url = param.String(doc="A link to the Github page of the Author")