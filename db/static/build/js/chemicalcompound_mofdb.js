/** url is provided by the template, pointing where the url where the json data resided.
 * Check views.py for the method to generate the json data (and urls.py)
 */

function display_datatable_chemicalcompound_list(){
    $(document).ready(function() {
        console.log('run_chemicalcompound-list_datatable');
        var table = $('#table-chemicalcompound-list').DataTable({
            "ajax": {
                "processing": true,
                "url": "/chemicalcompounds-table/1",
                "dataSrc": ""
            },
            "fixedHeader": true,
            "responsive": true,
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

        // // Add event listener for opening and closing details
        // $('#table-chemicalcompound-list tbody').on('click', 'td.details-control', function () {
        //     var tr = $(this).closest('tr');
        //     var row = table.row( tr );
        //
        //     if ( row.child.isShown() ) {
        //         // This row is already open - close it
        //         row.child.hide();
        //         tr.removeClass('shown');
        //     }
        //     else {
        //         // Open this row
        //         // row.child( mof_format_extra(row.data()) ).show();
        //         // row.child( mof_format_table_all(row.data()) ).show();
        //         tr.addClass('shown');
        //         // ajax_reload_tables(row);
        //     }
        //
        // } );
    } );
}
