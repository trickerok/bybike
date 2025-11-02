from fastapi import *
from Servicies.databases import *
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    description:str
    maplink: str
    photoname: str
    userid: int
class Info(BaseModel):
    city: str

class Comment(BaseModel):
    userid: int
    title:str
    description: str
    author: str
    cardid: int

@app.get("/posts",tags=["Posts"],summary="Получить все посты")
def posts():
    all_posts = GetPosts()
    return all_posts
@app.get("/posts/{username}",tags=["Posts"],summary="Получить все посты пользователя")
def getpost(username):
    posts = GetPostsByUserName(username=username)
    return posts
@app.post("/posts",tags=["Posts"],summary="Создать пост")
def upload_post(post:Post):
    try:
        CreateCard(post.userid,post.title,post.description,post.maplink,post.photoname)
        return {"Success":"True"}
    except Exception as ex:
        return {"Error":f"Can't publish - {ex}"}
@app.delete("/posts/{postid}",tags=["Posts"],summary="Удалить пост по id")
def RemovePost(postid):
    try:
        DeletePost(postid)
        return {"Deleted":"True"}
    except Exception as ex:
        return {"Error":f"Can't delete - {ex}"}
@app.patch("/posts/{postid}",tags=["Posts"],summary="Изменить пост")
def UpdatePost(postid):
    try:
        UpdatePost(postid)
        return {"Updated":"True"}
    except Exception as ex:
        return {"Error":f"Can't update - {ex}"}
@app.get("/comments/{userid}",tags=["Comments"],summary="Получить все комментарии пользователя")
def UserComments(userid):
    try:
        comments = GetCommentsByUser(userid=userid)
        return comments
    except Exception as ex:
        return {"Error":f"Can't update - {ex}"}
@app.delete("/comments/{id}",tags=["Comments"],summary="Удалить коммент по id")
def RemComment(id):
    try:
        DeleteComment(id)
        return {"Deleted":"True"}
    except Exception as ex:
        return {"Error":f"Can't delete - {ex}"}
@app.delete("/comments/users/{userid}",tags=["Comments"],summary="Удалить все от пользователя")
def RemByUser(userid):
    try:
        DeleteUserComments(userid)
        return {"Deleted":"True"}
    except Exception as ex:
        return {"Error":f"Can't delete - {ex}"}
@app.patch("/comments/{id}",tags=["Comments"],summary="Изменить комментарий")
def upcomment(id:int,comment: Comment):
    try:
        UpdateComment(id,comment.title,comment.description)
        return {"Updated":"True"}
    except Exception as ex:
        return {"Error":f"Can't update - {ex}"}
@app.delete("/post/{cardid}/comments",tags=["Comments"],summary="Удалить все комментарии поста")
def remallcominpost(cardid):
    try:
        DeleteCardComments(cardid)
        return {"Deleted":"True"}
    except Exception as ex:
        return {"Error":f"Can't delete - {ex}"}
@app.get("/post/{cardid}/comments",tags=["Comments"],summary="Получить все комментарии поста")
def getcombypost(cardid):
    try:
        comm = GetCommentsbyPost(cardid)
        return comm
    except Exception as ex:
        return {"Error":f"Can't get - {ex}"}

@app.post("/comments",tags=["Comments"],summary="Создать комментарий")
def CreateComments(comment: Comment):
    try:
        CreateComment(comment.userid,comment.title,comment.description,comment.author,comment.cardid)
        return {"Created":"True"}
    except Exception as ex:
        return {"Error":f"Can't create - {ex}"}


@app.get("/my",tags=["Система Рекомендаций"])
def recsystem(city:Info):
    return []
