# -*- coding:utf-8 -*-
import os
from flask import Flask
from flask.ext.cors  import CORS
import base64
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker

from flask import Flask, render_template, request, jsonify,Blueprint,g
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

common = Blueprint('common', __name__)

# create flask instance
# app = Flask(__name__)
# CORS(app)


@common.route('/search')
def index():
    if request.method == "POST":
	#nickname = request.form.get('nickname')
        wxh = request.form.get('name')
    if request.method == "GET":
	#return jsonify({"sorry": "bad request"}), 500
    	#nickname = request.args.get('nickname')
   	    wxh = request.args.get('name')
        # wxh=base64.b64decode(wxh.encode("utf-8"))
    print wxh
    if wxh!=None and wxh!='':
	   sql="select wxh,nickname,info,certification,url from wxh_info1 where (wxh like \"%%%s%%\" or nickname like \"%%%s%%\")and logoindex=2" %(wxh,wxh)
    #elif nickname!=None and nickname != '':
	#sql="select wxh,nickname,info,certification,url from wxh_info where nickname like \"%%%s%%\" and logoindex=2" %nickname
    else:
	   return jsonify(data="请输入参数")
    print sql
    try:
        data = g.db_conn.execute(text(sql)).fetchall()
    except:
	   return jsonify({"sorry": "Sorry, there is some problems!"}), 500
    out=[]
    print len(data)
    if len(data)>0:
    	for info in data:
    	    result={}
    	    result['wxh']=info[0]
    	    result['nickname']=info[1]
    	    result['info']=info[2]
    	    result['certification']=info[3]
    	    result['logo']=info[4]
    	    out.append(result)
            return jsonify(data=out)
    return jsonify({"sorry": "Sorry, no results!"}), 500


# run!
# if __name__ == '__main__':
#     app.run('127.0.0.1',5002, debug=True)

