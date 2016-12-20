from flask import Flask, request, g, render_template
from beaker.middleware import SessionMiddleware





session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.data_dir':'./'
}
app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)



@app.errorhandler(404)
def not_found(error):
    return render_template('common/404.html'), 404


@app.before_request
def get_connection_from_scoped_session():
    g.db_conn = db_session().connection()


@app.after_request
def commit_and_close_connection(response):
    try:
        db_session.commit()
    except:
        pass
    try:
        g.db_conn.close()
    except:
        pass
    return response

@app.teardown_request
def remove_db_session(exception):
    if exception:
        try:
            db_session.rollback()
        except:
            pass
        try:
            g.db_conn.close()
        except:
            pass
    db_session.remove()



from wechat.database import db_session
from wechat.views import wechet_platform
app.register_blueprint(wechet_platform.common)
