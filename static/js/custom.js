$('#myModal').on('show.bs.modal', function (e) {
    let link = $(e.relatedTarget);
    $(this).find(".modal-body").load(link.attr("href"));
});


function rightmove() {
    let data = $('#server_list').find("option:selected").text();
    // $('#server_list_execute').find("option").append(data);
    $('#server_list_execute').add("option")
}
