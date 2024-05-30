from flask import Flask
from app.user.views import user_bp
from app.blog.views import blog_bp
from app.comment.views import comment_bp

def create_app():
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object('config.Config')

    # 注册蓝图
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(comment_bp, url_prefix='/comment')

    return app
