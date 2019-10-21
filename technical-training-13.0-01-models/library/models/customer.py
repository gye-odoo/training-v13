# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class Customer(models.Model):
    
    _name = "library.customer"
    
    name = fields.Text(required=True, string="Customer Name")
    book_id = fields.Many2one("library.book")