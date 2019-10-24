# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    
    name = fields.Char(compute="_compute_rental_name")

    customer_id = fields.Many2one('res.partner', string='Customer', domain=[('partner_type', '=', 'customer')])
    copy_id = fields.Many2one('library.book.copy', string='Book')

    rental_date = fields.Date()
    return_date = fields.Date()
    is_late = fields.Boolean(string="Late Return", compute="_compute_is_late")

#     customer_address = fields.Text(related='customer_id.address')
    customer_email = fields.Char(related='customer_id.email')

    book_authors = fields.Many2many(related='copy_id.author_ids')
    book_edition_date = fields.Date(related='copy_id.edition_date')
    book_publisher = fields.Many2one(related='copy_id.publisher_id')
    
    @api.depends("copy_id.name")
    def _compute_rental_name(self):
        for rental in self:
            rental.name = "Rental {}: {}".format(rental.id, rental.copy_id.name)
    
    @api.depends("rental_date", "return_date")
    def _compute_is_late(self):
        for rental in self:
            today = fields.Date.today()
            rental.is_late = False
            if rental.rental_date:
                due_date = fields.Date.add(rental.rental_date, months=1)
                if rental.return_date:
                    rental.is_late = (due_date < rental.return_date)
                else:
                    rental.is_late = (today > due_date)