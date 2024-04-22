from datetime import timedelta, datetime

from flask import redirect, url_for
from pony.orm import db_session, select

from WebHostLib import app, cache
from .models import Room, Seed


@app.route('/', methods=['GET', 'POST'])
def get_first_room_tracker():
    with db_session:
        rooms = select(room for room in Room)
        if len(rooms) == 1:
            for room in rooms:
                return redirect(url_for("get_multiworld_tracker", tracker=room.tracker))
        else:
            return redirect(url_for("games"))
# @cache.cached(timeout=300)  # cache has to appear under app route for caching to work
# def landing():
#     rooms = count(room for room in Room if room.creation_time >= datetime.utcnow() - timedelta(days=7))
#     seeds = count(seed for seed in Seed if seed.creation_time >= datetime.utcnow() - timedelta(days=7))
#     return render_template("landing.html", rooms=rooms, seeds=seeds)
