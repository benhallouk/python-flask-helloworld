from flask import render_template, url_for, request, flash, redirect
from helloworld import app, db
from forms import ContactForm
from models import ContactMessage 
from flask_login import login_required

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html',text='This is absolutly dynamic')

@app.route('/about')
def about():
    return render_template('about.html',text='This is absolutly dynamic')

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        new_contact_message = ContactMessage(name=name,email=email,message=message)
        db.session.add(new_contact_message)
        db.session.commit()
        flash("Thanks you '<b>{}</b>' <br> Your message has been succesfully submited".format(name))
        return redirect(url_for('index'))
    return render_template('contact.html',form=form)

@app.route('/messages/<int:post_id>')
@app.route('/messages')
#@login_required
def messages(post_id=0):    
    post_id = request.args.get('post_id') if request.args.get('post_id') else post_id
    print post_id 
    if post_id==0:        
        return render_template('messages.html',messages=ContactMessage.query.limit(10))
    else:
        return render_template('messages.html',messages=ContactMessage.query.filter_by(id=post_id).limit(10))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)