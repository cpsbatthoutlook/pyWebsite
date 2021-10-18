from flask import Blueprint, Flask, redirect, render_template, url_for, session, request
from website.books.book_models import Bookmarks, BookmarksForm
from website import app, db

book_blueprint = Blueprint('book', __name__)

@book_blueprint.route("/book", methods=['GET', 'POST'])
# @book_blueprint.route("/book", methods=['GET', 'POST'])
def book_home():
    # form=BookmarksForm()
    if request.method == 'POST':
        session['book_option'] =request.form['category']
    else:
        try:
         if session['book_option'] == None:
            session['book_option']='Python'
        except :
            session['book_option']='Python'

    page = request.args.get('page', 1, type=int)
    data = Bookmarks.query.filter_by(catagory=session['book_option']).paginate(page=page, per_page=30) #Start paginating
    return render_template('book.html', title=session['book_option'], form=data)

@book_blueprint.route("/book/", methods=['GET', 'POST'])
# @book_blueprint.route("/book/<int:id>/update", methods=['GET', 'POST'])
# def bookedit(id):
def bookedit1():
    form=BookmarksForm()
    if form.is_submitted() and  request.method == 'POST':
        # return "%s %s %s" % (request.form.get("catagory"), form.url.data, form.details.data)
        rec=Bookmarks(catagory=request.form.get('catagory'), details=form.details.data, url=form.url.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('bookedit.html', title='Add bookmarks', form=form)

@book_blueprint.route("/book/<int:id>/update", methods=['GET', 'POST'])
def bookedit(id):
    form=BookmarksForm()
    rec=Bookmarks.query.get_or_404(id)
    if form.is_submitted():
        # rec.catagory=form.catagory.data
        rec.catagory=request.form.get('catagory')
        rec.details=form.details.data
        rec.id=id
        rec.url = form.url.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        form.details.data=rec.details
        form.catagory.data=rec.catagory
        form.id.data = id
        form.url.data = rec.url
        return render_template('bookedit.html', title='Add bookmarks', form=form)

