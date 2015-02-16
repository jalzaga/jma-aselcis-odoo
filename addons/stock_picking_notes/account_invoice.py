# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import itertools
from lxml import etree

from openerp.osv import fields, osv
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openerp.addons.decimal_precision as dp
from openerp.tools.float_utils import float_round as round



class account_invoice(osv.osv):
    _inherit = "account.invoice"
    
    def _withholding(self, cr, uid, ids, field_name, arg, context): 
        res={}
        for line in self.browse(cr, uid, ids):
            res[line.id] = line.amount_untaxed * (line.withholding_pct) / 100
        return res

    
    _columns = {

    'withholding_pct' : fields.integer(string='Withholding', digits=dp.get_precision('Account'),
        store=True , help="Enter the withholding percent"),
    'withholding' : fields.function(_withholding, digits_compute=dp.get_precision('Account'), type='float', method=True, string='Withholding'),  
            
                
    }



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
