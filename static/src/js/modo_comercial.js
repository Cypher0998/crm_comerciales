odoo.define('crm_comerciales.modo_comercial',function(require){

	"use strict";
	var AbstractAction = require('web.AbstractAction');
	var core = require('web.core');
	var Session = require('web.session');
	var QWeb = core.qweb;
	var _t = core._t;

	var CommercialMode = AbstractAction.extend ({
		start: function(){
			let self = this;
			self.$el.html(QWeb.render("CommercialModeMenu",{widget: self}));
		}
	});

	core.action_registry.add('modo_comercial', CommercialMode);
	return CommercialMode;
});