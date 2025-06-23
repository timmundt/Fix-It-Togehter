from flask import Flask, Blueprint, flash, render_template, redirect, request

staticpages_r=Blueprint('staticpages', __name__)

@staticpages_r.route('/')
def index():
    return render_template('index.html')


@staticpages_r.route('/startseite')
def home():
    return render_template('index.html')

@staticpages_r.route('/impresseum')
def imprint():
    return render_template('imprint.html')

@staticpages_r.route('/nutzungsbedingung')
def terms_of_use():
    return render_template('terms_of_use.html')

@staticpages_r.route('/datenschutz')
def privacy_policy():
    return render_template('privacy_policy.html')

    