from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app

from app import db
from app.main import bp
from app.models import User


@bp.route('/')
@bp.route('/index')
def index():
    return 'Hello World'
