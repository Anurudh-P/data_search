# -*- coding: utf-8 -*-


from odoo import models, fields


class DataSearch(models.TransientModel):
    """ model for  data search  """

    _name = 'data.search'
    _description = "data search"
    _transient_max_hours = 0.1
    _rec_name = 'search_field'

    search_field = fields.Char(string='Search here', required=True)
    model_name_id = fields.Many2one('ir.model', required=True,
                                    string='Model Name')
    field_name_id = fields.Many2one('ir.model.fields',
                                    string='Field Name', required=True,
                                    domain="[('model_id', '=', model_name_id)]")
    field_record_ids = fields.One2many('data.search.result',
                                       'result_id', readonly=True)

    def action_search(self):
        """ function for searching fields """

        if not self.model_name_id or not self.field_name_id:
            return
        self.field_record_ids.unlink()
        model_name = self.model_name_id.model
        field_name = self.field_name_id.name
        records = self.env[model_name].search_read(
            [(field_name, 'ilike', self.search_field)])
        result_records = []
        for record in records:
            result_records.append(fields.Command.create({
                'data': record.get(field_name)[1] if
                self.field_name_id.ttype == 'many2one'
                else record.get(field_name),
                'name_id': record.get('id'),
                'name': record.get('name'),
            }))
        self.write({
            'field_record_ids': result_records,
        })


class DataSearchResult(models.TransientModel):
    """ model for  storing data search result """

    _name = 'data.search.result'
    _description = "data search result"

    name_id = fields.Integer(string='id')
    data = fields.Char(string='Data')
    name = fields.Char(string='Name')
    result_id = fields.Many2one('data.search')
