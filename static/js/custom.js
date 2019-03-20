$('#myModal').on('show.bs.modal', function (e) {
    let link = $(e.relatedTarget);
    $(this).find(".modal-body").load(link.attr("href"));
});


$("#right_move").click(function () {
    console.log($("#server_list option:selected"));
    $("#server_list_execute").append($("#server_list option:selected"));
});

