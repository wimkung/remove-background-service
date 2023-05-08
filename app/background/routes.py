from app.background import bp


@bp.route('/background')
def index():
    return "This is background blueprint"
