# -*- coding: utf-8 -*-
# from odoo import http


# class ChequeBookOut(http.Controller):
#     @http.route('/cheque_book_out/cheque_book_out/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cheque_book_out/cheque_book_out/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cheque_book_out.listing', {
#             'root': '/cheque_book_out/cheque_book_out',
#             'objects': http.request.env['cheque_book_out.cheque_book_out'].search([]),
#         })

#     @http.route('/cheque_book_out/cheque_book_out/objects/<model("cheque_book_out.cheque_book_out"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cheque_book_out.object', {
#             'object': obj
#         })
