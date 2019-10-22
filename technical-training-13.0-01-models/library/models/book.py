# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class Book(models.Model):
    
    _name = "library.book"
    
    name = fields.Text(required=True)
    isbn = fields.Text(required=True)
    edition_date = fields.Date()
    rented_by = fields.Many2many("library.customer")
    author_ids = fields.Many2many("library.author")
    