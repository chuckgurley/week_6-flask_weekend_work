from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from bar_inventory.forms import BarForm
from bar_inventory.models import Bar, db
from bar_inventory.helpers import random_joke_generator

site = Blueprint('site', __name__, template_folder='site_templates')



@site.route('/')
def home():
    print("It's Magic time!")
    return render_template('index.html')

@site.route('/profile', methods = ['GET','POST'])
@login_required 
def profile():
    # random_joke_generator()
    my_bar = BarForm()

    try:
        if request.method == "POST" and my_bar.validate_on_submit():
            name = my_bar.name.data
            description = my_bar.description.data
            price = my_bar.price.data
            chocolate_quality = my_bar.chocolate_quality.data
            melt_temp = my_bar.melt_temp.data
            freeze_time = my_bar.freeze_time.data
            height = my_bar.height.data
            weight = my_bar.weight.data
            cost_of_production = my_bar.cost_of_production.data
            series = my_bar.series.data
            if my_bar.dad_joke.data:
                random_joke = my_bar.dad_joke.data
            else:
                random_joke = random_joke_generator()          
            user_token = current_user.token

            bar = Bar(name, description, price, chocolate_quality, melt_temp, freeze_time, height, weight, cost_of_production, series, random_joke, user_token)

            db.session.add(bar)
            db.session.commit()

            return redirect(url_for('site.profile'))
    except:
        raise Exception("Bar not created, please check your form and try again!")
    
    current_user_token = current_user.token

    bars = Bar.query.filter_by(user_token=current_user_token)

    
    return render_template('profile.html', form=my_bar, bars = bars )


