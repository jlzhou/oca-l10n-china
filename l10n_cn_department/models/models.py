# -*- coding: utf-8 -*-
# © 2016 Heng Shen Corp (www.hscarbonfibre.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class hr_employee(models.Model):
    _inherit = ['hr.employee']
    secondary_department_ids = fields.Many2many('hr.department', string='Secondary Departments')

