from flask import Flask, render_template,url_for,redirect,request,jsonify
import requests
import jwt
from datetime import datetime, timedelta
import time
import hashlib
from werkzeug.utils import secure_filename
from pymongo.mongo_client import MongoClient
from bson import ObjectId

app = Flask(__name__)

SECRET_KEY = "SPARTA"
TOKEN_KEY = 'mytoken'


client = MongoClient('mongodb://test:sparta@ac-tcz4ypm-shard-00-00.jrmp0f9.mongodb.net:27017,ac-tcz4ypm-shard-00-01.jrmp0f9.mongodb.net:27017,ac-tcz4ypm-shard-00-02.jrmp0f9.mongodb.net:27017/?ssl=true&replicaSet=atlas-cjylmf-shard-0&authSource=admin&retryWrites=true&w=majority')  # Ganti URL sesuai dengan pengaturan MongoDB Anda
db = client.sansco  # Ganti 'mydatabase' dengan nama database Anda

# user-page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/special-offers')
def specialoffers():
    return render_template('special-offers.html')

# reservasi-page-user
@app.route('/meeting',methods=['GET'])
def meeting():
    return render_template('reservasi-meeting.html')

@app.route('/meeting/posting',methods=['POST'])
def posting():
    nama = request.form.get('nama_give')
    telepon = request.form.get('telepon_give')
    komunitas = request.form.get('komunitas_give')
    date = request.form.get('date_give')
    time = request.form.get('time_give')
    durasi = request.form.get('durasi_give')
    jumlah = request.form.get('jumlah_give')
    pilih = request.form.get('pilih_give')
   
    dp = request.form.get('dp_give')
    # print('nama','telepon','komunitas','date','time','durasi','jumlah','dp')

    doc={
        'Nama':nama,
        'Telepon':telepon,
        'Komunitas':komunitas,
        'Tanggal':date,
        'Jam':time,
        'Durasi':durasi,
        'jumlah_orang':jumlah,
        'Area':pilih,
        'dp':dp
    }

    db.meeting.insert_one(doc)
    return jsonify({
        'msg':'Terimakasih sudah Reserevasi'
    })

@app.route('/event',methods=['GET'])
def event():
    return render_template('reservasi-event.html')

@app.route('/event/post',methods=['POST'])
def post():
    nama = request.form.get('nama_give')
    telepon = request.form.get('telepon_give')
    komunitas = request.form.get('komunitas_give')
    date = request.form.get('date_give')
    time = request.form.get('time_give')
    durasi = request.form.get('durasi_give')
    jumlah = request.form.get('jumlah_give')
    piliharea = request.form.get('piliharea_give')
    pilihmenu = request.form.get('pilihmenu_give')
    jammenu = request.form.get('jammenu_give')
    dp = request.form.get('dp_give')

    doc={
        'Nama':nama,
        'Telepon':telepon,
        'Komunitas':komunitas,
        'Tanggal':date,
        'Jam':time,
        'Durasi':durasi,
        'jumlah_orang':jumlah,
        'Area':piliharea,
        'Menu':pilihmenu,
        'Jam_keluar_menu':jammenu,
        'dp':dp
    }

    db.event.insert_one(doc)
    return jsonify({
        'msg':'Terimakasih sudah reservasi event'
    })


# @app.route('/nyoba',methods=['GET'])
# def nyoba():
#     return render_template('nyoba.html')

# @app.route('/nyoba/postingg',methods=['POST'])
# def postingg():
#     username = request.form.get('username_give')
#     password = request.form.get('password_give')

#     # print('nama','telepon','komunitas','date','time','durasi','jumlah','dp')

#     doc={
#         'username':username,
#         'password':password,
#     }
#     db.login.insert_one(doc)
#     return jsonify({
#         'msg':'Terimakasih sudah Reserevasi'
#     })


# LOGIN
@app.route('/login',methods=['GET'])
def login():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        user_info = db.users.find_one({'username': payload.get('id')})
        return redirect(url_for('admin_dashboard', user_info=user_info))
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        msg = request.args.get('msg')
        return render_template('login2.html', msg=msg)


@app.route('/login_save', methods=['POST'])
def login_save():
    username_receive = request.form['username_login']
    password_receive = request.form['password_login']
    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.login.find_one({
        'username': username_receive,
        'password': password_receive
    })
    if result:
        payload = {
            'id': username_receive,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 1),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({
            "result": "fail",
            "msg": "Kami tidak dapat menemukan pengguna dengan kombinasi id/kata sandi tersebut",
        })
    # return render_template('login2.html')



# admin-page-meeting

@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard():
    return render_template('dashboard.html')

@app.route('/adminm', methods=['GET'])
def adminm():
    data=db.meeting.find({})
    return render_template('admin2.html',data=data)

# edit-meeting
@app.route('/editt')
def editt():
    id=request.args.get('id')
    data=list(db.meeting.find({'_id':ObjectId(id)}))
    print(data)
    return render_template('edit2.html',data=data)

@app.route('/editt',methods=['POST'])
def ubahan():
    nama = request.form.get('nama_give')
    telepon = request.form.get('telepon_give')
    komunitas = request.form.get('komunitas_give')
    date = request.form.get('date_give')
    time = request.form.get('time_give')
    durasi = request.form.get('durasi_give')
    jumlah = request.form.get('jumlah_give')
    pilih = request.form.get('pilih_give')
    dp = request.form.get('dp_give')
    id = request.form.get('id_give')


    doc={
        'Nama':nama,
        'Telepon':telepon,
        'Komunitas':komunitas,
        'Tanggal':date,
        'Jam':time,
        'Durasi':durasi,
        'jumlah_orang':jumlah,
        'Area':pilih,
        'dp':dp,
        'id':id
    }

    db.meeting.update_one({'_id':ObjectId(id)},{'$set':doc})
    return jsonify({
        'msg':'data berhasil di edit'
    })

# delete-meetiing
@app.route('/deletee',methods=['GET'])
def deletee():
    id=request.args.get('id')
    db.meeting.delete_one({'_id':ObjectId(id)})
    return jsonify({
        'msg':'Yakin untuk menghapus data reservasi Meeting room?'
    })
    # data=list(db.meeting.find({}))
    # return render_template('admin2.html',data=data)



# admin-page-event
@app.route('/admine')
def admine():
    data=db.event.find({})
    return render_template('admin-event2.html',data=data)

# edit-event
@app.route('/edit')
def edit():
    id=request.args.get('id')
    data=list(db.event.find({'_id':ObjectId(id)}))
    print(data)
    return render_template('edit.html',data=data)

@app.route('/edit',methods=['POST'])
def ubah():
    nama = request.form.get('nama_give')
    telepon = request.form.get('telepon_give')
    komunitas = request.form.get('komunitas_give')
    date = request.form.get('date_give')
    time = request.form.get('time_give')
    durasi = request.form.get('durasi_give')
    jumlah = request.form.get('jumlah_give')
    piliharea = request.form.get('piliharea_give')
    pilihmenu = request.form.get('pilihmenu_give')
    jammenu = request.form.get('jammenu_give')
    dp = request.form.get('dp_give')
    id = request.form.get('id_give')


    doc={
        'Nama':nama,
        'Telepon':telepon,
        'Komunitas':komunitas,
        'Tanggal':date,
        'Jam':time,
        'Durasi':durasi,
        'jumlah_orang':jumlah,
        'Area':piliharea,
        'Menu':pilihmenu,
        'Jam_keluar_menu':jammenu,
        'dp':dp,
        'id':id
    }

    db.event.update_one({'_id':ObjectId(id)},{'$set':doc})
    return jsonify({
        'msg':'data berhasil di edit'
    })

# delete-event
@app.route('/delete',methods=['GET'])
def delete():
    id=request.args.get('id')
    db.event.delete_one({'_id':ObjectId(id)})
    return jsonify({
        'msg':'Yakin untuk menghapus data reservasi event?'
    })
    # data=list(db.event.find({}))
    # return render_template('admin-event2.html',data=data)





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
