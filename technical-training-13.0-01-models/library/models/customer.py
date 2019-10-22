# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class Customer(models.Model):
    
    _name = "library.customer"
    
    name = fields.Text(required=True, string="Customer Name")
    
    address = fields.Text()
    phone = fields.Text()
    email = fields.Text(required=True, default='')
    book_ids = fields.Many2many("library.book", readonly=True)