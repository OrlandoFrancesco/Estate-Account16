from odoo import models, Command

class EstateProperty(models.Model):
    _inherit="estate.property"

    def button_sold(self):
        self.env['account.move'].create({
            'partner_id': self.partner_id.id,
            'move_type': 'out_invoice',
            'name': self.name,
            'invoice_line_ids': [
                Command.create({
                    'quantity': 1.0,
                    'price_unit': self.best_price
                }),

                Command.create({
                    'name': 'Commission',
                    'quantity': 1.0,
                    'price_unit': ( self.best_price * 6 ) / 100
                }),

                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1.0,
                    'price_unit': 100.0
                })
            ]
        })
        
        return super().button_sold()