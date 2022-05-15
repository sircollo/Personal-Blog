from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Blog,Comment
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

admin = Admin(app)
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Blog,db.session))
admin.add_view(ModelView(Comment,db.session))

@manager.shell
def make_shell():
  return dict(app=app,db=db)


if __name__=='__main__':
  manager.run()