from flask import Flask, Blueprint, flash, render_template, redirect, request

staticpages_r=Blueprint('staticpages', __name__)

@staticpages_r.route('/')
def home():
    return render_template('index.html')


@staticpages_r.route('/startseite')
def return_home():
    return render_template('index.html')

@staticpages_r.route('/impresseum')
def imperessum():
    return render_template('imperessum.html')

@staticpages_r.route('/nutzungsbedingung')
def nutzungsbedingung():
    return render_template('nutzungsbedingung.html')

    