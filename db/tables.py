import django_tables2 as tables

# Tables {{{
class CatalystsTable(tables.Table):
    component_type = tables.Column()
    component_name = tables.Column()
    component_nick = tables.Column()
    # component = tables.LinkColumn()
    component = tables.Column()
    functional_group_name = tables.Column()
    chirality = tables.Column()
    rate_constant = tables.Column()
    conversion = tables.Column()
    ee = tables.Column()
    de = tables.Column()
    yield_field = tables.Column()
    amount = tables.Column()

class ReactantsTable(tables.Table):
    # component_type = tables.Column() #CC
    component_name = tables.Column()
    component_nick = tables.Column()
    component = tables.Column()

class ProductsTable(tables.Table):
    # component_type = tables.Column() #CC
    component_name = tables.Column()
    component_nick = tables.Column()
    component = tables.Column()
# }}}

