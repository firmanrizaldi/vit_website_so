
from odoo import api, fields, models
import time
import datetime
from odoo import http
import json as simplejson

from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class BaseWebsite(http.Controller):
    
    @http.route('/vit/so', type='http', auth='public', website=True)
    def index(self, **kw):
        
        sale_orders = request.env['sale.order'].search([])
        
        return request.render('vit_website_so.index', {
            'sale_orders' : sale_orders
        })
        
    @http.route('/vit/so_ajax', type='http', auth='public', website=True)
    def index_ajax(self, **kw): 
        
        return request.render('vit_website_so.index_ajax', {
            
        })
    
    @http.route('/vit/load_ajax', type='http', auth='public', website=True)
    def load_ajax(self,  **kw):
        sale_orders = request.env['sale.order'].search([])
        
        result = {}
        result['data'] = []
        
        for so in sale_orders :
            result['data'].append([ 
                so.name,
                so.confirmation_date,
                so.partner_id.name,
                so.user_id.name,
                so.amount_total,
                so.invoice_status,
            ])

        return simplejson.dumps(result, default=str)
