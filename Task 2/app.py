import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('f.html')

@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        business_name = request.form['business_name']
        about_bussiness = request.form['about_bussiness']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        whatsapp = request.form['whatsapp']
        instagram = request.form['instagram']
        facebook = request.form['facebook']
        twitter = request.form['twitter']
        website = request.form['website']
        address = request.form['address']
        if 'photo' in request.files:
            file = request.files['photo']
            uploads_dir = os.path.join(app.root_path, 'static', 'uploads')
            os.makedirs(uploads_dir, exist_ok=True)
            file.save(os.path.join(uploads_dir, file.filename))
            photo = file.filename
        else:
            photo = None
        return render_template('t.html',
                               name=name, email=email, phone=phone,
                               whatsapp=whatsapp, instagram=instagram,
                               facebook=facebook, twitter=twitter,
                               website=website, address=address,
                               business_name=business_name, photo=photo,about_bussiness=about_bussiness)

if __name__ == '__main__':
    app.run(debug=True)
