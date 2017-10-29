/** url is provided by the template, pointing where the url where the json data resided.
 * Check views.py for the method to generate the json data (and urls.py)
 */
function datatable_mof_ligands(id, url){
    console.log('run_mof_ligands_datatable');
    var table = $("#"+id+".table-mof-ligands").DataTable({
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
            { "data": "ligand_name" },
            { "data": "ligand_nick" },
            {
                "data": "ligand_url",
                "visible": false
            }
        ],
        "columnDefs": [
            {
                "targets":  0,
                "render": function (data, type, row) {
                    return '<a href="'+row.ligand_url+'">'+data+'</a>';
                }
            },
            {
                "targets":  1,
                "render": function (data, type, row) {
                    return '<a href="'+row.ligand_url+'">'+data+'</a>';
                }
            }
        ]
    } );
    return table;
}

function datatable_mof_ligands_short(id, url){
    console.log("run_mof_ligands_datatable");
    var table = $("#"+id+".table-mof-ligands").DataTable({
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
            { "data": "ligand_name" },
            { "data": "ligand_nick" },
            {
                "data": "ligand_url",
                "visible": false
            }
        ],
        "columnDefs": [
            {
                "targets":  0,
                "render": function (data, type, row) {
                    return '<a href="'+row.ligand_url+'">'+data+'</a>';
                }
            },
            {
                "targets":  1,
                "render": function (data, type, row) {
                    return '<a href="'+row.ligand_url+'">'+data+'</a>';
                }
            }
        ]
    } );
    return table;
}

function display_datatable_mof_ligands(id, url){
    console.log("run display_datatable_mof_ligands");
    $(document).ready(function() {
        datatable_mof_ligands(id, url);
    } );
}


function mof_format_table_mof_ligands( d ) {
    // `d` is the original data object for the row
    return '<h5>Ligands</h5>'+
      '<table id="'+d.id+'" class="table-mof-ligands table table-striped table-bordered dt-responsive nowrap" cellspacing="0" width="100%">'+
        '<thead>'+
          '<tr>'+
            '<th>Name</th>'+
            '<th>Nick</th>'+
            '<th>ligand_url</th>'+
          '</tr>'+
        '</thead>'+
        '<tbody></tbody>'+
      '</table>';
}

function mof_format_table_all (d) {
    return mof_format_table_mof_ligands(d)
}

function display_datatable_mof_list(){
    $(document).ready(function() {
        console.log('run_mof-list_datatable');
        var table = $('#table-mof-list').DataTable({
            "ajax": {
                "processing": true,
                "url": "/mofs-table/1",
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
                { "data": "nick" },
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
        $('#table-mof-list tbody').on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = table.row( tr );

            if ( row.child.isShown() ) {
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            }
            else {
                // Open this row
                // row.child( mof_format_extra(row.data()) ).show();
                row.child( mof_format_table_all(row.data()) ).show();
                tr.addClass('shown');
                ajax_reload_tables(row);
            }

        } );
    } );
}

function ajax_reload_tables(row){
    var origin = window.location.origin;
    // MofLigands
    var mof_ligands_url = origin + '/mof-ligands-table/' + row.data().id;
    var mof_ligands_table = datatable_mof_ligands_short(row.data().id, mof_ligands_url);
    mof_ligands_table.ajax.reload();
}
