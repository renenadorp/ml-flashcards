from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db

from app.email import send_email
from app.models import Card

from .forms import SearchForm

card = Blueprint('card', __name__)


@card.route('/', methods=["GET", "POST"])
@login_required
def index():

    """Card page."""

    #current_app.logger.info("Hello from the card page!")
    
      
    # SEARCH 
    search_form = SearchForm()

    # CARDS
    if request.method == "POST" and search_form.validate() and search_form['q']:
        search = "%{}%".format(search_form.q.data)
    
        cards = Card.query.filter(Card.title.like(search)).all()
    elif request.args.get("id") is not None:
            cards = Card.query.filter(Card.id == request.args.get("id"))

    else:    
        cards = Card.query.filter(Card.id <= 2)

    detail = request.args.get("detail")
    #detail = request.args.get("detail")
    return render_template("card/index.html", cards=cards, search_form=search_form, detail=detail)
#    return render_template("card/index.html", form=form, search_form=search_form, cards=cards, detail=detail)
