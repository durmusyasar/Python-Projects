import web, os
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity',
    '/profile/(.*)/info', 'UserInfo',
    '/settings', 'UserSettings',
    '/update-settings', 'UpdateSettings',
    '/profile/(.*)', 'UserProfile',
    '/submit-comment', 'SubmitComment',
    '/upload-image/(.*)', 'UploadImage',
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': 'none'})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})

# Classes/Results
class Home:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_post()
        return render.Home(posts)

class Register:
    def GET(self):
        return render.Register()

class Login:
    def GET(self):
        return render.Login()

class PostRegistration:
    def GET(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username

class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect
        return "error"

class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        post_model = Posts.Posts()
        new_post = post_model.insert_post(data)

        return "success"

class SubmitComment:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        post_model = Posts.Posts()
        added_comment = post_model.add_comment(data)
        if added_comment:
            return added_comment
        else:
            return {"error" : "403"}

        return "success"

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return "success"

class UserProfile:
    def GET(self):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)
        post_model = Posts.Posts()
        posts = post_model.get_all_post()
        return render.Profile(posts, user_info)

class UserInfo:
    def GET(self):
        data = type('obj', ('object',), {"username": "durmus", "password": "deneme123"})
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)
        return render.Info()

class UserSettings:
    def GET(self):
        return render.Settings()

class UpdateSettings:
    def POST(self):
        data = web.input
        data.username = session_data["user"]["username"]
        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return "success"
        else:
            return "A fatal error has occured"

class UploadImage:
    def POST(self, type):
        file = web.input(avatar={}, background={})
        file_dir = os.getcwd() + "static/uploads/" + session_data["user"]["username"]

        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        
        if "avatar" or "background" in file:
            filepath = file[type].filename.replace('\\', '/')
            filename = filepath.split("/")[-1]
            f = open(file_dir + "/" + filename, "wb")
            f.write(file[type].file.read())
            f.close()

            update = {}
            update["type"] = type
            update[type] = "/static/uploads" + session_data["user"]["username"] + "/" +filename
            update["username"] = session_data["user"]["username"]

            account_model = LoginModel.LoginModel()
            update_avatar = account_model.update_image(update)
        return web.seeother("/ settings")

if __name__ == "__main__":
    app.run()