# -*- coding: utf-8 -*-
from odoo import fields, models


# class Partner(models.Model):
#     _name = 'library.partner'
#     _description = 'Partner'

#     name = fields.Char()
#     email = fields.Char()
#     address = fields.Text()
#     partner_type = fields.Selection([('customer', 'Customer'), ('author', 'Author')], default="customer")

#     rental_ids = fields.One2many('library.rental', 'customer_id', string='Rentals')

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
#     address = fields.Text(default="Address Placeholder")
    
    partner_type = fields.Selection([('customer', 'Customer'), ('author', 'Author'), ('publisher', "Publisher")], default="customer")
    rental_ids = fields.One2many('library.rental', 'customer_id', string='Rentals')


class Partner(models.Model):
    _inherit = "res.partner"
    partner_type = fields.Selection(selection_add=[('reviewer', "Reviewer'")])
    
    
    
