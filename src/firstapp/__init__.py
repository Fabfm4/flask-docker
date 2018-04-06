from flask import Flask, render_template, redirect, request
from apiclient.discovery import build
import httplib2
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from oauth2client.client import OAuth2WebServerFlow
from googleapiclient import errors


app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('APP_CONFIG_FILE')
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


@app.route("/")
def hello(code = None):
    CLASSROOM_URL = 'https://www.googleapis.com/auth/classroom.'
    AUTH_URL = 'https://www.googleapis.com/auth/'

    classroom_scopes = [
        'rosters ',
        'courses ',
        'coursework.me ',
        'coursework.students ',
        'profile.photos ',
        'profile.emails'
    ]


    auth_scopes = [
        'contacts ',
        'contacts.readonly ',
        'profile.agerange.read ',
        'profile.language.read ',
        'user.addresses.read ',
        'user.birthday.read ',
        'user.emails.read ',
        'user.phonenumbers.read ',
        'admin.directory.group.readonly ',
        'admin.directory.group',
    ]

    CLASSROOM_SCOPES = CLASSROOM_URL + CLASSROOM_URL.join(classroom_scopes)
    PROFILE_SCOPES = AUTH_URL + AUTH_URL.join(auth_scopes)

    CALENDAR_SCOPES = 'https://www.googleapis.com/auth/calendar'

    DIRECTORI_SCOPES = 'https://www.googleapis.com/auth/admin.directory.user.readonly'

    CONTACT_SCOPES = 'https://www.googleapis.com/auth/contacts'

    FULL_SCOPES = CLASSROOM_SCOPES + ' ' + CALENDAR_SCOPES

    GOOGLE_APIS = {
        'full': {
            'name': 'classroom',
            'version': 'v1',
            'scope': FULL_SCOPES,
        },
        'user': {
            'name': 'directory',
            'version': 'v1',
            'scope': PROFILE_SCOPES,
        }
    }
    constructor_kwargs = {
        'auth_uri': "https://accounts.google.com/o/oauth2/auth",
        'token_uri': "https://accounts.google.com/o/oauth2/token",
    }
    flow = OAuth2WebServerFlow(
        client_id='720840152358-e7birgsn45dasn4n3uqn627hpavd2mq6.apps.googleusercontent.com',
        client_secret='JZgJpAHyIlPKz40uMg2K0PBs',
        scope=GOOGLE_APIS['user']['scope'],
        redirect_uri='http://localhost:8000',
        **constructor_kwargs
    )

    flow.params['approval_prompt'] = 'force'
    flow.params['access_type'] = 'offline'
    flow.params['state'] = 'state_parameter_passthrough_value'
    auth_uri = flow.step1_get_authorize_url()
    if request.args.get('code') is None:
        return redirect(auth_uri)
    code = request.args.get('code')
    credentials = flow.step2_exchange(code)
    http = credentials.authorize(httplib2.Http())
    initial_data = {
        'access_token': credentials.access_token,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'refresh_token': credentials.refresh_token,
        'token_expiry': credentials.token_expiry,
        'token_uri': credentials.token_uri,
        'revoke_uri': credentials.revoke_uri
    }
    service = build('people', 'v1', http=http)
    try:
        services = service.contactGroups().members(resourceNames="contactGroups/coworkers").execute()
        print(services)

    except errors.HttpError as e:
        print("entra")
        print(e.__dict__)
    return render_template('home.html')
