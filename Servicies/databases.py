import sqlite3


#id,username,email,hashedpaswd,fullname,town,role
#id,title,description,maplink,photoname,userid
#id,userid,title,description,author,cardid

def CreateUser(username,email,hashedpasswd,fullname,town,role):
    try:
        connection = sqlite3.connect('bike.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users (username, email, hashedpasswd,fullname,town,role) VALUES (?, ?, ?, ?, ?, ?)', (username, email, hashedpasswd,fullname,town,role))
        connection.commit()
        connection.close()
        return "UserCreated"
    except Exception as ex:
        return ex
def UpdateTown(newtown,username):
    try:
        connection = sqlite3.connect('bike.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE users SET town = ? WHERE username = ?', (newtown, username))
        connection.commit()
        connection.close()
        return "UserUpdated"
    except Exception as ex:
        return ex
def CreateCard(userid,title,description,maplink,photolink):
    try:
        connection = sqlite3.connect('bike.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO cards (userid, title, description,maplink,photolink) VALUES (?, ?, ?, ?, ?)', (userid,title,description,maplink,photolink))
        connection.commit()
        connection.close()
        return None
    except Exception as ex:
        return ex
def GetPosts():
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT userid, title, description, maplink, photolink FROM cards")
        posts = cursor.fetchall()
        connection.commit()
        connection.close()
        return posts
    except Exception as ex:
        print(f"Ошибка {ex}")
        return []
    finally:
        connection.close()
def GetPostsByUserName(username):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
        SELECT c.*
        FROM cards c
        JOIN users u ON c.userid = u.id
        WHERE u.username = ?
        """,(username,))
        posts = cursor.fetchall()
        connection.commit()
        connection.close()
        return posts
    except Exception as ex:
        print(f"Ошибка {ex}")
        return []
    finally:
        connection.close()
def CreateComment(userid,title,description,author,cardid):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO comments (userid, title, description,author,cardid) VALUES (?, ?, ?, ?, ? )', (userid,title,description,author,cardid,))
        connection.commit()
    except Exception as ex:
        print(f"Error {ex}")
        return ex
    finally:
        connection.close()
    return "CommentCreated"
def UpdateComment(id,title="",description=""):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute('UPDATE comments SET title = ?, description = ? WHERE id = ?', (title, description,id,))
        connection.commit()
    except Exception as ex:
        print(f"Error {ex}")
        return ex
    finally:
        connection.close()
    return "CommentUpdated"
def DeleteComment(id):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM comments WHERE id = ?",(id,))
        connection.commit()
    except Exception as ex:
        print(f"Error {ex}")
        return ex
    finally:
        connection.close()
    return "CommentDeleted"
def DeletePost(id):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM cards WHERE id = ?",(id,))
        connection.commit()
    except Exception as ex:
        print(f"Error {ex}")
        return ex
    finally:
        connection.close()
    return "PostDeleted"
def GetCommentsbyPost(cardid):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, description, author FROM comments WHERE cardid= ?", (cardid,))
        comments = cursor.fetchall()
        connection.commit()
        connection.close()
    except Exception as ex:
        print(f"Ошибка {ex}")
        return []
    finally:
        connection.close()
    return comments
def GetCommentsByUser(userid):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, description, author FROM comments WHERE userid= ?", (userid,))
        comments = cursor.fetchall()
        connection.commit()
        connection.close()
    except Exception as ex:
        print(f"Ошибка {ex}")
        return []
    finally:
        connection.close()
    return comments
def DeleteUserComments(userid):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM comments WHERE userid = ?",(userid,))
        connection.commit()
    except Exception as ex:
        print(f"Error {ex}")
        return ex
    finally:
        connection.close()
    return "CommentDeleted"
def DeleteCardComments(cardid):
    connection = sqlite3.connect('bike.db')
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM comments WHERE cardid = ?",(cardid,))
        connection.commit()
    except Exception as ex:
        print(f"Error {ex}")
        return ex
    finally:
        connection.close()
    return "CommentDeleted"