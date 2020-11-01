from typing import List

import param

from .base_model import BaseModel


class Author(BaseModel):
    name = param.String(doc="The name of the author or owner of the application.")
    url = param.String(doc="A link to a page about the author.")
    avatar_url = param.String(doc="A link to an avatar image of the author.")

    twitter_url = param.String(doc="A link to the Twitter page of the Author")
    linkedin_url = param.String(doc="A link to the Linked In page of the Author")
    github_url = param.String(doc="A link to the Github page of the Author")

    all: List["Author"] = []

    def __init__(self, **params):
        super().__init__(**params)

        self.all.append(self)
