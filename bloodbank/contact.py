from flask import Flask, render_template, request, flash
from forms import ContactForm


bp = Blueprint('contact', __name__)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
        msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)

        return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('bank/contact.html', form=form)



app = Flask(__name__)  
app.secret_key = 'development key'