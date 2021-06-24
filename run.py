from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

github_blueprint = make_github_blueprint(
    client_id="f78118de14a4a181ee40",
    client_secret="b924678e3c8e56e9106f282f82b2d01d80374ea9"
)

app.register_blueprint(github_blueprint_url_prefix='/login')


@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get("/user")
        if account_info.ok:
            account_info_json = account_info.json()
            return '<h1>Your github name is {}'.format(account_info_json['login'])
        return '<h1>Request failed!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
