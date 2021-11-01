from flask import Blueprint, Flask, redirect, render_template, url_for, session, request
from website.efforts.efforts_models import EffortsForm, efforts
from website import app, db

effort_blueprint = Blueprint('efforts', __name__)

@effort_blueprint.route("/efforts", methods=['GET', 'POST'])
def effort_home():
    #return render_template("efforts.html", title="Home Page", form=efforts.query.all())
    return render_template("efforts.html", title="Home Page", form=efforts.query.order_by(efforts.inserttime.desc()).limit(30).all())


# @effort_blueprint.route("/efforts/search")
# def pks():
#     return render_template("KnowSearch.html")



@effort_blueprint.route("/efforts/add", methods=['GET','POST'])
def effort_add():
    # rec = efforts.query.get_or_404(id=id)
    form = EffortsForm()
    if form.is_submitted() and request.method == 'POST':
        # rec = efforts(sitting=form.sitting.data,bother=form.bother.data, sleeptime=form.sleeptime.data, x=form.x.data, y=form.y.data, journal=form.journal.data, wisdom=form.wisdom.data, waketime=form.waketime.data)
        rec = efforts(siteven=form.siteven.data, sitoth=form.sitoth.data, anger=form.anger.data, harsh=form.harsh.data, abusive=form.abusive.data, readb=form.readb.data, s_e=form.s_e.data, help_good=form.help_good.data,sitting=form.sitting.data,bother=form.bother.data, sleeptime=form.sleeptime.data, x=form.x.data, y=form.y.data, journal=form.journal.data, wisdom=form.wisdom.data, waketime=form.waketime.data)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('efforts.effort_home'))
    return render_template("effortsAdd.html", title=form.inserttime.data, form=form, legend='Add')

@effort_blueprint.route("/efforts//view/<int:id>/update", methods=['GET', 'POST'])  ## int: to force integer
def effort_update(id):
    # rec = efforts.query.get_or_404(id=id)
    rec = efforts.query.filter_by(id=id).first_or_404()
    form = EffortsForm()
    if form.is_submitted():
        rec.sitting = form.sitting.data
        rec.x = form.x.data
        rec.y = form.y.data
        rec.journal = form.journal.data
        rec.wisdom = form.wisdom.data
        rec.waketime = form.waketime.data
        rec.sleeptime = form.sleeptime.data
        rec.bother = form.bother.data
        rec.siteven=form.siteven.data
        rec.sitoth=form.sitoth.data
        rec.anger=form.anger.data
        rec.harsh=form.harsh.data
        rec.abusive=form.abusive.data
        rec.readb=form.readb.data
        rec.s_e=form.s_e.data
        rec.help_good=form.help_good.data
        # rec.inserttime = form.inserttime.data
        db.session.commit()
        return redirect(url_for('efforts.effort_home'))
    else:
        form.sitting.data = rec.sitting
        form.x.data = rec.x
        form.y.data = rec.y
        form.journal.data = rec.journal
        form.wisdom.data = rec.wisdom
        form.waketime.data = rec.waketime
        form.sleeptime.data = rec.sleeptime
        form.inserttime.data = rec.inserttime
        form.bother.data = rec.bother
        form.siteven.data=rec.siteven
        form.sitoth.data=rec.sitoth
        form.anger.data=rec.anger
        form.harsh.data=rec.harsh
        form.abusive.data=rec.abusive
        form.readb.data=rec.readb
        form.s_e.data=rec.s_e
        form.help_good.data=rec.help_good
        # form.id = rec.id
        return render_template("effortsAdd.html", title=form.inserttime.data, form=form, legend='Update')

@effort_blueprint.route("/efforts/view/<int:id>", methods=['GET', 'POST'])  ## int: to force integer
def effort_view(id):
    form = efforts.query.filter_by(id=id).first_or_404()
    # form = efforts.query.get_or_404(id=id)
    return render_template("effortsview.html", title=form.inserttime, form=form, legend='Add')
