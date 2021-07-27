import marshmallow


class CalculateArgsSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    items_count = marshmallow.fields.Int(required=True)
    price = marshmallow.fields.Int(required=True) # in cents
    state_code = marshmallow.fields.String(required=True)


class CalculateResponseSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    cost_after_discount = marshmallow.fields.Int(required=True) # in cents
    cost_after_taxes = marshmallow.fields.Int(required=True) # in cents


