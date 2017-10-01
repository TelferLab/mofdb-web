/** url is provided by the template, pointing where the url where the json data resided.
 * Check views.py for the method to generate the json data (and urls.py)
 */
function datatable_reaction_catalysts(id, url){
    console.log('run_catalysts_datatable');
    var table = $("#"+id+".table-catalysts").DataTable({
        "ajax": {
            "processing": true,
            "url": url,
            "dataSrc": ""
        },
        "fixedHeader": true,
        "responsive": true,
        "paging": false,
        "pagingType": "numbers",
        "lengthChange": false,
        "info": false,
        "searching": false,
        // "ordering": true,
        // "order": [[0,'desc'], [1,'desc']],
        "columns": [
            { "data": "component_type" },
            { "data": "component_name" },
            { "data": "component_nick" },
            { "data": "rate_constant" },
            { "data": "conversion" },
            { "data": "ee" },
            { "data": "de" },
            { "data": "yield_field" },
            { "data": "amount" },
            {
                "data": "component_url",
                "visible": false
            }
        ],
        "columnDefs": [
            {
                "targets":  1,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            },
            {
                "targets":  2,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            }
        ]
    } );
    return table;
}

function datatable_reaction_catalysts_short(id, url){
    console.log("run_catalysts_datatable");
    var table = $("#"+id+".table-catalysts").DataTable({
        "ajax": {
            "processing": true,
            "url": url,
            "dataSrc": ""
        },
        "fixedHeader": true,
        "responsive": true,
        "paging": false,
        "pagingType": "numbers",
        "lengthChange": false,
        "info": false,
        "searching": false,
        // "ordering": true,
        // "order": [[0,'desc'], [1,'desc']],
        "columns": [
            { "data": "component_type" },
            { "data": "component_name" },
            { "data": "component_nick" },
            {
                "data": "component_url",
                "visible": false
            },
        ],
        "columnDefs": [
            {
                "targets":  1,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            },
            {
                "targets":  2,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            }
        ]
    } );
    return table;
}

function display_datatable_reaction_catalysts(id, url){
    console.log("run display_datatable_reaction_catalysts");
    $(document).ready(function() {
        datatable_reaction_catalysts(id, url);
    } );
}


function datatable_reaction_reactants(id, url){
    console.log("run_reactants_datatable");
    var table = $("#"+id+".table-reactants").DataTable({
        "ajax": {
            "processing": true,
            "url": url,
            "dataSrc": ""
        },
        "fixedHeader": true,
        "responsive": true,
        "ordering": true,
        "paging": false,
        "pagingType": "numbers",
        "lengthChange": false,
        "info": false,
        "searching": false,
        "columns": [
            { "data": "component_name" },
            { "data": "component_nick" },
            {
                "data": "component_url",
                "visible": false
            }
        ],
        "columnDefs": [
            {
                "targets":  0,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            },
            {
                "targets":  1,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            }
        ]
    } );
    return table;
}

function display_datatable_reaction_reactants(id, url){
    console.log("run display_datatable_reaction_reactants");
    $(document).ready(function() {
        datatable_reaction_reactants(id, url);
    } );
}

function datatable_reaction_products(id, url){
    console.log("run_products_datatable");
    var table = $("#"+id+".table-products").DataTable({
        "ajax": {
            "processing": true,
            "url": url,
            "dataSrc": ""
        },
        "fixedHeader": true,
        "responsive": true,
        "ordering": true,
        "paging": false,
        "pagingType": "numbers",
        "lengthChange": false,
        "info": false,
        "searching": false,
        "columns": [
            { "data": "component_name" },
            { "data": "component_nick" },
            {
                "data": "component_url",
                "visible": false
            }
        ],
        "columnDefs": [
            {
                "targets":  0,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            },
            {
                "targets":  1,
                "render": function (data, type, row) {
                    return '<a href="'+row.component_url+'">'+data+'</a>';
                }
            }
        ]
    } );
    return table;
}

function display_datatable_reaction_products(id, url){
    console.log("run display_datatable_reaction_products");
    $(document).ready(function() {
        datatable_reaction_products(id, url);
    } );
}

function reaction_format_table_catalysts( d ) {
    // `d` is the original data object for the row
    return '<h5>Catalysts</h5>'+
      '<table id="'+d.id+'" class="table-catalysts table table-striped table-bordered dt-responsive nowrap" cellspacing="0" width="100%">'+
        '<thead>'+
          '<tr>'+
            '<th>Type</th>'+
            '<th>Name</th>'+
            '<th>Nick</th>'+
            '<th>component_url</th>'+
          '</tr>'+
        '</thead>'+
        '<tbody></tbody>'+
      '</table>';
}

function reaction_format_table_products ( d ) {
    // `d` is the original data object for the row
    return '<h5>Products</h5>'+
      '<table id="'+d.id+'" class="table-products table table-striped table-bordered dt-responsive nowrap" cellspacing="0" width="100%">'+
        '<thead>'+
          '<tr>'+
            '<th>Name</th>'+
            '<th>Nick</th>'+
            '<th>component_url</th>'+
          '</tr>'+
        '</thead>'+
        '<tbody></tbody>'+
      '</table>';
}

function reaction_format_table_reactants ( d ) {
    // `d` is the original data object for the row
    return '<h5>Reactants</h5>'+
      '<table id="'+d.id+'" class="table-reactants table table-striped table-bordered dt-responsive nowrap" cellspacing="0" width="100%">'+
        '<thead>'+
          '<tr>'+
            '<th>Name</th>'+
            '<th>Nick</th>'+
            '<th>component_url</th>'+
          '</tr>'+
        '</thead>'+
        '<tbody></tbody>'+
      '</table>';
}

function reaction_format_table_all (d) {
    return reaction_format_table_catalysts(d) +
        reaction_format_table_reactants(d) +
        reaction_format_table_products(d);
}

function display_datatable_reaction_list(){
    $(document).ready(function() {
        console.log('run_reaction-list_datatable');
        var table = $('#table-reaction-list').DataTable({
            "ajax": {
                "processing": true,
                "url": "/reactions-table/1",
                "dataSrc": ""
            },
            "fixedHeader": true,
            // "responsive": true,
            // "paging": false,
            // "pagingType": "numbers",
            // "lengthChange": false,
            "info": false,
            // "searching": false,
            "columns": [
                {
                    "className":      'details-control',
                    "orderable":      false,
                    "data":           null,
                    "defaultContent": ''
                },
                { "data": "id" },
                { "data": "name" },
                { "data": "category" },
                {
                    "data": "url",
                    "visible": false
                },
            ],
            "columnDefs": [
                {
                    "targets":  1,
                    "render": function (data, type, row) {
                        return '<a href="'+row.url+'">'+data+'</a>';
                    }
                },
                {
                    "targets":  2,
                    "render": function (data, type, row) {
                        return '<a href="'+row.url+'">'+data+'</a>';
                    }
                }
            ],
            "ordering": true,
            "order": [[1, 'asc']]
        } );

        // Add event listener for opening and closing details
        $('#table-reaction-list tbody').on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = table.row( tr );

            if ( row.child.isShown() ) {
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            }
            else {
                // Open this row
                // row.child( reaction_format_extra(row.data()) ).show();
                row.child( reaction_format_table_all(row.data()) ).show();
                tr.addClass('shown');
                ajax_reload_all_tables(row);
            }

        } );
    } );
}

function ajax_reload_all_tables(row){
    var origin = window.location.origin;
    // Catalysts
    var catalysts_url = origin + '/reaction-catalysts-table/' + row.data().id;
    var catalysts_table = datatable_reaction_catalysts_short(row.data().id, catalysts_url);
    catalysts_table.ajax.reload();
    // Reactants
    var reactants_url = origin + '/reaction-reactants-table/' + row.data().id;
    var reactants_table = datatable_reaction_reactants(row.data().id, reactants_url);
    reactants_table.ajax.reload();
    // Product
    var products_url = origin + '/reaction-products-table/' + row.data().id;
    var products_table = datatable_reaction_products(row.data().id, products_url);
    products_table.ajax.reload();
}
