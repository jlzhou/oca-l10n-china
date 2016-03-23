# -*- coding: utf-8 -*-
from openerp import http

# class L10nCnDepartment(http.Controller):
#     @http.route('/l10n_cn_department/l10n_cn_department/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cn_department/l10n_cn_department/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cn_department.listing', {
#             'root': '/l10n_cn_department/l10n_cn_department',
#             'objects': http.request.env['l10n_cn_department.l10n_cn_department'].search([]),
#         })

#     @http.route('/l10n_cn_department/l10n_cn_department/objects/<model("l10n_cn_department.l10n_cn_department"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cn_department.object', {
#             'object': obj
#         })