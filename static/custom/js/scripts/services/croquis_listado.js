$services.croquis_listado = (function (){

    var reporte_avance_mapa = function (tipo,codigo,callbacksuccess){
        var slug = 'croquis_listado_api/reportes/reporte_avance_segmentacion/'.concat(tipo,'/',codigo);

        $services.ajax.get({
            url: $utils.urlServer(slug),
            success: function (data) {
            callbacksuccess(data);
            },
        });
    }


    return {
        reporte_avance_mapa:reporte_avance_mapa,

    }

})();