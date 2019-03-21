$('#myModal').on('show.bs.modal', function (e) {
    let link = $(e.relatedTarget);
     $(this).find(".modal-body").load(link.attr("href"));
});



$().ready(function() {
    $("#right_move").click(function () {
        $("#server_list_execute").append($("#server_list option:selected"));
    });
});



