from flask import Blueprint, Flask, redirect, render_template, url_for, session, request
from website.know.know_models import KnowledgebaseForm, knowledgebase
from website import app, db

know_blueprint = Blueprint('know', __name__)

@know_blueprint.route("/know", methods=['GET', 'POST'])
def know_home():
    # category
    if request.method=='POST':
        session['know_option'] = request.form['category']
        page=1
    else:
        page = request.args.get('page', 1, type=int)
        try:
            session['know_option']
        except:
            session['know_option'] = 'Python'
    
    
    # data = knowledgebase.query.all()
    data = knowledgebase.query.filter_by(category=session['know_option']).paginate(page=page, per_page=30)
    return render_template("Know.html", title=session['know_option'], form=data)


@know_blueprint.route("/know/search")
def pks():
    return render_template("KnowSearch.html")


@know_blueprint.route("/know/add", methods=['GET','POST'])
def pka():
    form = KnowledgebaseForm()
    if form.is_submitted():
        rec = knowledgebase(category=form.category.data, subcategory=form.subcategory.data, subject=form.subject.data, description=form.description.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('know_home'))
    return render_template("KnowAdd.html", title='Add records', form=form)

@know_blueprint.route("/know//view/<int:id>/update", methods=['GET', 'POST'])  ## int: to force integer
def pku(id):
    # rec = knowledgebase.query.get_or_404(id=id)
    rec = knowledgebase.query.filter_by(id=id).first_or_404()
    form = KnowledgebaseForm()
    if form.is_submitted():
        # rec = knowledgebase(category=form.category.data, subcategory=form.subcategory.data, subject=form.subject.data, description=form.description.data, id=form.id.data)        rec.category=form.category.data;rec.subcategory=form.subcategory.data;rec.subject=form.subject.data
        rec.description=form.description.data
        # rec.id=form.id.data
        db.session.commit()
        return redirect(url_for('know_home'))
    else:
        form.category.data=rec.category
        form.subcategory.data=rec.subcategory
        form.subject.data=rec.subject
        form.description.data=rec.description
        # form.id = rec.id
        return render_template("KnowAdd.html", title=form.subject, form=form, legend='Update')

@know_blueprint.route("/know/view/<int:id>", methods=['GET', 'POST'])  ## int: to force integer
def pkv(id):
    form = knowledgebase.query.filter_by(id=id).first_or_404()
    # form = knowledgebase.query.get_or_404(id=id)
    return render_template("KnowView.html", title=form.subject, form=form, legend='Add')
