// funciones para hacer los cálculos en la nómina

function calcular_nomina() {

    var nombre_parafiscal,nombre_extras, valpagar, valpagar2, parafiscal,subtotal,total,cant_horas,horas_extras;
    // nomina = "1"
    // periodo = "1"
    // empleado = "1"
    // estado = 1
    //new Intl.NumberFormat([locales [valpagar, horas_extras, subtotal, parafiscal, cant_horas]])
    
    //id_nomina= document.getElementById("id_nomina").value //$("#id_nomina").val();
    nombre_parafiscal=$("#id_nombre_parafiscal").val();
    nombre_extras=$("#id_nombre_extras").val();
    /* nombre_extras=nombre_extras===""? 0 : +nombre_extras;
    nombre_extras=nombre_extras<0? 0: nombre_extras; */
   
    parafiscal=$("#id_parafiscales").val();
    // validamos que si la cantidad llega vacía le coloque un cero 
    //parafiscal= parafiscal===""? 0 :+parafiscal;
    // si es menor que cero que me le asigne un cero a la cantidad de parafiscal
    //parafiscal= parafiscal<0 ? 0 : parafiscal;
    
    cant_horas=$("#id_cantidad_horas").val();
    cant_horas = parseFloat(cant_horas)
    //cant_horas=parseInt(document.getElementById("id_cantidad_horas").value);
   /*  cant_horas=cant_horas===""? 0 : +cant_horas;
    cant_horas=cant_horas<0? 0: cant_horas; */
    horas_extras=$("#id_horas").val();
    horas_extras = (parseInt(horas_extras)/100);
    //horas_extras=parseFloat(document.getElementById("id_horas").value);
    //horas_extras=horas_extras/100
    
    /* horas_extras=horas_extras===""? 0 : +horas_extras;
    horas_extras=horas_extras<0? 0 : horas_extras; */

    valpagar=$("#id_valorpagar").val();
    valpagar = parseInt(valpagar)
    //valpagar=parseFloat(document.getElementById("id_valorpagar").value);
  
   //fin de los cálculos de las horas extras, cons sus diferentes valores
    
    //subtotal = valpagar/horas;
    //subtotal = valpagar*(horas_extras*cant_horas)+valpagar;
    subtotal= (valpagar/240)*(horas_extras*(parseInt(cant_horas)))+valpagar;
    //subtotal = (parseInt(valpagar)/240) + parseInt(horas_extras),
    parafiscal  = (parseInt(parafiscal)/100) * valpagar;
    //subtotal=(horas_extras*(valpagar/240))*cant_horas;
    //subtotal=horas_extras+valpagar;
    
    total= (subtotal - parafiscal) ;
    subtotal= parseFloat(subtotal);
    total = parseFloat(total);
    valpagar = parseFloat(valpagar);
    valpagar2= parseFloat(document.getElementById("id_valorpagar2").value);
    //valpagar2=6000000
    // $('#id_nomina').val(nomina);
    // $('#id_periodo').val(periodo);
    // $('#id_empleado').val(empleado);
    // $('#id_estado').val(estado);
    $('#id_nombre_extras').val(nombre_extras);
    $('#id_parafiscales').val(parafiscal);
    $('#id_nombre_parafiscal').val(nombre_parafiscal);
    $('#id_subtotal').val(subtotal);
    $('#id_cantidad_horas').val(cant_horas);
    $('#id_horas').val(horas_extras);
    //$('#id_valorpagar').val(valpagar);
    $('#id_valorpagar2').val(valpagar);
    $('#id_total').val(total);
    //$('#id_nomina').val(id_nomina);
    alert(valpagar);
    alert(horas_extras);
    alert(subtotal);
    alert(total);
    
   // alert(id_nomina);
   // alert(horas_extras);

} 