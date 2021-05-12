odoo.define('crm_comerciales.registro', function (require) {
"use strict";
    var core = require('web.core');
    var Widget = require('web.Widget');
    var QWeb = core.qweb;
    var _t = core._t;
    var crm_comerciales = require('crm_comerciales.registro');
    var long = '0.0';
    var lat = '0.0';
    

    navigator.geolocation.getCurrentPosition(showPosition);
  /*  long = '0.0';
    lat = '0.0';*/
    

    function showPosition(position) {
      this.lat = position.coords.latitude;
      this.long = position.coords.longitude;
    }

    function geolocateMe(){
      if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);
        Document.getElementById("latitud").innerHTML = this.lat;
        Document.getElementById("longitud").innerHTML = this.long;
      }
    }
});

