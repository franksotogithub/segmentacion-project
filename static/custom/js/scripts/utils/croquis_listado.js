$utils.croquis_listado=(function ( service){
    var global ={
        optionsMaps:{
            showLabels: true,
            basemap:"topo",
            center:[-75,-9.304029],
            zoom:6
        },
        idMap : "mapa",
        idAmbitoGeografico:"ambitoGeografico",
        idCapasTematicos:'capasTematicos',
        /*capas : [
            {
                id:'capasTematicos',
                urlMap :"http://arcgis.inei.gob.pe:6080/arcgis/rest/services/CARTOGRAFIA_BASE_INEI/LIMITE_TEMATICOS/MapServer",
                defaultIniLayers:[0],
                idLayers:[0],
                datosLayers:[
                    {   id:0,
                        layer:'',
                        minScale:0,
                        maxScale:0,
                        visible:true,
                        showLabels:true,
                    },
                    {   id:1,
                        layer:'',
                        minScale:0,
                        maxScale:0,
                        visible:true,
                        showLabels:false,
                    }

                ],



            },
        ]*/
        capas:{
            'capasTematicos':{
                urlMap :"http://arcgis.inei.gob.pe:6080/arcgis/rest/services/CARTOGRAFIA_BASE_INEI/LIMITE_TEMATICOS/MapServer",
                defaultIniLayers:[0],
                idLayers:[0],
                datosLayers:[
                    {   id:0,
                        layer:'',
                        minScale:0,
                        maxScale:0,
                        visible:true,
                        showLabels:true,


                    },
                    {   id:1,
                        layer:'',
                        //minScale:0,
                        //maxScale:0,
                        visible:true,
                        showLabels:true,

                    },

                    {   id:2,
                        layer:'',
                        //minScale:0,
                        //maxScale:0,
                        visible:true,
                        showLabels:false,

                    }

                ],

            }
        }


    };



    var iniciarMapa = function () {

        require([
            "esri/map","esri/layers/FeatureLayer","esri/layers/ArcGISDynamicMapServiceLayer"
        ],function (Map,FeatureLayer,ArcGISDynamicMapServiceLayer) {
            var $idAmbitoGeografico=$("#"+global.idAmbitoGeografico);
            global.map = new Map(
                 global.idMap
                ,global.optionsMaps);

            var renderMapa = function(){

            }

            var iniciarCapas = function () {

                for (var prop in global.capas){
                    var capa = global.capas[prop];
                    var urlMap= capa.urlMap;
                    var datos=capa.datosLayers;
                    datos.forEach(function (dato) {
                        var urlLayer=urlMap.concat('/',dato.id);
                        var optionsFeatureLayer ={
                                outFiedls:['*'],
                                opacity:1,
                                mode:FeatureLayer.MODE_AUTO,
                            };

                        (dato.minScale!==undefined)?optionsFeatureLayer.minScale=dato.minScale:false;
                        (dato.maxScale!==undefined)?optionsFeatureLayer.maxScale=dato.maxScale:false;
                        (dato.visible!==undefined)?optionsFeatureLayer.visible=dato.visible:false;
                        (dato.showLabels!==undefined)?optionsFeatureLayer.showLabels=dato.showLabels:false;


                        var feaureLayer = new FeatureLayer(urlLayer,optionsFeatureLayer);

                        dato.layer=feaureLayer;
                        global.map.addLayer(feaureLayer);

                    });
                }


                /*
                global.capas.forEach(function (capa, index) {
                    var urlMap= capa.urlMap;
                    var id=capa.id;
                    var datos=capa.datosLayers;

                    datos.forEach(function (dato) {
                        var urlLayer=urlMap.concat('/',dato.id);
                        var optionsFeatureLayer ={
                                outFiedls:['*'],
                                opacity:1,
                                mode:FeatureLayer.MODE_AUTO,
                            };

                        (dato.minScale!==undefined)?optionsFeatureLayer.minScale=dato.minScale:false;
                        (dato.maxScale!==undefined)?optionsFeatureLayer.maxScale=dato.maxScale:false;
                        (dato.visible!==undefined)?optionsFeatureLayer.visible=dato.visible:false;
                        (dato.showLabels!==undefined)?optionsFeatureLayer.showLabels=dato.showLabels:false;


                        var feaureLayer = new FeatureLayer(urlLayer,optionsFeatureLayer);

                        dato.layer=feaureLayer;
                        global.map.addLayer(feaureLayer);

                    });


                });*/
            }

            global.map.on('load',function (map) {
                iniciarCapas();
            });

            $idAmbitoGeografico.on('change',function(){
                var ambito=parseInt($(this).val());
                var capasTematicos=global.capas[global.idCapasTematicos].datosLayers;

                capasTematicos.forEach(function (capaTematico) {
                    console.log('capaTematico',capaTematico);
                    (capaTematico.id==ambito)?capaTematico.layer.setVisibility(true):capaTematico.layer.setVisibility(false);
                });
            });

        });
    }

    var init = function () {

        service.reporte_avance_mapa(1,'00',function (data) {
            //iniciarMapa();
        });

    }

    return {
        init:init,
        global:global,
    }
})($services.croquis_listado);

$utils.croquis_listado.init();