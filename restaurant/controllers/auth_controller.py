from flask import Blueprint, render_template,request, redirect, url_for, flash

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

registered=[]

@auth.route("/")
def auth_index():
    return render_template("auth/auth_index.html")

@auth.route("/cadastros")
def cadastros():
    global auth_register
    return render_template("auth/cadastros.html", registers = registered)

@auth.route("/login")
def auth_login():
    return render_template("auth/auth_login.html")

@auth.route("/register")
def auth_register():
    return render_template("auth/auth_register.html")

@auth.route("/save", methods=["POST", "GET"])
def save_registers():
        inputName = request.form.get("inputName", None) 
        inputUsername = request.form.get("inputUsername", None) 
        inputEmail = request.form.get("inputEmail", None) 
        inputPassword = request.form.get("inputPassword", None) 
        inputConfirmPassword = request.form.get("inputConfirmPassword", None) 
        global registered

        if (inputName == "") or (inputUsername == "") or (inputEmail == "") or (inputPassword == "") or (inputConfirmPassword == ""):
            #error = 'Campo obrigatório não preenchido'
            #flash('', 'error')
            return render_template('auth/auth_register.html')

        if inputPassword != inputConfirmPassword:
            #error = 'As senhas não coincidem'
            return render_template('auth/auth_register.html')

        if inputUsername in registered:
            #error = 'O nome de usuário já está em uso'
            return render_template('auth.auth_register.html')
        
        if inputEmail in registered:
            #error = 'O email já está em uso'
            return render_template('auth.auth_register.html')
        
        registered.append({'nome': inputName, 'usuario': inputUsername, 'email': inputEmail, 'senha': inputPassword})

        return redirect(url_for("auth.auth_login"))



@auth.route('/auth_login', methods=['GET', 'POST'])
def login():
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        for user in registered:
            if user['usuario'] == email or user['email'] == email:
                if user['senha'] == password:
                    return redirect(url_for("index"))
                 
        return  redirect(url_for("auth.auth_login"))
                  
                  
                
