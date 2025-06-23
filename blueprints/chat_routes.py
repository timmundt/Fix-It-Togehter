from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for

chat_r =Blueprint('chat', __name__)
