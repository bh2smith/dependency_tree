# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
from . import utils


class IrModule(models.Model):
    _inherit = 'ir.module.module'

    def dependency_tree(self):
        if not self.dependencies_id.ids or self.name == 'base':
            return None
        names = self.dependencies_id.mapped('name')
        children = self.search([('name', 'in', names)])
        if children:
            return {str(mod.name): mod.dependency_tree() for mod in children}


class BasicDepends(models.Model):
    _name = 'basic.dependency'
    _description = 'Dependency Tree'

    name = fields.Char(compute='_get_dependencies')
    root_id = fields.Many2one('ir.module.module', string="Root Module")
    dependency_tree = fields.Text(compute='_get_dependencies', store=True)
    distinct_ids = fields.Many2many(
        'ir.module.module', compute='_get_dependencies', store=True)

    dependency_count = fields.Integer(compute='_get_dependencies')
    depth = fields.Integer(compute='_get_dependencies', store=True)

    @api.depends('root_id')
    def _get_dependencies(self):
        for r in self:
            tree_dict = r.root_id.dependency_tree()

            r.name = str(datetime.today().date())
            if r.root_id:
                r.name = r.root_id.name + ':' + r.name

            r.depth = utils.depth(tree_dict)

            r.dependency_tree = utils.beautify(tree_dict)

            r.distinct_ids = self.env['ir.module.module'].search([
                ('name', 'in', utils.keywords(tree_dict))])

            r.dependency_count = len(r.distinct_ids)

