# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Sale Contrat Details

    country_origin_id = fields.Many2one('res.country', string='Origin', required=True)
    crop_year_id = fields.Many2one('sale.contract.crop.year', string='Crop Year', required=True) 
    quaily_specs = fields.Text(string='Quality/Specs', required=True)
    packing_id = fields.Many2one('sale.contract.packing', string='Packing', required=True)
    details = fields.Text(string='Details', required=True)

    shipment_date = fields.Date(string='Shipment Date')
    shipment_date_end = fields.Date(string='Shipment Date End')

    loading_port_id = fields.Many2one('sale.contract.port', string='Loading Port', required=True)
    destination_port_id = fields.Many2one('sale.contract.port', string='Destination Port', required=True)

    document_ids = fields.Many2many('sale.contract.document', string='Document')

    remarks_id = fields.Many2one('sale.contract.remark', string='Remarks')
    remarks = fields.Text(string='Remarks Text')

    payment_term2_id = fields.Many2one('sale.contract.term', string='Payment Terms2')

    payment_term_text = fields.Text(string='Payment Term Text')

    

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    containers = fields.Float(string='Container', digits=(6, 2))
    con_dimension = fields.Many2one('sale.contract.dimension', string='Containers Dimesion')