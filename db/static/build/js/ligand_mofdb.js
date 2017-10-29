/** url is provided by the template, pointing where the url where the json data resided.
 * Check views.py for the method to generate the json data (and urls.py)
 */

function display_datatable_ligand_list(){
    $(document).ready(function() {
        console.log('run_ligand-list_datatable');
        var table = $('#table-ligand-list').DataTable({
            "ajax": {
                "processing": true,
                "url": "/ligands-table/1",
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
    } );
}
