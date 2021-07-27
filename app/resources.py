from flask_smorest import Blueprint
from flask.views import MethodView
from app.schemas import CalculateArgsSchema, CalculateResponseSchema
from app.utils import apply_discount, apply_state_taxes

blueprint = Blueprint('Calculator', 'Calculator')


@blueprint.route('/calculate')
class CalculateResource(MethodView):
    @blueprint.arguments(CalculateArgsSchema)
    def post(self, params):
        result = dict()
        result['cost_after_discount'] = apply_discount(params['price'] * params['items_count'])
        result['cost_after_taxes'] = round(apply_state_taxes(result['cost_after_discount'], params['state_code']))

        return CalculateResponseSchema().load(result)
