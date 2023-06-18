import typing
import strawberry
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Post:
    title: str
    author: str

def get_posts():
    return [
        Post(
            title="This is a post",
            author="kennedy"
        )
    ]

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="kennedy", age=9000)
    posts: typing.List[Post] = strawberry.field(resolver=get_posts)


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema=schema)