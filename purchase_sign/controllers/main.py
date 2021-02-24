# -*- coding: utf-8 -*-

import base64
from datetime import datetime
import binascii

from odoo import fields, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request, Response
from odoo.tools import image_process
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortal(CustomerPortal):

    @http.route(['/my/purchase/<int:order_id>/accept'], type='json', auth="public", website=True)
    def portal_po_accept(self, order_id, access_token=None, name=None, signature=None):
        # get from query string if not on json param
        access_token = access_token or request.httprequest.args.get('access_token')
        try:
            order_sudo = self._document_check_access('purchase.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return {'error': _('Invalid order.')}
        if not signature:
            return {'error': _('Signature is missing.')}

        try:
            order_sudo.write({
                'signed_by': name,
                'signed_on': fields.Datetime.now(),
                'signature': signature,
            })
            request.env.cr.commit()
        except (TypeError, binascii.Error) as e:
            return {'error': _('Invalid signature data.')}
        # order_sudo.action_confirm()
        # order_sudo._send_order_confirmation_mail()

        # pdf = request.env.ref('sale.action_report_saleorder').sudo()._render_qweb_pdf([order_sudo.id])[0]

        # _message_post_helper(
        #     'sale.order', order_sudo.id, _('Order signed by %s') % (name,),
        #     attachments=[('%s.pdf' % order_sudo.name, pdf)],
        #     **({'token': access_token} if access_token else {}))

        query_string = '&message=sign_ok'
        # if order_sudo.has_to_be_paid(True):
        #     query_string += '#allow_payment=yes'
        return {
            'force_refresh': True,
            'redirect_url': order_sudo.get_portal_url(query_string=query_string),
        }