# -*- coding: utf-8 -*-
from odoo import fields, models


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')

    author_ids = fields.Many2many("res.partner", string="Authors", domain=[('partner_type', '=', 'author')])
    edition_date = fields.Date()
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('res.partner', string='Publisher', domain=[('partner_type', '=', 'publisher')])

    rental_ids = fields.One2many('library.rental', 'copy_id', string='Rentals')
#     copy_ids = fields.One2many("library.book.copy", "book_id")

class BookCopy(models.Model):
    _name = "library.book.copy"
    _description = "Individual copy of a book."
    _inherits = {
        "library.book": "book_id"
    }
    _rec_name = "ref"
    
    ref = fields.Char(required=True)
    book_id = fields.Many2one("library.book", required=True)