from osv import fields, osv, orm
import netsvc
import pooler
import time

from tools.misc import logged

class account_discount(osv.osv):
    _name = 'account.discount'
    _description = "Discounts"
    _columns={
        'name':fields.char('Discount Name',size=64),
        'rate':fields.float('Rate'),
        'account_id':fields.many2one('account.account', 'Account'),
        }
    _order = 'rate asc'
account_discount()