# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class SaleContractCropYear(models.Model):
    _name = 'sale.contract.crop.year'
    _description = 'Sale Contract Crop Year'

    name = fields.Char(string='Name', required=True)
    data = fields.Char(string='Data')
    data2 = fields.Char(string='Data2')


class SaleContractPacking(models.Model):
    _name = 'sale.contract.packing'
    _description = 'Sale Contract Packing'

    name = fields.Char(string='Name', required=True)
    qty = fields.Float(string='Qty', digits=(6, 2), required=True)
    uom_id = fields.Many2one('uom.uom', string='UoM', required=True)
    comment = fields.Text(string='Comment')


class SaleContractPort(models.Model):
    _name = 'sale.contract.port'
    _description = 'Sale Contract Port'

    name = fields.Char(string='Name', required=True)
    city = fields.Char(string='City')
    country_id = fields.Many2one('res.country', string='Origin', required=True)


class SaleContractDocument(models.Model):
    _name = 'sale.contract.document'
    _description = 'Sale Contract Document'

    name = fields.Char(string='Name', required=True)
    data = fields.Char(string='Data')
    data2 = fields.Char(string='Data2')
    comment = fields.Text(string='Comment')


class SaleContractRemark(models.Model):
    _name = 'sale.contract.remark'
    _description = 'Sale Contract Remark'

    name = fields.Char(string='Name', required=True)
    data = fields.Char(string='Data')
    data2 = fields.Char(string='Data2')

class SaleContractDimension(models.Model):
    _name = 'sale.contract.dimension'
    _description = 'Sale Contract Dimension'

    name = fields.Char(string='Name', required=True)
    data = fields.Char(string='Data')
    data2 = fields.Char(string='Data2')