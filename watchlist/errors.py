from flask import render_template

from watchlist import app

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(err):  # 接受异常对象作为参数
    return render_template('errors/404.html', err = err), 404  # 返回模板和状态码

@app.errorhandler(500)  # 传入要处理的错误代码
def page_not_found(err):  # 接受异常对象作为参数
    return render_template('errors/500.html', err = err), 500  # 返回模板和状态码

@app.errorhandler(400)  # 传入要处理的错误代码
def page_not_found(err):  # 接受异常对象作为参数
    return render_template('errors/400.html', err = err), 400  # 返回模板和状态码